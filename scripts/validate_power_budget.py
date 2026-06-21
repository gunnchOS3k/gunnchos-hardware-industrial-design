#!/usr/bin/env python3
"""Validate power budget CSV column headers."""
import csv
import sys
from pathlib import Path

REQUIRED = """device,subsystem,mode,min_w_typ,max_w_typ,duty_cycle_estimate,notes""".split(",")

FILES = [
    "student_14_power_budget.csv",
    "handheld_hybrid_power_budget.csv",
    "ds_xl_coder_power_budget.csv",
    "wearables_arena_power_budget.csv",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "power"
    files = [root / f for f in FILES]
    files = [f for f in files if f.exists()]
    if len(files) != len(FILES):
        print("Missing power budget CSV files")
        return 1
    for f in files:
        with f.open() as fh:
            headers = next(csv.reader(fh))
        missing = [h for h in REQUIRED if h not in headers]
        if missing:
            print(f"FAIL {f.name}: missing {missing}")
            return 1
        rows = list(csv.DictReader(f.open()))
        if len(rows) < 3:
            print(f"FAIL {f.name}: expected at least 3 rows")
            return 1
    print(f"PASS {len(files)} power budget files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
