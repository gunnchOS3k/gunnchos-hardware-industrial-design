#!/usr/bin/env python3
"""Simulation: simulate_storage_memory_pressure.py."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "storage_memory_pressure.json"


def main() -> int:
    data = {"student_14_5": {"ram_gb": 16, "storage_pressure": "low"}}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
