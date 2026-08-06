"""Calibration session registry (surface + calibration id binding)."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CalibrationRegistry:
    _active: dict[str, dict[str, Any]] = field(default_factory=dict)

    def create(
        self,
        *,
        surface_id: str,
        device_id: str,
        user_id: str,
        ttl_ms: int = 3_600_000,
        now_ms: int | None = None,
        transform: dict[str, float] | None = None,
    ) -> dict[str, Any]:
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        record = {
            "calibration_id": f"cal-{uuid.uuid4().hex[:12]}",
            "surface_id": surface_id,
            "device_id": device_id,
            "user_id": user_id,
            "created_ts_ms": now,
            "expires_ts_ms": now + ttl_ms,
            "active": True,
            "transform": transform
            or {"scale_x": 1.0, "scale_y": 1.0, "offset_x": 0.0, "offset_y": 0.0},
            "notes": "SOFTWARE_SIMULATED calibration; physical ring pending",
        }
        self._active[record["calibration_id"]] = record
        return dict(record)

    def get(self, calibration_id: str) -> dict[str, Any] | None:
        return self._active.get(calibration_id)

    def matches(
        self,
        *,
        calibration_id: str,
        surface_id: str,
        device_id: str,
        now_ms: int | None = None,
    ) -> bool:
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        rec = self._active.get(calibration_id)
        if not rec or not rec.get("active"):
            return False
        if rec["surface_id"] != surface_id or rec["device_id"] != device_id:
            return False
        if now > int(rec["expires_ts_ms"]):
            return False
        return True
