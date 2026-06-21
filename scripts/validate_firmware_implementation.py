#!/usr/bin/env python3
"""Validate firmware implementation layer — fail if requirements-only without artifacts."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "firmware/README.md",
    "firmware/CLAIM_BOUNDARY.md",
    "firmware/IMPLEMENTATION_STATUS.md",
    "firmware/interfaces/docking_external_display_contract.yaml",
    "firmware/capsule_update/simulate_capsule_update.py",
    "firmware/qemu/run_device_profile_vm.py",
]

FORBIDDEN = [
    r"\bphysical-board boot complete\b",
    r"\bHLK passed\b",
    r"\bHLK certified\b",
    r"\bproduction firmware ready\b",
    r"\bphysical hardware validated:\s*true\b",
]

DOCK_REQ = ROOT / "firmware_os_interface/DOCKING_AND_EXTERNAL_DISPLAY_REQUIREMENTS.md"
IMPL_LINK = "firmware/interfaces/docking_external_display_contract.yaml"


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("FAIL missing firmware implementation files:", missing)
        return 1

    if not DOCK_REQ.exists() or IMPL_LINK not in DOCK_REQ.read_text():
        print("FAIL docking requirements must link to implementation contract")
        return 1
    if "requirements defined only" in DOCK_REQ.read_text().lower() and "Implementation artifacts" not in DOCK_REQ.read_text():
        print("FAIL docking doc still requirements-only without implementation section")
        return 1

    status = ROOT / "firmware_os_interface/FIRMWARE_OS_INTERFACE_STATUS.md"
    if status.exists():
        text = status.read_text()
        if "requirements defined only" in text.lower() and "implemented in emulation" not in text.lower():
            print("FAIL FIRMWARE_OS_INTERFACE_STATUS not updated to implementation status")
            return 1

    for pat in FORBIDDEN:
        for p in ROOT.glob("firmware/**/*.md"):
            if re.search(pat, p.read_text(), re.I):
                print(f"FAIL forbidden claim in {p}: {pat}")
                return 1

    print("PASS firmware implementation validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
