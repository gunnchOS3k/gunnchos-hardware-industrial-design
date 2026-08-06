"""Protocol tests for authenticated ring input vertical slice.

Evidence: SOFTWARE_SIMULATED fixtures only. Physical ring: PENDING.
"""

from __future__ import annotations

from pathlib import Path

from authenticated_ring_input import (
    AuthenticatedReceiver,
    AuthenticatedSender,
    CalibrationRegistry,
    PairingStateMachine,
    RejectReason,
    SafeFallback,
    SimulatedSensorStream,
)

FIX = Path(__file__).resolve().parents[1] / "fixtures"
BASE_TS = 1_700_000_000_000


def _pair(
    *,
    device_id: str = "ring-sim-001",
    user_id: str = "user-alice",
    host_id: str = "host-dsxl-01",
    secret: bytes = b"device-secret-software-only",
    scope: list[str] | None = None,
) -> PairingStateMachine:
    sm = PairingStateMachine(
        device_id=device_id,
        user_id=user_id,
        host_id=host_id,
        device_secret=secret,
        permission_scope=scope
        or [
            "pointer_move",
            "click",
            "key_press",
            "scroll",
            "heartbeat",
            "destructive_confirm",
        ],
    )
    sm.start_challenge()
    resp = sm.device_respond()
    assert sm.host_verify(resp)
    sm.confirm()
    assert sm.is_paired_offline()
    return sm


def _pipeline(now_ms: int = BASE_TS):
    sm = _pair()
    cal_reg = CalibrationRegistry()
    cal = cal_reg.create(
        surface_id="desk-surface-a",
        device_id=sm.device_id,
        user_id=sm.user_id,
        now_ms=now_ms,
    )
    sender = AuthenticatedSender(
        pairing=sm,
        target_device_id=sm.host_id,
        surface_id=cal["surface_id"],
        calibration_id=cal["calibration_id"],
    )
    sess = sender.open_session(offline=True, now_ms=now_ms)
    recv = AuthenticatedReceiver(host_id=sm.host_id, known_devices={sm.device_id})
    recv.calibration = cal_reg
    recv.now_ms = now_ms
    recv.register_session(sender.export_session_material())
    return sm, sender, recv, sess, cal


def test_valid_accept():
    _, sender, recv, _, _ = _pipeline()
    ev = sender.emit("pointer_move", confidence=0.95, payload={"dx": 1, "dy": 0}, ts_ms=BASE_TS)
    ok, reason, out = recv.receive(ev)
    assert ok and reason is None and out is not None
    assert out["seq"] == 0
    assert all(e.get("payload_omitted") for e in recv.audit.entries if e["decision"] == "accept")


def test_bad_signature():
    _, sender, recv, _, _ = _pipeline()
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    ev["mac"] = "0" * 64
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.BAD_SIGNATURE


def test_unknown_device():
    _, sender, recv, _, _ = _pipeline()
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    recv.known_devices.clear()
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.UNKNOWN_DEVICE


def test_wrong_target():
    _, sender, recv, _, _ = _pipeline()
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    # Re-sign would be needed for MAC; tamper target after signing → bad sig OR wrong target
    # Receiver checks target before MAC in our pipeline? Actually MAC then target order:
    # Looking at receiver: unknown, revoked, wrong_target, then MAC.
    # So if we change target after sign, wrong_target triggers first.
    ev["target_device_id"] = "host-other"
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.WRONG_TARGET


def test_replay():
    _, sender, recv, _, _ = _pipeline()
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    assert recv.receive(ev)[0]
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.REPLAY


def test_stale():
    _, sender, recv, _, _ = _pipeline(now_ms=BASE_TS)
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS - 60_000)
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.STALE


def test_revoked():
    sm, sender, recv, _, _ = _pipeline()
    recv.revocation.revoke_device(sm.device_id)
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.REVOKED


def test_low_confidence_destructive_rejected():
    _, sender, recv, _, _ = _pipeline()
    # Need destructive in scope — already included
    # First emit a heartbeat-level filler? seq 0 is destructive
    # Expand scope on sender pairing already has destructive_confirm
    # But session material permission_scope includes it
    ev = sender.emit("destructive_confirm", confidence=0.4, ts_ms=BASE_TS)
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.LOW_CONFIDENCE_DESTRUCTIVE


def test_calibration_mismatch():
    _, sender, recv, _, _ = _pipeline()
    sender.calibration_id = "cal-wrong"
    ev = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    ok, reason, _ = recv.receive(ev)
    assert not ok and reason == RejectReason.CALIBRATION_MISMATCH


def test_offline_paired():
    sm = _pair()
    assert sm.state == "PAIRED"
    assert sm.offline_capable
    assert sm.is_paired_offline()
    # Offline session open without network
    cal_reg = CalibrationRegistry()
    cal = cal_reg.create(
        surface_id="desk-surface-a",
        device_id=sm.device_id,
        user_id=sm.user_id,
        now_ms=BASE_TS,
    )
    sender = AuthenticatedSender(
        pairing=sm,
        target_device_id=sm.host_id,
        surface_id=cal["surface_id"],
        calibration_id=cal["calibration_id"],
    )
    sess = sender.open_session(offline=True, now_ms=BASE_TS)
    assert sess["offline"] is True


def test_fallback_available():
    fb = SafeFallback()
    status = fb.engage("link_lost")
    assert status["fallback_active"]
    assert status["silent_accept"] is False
    assert fb.status()["available"]


def test_key_rotation_path():
    _, sender, recv, _, _ = _pipeline()
    ev0 = sender.emit("click", confidence=0.95, ts_ms=BASE_TS)
    assert recv.receive(ev0)[0]
    new_ver = sender.rotate_session_key()
    assert new_ver == 2
    # Receiver must learn rotated key
    recv.register_session(sender.export_session_material())
    ev1 = sender.emit("click", confidence=0.95, ts_ms=BASE_TS + 10)
    ok, reason, out = recv.receive(ev1)
    assert ok and out["session_key_version"] == 2


def test_challenge_response_pairing_failure():
    sm = PairingStateMachine(
        device_id="ring-sim-001",
        user_id="user-alice",
        host_id="host-dsxl-01",
        device_secret=b"secret",
    )
    sm.start_challenge()
    sm.device_respond()
    assert sm.host_verify("deadbeef") is False
    assert sm.state == "FAILED"


def test_simulated_stream_labeled():
    stream = SimulatedSensorStream()
    samples = stream.generate(n=3, base_ts_ms=BASE_TS)
    assert all(s["evidence_class"] == "SOFTWARE_SIMULATED" for s in samples)
    assert all(s["physical_ring_claimed"] is False for s in samples)


def test_fixture_vectors_exist():
    pos = FIX / "test_vectors"
    neg = FIX / "negative"
    assert (pos / "valid_accept.json").exists()
    assert (neg / "bad_signature.json").exists()


def test_end_to_end_simulated_stream_to_receiver():
    _, sender, recv, _, _ = _pipeline()
    stream = SimulatedSensorStream()
    accepted = 0
    for sample in stream.generate(n=5, base_ts_ms=BASE_TS):
        # Skip low-confidence non-destructive by mapping to heartbeat if low
        et = sample["gesture_hint"]
        conf = sample["confidence_hint"]
        if conf < 0.7:
            continue
        ev = sender.emit(et, confidence=conf, payload={"sim": True}, ts_ms=sample["ts_ms"])
        recv.now_ms = sample["ts_ms"]
        ok, _, _ = recv.receive(ev)
        if ok:
            accepted += 1
    assert accepted >= 1
    # No raw motion in audit
    for e in recv.audit.entries:
        assert "ax" not in e and e.get("payload_omitted", True)


def test_statuses_constant():
    from authenticated_ring_input import PHYSICAL_RING_CLAIMED, STATUSES

    assert STATUSES["AUTHENTICATED_INPUT_PROTOCOL_PASS"] is True
    assert STATUSES["RING_PHYSICAL_PROTOTYPE_PENDING"] is True
    assert PHYSICAL_RING_CLAIMED is False
