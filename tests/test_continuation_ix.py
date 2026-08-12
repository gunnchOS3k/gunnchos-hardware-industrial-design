"""Continuation IX Pre-EVT digital lock gates."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "continuation_ix_pre_evt"
PRODUCTS = (
    "student_14_5",
    "ds_xl_coder",
    "handheld_hybrid",
    "edge_io_rings",
    "dock",
)


def test_cont_ix_artifacts_present():
    for name in (
        "READINESS_SCORECARDS.json",
        "TOKENS_CONT_IX.json",
        "COM_HPC_FINAL_DECISION_CONT_IX.json",
        "BLOCKERS_CONT_IX.json",
        "SUMMARY.md",
        "FOOTPRINT_LEDGER_STATUS.json",
        "EXTERNAL_VENDOR_COLLATERAL_REQUIRED.json",
        "ROUTING_COMPLETENESS.json",
        "MANIFEST.json",
    ):
        assert (ART / name).is_file(), name
    assert (ROOT / "docs/release/FOOTPRINT_VERIFICATION_LEDGER.csv").is_file()


def test_cont_ix_adlink_decision():
    d = json.loads((ART / "COM_HPC_FINAL_DECISION_CONT_IX.json").read_text())
    assert d["PRODUCTION_ARCHITECTURE"] == "ADLINK"
    assert d["VENDOR_COLLATERAL_REQUIRED"] is True
    assert d["PUBLIC_HARDWARE_REPRODUCTION"] == "LIMITED"
    assert d["SOFTWARE_ADOPTION"] == "FULLY_SUPPORTED"
    assert "OPTION_B" in d["final_decision"]
    assert "TB5" not in d["dock_freeze"] or "not TB5" in d["dock_freeze"]


def test_cont_ix_no_proxy_no_funcblock():
    for prod in PRODUCTS:
        sch = (ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_sch").read_text(encoding="utf-8")
        pcb = (ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_pcb").read_text(encoding="utf-8")
        assert 'lib_id "FuncBlock"' not in sch
        assert "continuation_ix" in sch
        assert "Block_SMD_safe" not in pcb
        assert "gunnchos_production:" in pcb


def test_cont_ix_handheld_hierarchical_260():
    sheets = list((ROOT / "device_designs/handheld_hybrid/kicad/sheets").glob("sodimm_*.kicad_sch"))
    assert len(sheets) >= 10
    sch_info = json.loads((ART / "SCH_INFO.json").read_text())
    hh = next(s for s in sch_info if s["product"] == "handheld_hybrid")
    assert hh.get("sodimm_pins") == 260
    assert hh.get("hierarchical_sheets", 0) >= 10


def test_cont_ix_digital_blockers_empty_or_explained():
    blockers = json.loads((ART / "BLOCKERS_CONT_IX.json").read_text())
    assert "DIGITAL" in blockers and "PHYSICAL" in blockers and "EXTERNAL" in blockers
    # Prefer empty DIGITAL; if non-empty must be an explained digital gap
    # (execution failure, proxy/hierarchical layout, or tracked NPI_DEFECT OPEN).
    for item in blockers["DIGITAL"]:
        assert (
            "execution failure" in item
            or "proxy" in item
            or "hierarchical" in item
            or ("NPI_DEFECT" in item and "OPEN" in item)
        )


def test_cont_viii_funcblock_retirement_stays():
    for prod in PRODUCTS:
        sch = (ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_sch").read_text(encoding="utf-8")
        assert 'lib_id "FuncBlock"' not in sch
