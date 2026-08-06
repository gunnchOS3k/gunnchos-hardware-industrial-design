"""Safe fallback when authenticated ring input is unavailable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SafeFallback:
    """Never silently accept unauthenticated ring events."""

    available_modalities: list[str] = field(
        default_factory=lambda: ["keyboard", "touch", "trackpad"]
    )
    active: bool = False
    reason: str = ""

    def engage(self, reason: str) -> dict[str, Any]:
        self.active = True
        self.reason = reason
        return {
            "fallback_active": True,
            "reason": reason,
            "modalities": list(self.available_modalities),
            "silent_accept": False,
        }

    def status(self) -> dict[str, Any]:
        return {
            "fallback_active": self.active,
            "reason": self.reason,
            "modalities": list(self.available_modalities),
            "available": len(self.available_modalities) > 0,
        }
