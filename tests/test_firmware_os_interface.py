from pathlib import Path
import subprocess
import sys


def test_validate_firmware_os_interface():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_firmware_os_interface.py"], cwd=root)
    assert r.returncode == 0
