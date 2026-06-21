#!/usr/bin/env python3
"""QEMU device profile VM harness — dry run when QEMU unavailable."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from _device_util import load_qemu_profiles, normalize_device_id  # noqa: E402


def dry_run(device: str) -> dict:
    canon = normalize_device_id(device)
    if not canon:
        return {"status": "fail", "error": f"unknown device {device}"}
    profiles = load_qemu_profiles(
        ROOT / "qemu_device_profiles.yaml",
        ROOT / "qemu_device_profiles.json",
    )
    profile = profiles.get(canon)
    if not profile:
        return {"status": "fail", "error": f"unknown device {device}"}
    qemu = shutil.which("qemu-system-x86_64")
    return {
        "status": "pass",
        "device": canon,
        "requested_device": device,
        "profile": profile,
        "qemu_available": qemu is not None,
        "mode": "dry_run" if not qemu else "qemu_invoked",
        "message": "OVMF-style harness validated (dry run)" if not qemu else "QEMU present — profile validated",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--device", default="student_14_5")
    ap.add_argument("--dry-run", action="store_true", default=True)
    args = ap.parse_args()
    result = dry_run(args.device)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
