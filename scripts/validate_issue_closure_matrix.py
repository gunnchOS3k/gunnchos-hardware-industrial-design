#!/usr/bin/env python3
"""Validate issue closure matrix covers required GitHub issues."""
import re
import sys
from pathlib import Path

REQUIRED_ISSUES = list(range(1, 16)) + [17]
ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "ISSUE_CLOSURE_MATRIX.md"

STL_FILES = [
    "exports/stl/student_14_placeholder.stl",
    "exports/stl/handheld_hybrid_placeholder.stl",
    "exports/stl/ds_xl_coder_placeholder.stl",
    "exports/stl/wearables_arena_set_placeholder.stl",
]


def stl_exports_ok() -> bool:
    return all((ROOT / f).exists() and (ROOT / f).stat().st_size > 100 for f in STL_FILES)


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

    stl_ok = stl_exports_ok()
    row12 = re.search(r"\|\s*#12\s*\|[^|\n]*\|[^|\n]*\|[^|\n]*\|([^|]+)\|([^|]+)\|", text)
    if row12:
        close_status = row12.group(1).strip()
        if stl_ok and "Closes #12" not in close_status:
            print("FAIL STL files exist but #12 not marked Closes #12")
            return 1
        if not stl_ok and "Closes #12" in close_status:
            print("FAIL #12 marked Closes #12 without real STL files")
            return 1

    print(f"PASS issue closure matrix covers {len(REQUIRED_ISSUES)} issues")
    return 0


if __name__ == "__main__":
    sys.exit(main())
