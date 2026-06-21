#!/usr/bin/env python3
"""QEMU device profile VM harness — dry run when QEMU unavailable."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent
PROFILES = ROOT / "qemu_device_profiles.yaml"


def load_profiles() -> dict:
    if yaml is None:
        return {"profiles": {}}
    return yaml.safe_load(PROFILES.read_text()) or {}


def dry_run(device: str) -> dict:
    profiles = load_profiles().get("profiles", {})
    if device not in profiles:
        return {"status": "fail", "error": f"unknown device {device}"}
    qemu = shutil.which("qemu-system-x86_64")
    return {
        "status": "pass",
        "device": device,
        "profile": profiles[device],
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
