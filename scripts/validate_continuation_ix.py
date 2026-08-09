#!/usr/bin/env python3
"""Validate Continuation IX Pre-EVT digital lock gates."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/continuation_ix_pre_evt"
DOCS = ROOT / "docs/full_product_family"
PRODUCTS = [
    "handheld_hybrid",
    "edge_io_rings",
    "dock",
    "student_14_5",
    "ds_xl_coder",
]


def main() -> int:
    errors: list[str] = []
    required = [
        ART / "SUMMARY.md",
        ART / "TOKENS_CONT_IX.json",
        ART / "BLOCKERS_CONT_IX.json",
        ART / "COM_HPC_FINAL_DECISION_CONT_IX.json",
        ART / "READINESS_SCORECARDS.json",
        ART / "MANIFEST.json",
        ART / "FOOTPRINT_LEDGER_STATUS.json",
        ART / "EXTERNAL_VENDOR_COLLATERAL_REQUIRED.json",
        ART / "ROUTING_COMPLETENESS.json",
        ROOT / "docs/release/FOOTPRINT_VERIFICATION_LEDGER.csv",
        DOCS / "COM_HPC_FINAL_DECISION_CONT_IX.md",
        DOCS / "TOKENS_CONT_IX.md",
        DOCS / "BLOCKERS_CONT_IX.md",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"missing {p}")

    if (ART / "COM_HPC_FINAL_DECISION_CONT_IX.json").exists():
        decision = json.loads((ART / "COM_HPC_FINAL_DECISION_CONT_IX.json").read_text())
        if decision.get("PRODUCTION_ARCHITECTURE") != "ADLINK":
            errors.append("expected PRODUCTION_ARCHITECTURE=ADLINK")
        if decision.get("VENDOR_COLLATERAL_REQUIRED") is not True:
            errors.append("expected VENDOR_COLLATERAL_REQUIRED=True")
        if "OPTION_B" not in decision.get("final_decision", ""):
            errors.append("expected Option B retained")

    for product in PRODUCTS:
        sch = ROOT / f"device_designs/{product}/kicad/{product}.kicad_sch"
        pcb = ROOT / f"device_designs/{product}/kicad/{product}.kicad_pcb"
        if not sch.exists() or not pcb.exists():
            errors.append(f"missing kicad for {product}")
            continue
        sch_txt = sch.read_text(encoding="utf-8")
        pcb_txt = pcb.read_text(encoding="utf-8")
        if 'lib_id "FuncBlock"' in sch_txt:
            errors.append(f"{product} still places FuncBlock")
        if "continuation_ix" not in sch_txt:
            errors.append(f"{product} schematic not Cont IX generator")
        if "Block_SMD_safe" in pcb_txt:
            errors.append(f"{product} PCB still has Block_SMD_safe proxy")
        if "_proxy" in pcb_txt.lower():
            errors.append(f"{product} PCB still has proxy footprint name")
        if "gunnchos_production:" not in pcb_txt:
            errors.append(f"{product} PCB missing gunnchos_production footprints")
        for doc in (
            "ASSEMBLY_WORK_INSTRUCTION.md",
            "ASSEMBLY_SEQUENCE.md",
            "TORQUE_TABLE.csv",
            "QC_CHECKLIST.md",
            "PROGRAMMING.md",
            "CALIBRATION.md",
            "REWORK.md",
        ):
            if not (ROOT / f"device_designs/{product}/manufacturing/{doc}").exists():
                errors.append(f"missing {product} manufacturing/{doc}")

    # Handheld hierarchical sheets
    sheets = list((ROOT / "device_designs/handheld_hybrid/kicad/sheets").glob("sodimm_*.kicad_sch"))
    if len(sheets) < 10:
        errors.append(f"handheld hierarchical sheets expected >=10, got {len(sheets)}")

    if (ART / "BLOCKERS_CONT_IX.json").exists():
        blockers = json.loads((ART / "BLOCKERS_CONT_IX.json").read_text())
        for key in ("DIGITAL", "PHYSICAL", "EXTERNAL"):
            if key not in blockers:
                errors.append(f"blockers missing {key}")
        # Cont VIII FuncBlock retirement must stay
        for product in PRODUCTS:
            sch = (ROOT / f"device_designs/{product}/kicad/{product}.kicad_sch").read_text(encoding="utf-8")
            if 'lib_id "FuncBlock"' in sch:
                errors.append(f"Cont VIII FuncBlock retirement violated on {product}")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS Cont IX validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
