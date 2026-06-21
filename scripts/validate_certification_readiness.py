#!/usr/bin/env python3
"""Validate certification readiness package and honest status claims."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "certification/README.md",
    "certification/CERTIFICATION_READINESS_MATRIX.md",
    "certification/CERTIFICATION_STATUS.md",
    "certification/CERTIFICATION_EVIDENCE_REQUIRED.md",
    "certification/FCC_CERTIFICATION_READINESS.md",
    "certification/CE_UKCA_READINESS.md",
]

FORBIDDEN = [
    r"\bFCC approved\b",
    r"\bCE approved\b",
    r"\bUKCA approved\b",
    r"\bbattery certified\b",
    r"\bcertified hardware\b",
]

PASSED_WITHOUT_EVIDENCE = re.compile(r"\|\s*passed\s*\|", re.I)


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing certification files:", missing)
        return 1
    status = (ROOT / "certification/CERTIFICATION_STATUS.md").read_text()
    if "Not certified" not in status:
        print("FAIL CERTIFICATION_STATUS must state Not certified")
        return 1
    for pat in FORBIDDEN:
        if re.search(pat, status, re.I):
            print(f"FAIL forbidden claim: {pat}")
            return 1
    matrix = (ROOT / "certification/CERTIFICATION_READINESS_MATRIX.md").read_text()
    # Allow 'passed' column header but not data rows claiming passed without evidence dir
    evidence_dir = ROOT / "certification" / "evidence"
    has_evidence = evidence_dir.exists() and any(evidence_dir.iterdir())
    if not has_evidence:
        for line in matrix.splitlines():
            if line.startswith("|") and "| passed |" in line.lower() and "Status" not in line:
                print("FAIL matrix claims passed without evidence files")
                return 1
    print("PASS certification readiness validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
