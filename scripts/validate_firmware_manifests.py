#!/usr/bin/env python3
"""Validate firmware manifests for all device families."""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL pyyaml required")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
FW = ROOT / "firmware" / "manifests"
DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
REQUIRED = [
    "device_id", "device_name", "firmware_target", "firmware_version", "boot_model",
    "supported_boot_paths", "hardware_interfaces", "firmware_variables", "capsule_update",
    "descriptor_sources", "os_compatibility", "claim_boundary",
]


def main() -> int:
    for d in DEVICES:
        path = FW / f"{d}_firmware_manifest.yaml"
        if not path.exists():
            print(f"FAIL missing {path}")
            return 1
        data = yaml.safe_load(path.read_text()) or {}
        for key in REQUIRED:
            if key not in data:
                print(f"FAIL {path.name} missing {key}")
                return 1
        if data["device_id"] != d:
            print(f"FAIL device_id mismatch in {path.name}")
            return 1
    print("PASS firmware manifest validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
