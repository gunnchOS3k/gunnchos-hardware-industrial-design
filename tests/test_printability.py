from pathlib import Path
import subprocess
import sys


def test_validate_printability():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_printability.py"], cwd=root)
    assert r.returncode == 0
