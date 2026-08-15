"""HW-FW-RC-001 digital release package honesty gates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RC = ROOT / "artifacts" / "hw_fw_rc_001"
PRODUCTS = [
    "student_14_5",
    "ds_xl_coder",
    "handheld_hybrid",
    "dock",
    "edge_io_rings",
]
TOKENS = [
    "STUDENT_HW_DIGITAL_RELEASE_PACKAGE",
    "DSXL_HW_DIGITAL_RELEASE_PACKAGE",
    "HANDHELD_HW_DIGITAL_RELEASE_PACKAGE",
    "DOCK_HW_DIGITAL_RELEASE_PACKAGE",
    "RING_HW_DIGITAL_RELEASE_PACKAGE",
]
FALSE_ALWAYS = [
    "EVT_PASS",
    "DVT_PASS",
    "PVT_PASS",
    "RF_CERTIFIED",
    "EMC_CERTIFIED",
    "BATTERY_CERTIFIED",
    "SHIPPING_HARDWARE",
]


def test_rc001_artifacts_present():
    assert (RC / "PACKET_SUMMARY.json").is_file()
    assert (RC / "TOKENS_HW_FW_RC_001.json").is_file()
    assert (RC / "VENDOR_TRUTH_REFRESH.json").is_file()
    assert (RC / "DVPR_MASTER.json").is_file()
    assert (RC / "USB_DOCK_DIGITAL_VALIDATE.json").is_file()
    assert (RC / "COMPATIBILITY_MATRIX.json").is_file()
    assert (RC / "RING_SENSING_MAP.json").is_file()
    assert (RC / "SELF_CHALLENGE_VP.json").is_file()
    for p in PRODUCTS:
        assert (RC / "products" / p / "DIGITAL_RELEASE_PACKAGE.json").is_file()
        assert (ROOT / "device_designs" / p / "digital_release" / "INDEX.json").is_file()


def test_rc001_false_physical_certs():
    tokens = json.loads((RC / "TOKENS_HW_FW_RC_001.json").read_text())
    summary = json.loads((RC / "PACKET_SUMMARY.json").read_text())
    for k in FALSE_ALWAYS:
        assert tokens[k] is False
        assert summary.get(k, False) is False or k not in summary
    assert tokens["HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE"] is False
    assert summary["HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE"] is False


def test_rc001_vendor_truth_anchors():
    v = json.loads((RC / "VENDOR_TRUTH_REFRESH.json").read_text())
    a = v["anchors"]
    assert a["student_dsxl_com"]["mpn"] == "COM-HPC-mMTL-155H-32G"
    assert a["handheld_som"]["mpn"] == "RM121-D8E32"
    assert a["handheld_som"]["storage_architecture"]["emmc"] == "system/recovery"
    assert a["cellular"]["mpn"] == "RM520N-GL"
    assert a["cellular"]["ntn"] is False
    assert a["cellular"]["is_6g"] is False
    assert a["dock"]["controller"] == "JHL8440"
    assert a["dock"]["retimer"] == "JHL9040R"
    assert a["dock"]["tb5"] is False
    assert a["rings"]["cap"] == "IQS7222A"


def test_rc001_dock_not_tb5():
    usb = json.loads((RC / "USB_DOCK_DIGITAL_VALIDATE.json").read_text())
    assert usb["silicon"]["link_gbps"] == 40
    assert usb["silicon"]["tb5"] is False
    assert usb["silicon"]["controller"] == "JHL8440"


def test_rc001_ring_not_imu_only():
    ring = json.loads((RC / "RING_SENSING_MAP.json").read_text())
    assert ring["imu_only_absolute_position"] is False
    assert "CAP_IQS7222A" in ring["modalities_required"]
    assert "SE_SE050" in ring["modalities_required"]
    for action in ("pointer", "click", "text", "delete", "shortcut", "gaming"):
        assert action in ring["action_map"]
    assert ring["spatial_accuracy"] == "PHYSICAL_PENDING"


def test_rc001_nda_products_prefer_fail_tokens():
    tokens = json.loads((RC / "TOKENS_HW_FW_RC_001.json").read_text())["tokens"]
    # Prefer FAIL: Student/DS-XL/Dock withhold while NDA pin-accurate fanout EXTERNAL
    assert tokens["STUDENT_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False
    assert tokens["DSXL_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False
    assert tokens["DOCK_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False


def test_rc001_handheld_ring_token_requires_gates():
    tokens = json.loads((RC / "TOKENS_HW_FW_RC_001.json").read_text())["tokens"]
    for name in ("HANDHELD_HW_DIGITAL_RELEASE_PACKAGE", "RING_HW_DIGITAL_RELEASE_PACKAGE"):
        t = tokens[name]
        if t["earned"]:
            assert t["criteria"]["erc_pass"] is True
            assert t["criteria"]["firmware_builds"] is True
            assert t["criteria"]["bom_avl_honest"] is True
            assert t["criteria"]["s0_digital_zero"] is True
            assert t["criteria"]["s1_digital_zero"] is True


def test_rc001_no_bare_cpu_in_student_legacy_bom():
    text = (ROOT / "bom" / "student_14_5" / "bom.csv").read_text()
    assert "COM-HPC-mMTL-155H-32G" in text
    assert "Core Ultra 7 155H,Application processor,BGA" not in text
    assert "UNKNOWN_UNTIL_QUOTE" in text
    # No fabricated numeric unit costs
    for line in text.splitlines()[1:]:
        cols = line.split(",")
        if len(cols) >= 9:
            assert cols[8] in {"UNKNOWN_UNTIL_QUOTE", "UNKNOWN", ""}


def test_rc001_self_challenge_no_tb5_or_imu_only_fail():
    vp = json.loads((RC / "SELF_CHALLENGE_VP.json").read_text())
    bad = [
        f
        for f in vp["findings"]
        if f["result"] == "FAIL"
        and f["challenge"] in {"fake_tb5", "ring_imu_only", "firmware_does_not_build"}
    ]
    assert bad == []


def test_rc001_dvpr_covers_domains():
    dvpr = json.loads((RC / "DVPR_MASTER.json").read_text())
    assert dvpr["row_count"] >= 16 * 4  # 5 products minus dock-battery
    domains = {r["requirement"].split()[0] for r in dvpr["rows"]}
    assert "electrical" in domains or any("electrical" in r["id"] for r in dvpr["rows"])
