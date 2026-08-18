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


def test_handoff_covers_device_quartet_and_stays_physical_pending():
    root = Path(__file__).resolve().parents[1]
    text = (root / "DIGITAL_TO_PHYSICAL_HANDOFF.md").read_text()
    for name in ("Student 14.5", "Handheld Hybrid", "DS-XL Coder", "Edge I/O Rings"):
        assert name in text
    assert "PHYSICAL_PENDING" in text
    assert "generic gaming" in text.lower()
    assert "fcc certified" not in text.lower()


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
