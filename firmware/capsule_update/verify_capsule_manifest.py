#!/usr/bin/env python3
"""Verify capsule manifest schema and simulated_only flag."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_YAML = ROOT / "sample_capsule_manifest.yaml"
MANIFEST_JSON = ROOT / "sample_capsule_manifest.json"
sys.path.insert(0, str(ROOT.parent))
from _device_util import load_structured  # noqa: E402


def load_manifest() -> dict:
    if MANIFEST_JSON.exists():
        return json.loads(MANIFEST_JSON.read_text())
    return load_structured(MANIFEST_YAML)


def main() -> int:
    if not MANIFEST_YAML.exists() and not MANIFEST_JSON.exists():
        print("FAIL sample capsule manifest missing")
        return 1
    data = load_manifest()
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
