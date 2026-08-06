"""Latency hooks for authenticated ring input path."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class LatencyHooks:
    samples: list[dict[str, Any]] = field(default_factory=list)

    def mark(self, stage: str, **meta: Any) -> float:
        ts = time.perf_counter()
        self.samples.append({"stage": stage, "perf_counter": ts, **meta})
        return ts

    def span_ms(self, start_stage: str, end_stage: str) -> float | None:
        start = next((s for s in reversed(self.samples) if s["stage"] == start_stage), None)
        end = next((s for s in reversed(self.samples) if s["stage"] == end_stage), None)
        if not start or not end:
            return None
        return (end["perf_counter"] - start["perf_counter"]) * 1000.0

    def summary(self) -> dict[str, Any]:
        encode_ms = self.span_ms("encode_start", "encode_end")
        verify_ms = self.span_ms("verify_start", "verify_end")
        return {
            "encode_ms": encode_ms,
            "verify_ms": verify_ms,
            "sample_count": len(self.samples),
            "evidence_class": "SOFTWARE_SIMULATED",
        }
