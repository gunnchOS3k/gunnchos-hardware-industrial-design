import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_continuation_vi_validator():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_continuation_vi.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_handheld_pinout_csv_260():
    path = ROOT / "device_designs/handheld_hybrid/docs/radxa_nx5_public_pinout_table.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    assert len(rows) == 260
    assert rows[0]["evidence"] == "PUBLIC_PINOUT"
