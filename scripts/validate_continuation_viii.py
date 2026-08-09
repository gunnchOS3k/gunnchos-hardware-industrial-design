#!/usr/bin/env python3
"""Validate Continuation VIII manufacturer-release artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/continuation_viii_manufacturer_release"
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
        ART / "COM_HPC_FINAL_DECISION_CONT_VIII.json",
        ART / "READINESS_SCORECARDS.json",
        ART / "TOKENS_CONT_VIII.json",
        ART / "BLOCKERS_CONT_VIII.json",
        ART / "MANIFEST.json",
        DOCS / "COM_HPC_FINAL_DECISION_CONT_VIII.md",
        DOCS / "TOKENS_CONT_VIII.md",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"missing {p}")

    decision = json.loads((ART / "COM_HPC_FINAL_DECISION_CONT_VIII.json").read_text())
    if "OPTION_B" not in decision.get("final_decision", ""):
        errors.append("expected Option B final decision (or update validator if C earned)")

    for product in PRODUCTS:
        sch = ROOT / f"device_designs/{product}/kicad/{product}.kicad_sch"
        pcb = ROOT / f"device_designs/{product}/kicad/{product}.kicad_pcb"
        if not sch.exists() or not pcb.exists():
            errors.append(f"missing kicad for {product}")
            continue
        sch_txt = sch.read_text(encoding="utf-8")
        if 'lib_id "FuncBlock"' in sch_txt:
            errors.append(f"{product} still places FuncBlock instances")
        if 'generator "continuation_viii' not in sch_txt and 'generator "continuation_ix' not in sch_txt:
            errors.append(f"{product} schematic not Cont VIII/IX generator")
        for doc in (
            "DFM_PRECHECK.md",
            "ASSEMBLY_WORK_INSTRUCTION.md",
            "ASSEMBLY_BOM.csv",
            "FASTENER_TORQUE_TABLE.csv",
            "ADHESIVE_THERMAL_MATERIAL_TABLE.csv",
            "QC_CHECKLIST.md",
            "RFQ_DIGITAL_PACKAGE.md",
        ):
            if not (ROOT / f"device_designs/{product}/manufacturing/{doc}").exists():
                errors.append(f"missing {product} manufacturing/{doc}")

    if '(lib_id "FuncBlock")' in (
        ROOT / "device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch"
    ).read_text():
        errors.append("handheld still places FuncBlock instances")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS Cont VIII validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
