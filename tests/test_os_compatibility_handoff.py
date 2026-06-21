from pathlib import Path
import subprocess
import sys


def _run(script: str) -> None:
    root = Path(__file__).resolve().parents[1]
    r = subprocess.run([sys.executable, f"scripts/{script}"], cwd=root)
    assert r.returncode == 0


def test_validate_os_compatibility_handoff():
    _run("validate_os_compatibility_handoff.py")


def test_validate_firmware_os_interface():
    _run("validate_firmware_os_interface.py")


def test_validate_hardware_os_validation():
    _run("validate_hardware_os_validation.py")


def test_validate_hlk_readiness():
    _run("validate_hlk_readiness.py")
