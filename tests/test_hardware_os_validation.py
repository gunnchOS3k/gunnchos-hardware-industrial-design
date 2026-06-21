from pathlib import Path
import subprocess
import sys


def test_validate_hardware_os_validation():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_hardware_os_validation.py"], cwd=root)
    assert r.returncode == 0
