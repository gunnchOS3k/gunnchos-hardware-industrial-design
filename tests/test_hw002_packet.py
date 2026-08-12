"""HW-002 packet honesty gates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HW002 = ROOT / "artifacts" / "hw002"


def test_hw002_package_complete_remains_false():
    summary = json.loads((HW002 / "HW002_PACKET_SUMMARY.json").read_text())
    assert summary["HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE"] is False
    assert summary["physical_pass"] is False
    assert summary["npi"]["NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001"] == "OPEN"
    assert summary["npi"]["NPI_DEFECT-HANDHELD-EDA-DANGLING-SILK-001"] == "CLOSED"
    assert summary["zephyr_west"]["west_build_pass"] is True
    assert summary["zephyr_west"]["soft_skip"] is False


def test_hw002_west_probe_no_soft_skip():
    probe = json.loads((HW002 / "zephyr_west" / "ZEPHYR_WEST_PROBE.json").read_text())
    assert probe["west_build_pass"] is True
    assert probe["soft_skip"] is False
    assert probe["blockers"] == []


def test_hw002_image_fit_stays_open():
    defect = json.loads(
        (ROOT / "npi/phase_xv/handheld_storage_headroom/NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001.json").read_text()
    )
    remodel = json.loads(
        (ROOT / "npi/phase_xv/handheld_storage_headroom/HANDHELD_STORAGE_IMAGE_FIT_REMODEL.json").read_text()
    )
    assert defect["status"] == "OPEN"
    assert remodel["npi_status"] == "OPEN"
    assert remodel["fit_assessment"]["production_image_fit_verdict"] == "FAIL"
    assert remodel["hardware_truth"]["larger_emmc_sku_invented"] is False


def test_hw002_west_script_forbids_soft_skip():
    script = (ROOT / "firmware/edge_io_rings/zephyr_west/scripts/require_west_build.sh").read_text()
    assert "soft-skip" in script.lower() or "soft_skip" in script.lower()
    assert "exit 1" in script
    assert "RING_ZEPHYR_WEST_BUILD_FAIL" in script
