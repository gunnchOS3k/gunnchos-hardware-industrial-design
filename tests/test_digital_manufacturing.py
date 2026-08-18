from pathlib import Path
import subprocess
import sys


def test_validate_digital_manufacturing():
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run(
        [sys.executable, "scripts/validate_digital_manufacturing.py"],
        cwd=root,
    )
    assert r.returncode == 0


def test_readiness_does_not_claim_fab_or_cert():
    root = Path(__file__).resolve().parents[1]
    text = (root / "DIGITAL_MANUFACTURING_READINESS.md").read_text()
    assert "DIGITAL_FABRICATION_PASS" in text
    assert "**FALSE**" in text
    assert "PHYSICAL_PENDING" in text
    assert "FCC" in text
    lower = text.lower()
    assert "fcc certified" not in lower
    assert "| **false**" in lower or "`false`" in lower
