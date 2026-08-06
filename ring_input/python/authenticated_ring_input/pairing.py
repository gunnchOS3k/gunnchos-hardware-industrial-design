"""Pairing ceremony state machine with challenge-response."""

from __future__ import annotations

import hashlib
import hmac
import secrets
import time
import uuid
from dataclasses import dataclass, field
from typing import Any


STATES = ("DISCOVER", "CHALLENGE", "VERIFY", "CONFIRM", "PAIRED", "FAILED", "REVOKED")


@dataclass
class PairingStateMachine:
    """Explicit pairing ceremony. Offline-capable once PAIRED."""

    device_id: str
    user_id: str
    host_id: str
    device_secret: bytes
    permission_scope: list[str] = field(
        default_factory=lambda: ["pointer_move", "click", "key_press", "scroll", "heartbeat"]
    )
    pairing_id: str = field(default_factory=lambda: f"pair-{uuid.uuid4().hex[:12]}")
    state: str = "DISCOVER"
    challenge_nonce: str = ""
    challenge_response: str | None = None
    created_ts_ms: int = field(default_factory=lambda: int(time.time() * 1000))
    paired_ts_ms: int | None = None
    offline_capable: bool = True
    pairing_key: bytes | None = None

    def start_challenge(self) -> dict[str, Any]:
        if self.state not in ("DISCOVER", "FAILED"):
            raise ValueError(f"cannot challenge from {self.state}")
        self.challenge_nonce = secrets.token_hex(16)
        self.state = "CHALLENGE"
        return self.to_record()

    def device_respond(self) -> str:
        if self.state != "CHALLENGE":
            raise ValueError(f"cannot respond from {self.state}")
        msg = f"{self.device_id}|{self.user_id}|{self.host_id}|{self.challenge_nonce}".encode()
        self.challenge_response = hmac.new(self.device_secret, msg, hashlib.sha256).hexdigest()
        self.state = "VERIFY"
        return self.challenge_response

    def host_verify(self, response: str | None = None) -> bool:
        if self.state != "VERIFY":
            raise ValueError(f"cannot verify from {self.state}")
        expected = hmac.new(
            self.device_secret,
            f"{self.device_id}|{self.user_id}|{self.host_id}|{self.challenge_nonce}".encode(),
            hashlib.sha256,
        ).hexdigest()
        got = response if response is not None else self.challenge_response
        if not got or not hmac.compare_digest(expected, got):
            self.state = "FAILED"
            return False
        self.state = "CONFIRM"
        return True

    def confirm(self) -> dict[str, Any]:
        if self.state != "CONFIRM":
            raise ValueError(f"cannot confirm from {self.state}")
        self.state = "PAIRED"
        self.paired_ts_ms = int(time.time() * 1000)
        # Derive long-lived pairing key for offline session opens
        self.pairing_key = hashlib.sha256(
            self.device_secret
            + self.pairing_id.encode()
            + self.challenge_nonce.encode()
            + b"|paired"
        ).digest()
        return self.to_record()

    def revoke(self) -> None:
        self.state = "REVOKED"
        self.pairing_key = None

    def is_paired_offline(self) -> bool:
        return self.state == "PAIRED" and self.offline_capable and self.pairing_key is not None

    def to_record(self) -> dict[str, Any]:
        return {
            "pairing_id": self.pairing_id,
            "device_id": self.device_id,
            "user_id": self.user_id,
            "host_id": self.host_id,
            "state": self.state,
            "challenge_nonce": self.challenge_nonce,
            "challenge_response": self.challenge_response,
            "created_ts_ms": self.created_ts_ms,
            "paired_ts_ms": self.paired_ts_ms,
            "offline_capable": self.offline_capable,
            "permission_scope": list(self.permission_scope),
            "device_secret_fingerprint": hashlib.sha256(self.device_secret).hexdigest()[:16],
        }
