#!/usr/bin/env python3
from pathlib import Path
import sys

REQ = [
    "docs/00_START_HERE.md",
    "docs/02_6G_URLLC_ALIGNMENT.md",
    "results/e2e/hardware_e2e_report.md",
    "results/e2e/device_spec_summary.md",
    "devices/student_14_5/README.md",
]

def main():
    root = Path(__file__).resolve().parents[1]
    missing = [p for p in REQ if not (root / p).exists()]
    if missing:
        print("FAIL", missing)
        return 1
    print("PASS hardware e2e")
    return 0

if __name__ == "__main__":
    sys.exit(main())
