"""C-PKT-003 hardware EVT digital readiness honesty checks."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "c_pkt_003"


def test_firmware_gap_matrix_five_devices():
    gap = json.loads((ART / "FIRMWARE_GAP_MATRIX.json").read_text())
    assert set(gap["devices"]) == {
        "student_14_5",
        "ds_xl_coder",
        "handheld_hybrid",
        "dock",
        "edge_io_rings",
    }
    assert gap["devices"]["edge_io_rings"]["token_earned"] is True
    assert gap["devices"]["student_14_5"]["token_earned"] is False
    assert gap["devices"]["student_14_5"]["on_target_build"] == "VENDOR_TOOLCHAIN_EXTERNAL"
    assert gap["summary"]["PHYSICAL_FACTORY_PASS"] is False


def test_evt_digital_infra_ready_not_physical():
    matrix = json.loads((ART / "EVT_READINESS_MATRIX.json").read_text())
    assert matrix["EVT_DIGITAL_EXECUTION_INFRA_READY"] is True
    assert matrix["EVT_PHYSICAL_PASS"] is False
    assert matrix["FACTORY_PHYSICAL_PASS"] is False
    assert (ART / "EVT_EXECUTION_RUNBOOK.md").is_file()
    for prod in matrix["devices"]:
        assert (ART / "evt" / prod / "EVT_DIGITAL_PACKET.json").is_file()


def test_hil_mock_not_factory_pass():
    contract = json.loads((ART / "factory_hil" / "HIL_INTERFACE_CONTRACT.json").read_text())
    assert contract["PHYSICAL_FACTORY_PASS"] is False
    for prod in ("student_14_5", "ds_xl_coder", "handheld_hybrid", "dock", "edge_io_rings"):
        res = json.loads((ART / "factory_hil" / "results" / f"{prod}_hil_mock.json").read_text())
        assert res["FACTORY_PHYSICAL_PASS"] is False
        assert res["mode"] == "MOCK_DIGITAL_ONLY"
