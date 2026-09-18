#!/usr/bin/env python3
"""Dry-run / refuse physical PASS without explicit lab evidence flag."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    p = argparse.ArgumentParser(description="Stream F EVT/DVT/PVT pack runner")
    p.add_argument("--phase", choices=["EVT", "DVT", "PVT"], required=True)
    p.add_argument(
        "--i-have-lab-evidence",
        action="store_true",
        help="Required to even attempt PASS recording (still refuses auto-PASS)",
    )
    args = p.parse_args()
    pack_path = ROOT / "evt_dvt_pvt" / args.phase.lower() / f"{args.phase}_TEST_PACK.json"
    if not pack_path.exists():
        print(f"FAIL missing {pack_path}")
        return 1
    pack = json.loads(pack_path.read_text())
    print(f"Loaded {pack['case_count']} {args.phase} cases (digital prep).")
    if not args.i_have_lab_evidence:
        print("REFUSE: physical execution blocked (omit lab evidence flag).")
        print("All physical_pass tokens remain false.")
        return 2
    print("Lab evidence flag set, but this runner still will NOT auto-mark PASS.")
    print("Record evidence via evt_dvt_pvt/schemas/evidence_record.schema.json in lab MES.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
