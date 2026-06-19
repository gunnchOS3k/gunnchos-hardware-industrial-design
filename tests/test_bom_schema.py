from pathlib import Path
import subprocess, sys
def test_validate_bom():
    r = subprocess.run([sys.executable, "scripts/validate_bom.py"], cwd=Path(__file__).resolve().parents[1])
    assert r.returncode == 0
