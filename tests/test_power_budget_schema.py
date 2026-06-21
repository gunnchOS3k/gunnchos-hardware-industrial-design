from pathlib import Path
import subprocess
import sys


def test_validate_power_budget():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_power_budget.py"], cwd=root)
    assert r.returncode == 0
