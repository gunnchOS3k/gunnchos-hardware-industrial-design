"""Audit log that never persists raw motion by default."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AuditLog:
    persist_raw_motion: bool = False
    entries: list[dict[str, Any]] = field(default_factory=list)

    def record(
        self,
        action: str,
        *,
        decision: str,
        reason: str = "",
        event: dict[str, Any] | None = None,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        entry: dict[str, Any] = {
            "ts_ms": int(time.time() * 1000),
            "action": action,
            "decision": decision,
            "reason": reason,
        }
        if event:
            entry["device_id"] = event.get("device_id")
            entry["session_id"] = event.get("session_id")
            entry["seq"] = event.get("seq")
            entry["event_type"] = event.get("event_type")
            entry["confidence"] = event.get("confidence")
            entry["target_device_id"] = event.get("target_device_id")
            # Explicitly omit raw motion / IMU vectors unless opted in
            if self.persist_raw_motion and isinstance(event.get("payload"), dict):
                entry["payload"] = event["payload"]
            else:
                entry["payload_omitted"] = True
                if isinstance(event.get("payload"), dict):
                    entry["payload_keys"] = sorted(event["payload"].keys())
        if extra:
            entry.update(extra)
        self.entries.append(entry)
        return entry
