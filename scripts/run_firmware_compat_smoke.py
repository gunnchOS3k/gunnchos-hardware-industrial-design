#!/usr/bin/env python3
"""Run firmware compatibility smoke test and write report."""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "FIRMWARE_COMPATIBILITY_SMOKE_REPORT.md"


def run(cmd: list[str]) -> tuple[int, str]:
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def main() -> int:
    steps = [
        ("validate_firmware_manifests", [sys.executable, "scripts/validate_firmware_manifests.py"]),
        ("validate_firmware_descriptors", [sys.executable, "scripts/validate_firmware_descriptors.py"]),
        ("validate_capsule_update_simulation", [sys.executable, "scripts/validate_capsule_update_simulation.py"]),
        ("validate_firmware_implementation", [sys.executable, "scripts/validate_firmware_implementation.py"]),
        ("qemu_dry_run", [sys.executable, "firmware/qemu/run_device_profile_vm.py", "--dry-run", "--device", "student_14_5"]),
        ("capsule_sim", [sys.executable, "firmware/capsule_update/simulate_capsule_update.py"]),
    ]
    results = {}
    ok = True
    for name, cmd in steps:
        code, out = run(cmd)
        results[name] = {"exit_code": code, "output": out[-500:]}
        ok = ok and code == 0

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(
        "# Firmware Compatibility Smoke Report\n\n"
        f"Generated: {datetime.now(timezone.utc).isoformat()}\n\n"
        f"Overall: {'PASS' if ok else 'FAIL'}\n\n"
        f"```json\n{json.dumps(results, indent=2)}\n```\n"
    )
    print(f"Smoke report: {RESULTS} — {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
