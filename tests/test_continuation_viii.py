"""Continuation VIII manufacturer-release package guards."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "continuation_viii_manufacturer_release"

PRODUCTS = (
    "student_14_5",
    "ds_xl_coder",
    "handheld_hybrid",
    "edge_io_rings",
    "dock",
)

REQUIRED_SYMBOLS = {
    "student_14_5": {"COMHPC_PUBLIC", "BUCK", "PD_CTRL", "USB_C"},
    "ds_xl_coder": {"COMHPC_PUBLIC", "PANEL_EDP", "PANEL_EDP2", "BUCK"},
    "handheld_hybrid": {"SODIMM260", "HID_MCU", "BUCK", "USB_C"},
    "edge_io_rings": {"NRF52840", "NPM1300", "BMI270", "IQS7222A"},
    "dock": {"JHL8440_ROLE", "VL817", "RTL8156", "USB_C"},
}


def test_cont_viii_artifacts_present():
    for name in (
        "READINESS_SCORECARDS.json",
        "TOKENS_CONT_VIII.json",
        "COM_HPC_FINAL_DECISION_CONT_VIII.json",
        "BLOCKERS_CONT_VIII.json",
        "SUMMARY.md",
    ):
        assert (ART / name).is_file(), name


def test_cont_viii_option_b_decision():
    decision = json.loads((ART / "COM_HPC_FINAL_DECISION_CONT_VIII.json").read_text())
    assert decision["final_decision"] == "OPTION_B_KEEP_ADLINK_ACCEPT_NARROW_EXTERNAL_BLOCK"
    assert decision["evaluation"]["C_feasible"] is False
    assert decision["dock_freeze"] == "USB4/TB4 (not TB5)"


def test_cont_viii_schematics_functional_not_funcblock():
    for prod in PRODUCTS:
        sch = (ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_sch").read_text(
            encoding="utf-8"
        )
        assert "(wire " in sch
        assert 'lib_id "FuncBlock"' not in sch
        for sym in REQUIRED_SYMBOLS[prod]:
            assert f'lib_id "{sym}"' in sch, f"{prod} missing {sym}"


def test_cont_viii_readiness_honesty():
    cards = json.loads((ART / "READINESS_SCORECARDS.json").read_text())
    for prod in PRODUCTS:
        card = cards[prod]
        assert card["manufacturer_ready"] == "conditional"
        assert card["erc_errors"] == 0
        assert card["drc_errors"] == 0
        # Boolean true manufacturer_ready is forbidden while proxies/NDA remain.
        assert card["manufacturer_ready"] is not True


def test_cont_viii_blockers_buckets_only():
    blockers = json.loads((ART / "BLOCKERS_CONT_VIII.json").read_text())
    for key in ("DIGITAL", "PHYSICAL", "EXTERNAL"):
        assert key in blockers
        assert isinstance(blockers[key], list)
    assert blockers["DIGITAL"], "expected residual digital packaging work"
