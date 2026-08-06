"""Authenticated sender: builds signed events with monotonic seq and session key rotation."""

from __future__ import annotations

import hashlib
import secrets
import time
import uuid
from dataclasses import dataclass, field
from typing import Any

from .codec import encode_event
from .latency import LatencyHooks
from .pairing import PairingStateMachine


@dataclass
class AuthenticatedSender:
    pairing: PairingStateMachine
    target_device_id: str
    surface_id: str
    calibration_id: str
    session_ttl_ms: int = 3_600_000
    latency: LatencyHooks = field(default_factory=LatencyHooks)
    session_id: str = ""
    session_key: bytes = b""
    session_key_version: int = 1
    next_seq: int = 0
    opened_ts_ms: int = 0
    expires_ts_ms: int = 0
    _prior_keys: dict[int, bytes] = field(default_factory=dict)

    def open_session(self, *, offline: bool = True, now_ms: int | None = None) -> dict[str, Any]:
        if not self.pairing.is_paired_offline():
            raise RuntimeError("pairing required before session open")
        assert self.pairing.pairing_key is not None
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        self.session_id = f"sess-{uuid.uuid4().hex[:12]}"
        self.session_key_version = 1
        self.session_key = hashlib.sha256(
            self.pairing.pairing_key + self.session_id.encode() + b"|v1"
        ).digest()
        self.next_seq = 0
        self.opened_ts_ms = now
        self.expires_ts_ms = now + self.session_ttl_ms
        return {
            "session_id": self.session_id,
            "device_id": self.pairing.device_id,
            "user_id": self.pairing.user_id,
            "host_id": self.pairing.host_id,
            "session_key_version": self.session_key_version,
            "opened_ts_ms": self.opened_ts_ms,
            "expires_ts_ms": self.expires_ts_ms,
            "permission_scope": list(self.pairing.permission_scope),
            "next_seq": self.next_seq,
            "surface_id": self.surface_id,
            "calibration_id": self.calibration_id,
            "offline": offline,
        }

    def rotate_session_key(self) -> int:
        """Key rotation path: bump version, retain prior briefly on receiver side."""
        if not self.session_id:
            raise RuntimeError("no session")
        assert self.pairing.pairing_key is not None
        self._prior_keys[self.session_key_version] = self.session_key
        self.session_key_version += 1
        self.session_key = hashlib.sha256(
            self.pairing.pairing_key
            + self.session_id.encode()
            + f"|v{self.session_key_version}".encode()
        ).digest()
        return self.session_key_version

    def emit(
        self,
        event_type: str,
        *,
        confidence: float,
        payload: dict[str, Any] | None = None,
        ts_ms: int | None = None,
        permission_scope: list[str] | None = None,
    ) -> dict[str, Any]:
        if not self.session_id:
            raise RuntimeError("session not open")
        now = ts_ms if ts_ms is not None else int(time.time() * 1000)
        if now > self.expires_ts_ms:
            raise RuntimeError("session expired")
        self.latency.mark("encode_start", seq=self.next_seq)
        event = {
            "protocol_version": "1.0",
            "device_id": self.pairing.device_id,
            "user_id": self.pairing.user_id,
            "source_device_id": self.pairing.device_id,
            "target_device_id": self.target_device_id,
            "session_id": self.session_id,
            "session_key_version": self.session_key_version,
            "seq": self.next_seq,
            "nonce": secrets.token_hex(8),
            "ts_ms": now,
            "event_type": event_type,
            "permission_scope": list(permission_scope or self.pairing.permission_scope),
            "confidence": confidence,
            "surface_id": self.surface_id,
            "calibration_id": self.calibration_id,
            "payload": payload or {},
            "evidence_class": "SOFTWARE_SIMULATED",
        }
        signed = encode_event(event, self.session_key)
        self.next_seq += 1
        self.latency.mark("encode_end", seq=signed["seq"])
        return signed

    def export_session_material(self) -> dict[str, Any]:
        """Share session keys with a trusted receiver (local software harness)."""
        keys = dict(self._prior_keys)
        keys[self.session_key_version] = self.session_key
        return {
            "session_id": self.session_id,
            "device_id": self.pairing.device_id,
            "user_id": self.pairing.user_id,
            "host_id": self.pairing.host_id,
            "keys_by_version": {str(k): v.hex() for k, v in keys.items()},
            "permission_scope": list(self.pairing.permission_scope),
            "surface_id": self.surface_id,
            "calibration_id": self.calibration_id,
            "expires_ts_ms": self.expires_ts_ms,
        }
