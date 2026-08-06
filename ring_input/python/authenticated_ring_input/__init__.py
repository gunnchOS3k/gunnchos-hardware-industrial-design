"""Authenticated ring input reference implementation (software only).

Statuses: AUTHENTICATED_INPUT_PROTOCOL_PASS · RING_PHYSICAL_PROTOTYPE_PENDING
No physical ring is claimed.
"""

from .audit import AuditLog
from .calibration import CalibrationRegistry
from .codec import decode_event, encode_event, mac_payload
from .fallback import SafeFallback
from .latency import LatencyHooks
from .pairing import PairingStateMachine
from .receiver import AuthenticatedReceiver, RejectReason
from .replay_cache import ReplayCache
from .revocation import RevocationRegistry
from .sender import AuthenticatedSender
from .simulated_stream import SimulatedSensorStream

__all__ = [
    "AuditLog",
    "AuthenticatedReceiver",
    "AuthenticatedSender",
    "CalibrationRegistry",
    "LatencyHooks",
    "PairingStateMachine",
    "RejectReason",
    "ReplayCache",
    "RevocationRegistry",
    "SafeFallback",
    "SimulatedSensorStream",
    "decode_event",
    "encode_event",
    "mac_payload",
]

PROTOCOL_VERSION = "1.0"
STATUSES = {
    "AUTHENTICATED_INPUT_PROTOCOL_PASS": True,
    "RING_PHYSICAL_PROTOTYPE_PENDING": True,
}
PHYSICAL_RING_CLAIMED = False
