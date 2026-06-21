#!/usr/bin/env python3
"""Validate production release gate package and block false release claims."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "production_release/README.md",
    "production_release/PRODUCTION_RELEASE_REQUIREMENTS.md",
    "production_release/PRODUCTION_RELEASE_GATE.md",
    "production_release/PRODUCTION_RELEASE_EVIDENCE_MATRIX.md",
    "production_release/PRODUCTION_RELEASE_STATUS.md",
]

FORBIDDEN = [
    r"\bproduction release complete\b",
    r"\bmanufacturing release complete\b",
    r"\bmass-production ready\b",
    r"\bproduction-ready hardware\b",
    r"\bproduction released\b",
]

GERBER_GLOBS = list((ROOT / "pcb").glob("**/*.gbr")) + list((ROOT / "manufacturing").glob("**/gerbers/**/*.gbr"))


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing production release files:", missing)
        return 1
    status = (ROOT / "production_release/PRODUCTION_RELEASE_STATUS.md").read_text()
    if "Not released" not in status:
        print("FAIL PRODUCTION_RELEASE_STATUS must state Not released")
        return 1
    for pat in FORBIDDEN:
        if re.search(pat, status, re.I):
            print(f"FAIL forbidden claim: {pat}")
            return 1
    matrix = (ROOT / "production_release/PRODUCTION_RELEASE_EVIDENCE_MATRIX.md").read_text()
    if not GERBER_GLOBS:
        for line in matrix.splitlines():
            if "Gerber" in line and re.search(r"\|\s*pass(ed)?\s*\|", line, re.I):
                print("FAIL Gerber gate marked pass without Gerber files")
                return 1
    print("PASS production release gate validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
