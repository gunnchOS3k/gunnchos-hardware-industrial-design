#!/usr/bin/env python3
"""Validate BOM CSV column headers."""
import csv
import sys
from pathlib import Path

REQUIRED = """device,subsystem,part_category,example_part_or_module,quantity,criticality,target_cost_low,target_cost_high,vendor_candidates,notes""".split(",")

def main():
    root = Path(__file__).resolve().parents[1] / "bom"
    files = [
        root / "student_14_bom.csv",
        root / "handheld_hybrid_bom.csv",
        root / "ds_xl_coder_bom.csv",
        root / "wearables_arena_bom.csv",
    ]
    files = [f for f in files if f.exists()]
    if not files:
        print("No BOM files")
        return 1
    for f in files:
        with f.open() as fh:
            headers = next(csv.reader(fh))
        missing = [h for h in REQUIRED if h not in headers]
        if missing:
            print(f"FAIL {f}: missing {missing}")
            return 1
    print(f"PASS {len(files)} BOM files")
    return 0

if __name__ == "__main__":
    sys.exit(main())
