from pathlib import Path
import subprocess
import sys


def test_secure_boot_simulation_scripts():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_secure_boot_simulation.py"], cwd=root)
    assert r.returncode == 0
