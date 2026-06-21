#!/usr/bin/env python3
"""Simulation: simulate_user_persona_fit.py."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "user_persona_fit.json"


def main() -> int:
    data = {"best_device_for_gamer": "handheld_hybrid", "best_device_for_cs_student": "student_14_5"}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
