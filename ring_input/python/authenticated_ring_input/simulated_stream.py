"""Simulated sensor stream — SOFTWARE_SIMULATED evidence only."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator


@dataclass
class SimulatedSensorStream:
    """Labeled simulated IMU/gesture samples. Not physical hardware evidence."""

    evidence_class: str = "SOFTWARE_SIMULATED"
    physical_ring_claimed: bool = False

    def generate(self, n: int = 8, base_ts_ms: int = 1_700_000_000_000) -> list[dict[str, Any]]:
        samples: list[dict[str, Any]] = []
        for i in range(n):
            samples.append(
                {
                    "evidence_class": self.evidence_class,
                    "physical_ring_claimed": False,
                    "ts_ms": base_ts_ms + i * 16,
                    "ax": 0.01 * i,
                    "ay": 0.02 * i,
                    "az": 0.98,
                    "gesture_hint": "pointer_move" if i % 3 else "click",
                    "confidence_hint": 0.92 if i % 4 else 0.35,
                }
            )
        return samples

    def iter_file(self, path: Path) -> Iterator[dict[str, Any]]:
        with path.open() as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                obj.setdefault("evidence_class", self.evidence_class)
                obj["physical_ring_claimed"] = False
                yield obj
