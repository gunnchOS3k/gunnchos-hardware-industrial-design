from pathlib import Path
import subprocess
import sys


def test_validate_dvt_pvt_readiness():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_dvt_pvt_readiness.py"], cwd=root)
    assert r.returncode == 0
