#!/usr/bin/env python3
"""Simulate capsule firmware update — never flashes real firmware."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "sample_capsule_manifest.yaml"


def load_manifest(path: Path) -> dict:
    text = path.read_text()
    if yaml:
        return yaml.safe_load(text) or {}
    return json.loads(text) if text.strip().startswith("{") else {}


def simulate(manifest: dict) -> dict:
    if not manifest.get("simulated_only", True):
        return {"status": "fail", "error": "Refusing non-simulated capsule"}
    return {
        "status": "success",
        "simulated_only": True,
        "capsule_id": manifest.get("capsule_id"),
        "target_version": manifest.get("target_version"),
        "device_id": manifest.get("device_id"),
        "reboot_required": True,
        "message": "Simulated capsule staged — no real firmware flashed",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, default=MANIFEST)
    ap.add_argument("--output", type=Path, default=None)
    args = ap.parse_args()
    result = simulate(load_manifest(args.manifest))
    out = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out + "\n")
    print(out)
    return 0 if result["status"] == "success" else 1


if __name__ == "__main__":
    sys.exit(main())
