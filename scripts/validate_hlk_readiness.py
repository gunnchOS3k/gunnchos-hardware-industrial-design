#!/usr/bin/env python3
"""Validate HLK-style readiness package — no false certification claims."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "hlk_readiness/README.md",
    "hlk_readiness/HLK_STYLE_READINESS_PLAN.md",
    "hlk_readiness/WINDOWS_HARDWARE_COMPATIBILITY_PROGRAM_NOTES.md",
    "hlk_readiness/DRIVER_AND_DEVICE_TEST_REQUIREMENTS.md",
    "hlk_readiness/SYSTEM_TEST_REQUIREMENTS.md",
    "hlk_readiness/GRAPHICS_MEDIA_PERFORMANCE_TEST_NOTES.md",
    "hlk_readiness/HLK_EVIDENCE_REQUIRED.md",
    "hlk_readiness/HLK_CLAIM_BOUNDARY.md",
    "hlk_readiness/HLK_READINESS_STATUS.md",
]

FORBIDDEN = [
    r"\bHLK passed\b",
    r"\bHLK certified\b",
    r"\bpassed HLK tests\b",
    r"\bqualifies for the Windows Hardware Compatibility Program\b",
    r"\bWHCP qualified\b",
]

REQUIRED_BOUNDARY = "does not claim Windows HLK testing has been run"


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing HLK readiness files:", missing)
        return 1

    boundary = (ROOT / "hlk_readiness/HLK_CLAIM_BOUNDARY.md").read_text()
    if REQUIRED_BOUNDARY not in boundary:
        print("FAIL HLK_CLAIM_BOUNDARY missing required statement")
        return 1

    status = (ROOT / "hlk_readiness/HLK_READINESS_STATUS.md").read_text()
    if "Not started" not in status:
        print("FAIL HLK testing must be Not started")
        return 1

    for pat in FORBIDDEN:
        for f in REQUIRED:
            text = (ROOT / f).read_text()
            if re.search(pat, text, re.I) and "does not claim" not in text.lower():
                print(f"FAIL forbidden HLK claim in {f}: {pat}")
                return 1

    print("PASS HLK readiness validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
