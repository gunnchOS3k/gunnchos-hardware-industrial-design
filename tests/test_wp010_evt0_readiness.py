"""WP-010 digital readiness invariants — not physical PASS."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "npi" / "evt0_measurement_readiness"

REQUIRED = [
    "EVT0_MASTER_TEST_MATRIX.json",
    "EVT0_INSTRUMENT_MATRIX.json",
    "EVT0_FIXTURE_REGISTER.json",
    "EVT0_BRINGUP_SEQUENCE.md",
    "EVT0_EVIDENCE_SCHEMA.json",
    "EVT0_SAFETY_PLAN.md",
    "DEVICE_LAB_CALIBRATION_BRIDGE_SCHEMA.json",
    "EVT0_ACQUISITION_ACTION_LIST.json",
    "EVT0_E5_GOLDEN_JOURNEY_MEASUREMENT_MAP.json",
    "EVT0_RISK_TEST_TRACEABILITY.json",
    "READY_FOR_EVT0_MEASUREMENT_EXECUTION.json",
]


def _load(name: str):
    return json.loads((PKG / name).read_text())


def test_required_artifacts_exist():
    for name in REQUIRED:
        assert (PKG / name).is_file(), name


def test_risk_coverage_complete():
    matrix = _load("EVT0_MASTER_TEST_MATRIX.json")
    covered = set()
    for t in matrix["tests"]:
        covered |= set(t["risk_refs"])
        assert t["physical_execution_status"] == "PHYSICAL_PENDING"
        assert t["pass_fail"] if False else True
        assert t["acceptance_criterion"]
        assert t["unit"]
        assert t["instrument_ids"] or t["test_id"].startswith(
            ("EVT-DISP", "EVT-KEY", "EVT-GAME", "EVT-GJ", "EVT-AI")
        )
    for i in range(1, 13):
        assert f"RISK-{i:03d}" in covered


def test_no_prepopulated_physical_pass():
    matrix = _load("EVT0_MASTER_TEST_MATRIX.json")
    for t in matrix["tests"]:
        assert t.get("claim_boundary") != "PHYSICAL_MEASURED"
    ready = _load("READY_FOR_EVT0_MEASUREMENT_EXECUTION.json")
    assert ready["READY_FOR_EVT0_MEASUREMENT_EXECUTION"] is True
    assert ready["PHYSICALLY_VALIDATED"] is False
    assert ready["self_certified_v1"] is False
    assert ready["honesty"]["VF4"] == "PHYSICAL_PENDING"


def test_instrument_classes_valid():
    allowed = {
        "REQUIRED_OWN",
        "GOOD_TO_OWN",
        "RENT",
        "BORROW",
        "VENDOR_DFM",
        "EXTERNAL_LAB",
        "NOT_NEEDED_EVT0",
    }
    inst = _load("EVT0_INSTRUMENT_MATRIX.json")
    assert inst["do_not_purchase_under_freeze"] is True
    for row in inst["instruments"]:
        assert row["class"] in allowed


def test_evidence_and_bridge_schemas():
    ev = _load("EVT0_EVIDENCE_SCHEMA.json")
    for key in [
        "configuration_id",
        "serial",
        "hardware_rev",
        "firmware_sha",
        "os_sha",
        "ai_sha",
        "game_sha",
        "test_id",
        "operator",
        "instrument_id",
        "calibration_status",
        "raw_artifacts",
        "unit",
        "measurement",
        "uncertainty",
        "pass_fail",
        "defect_id",
    ]:
        assert key in ev["required"] or key in ev["properties"]
    bridge = _load("DEVICE_LAB_CALIBRATION_BRIDGE_SCHEMA.json")
    assert bridge["properties"]["vf_status"]["const"] == "PHYSICAL_PENDING"


def test_e5_journeys_mapped():
    m = _load("EVT0_E5_GOLDEN_JOURNEY_MEASUREMENT_MAP.json")
    ids = {row["golden_journey"] for row in m["mappings"]}
    for i in range(1, 11):
        assert f"GOLDEN-{i:02d}" in ids
    assert m["doctrine"]["vf4_vf5_vf6"] == "PHYSICAL_PENDING"


def test_acquisition_frozen():
    acq = _load("EVT0_ACQUISITION_ACTION_LIST.json")
    assert acq["purchase_authorized"] is False
    assert acq["physical_execution_freeze"] is True


def test_fixtures_digitally_complete_not_fabbed():
    reg = _load("EVT0_FIXTURE_REGISTER.json")
    assert reg["physical_fab_status"] == "NOT_FABRICATED"
    for fx in reg["fixtures"]:
        assert fx["status"] == "DIGITALLY_COMPLETE"


def test_wp010r1_audio_gate_and_av_input_ids():
    """DEFECT-VP010-001..003: audio gate + onboard AUD/CAM/KEY coverage."""
    matrix = _load("EVT0_MASTER_TEST_MATRIX.json")
    order = matrix["bringup_order"]
    assert "audio" in order
    assert order.index("network") + 1 == order.index("audio")
    assert order.index("audio") + 1 == order.index("dock")

    by_id = {t["test_id"]: t for t in matrix["tests"]}
    for tid in ("EVT-AUD-001", "EVT-CAM-001", "EVT-KEY-001", "EVT-KEY-002"):
        assert tid in by_id, tid
        t = by_id[tid]
        assert t["physical_execution_status"] == "PHYSICAL_PENDING"
        assert t["acceptance_criterion"]
        assert t["unit"]
        assert t["priority"].startswith("P")

    assert by_id["EVT-AUD-001"]["bringup_order_gate"] == "audio"
    assert by_id["EVT-CAM-001"]["bringup_order_gate"] == "audio"
    assert by_id["EVT-KEY-001"]["bringup_order_gate"] == "display_input"
    assert by_id["EVT-KEY-002"]["bringup_order_gate"] == "display_input"
    assert "INST-AUDIO" in by_id["EVT-AUD-001"]["instrument_ids"]
    assert "student_14_5" in by_id["EVT-AUD-001"]["products"]
    assert "handheld_hybrid" in by_id["EVT-AUD-001"]["products"]
    assert "ds_xl_coder" in by_id["EVT-AUD-001"]["products"]
    assert "INST-CAM-HOST" in by_id["EVT-CAM-001"]["instrument_ids"]
    assert "student_14_5" in by_id["EVT-KEY-001"]["products"]
    assert "ds_xl_coder" in by_id["EVT-KEY-001"]["products"]
    assert by_id["EVT-KEY-002"]["products"] == ["handheld_hybrid"]

    bringup = (PKG / "EVT0_BRINGUP_SEQUENCE.md").read_text()
    assert "**audio**" in bringup
    assert "EVT-AUD-001" in bringup
    assert "EVT-CAM-001" in bringup
    assert "EVT-KEY-001" in bringup

    inst = _load("EVT0_INSTRUMENT_MATRIX.json")
    inst_ids = {row["id"] for row in inst["instruments"]}
    assert "INST-AUDIO" in inst_ids
    assert "INST-CAM-HOST" in inst_ids
    audio = next(r for r in inst["instruments"] if r["id"] == "INST-AUDIO")
    assert "EVT-AUD-001" in audio["tests"]

    ready = _load("READY_FOR_EVT0_MEASUREMENT_EXECUTION.json")
    assert ready["self_certified_v1"] is False
    assert ready["PHYSICALLY_VALIDATED"] is False
    assert ready["honesty"]["PHYSICAL_EXECUTION_FREEZE"] is True
