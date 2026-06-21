#!/usr/bin/env python3
"""Simulation: simulate_power_thermal_budget.py."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "power_thermal_simulation.json"


def main() -> int:
    data = {"student_14_5": {"watts_peak": 25, "thermal_risk": "medium"}, "handheld_hybrid": {"watts_peak": 30, "thermal_risk": "high"}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
