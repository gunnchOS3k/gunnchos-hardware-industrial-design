#!/usr/bin/env python3
"""Static validation for Continuation VII EDA release-clean artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/continuation_vii_eda_release_clean"
DOCS = ROOT / "docs/full_product_family"
PRODUCTS = [
    "student_14_5",
    "ds_xl_coder",
    "handheld_hybrid",
    "edge_io_rings",
    "dock",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    required = [
        ART / "VALIDATION_SUMMARY.json",
        ART / "EDA_VIOLATION_SEVERITY_LEDGER.json",
        ART / "RELEASE_CLEAN_TOKENS.json",
        ART / "PCB_REDTEAM.json",
        ART / "COM_HPC_NDA_DECISION.json",
        ART / "EXTERNAL_NDA_BLOCKED_REGISTER.json",
        DOCS / "EDA_VIOLATION_SEVERITY_LEDGER.md",
        DOCS / "PCB_REDTEAM_CONT_VII.md",
        DOCS / "EDA_TO_MECHANICAL_FIT_REPORT.md",
        DOCS / "COM_HPC_NDA_DECISION_CONT_VII.md",
        DOCS / "TOKENS_CONT_VII.md",
        DOCS / "KICAD_EDA_RELEASE_CLEAN_CONT_VII.md",
    ]
    for p in required:
        if not p.exists():
            fail(f"missing {p.relative_to(ROOT)}")

    summary = json.loads((ART / "VALIDATION_SUMMARY.json").read_text(encoding="utf-8"))
    tokens = json.loads((ART / "RELEASE_CLEAN_TOKENS.json").read_text(encoding="utf-8"))
    ledger = json.loads(
        (ART / "EDA_VIOLATION_SEVERITY_LEDGER.json").read_text(encoding="utf-8")
    )
    nda = json.loads((ART / "COM_HPC_NDA_DECISION.json").read_text(encoding="utf-8"))

    if not tokens.get("KICAD_CLI_EXECUTION_PASS"):
        fail("KICAD_CLI_EXECUTION_PASS must be true")
    for prod in PRODUCTS:
        key = {
            "student_14_5": "STUDENT_14_5_EDA_RELEASE_CLEAN_PASS",
            "ds_xl_coder": "DS_XL_EDA_RELEASE_CLEAN_PASS",
            "handheld_hybrid": "HANDHELD_EDA_RELEASE_CLEAN_PASS",
            "edge_io_rings": "RING_EDA_RELEASE_CLEAN_PASS",
            "dock": "DOCK_EDA_RELEASE_CLEAN_PASS",
        }[prod]
        # Honest: structural boards must not claim release-clean yet
        if tokens.get(key) is True:
            fail(f"{key} claimed TRUE but Cont VII still structural")

    allowed = {"FIXED", "FORMALLY_WAIVED_WARNING", "EXTERNAL_NDA_BLOCKED"}
    for e in ledger.get("entries", []):
        if e.get("status") not in allowed:
            fail(f"illegal ledger status {e.get('status')}")
        if e.get("status") in {"IGNORED", "KNOWN", "LATER"}:
            fail("forbidden status present")

    if nda.get("decision") != "KEEP_ADLINK_AND_ACCEPT_NARROW_EXTERNAL_BLOCK":
        fail("unexpected NDA decision")

    for prod in PRODUCTS:
        sch = ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_sch"
        pcb = ROOT / f"device_designs/{prod}/kicad/{prod}.kicad_pcb"
        if "(wire " not in sch.read_text(encoding="utf-8"):
            fail(f"{prod} schematic has no wires")
        if "MountingHole" not in pcb.read_text(encoding="utf-8"):
            fail(f"{prod} PCB missing mounting holes")
        mfg = ROOT / f"manufacturing/{prod}/PREMANUFACTURING_READINESS.md"
        if not mfg.exists():
            fail(f"missing mfg package {mfg.relative_to(ROOT)}")

    # ERC/DRC error counts in summary must be zero when reports present
    for prod, board in summary.get("boards", {}).items():
        if board.get("erc_errors") not in (0, None):
            if board.get("erc_errors", 0) > 0:
                fail(f"{prod} still has ERC errors: {board.get('erc_errors')}")
        if board.get("drc_errors") not in (0, None):
            if board.get("drc_errors", 0) > 0:
                fail(f"{prod} still has DRC errors: {board.get('drc_errors')}")

    print("validate_continuation_vii: PASS")
    print(f"  ledger entries: {len(ledger.get('entries', []))}")
    print(f"  nda: {nda.get('decision')}")
    print(f"  KICAD_CLI_EXECUTION_PASS={tokens.get('KICAD_CLI_EXECUTION_PASS')}")


if __name__ == "__main__":
    main()
