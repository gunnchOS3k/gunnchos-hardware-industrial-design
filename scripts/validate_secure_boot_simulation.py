#!/usr/bin/env python3
"""Validate secure boot simulation harness."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    for script in [
        "secure_boot/scripts/simulate_secure_boot_chain.py",
        "secure_boot/scripts/simulate_measured_boot_log.py",
        "secure_boot/scripts/verify_boot_artifact_signature.py",
    ]:
        p = ROOT / script
        if not p.exists():
            print(f"FAIL missing {script}")
            return 1
        r = subprocess.run([sys.executable, str(p)], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"FAIL {script}:", r.stdout, r.stderr)
            return 1
    status = (ROOT / "secure_boot/SECURE_BOOT_STATUS.md").read_text()
    if "simulation: implemented" not in status.lower():
        print("FAIL SECURE_BOOT_STATUS must document simulation implemented")
        return 1
    print("PASS secure boot simulation validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
