#!/usr/bin/env python3
"""Validate firmware OS interface package links to implementation artifacts."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "firmware_os_interface/README.md",
    "firmware_os_interface/FIRMWARE_OS_INTERFACE_REQUIREMENTS.md",
    "firmware_os_interface/BOOT_DISCOVERY_REQUIREMENTS.md",
    "firmware_os_interface/DEVICE_IDENTITY_AND_PROFILE_DISCOVERY.md",
    "firmware_os_interface/UEFI_ACPI_READINESS_PLAN.md",
    "firmware_os_interface/SECURE_BOOT_REQUIREMENTS.md",
    "firmware_os_interface/TPM_AND_MEASURED_BOOT_REQUIREMENTS.md",
    "firmware_os_interface/POWER_STATE_REQUIREMENTS.md",
    "firmware_os_interface/THERMAL_SENSOR_INTERFACE_REQUIREMENTS.md",
    "firmware_os_interface/BATTERY_STATUS_INTERFACE_REQUIREMENTS.md",
    "firmware_os_interface/INPUT_DEVICE_ENUMERATION_REQUIREMENTS.md",
    "firmware_os_interface/DISPLAY_ENUMERATION_REQUIREMENTS.md",
    "firmware_os_interface/DOCKING_AND_EXTERNAL_DISPLAY_REQUIREMENTS.md",
    "firmware_os_interface/RECOVERY_BOOT_REQUIREMENTS.md",
    "firmware_os_interface/FIRMWARE_OS_INTERFACE_STATUS.md",
]

FORBIDDEN = [
    r"\bUEFI/ACPI implementation complete\b",
    r"\bsecure boot complete\b",
    r"\bphysical-board boot complete\b",
    r"\bTPM implementation complete\b",
    r"\bmeasured boot complete\b",
    r"\breal hardware profile discovery proven\b",
    r"\bHLK passed\b",
]

IMPL_MARKERS = ["firmware/manifests/", "firmware/interfaces/", "implemented in emulation"]


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing firmware OS interface files:", missing)
        return 1

    status = (ROOT / "firmware_os_interface/FIRMWARE_OS_INTERFACE_STATUS.md").read_text()
    if "implemented in emulation" not in status.lower():
        print("FAIL status must state implemented in emulation/host harness")
        return 1
    if "Physical-board validation remains pending" not in status:
        print("FAIL status must state physical-board validation pending")
        return 1

    dock = (ROOT / "firmware_os_interface/DOCKING_AND_EXTERNAL_DISPLAY_REQUIREMENTS.md").read_text()
    if "Implementation artifacts" not in dock:
        print("FAIL docking doc must list implementation artifacts")
        return 1

    for pat in FORBIDDEN:
        for f in REQUIRED:
            if re.search(pat, (ROOT / f).read_text(), re.I):
                print(f"FAIL forbidden firmware claim in {f}: {pat}")
                return 1

    print("PASS firmware OS interface validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
