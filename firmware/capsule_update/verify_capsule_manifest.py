#!/usr/bin/env python3
"""Verify capsule manifest schema and simulated_only flag."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL pyyaml required")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "sample_capsule_manifest.yaml"


def main() -> int:
    if not MANIFEST.exists():
        print("FAIL sample_capsule_manifest.yaml missing")
        return 1
    data = yaml.safe_load(MANIFEST.read_text()) or {}
    for key in ("capsule_id", "target_version", "device_id", "simulated_only"):
        if key not in data:
            print(f"FAIL missing {key}")
            return 1
    if not data.get("simulated_only"):
        print("FAIL capsule must be simulated_only")
        return 1
    print("PASS capsule manifest verification")
    return 0


if __name__ == "__main__":
    sys.exit(main())
