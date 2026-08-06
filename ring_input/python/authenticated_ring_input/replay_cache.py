"""Anti-replay cache keyed by (device_id, session_id, seq)."""

from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class ReplayCache:
    ttl_ms: int = 120_000
    _seen: dict[tuple[str, str, int], int] = field(default_factory=dict)

    def seen(self, device_id: str, session_id: str, seq: int, now_ms: int | None = None) -> bool:
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        self._purge(now)
        return (device_id, session_id, seq) in self._seen

    def remember(
        self, device_id: str, session_id: str, seq: int, now_ms: int | None = None
    ) -> None:
        now = now_ms if now_ms is not None else int(time.time() * 1000)
        self._purge(now)
        self._seen[(device_id, session_id, seq)] = now

    def _purge(self, now_ms: int) -> None:
        expired = [k for k, ts in self._seen.items() if now_ms - ts > self.ttl_ms]
        for k in expired:
            del self._seen[k]
