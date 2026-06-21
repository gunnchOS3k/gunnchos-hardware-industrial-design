#!/usr/bin/env python3
"""Validate issue closure matrix covers required GitHub issues."""
import re
import sys
from pathlib import Path

REQUIRED_ISSUES = list(range(1, 16)) + [17]
MATRIX = Path(__file__).resolve().parents[1] / "docs" / "ISSUE_CLOSURE_MATRIX.md"


def main() -> int:
    if not MATRIX.exists():
        print(f"Missing {MATRIX}")
        return 1
    text = MATRIX.read_text()
    missing = []
    for issue in REQUIRED_ISSUES:
        if not re.search(rf"\|\s*#{issue}\s*\|", text):
            missing.append(issue)
    if missing:
        print(f"Missing issues in matrix: {missing}")
        return 1
    if "Close status" not in text or "PR keyword" not in text:
        print("Matrix missing required columns")
        return 1
    print(f"PASS issue closure matrix covers {len(REQUIRED_ISSUES)} issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
