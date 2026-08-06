"""Lost-device / session revocation registry."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RevocationRegistry:
    _devices: set[str] = field(default_factory=set)
    _sessions: set[str] = field(default_factory=set)

    def revoke_device(self, device_id: str) -> None:
        self._devices.add(device_id)

    def revoke_session(self, session_id: str) -> None:
        self._sessions.add(session_id)

    def is_revoked(self, device_id: str, session_id: str | None = None) -> bool:
        if device_id in self._devices:
            return True
        if session_id is not None and session_id in self._sessions:
            return True
        return False
