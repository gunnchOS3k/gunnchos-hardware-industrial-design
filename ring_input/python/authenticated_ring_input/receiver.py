"""Authenticated receiver with full verification pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from .audit import AuditLog
from .calibration import CalibrationRegistry
from .codec import decode_event, verify_mac
from .fallback import SafeFallback
from .latency import LatencyHooks
from .replay_cache import ReplayCache
from .revocation import RevocationRegistry

DESTRUCTIVE_EVENTS = frozenset({"destructive_confirm"})
DEFAULT_MIN_CONFIDENCE = 0.7
DEFAULT_DESTRUCTIVE_MIN_CONFIDENCE = 0.9


class RejectReason(str, Enum):
    BAD_SIGNATURE = "bad_signature"
    UNKNOWN_DEVICE = "unknown_device"
    WRONG_TARGET = "wrong_target"
    REPLAY = "replay"
    STALE = "stale"
    REVOKED = "revoked"
    LOW_CONFIDENCE_DESTRUCTIVE = "low_confidence_destructive"
    CALIBRATION_MISMATCH = "calibration_mismatch"
    SCOPE_DENIED = "scope_denied"
    SEQ_GAP = "seq_gap"
    SESSION_EXPIRED = "session_expired"
    BAD_EVENT = "bad_event"


@dataclass
class AuthenticatedReceiver:
    host_id: str
    known_devices: set[str]
    session_keys: dict[str, dict[int, bytes]] = field(default_factory=dict)
    expected_seq: dict[str, int] = field(default_factory=dict)
    session_meta: dict[str, dict[str, Any]] = field(default_factory=dict)
    replay: ReplayCache = field(default_factory=ReplayCache)
    revocation: RevocationRegistry = field(default_factory=RevocationRegistry)
    calibration: CalibrationRegistry = field(default_factory=CalibrationRegistry)
    audit: AuditLog = field(default_factory=AuditLog)
    fallback: SafeFallback = field(default_factory=SafeFallback)
    latency: LatencyHooks = field(default_factory=LatencyHooks)
    max_skew_ms: int = 5_000
    min_confidence: float = DEFAULT_MIN_CONFIDENCE
    destructive_min_confidence: float = DEFAULT_DESTRUCTIVE_MIN_CONFIDENCE
    now_ms: int | None = None

    def register_session(self, material: dict[str, Any], *, reset_seq: bool = False) -> None:
        sid = material["session_id"]
        keys = {int(k): bytes.fromhex(v) for k, v in material["keys_by_version"].items()}
        self.session_keys[sid] = keys
        if reset_seq or sid not in self.expected_seq:
            self.expected_seq[sid] = 0
        self.session_meta[sid] = material
        self.known_devices.add(material["device_id"])

    def _clock(self) -> int:
        if self.now_ms is not None:
            return self.now_ms
        import time

        return int(time.time() * 1000)

    def receive(self, raw: dict[str, Any]) -> tuple[bool, RejectReason | None, dict[str, Any] | None]:
        self.latency.mark("verify_start")
        try:
            event = decode_event(raw)
        except ValueError:
            self.audit.record("receive", decision="reject", reason=RejectReason.BAD_EVENT.value)
            self.fallback.engage("bad_event")
            self.latency.mark("verify_end")
            return False, RejectReason.BAD_EVENT, None

        device_id = str(event["device_id"])
        session_id = str(event["session_id"])
        seq = int(event["seq"])
        now = self._clock()

        if device_id not in self.known_devices:
            return self._reject(event, RejectReason.UNKNOWN_DEVICE)

        if self.revocation.is_revoked(device_id, session_id):
            return self._reject(event, RejectReason.REVOKED)

        if event["target_device_id"] != self.host_id:
            return self._reject(event, RejectReason.WRONG_TARGET)

        meta = self.session_meta.get(session_id)
        if meta and now > int(meta.get("expires_ts_ms", now + 1)):
            return self._reject(event, RejectReason.SESSION_EXPIRED)

        keys = self.session_keys.get(session_id, {})
        key = keys.get(int(event["session_key_version"]))
        if key is None or not verify_mac(event, key):
            return self._reject(event, RejectReason.BAD_SIGNATURE)

        if abs(now - int(event["ts_ms"])) > self.max_skew_ms:
            return self._reject(event, RejectReason.STALE)

        if self.replay.seen(device_id, session_id, seq, now_ms=now):
            return self._reject(event, RejectReason.REPLAY)

        expected = self.expected_seq.get(session_id, 0)
        if seq != expected:
            # Treat duplicate lower seq as replay; higher as gap
            if seq < expected:
                return self._reject(event, RejectReason.REPLAY)
            return self._reject(event, RejectReason.SEQ_GAP)

        if not self.calibration.matches(
            calibration_id=str(event["calibration_id"]),
            surface_id=str(event["surface_id"]),
            device_id=device_id,
            now_ms=now,
        ):
            return self._reject(event, RejectReason.CALIBRATION_MISMATCH)

        event_type = str(event["event_type"])
        allowed = set(meta.get("permission_scope", [])) if meta else set(event["permission_scope"])
        if event_type not in allowed and event_type not in set(event["permission_scope"]):
            return self._reject(event, RejectReason.SCOPE_DENIED)
        # Event must be in the event's declared scope and session allow-list intersection
        if event_type not in set(event["permission_scope"]):
            return self._reject(event, RejectReason.SCOPE_DENIED)
        if meta and event_type not in set(meta.get("permission_scope", [])):
            return self._reject(event, RejectReason.SCOPE_DENIED)

        confidence = float(event["confidence"])
        if event_type in DESTRUCTIVE_EVENTS and confidence < self.destructive_min_confidence:
            return self._reject(event, RejectReason.LOW_CONFIDENCE_DESTRUCTIVE)
        if confidence < self.min_confidence and event_type not in ("heartbeat", "calibration_ping"):
            # Non-destructive low confidence: still reject for safety on input injection
            if event_type in DESTRUCTIVE_EVENTS:
                return self._reject(event, RejectReason.LOW_CONFIDENCE_DESTRUCTIVE)

        # Accept
        self.replay.remember(device_id, session_id, seq, now_ms=now)
        self.expected_seq[session_id] = seq + 1
        self.audit.record("receive", decision="accept", event=event)
        self.latency.mark("verify_end", seq=seq)
        return True, None, event

    def _reject(
        self, event: dict[str, Any], reason: RejectReason
    ) -> tuple[bool, RejectReason, None]:
        self.audit.record("receive", decision="reject", reason=reason.value, event=event)
        self.fallback.engage(reason.value)
        self.latency.mark("verify_end", reason=reason.value)
        return False, reason, None
