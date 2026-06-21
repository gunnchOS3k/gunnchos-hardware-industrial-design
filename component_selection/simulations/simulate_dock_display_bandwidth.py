#!/usr/bin/env python3
"""Simulation: simulate_dock_display_bandwidth.py."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "dock_display_bandwidth.json"


def main() -> int:
    data = {"student_14_5": {"dp_alt_mode": "simulated", "physical_validated": False}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
