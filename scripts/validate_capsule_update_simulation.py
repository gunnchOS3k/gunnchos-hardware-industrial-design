#!/usr/bin/env python3
"""Validate capsule update simulation runs."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIM = ROOT / "firmware" / "capsule_update" / "simulate_capsule_update.py"


def main() -> int:
    if not SIM.exists():
        print("FAIL simulate_capsule_update.py missing")
        return 1
    r = subprocess.run([sys.executable, str(SIM)], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0 or "simulated_only" not in r.stdout:
        print("FAIL capsule simulation:", r.stdout, r.stderr)
        return 1
    print("PASS capsule update simulation validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
