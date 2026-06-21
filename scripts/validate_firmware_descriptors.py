#!/usr/bin/env python3
"""Validate ACPI and DeviceTree descriptor prototypes exist."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
PROTOTYPE = "Prototype descriptor for firmware/OS compatibility harness"


def main() -> int:
    for d in DEVICES:
        acpi = ROOT / f"firmware/descriptors/acpi/{d}_dsdt.dsl"
        dts = ROOT / f"firmware/descriptors/devicetree/{d}.dts"
        for p in (acpi, dts):
            if not p.exists():
                print(f"FAIL missing {p}")
                return 1
            if PROTOTYPE not in p.read_text():
                print(f"FAIL {p} missing prototype comment")
                return 1
    print("PASS firmware descriptor validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
