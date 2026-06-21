#!/usr/bin/env python3
"""Validate production-candidate track docs and truthful status claims."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROTOTYPE_REQUIRED = [
    "versions/README.md",
    "versions/prototype_evt1/README.md",
    "versions/prototype_evt1/PROTOTYPE_READY_PACKAGE.md",
    "versions/prototype_evt1/PROTOTYPE_FILE_MANIFEST.md",
    "versions/prototype_evt1/PROTOTYPE_VENDOR_HANDOFF.md",
    "versions/prototype_evt1/PROTOTYPE_BUILD_SCOPE.md",
    "versions/prototype_evt1/PROTOTYPE_ACCEPTANCE_TEST_PLAN.md",
    "versions/prototype_evt1/PROTOTYPE_KNOWN_GAPS.md",
]

PRODUCTION_REQUIRED = [
    "versions/production_candidate/README.md",
    "versions/production_candidate/PRODUCTION_READINESS_REQUIREMENTS.md",
    "versions/production_candidate/PRODUCTION_RELEASE_CHECKLIST.md",
    "versions/production_candidate/PRODUCTION_FILE_MANIFEST_REQUIRED.md",
    "versions/production_candidate/PRODUCTION_GAP_ANALYSIS.md",
    "versions/production_candidate/PRODUCTION_ACCEPTANCE_TEST_PLAN.md",
    "production_backlog/PRODUCTION_ISSUES_TO_CREATE.md",
    "manufacturing/PRODUCTION_RELEASE_PLAN.md",
    "manufacturing/PRODUCTION_GATE_REVIEW.md",
    "pcb/GERBER_OUTPUT_STATUS.md",
    "compliance/PRODUCTION_COMPLIANCE_PLAN.md",
]

STL_FILES = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]

FORBIDDEN_CLAIMS = [
    r"\bFCC approved\b",
    r"\bCE approved\b",
    r"\bmanufacturing-ready\b",
    r"\bproduction-ready hardware\b",
    r"\bDVT complete\b",
    r"\bPVT complete\b",
    r"\bready for mass production\b",
    r"\bbattery certified\b",
]

GERBER_PATHS = list((ROOT / "pcb").glob("**/*.gbr")) + list((ROOT / "manufacturing").glob("**/gerbers/**/*.gbr"))


def stl_exports_ok() -> bool:
    return all((ROOT / f).exists() and (ROOT / f).stat().st_size > 100 for f in STL_FILES)


def main() -> int:
    missing = [f for f in PROTOTYPE_REQUIRED + PRODUCTION_REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing production track files:")
        for m in missing:
            print(f"  - {m}")
        return 1

    prod_readme = (ROOT / "versions/production_candidate/README.md").read_text()
    if "does not yet meet" not in prod_readme.lower() and "not met" not in prod_readme.lower():
        print("FAIL production_candidate README must state gates not met")
        return 1

    pcb_status = (ROOT / "pcb/GERBER_OUTPUT_STATUS.md").read_text()
    if "No Gerbers exist yet" not in pcb_status and not GERBER_PATHS:
        print("FAIL GERBER status must say no Gerbers unless files exist")
        return 1
    if GERBER_PATHS and "No Gerbers exist yet" in pcb_status:
        print("FAIL Gerber files exist but status claims none")
        return 1

    compliance = (ROOT / "compliance/PRODUCTION_COMPLIANCE_PLAN.md").read_text()
    if "Not certified" not in compliance:
        print("FAIL compliance plan must state not certified")
        return 1

    matrix = (ROOT / "docs/ISSUE_CLOSURE_MATRIX.md").read_text()
    stl_ok = stl_exports_ok()
    if stl_ok:
        if "Closes #12" not in matrix:
            print("FAIL STL exports exist but matrix does not say Closes #12")
            return 1
    else:
        if re.search(r"\|\s*#12\s*\|[^|]*\|\s*Refs #12", matrix) is None and "Refs #12" not in matrix:
            print("FAIL STL exports missing but matrix does not say Refs #12")
            return 1
        if "Closes #12" in matrix and not stl_ok:
            print("FAIL matrix claims Closes #12 without real STL files")
            return 1

    scan_paths = [
        ROOT / "versions/production_candidate",
        ROOT / "compliance/PRODUCTION_COMPLIANCE_PLAN.md",
        ROOT / "pcb/GERBER_OUTPUT_STATUS.md",
    ]
    for base in scan_paths:
        paths = [base] if base.is_file() else base.rglob("*.md")
        for p in paths:
            text = p.read_text()
            for pat in FORBIDDEN_CLAIMS:
                if re.search(pat, text, re.I):
                    print(f"FAIL forbidden claim in {p}: {pat}")
                    return 1

    print("PASS production track validation")
    if stl_ok:
        print("PASS STL exports present and non-empty")
    else:
        print("Note: STL exports pending — issue #12 should remain Refs #12")
    return 0


if __name__ == "__main__":
    sys.exit(main())
