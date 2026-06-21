from pathlib import Path
import subprocess
import sys


def test_validate_mechanical_correctness():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, "scripts/validate_mechanical_correctness.py"], cwd=root)
    assert r.returncode == 0


def test_mechanical_targets_json():
    root = Path(__file__).resolve().parents[1]
    assert (root / "mechanical_correctness/device_mechanical_targets.json").exists()
