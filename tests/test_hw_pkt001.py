"""STREAM-C-PKT-001 honesty gates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKT = ROOT / "artifacts" / "hw_pkt001"


def test_pkt001_package_complete_remains_false():
    summary = json.loads((PKT / "PACKET_SUMMARY.json").read_text())
    assert summary["HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE"] is False
    assert summary["physical_pass"] is False
    assert summary["SHIPPING_IMAGE"] is False
    assert summary["PRODUCTION_RELEASE_CLAIMED"] is False
    assert summary["SoA"] is False
    assert summary["PHYSICAL"] is False
    assert summary["npi"]["NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001"] == "CLOSED"


def test_pkt001_image_fit_remeasure_authentic():
    vp = json.loads((PKT / "VP_IMAGE_FIT_REMEASURE.json").read_text())
    dos = json.loads((PKT / "image_fit" / "IMAGE_FIT_MANIFEST.json").read_text())
    assert vp["device_os_tip"] == "a1e11efcb502ce053d755a2539c26d252e216226"
    assert vp["verdict"] == "PASS_PRODUCTION_INTENT_DIGITAL_FIT"
    assert vp["npi_status"] == "CLOSED"
    assert vp["SHIPPING_IMAGE"] is False
    assert vp["PRODUCTION_RELEASE_CLAIMED"] is False
    assert vp["authenticity"]["stub_like_rootfs_payloads"] is False
    assert vp["authenticity"]["production_intent_digital_present"] is True
    for slot in ("slot_a", "slot_b", "recovery"):
        assert vp["margins_gib"][slot] > 0
    assert dos["npi"]["recommended_status"] == "CLOSE"
    assert dos["fit_assessment"]["production_image_fit_verdict"] == "PASS_PRODUCTION_INTENT_DIGITAL_FIT"


def test_pkt001_kicad_cli_zero_errors():
    cli = json.loads((PKT / "kicad_cli" / "CLI_RESULTS.json").read_text())
    assert len(cli["results"]) == 5
    for r in cli["results"]:
        assert r.get("status") == "RAN"
        assert r["erc"]["errors"] == 0
        assert r["drc"]["errors"] == 0


def test_pkt001_validators_pass():
    val = json.loads((PKT / "DIGITAL_VALIDATORS.json").read_text())
    assert val["overall"] == "PASS"
