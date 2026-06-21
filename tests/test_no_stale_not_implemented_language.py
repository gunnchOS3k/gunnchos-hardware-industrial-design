from pathlib import Path
import subprocess
import sys


def test_stale_language_validator():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_no_stale_not_implemented_language.py"], cwd=root)
    assert r.returncode == 0
