"""Canonical encoding and HMAC integrity for authenticated ring input events."""

from __future__ import annotations

import hashlib
import hmac
import json
from typing import Any, Mapping

PROTOCOL_VERSION = "1.0"
MAC_FIELDS = (
    "protocol_version",
    "device_id",
    "user_id",
    "source_device_id",
    "target_device_id",
    "session_id",
    "session_key_version",
    "seq",
    "nonce",
    "ts_ms",
    "event_type",
    "permission_scope",
    "confidence",
    "surface_id",
    "calibration_id",
    "payload",
)


def canonical_bytes(event: Mapping[str, Any]) -> bytes:
    body = {k: event[k] for k in MAC_FIELDS if k in event}
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode(
        "utf-8"
    )


def mac_payload(event: Mapping[str, Any], session_key: bytes) -> str:
    return hmac.new(session_key, canonical_bytes(event), hashlib.sha256).hexdigest()


def encode_event(event: Mapping[str, Any], session_key: bytes) -> dict[str, Any]:
    out = dict(event)
    out.setdefault("protocol_version", PROTOCOL_VERSION)
    out.setdefault("evidence_class", "SOFTWARE_SIMULATED")
    out["mac"] = mac_payload(out, session_key)
    return out


def decode_event(raw: Mapping[str, Any]) -> dict[str, Any]:
    required = set(MAC_FIELDS) | {"mac"}
    missing = required - set(raw.keys())
    if missing:
        raise ValueError(f"missing fields: {sorted(missing)}")
    return dict(raw)


def verify_mac(event: Mapping[str, Any], session_key: bytes) -> bool:
    expected = mac_payload(event, session_key)
    return hmac.compare_digest(expected, str(event.get("mac", "")))
