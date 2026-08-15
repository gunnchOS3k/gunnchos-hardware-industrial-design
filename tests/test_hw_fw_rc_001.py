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


def test_rc001_handheld_tip_drc_not_cont_ix():
    tip = json.loads((RC / "eda" / "handheld_hybrid_drc_tip.json").read_text())
    vs = tip.get("violations") or []
    assert sum(1 for v in vs if v.get("severity") == "error") == 0
    assert len(vs) == 39
    assert all(v.get("type") == "lib_footprint_mismatch" for v in vs)
    status = json.loads(
        (ROOT / "device_designs/handheld_hybrid/manufacturing/ERC_DRC_STATUS.json").read_text()
    )
    assert status["drc"]["errors"] == 0
    assert status["drc"]["warnings"] == 39
    assert status["drc"]["track_dangling"] == 0
    assert status["drc"]["silk_over_copper"] == 0
    assert "handheld_hybrid_drc_tip.json" in status["drc"]["source"]
    # Cont IX stale signature must not appear as current DRC
    assert status["drc"]["warnings"] != 50
    pkg = json.loads(
        (RC / "products/handheld_hybrid/DIGITAL_RELEASE_PACKAGE.json").read_text()
    )
    assert pkg["eda"]["drc"]["warnings"] == 39
    assert pkg["eda"]["drc"]["track_dangling"] == 0
    assert pkg["eda"]["drc"]["silk_over_copper"] == 0
    assert "Cont IX" not in str(pkg["eda"]["drc"].get("source") or "")
    summary = json.loads((RC / "PACKET_SUMMARY.json").read_text())
    hh = summary["erc_drc"]["handheld_hybrid"]
    assert hh["drc_warnings"] == 39
    assert hh["track_dangling"] == 0
    assert hh["silk_over_copper"] == 0


def test_rc001_self_challenge_rejects_stale_handheld_drc():
    vp = json.loads((RC / "SELF_CHALLENGE_VP.json").read_text())
    assert vp["verdict"] == "PASS"
    assert not any(f["challenge"] == "handheld_drc_stale_cont_ix" and f["result"] == "FAIL" for f in vp["findings"])
    assert any(f["challenge"] == "handheld_tip_drc_cited" and f["result"] == "PASS" for f in vp["findings"])


def test_rc001_nda_tokens_stay_false_no_placeholder():
    tokens = json.loads((RC / "TOKENS_HW_FW_RC_001.json").read_text())["tokens"]
    assert tokens["STUDENT_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False
    assert tokens["DSXL_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False
    assert tokens["DOCK_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is False
    assert tokens["HANDHELD_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is True
    assert tokens["RING_HW_DIGITAL_RELEASE_PACKAGE"]["earned"] is True
    ext = json.loads((RC / "EDMUND_EXTERNAL_BLOCKERS.json").read_text())
    ids = {b["id"] for b in ext["blockers"]}
    assert "EXT-COM-HPC-400PIN" in ids
    assert "EXT-DSXL-DUAL-EDP" in ids
    assert "EXT-JHL8440-BALLMAP" in ids
    assert "EXT-JHL9040R-BALLMAP" in ids
    assert ext["policy"]["no_invented_nda_pin_maps"] is True
    dock_topo = json.loads(
        (ROOT / "device_designs/dock/digital_release/USB4_TB4_40G_TOPOLOGY.json").read_text()
    )
    assert dock_topo["tb5"] is False
    assert dock_topo["link_gbps"] == 40
    dsxl = json.loads(
        (ROOT / "device_designs/ds_xl_coder/digital_release/DISPLAY_TOPOLOGY.json").read_text()
    )
    assert dsxl["independent_useful_displays"] == 2
    assert dsxl["invented_com_pin_numbers"] is False
    assert dsxl["pin_accurate_status"] == "EXTERNAL_NDA"
    ledger = json.loads((RC / "RING_FOOTPRINT_LEDGER.json").read_text())
    assert ledger["tip_kicad_pcb_footprint_count"] == 11
    assert ledger["cont_ix_routing_completeness_footprints"] == 15
    assert ledger["tip_authoritative_for_rc001"] is True
    assert ledger["blocking"] is False


def test_rc001_tip_drc_citations_for_nda_products():
    for p, warns in (
        ("student_14_5", 50),
        ("ds_xl_coder", 51),
        ("dock", 39),
        ("edge_io_rings", 22),
    ):
        tip = json.loads((RC / "eda" / f"{p}_drc_tip.json").read_text())
        assert len(tip["violations"]) == warns
        status = json.loads(
            (ROOT / f"device_designs/{p}/manufacturing/ERC_DRC_STATUS.json").read_text()
        )
        assert status["drc"]["warnings"] == warns
        assert f"{p}_drc_tip.json" in status["drc"]["source"]
        pkg = json.loads((RC / "products" / p / "DIGITAL_RELEASE_PACKAGE.json").read_text())
        assert pkg["eda"]["drc"]["warnings"] == warns
        assert f"{p}_drc_tip.json" in str(pkg["eda"]["drc"].get("source") or "")


def test_rc001_dvpr_covers_domains():
    dvpr = json.loads((RC / "DVPR_MASTER.json").read_text())
    assert dvpr["row_count"] >= 16 * 4  # 5 products minus dock-battery
    domains = {r["requirement"].split()[0] for r in dvpr["rows"]}
    assert "electrical" in domains or any("electrical" in r["id"] for r in dvpr["rows"])
