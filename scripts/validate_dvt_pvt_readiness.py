#!/usr/bin/env python3
"""Validate DVT and PVT readiness packages with honest status claims."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DVT_REQUIRED = [
    "dvt/README.md",
    "dvt/DVT_READINESS_REQUIREMENTS.md",
    "dvt/DVT_TEST_PLAN.md",
    "dvt/DVT_STATUS.md",
]

PVT_REQUIRED = [
    "pvt/README.md",
    "pvt/PVT_READINESS_REQUIREMENTS.md",
    "pvt/PVT_TEST_PLAN.md",
    "pvt/PVT_STATUS.md",
]

FORBIDDEN = [
    r"\bDVT complete status:\s*(?:yes|true|complete|passed|met)\b",
    r"\bPVT complete status:\s*(?:yes|true|complete|passed|met)\b",
    r"\bDVT passed\b",
    r"\bPVT passed\b",
    r"\bDVT signoff complete\b",
    r"\bPVT signoff complete\b",
]


def check_status(path: Path, not_complete_phrase: str) -> bool:
    text = path.read_text()
    if not_complete_phrase.lower() not in text.lower():
        return False
    for pat in FORBIDDEN:
        if re.search(pat, text, re.I):
            return False
    return True


def main() -> int:
    missing = [f for f in DVT_REQUIRED + PVT_REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing DVT/PVT files:", missing)
        return 1
    if not check_status(ROOT / "dvt/DVT_STATUS.md", "Not complete"):
        print("FAIL DVT_STATUS must state not complete without false pass claims")
        return 1
    if not check_status(ROOT / "pvt/PVT_STATUS.md", "Not complete"):
        print("FAIL PVT_STATUS must state not complete without false pass claims")
        return 1
    print("PASS DVT/PVT readiness validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
