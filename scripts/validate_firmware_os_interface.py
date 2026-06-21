#!/usr/bin/env python3
"""Validate firmware OS interface package — requirements only, no false implementation claims."""
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
    r"\bfirmware implementation exists\b",
    r"\bTPM implementation complete\b",
    r"\bmeasured boot complete\b",
    r"\breal hardware profile discovery proven\b",
]

REQUIRED_STATUS = "requirements defined only"


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing firmware OS interface files:", missing)
        return 1

    status = (ROOT / "firmware_os_interface/FIRMWARE_OS_INTERFACE_STATUS.md").read_text()
    if REQUIRED_STATUS not in status:
        print("FAIL FIRMWARE_OS_INTERFACE_STATUS must state requirements defined only")
        return 1
    if "Not yet proven" not in status:
        print("FAIL FIRMWARE_OS_INTERFACE_STATUS must list not-yet-proven items")
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
