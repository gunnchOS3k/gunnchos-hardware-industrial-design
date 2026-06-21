#!/usr/bin/env python3
"""Validate external evidence layer placeholders exist and do not claim completion."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "os_compatibility_evidence/README.md",
    "os_compatibility_evidence/EVIDENCE_INTAKE_PROCESS.md",
    "os_compatibility_evidence/EXTERNAL_REVIEW_SIGNOFF_PLACEHOLDER.md",
]

PLACEHOLDER_PHRASE = "No real hardware evidence submitted yet"


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing external evidence layer files:", missing)
        return 1
    for f in REQUIRED:
        if PLACEHOLDER_PHRASE not in (ROOT / f).read_text():
            print(f"FAIL {f} missing placeholder phrase")
            return 1
    print("PASS external evidence layer validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
