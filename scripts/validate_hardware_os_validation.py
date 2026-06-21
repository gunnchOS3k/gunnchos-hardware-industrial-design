#!/usr/bin/env python3
"""Validate hardware-side OS validation package."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "hardware_os_validation/README.md",
    "hardware_os_validation/HARDWARE_OS_VALIDATION_PLAN.md",
    "hardware_os_validation/DEVICE_CLASS_VALIDATION_CHECKLIST.md",
    "hardware_os_validation/STUDENT_14_5_OS_VALIDATION.md",
    "hardware_os_validation/HANDHELD_HYBRID_OS_VALIDATION.md",
    "hardware_os_validation/DS_XL_CODER_OS_VALIDATION.md",
    "hardware_os_validation/WEARABLES_ARENA_OS_VALIDATION.md",
    "hardware_os_validation/INPUT_VALIDATION_PLAN.md",
    "hardware_os_validation/DISPLAY_VALIDATION_PLAN.md",
    "hardware_os_validation/POWER_THERMAL_VALIDATION_PLAN.md",
    "hardware_os_validation/STORAGE_NETWORK_VALIDATION_PLAN.md",
    "hardware_os_validation/ACCESSIBILITY_VALIDATION_PLAN.md",
    "hardware_os_validation/BOOT_RECOVERY_VALIDATION_PLAN.md",
    "hardware_os_validation/EDGE_IO_VALIDATION_PLAN.md",
    "hardware_os_validation/WAIKE_VALIDATION_PLAN.md",
    "hardware_os_validation/HARDWARE_OS_VALIDATION_STATUS.md",
]

FORBIDDEN = [
    r"\bReal hardware validation status:\s*Started\b",
    r"\bReal hardware validation status:\s*Complete\b",
    r"\breal hardware validation passed\b",
    r"\bhardware-compatible release passed\b",
]


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("Missing hardware OS validation files:", missing)
        return 1

    status = (ROOT / "hardware_os_validation/HARDWARE_OS_VALIDATION_STATUS.md").read_text()
    if "hardware-side validation plan exists" not in status:
        print("FAIL HARDWARE_OS_VALIDATION_STATUS must state plan exists")
        return 1
    if "implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md" not in status:
        print("FAIL status must link to REAL_HARDWARE_VALIDATION_ISSUES evidence gate")
        return 1
    if re.search(r"\breal hardware validation (passed|complete)\b", status, re.I):
        print("FAIL must not claim real hardware validation passed")
        return 1

    evidence_dir = ROOT / "os_compatibility_evidence"
    has_boot_log = any(
        p.name.endswith(".md")
        and "PLACEHOLDER" not in p.name
        and "README" not in p.name
        and "EVIDENCE_INTAKE" not in p.name
        for p in evidence_dir.glob("*.md")
    )
    if has_boot_log:
        for pat in FORBIDDEN:
            if re.search(pat, status, re.I):
                print(f"FAIL forbidden validation claim without evidence: {pat}")
                return 1

    for pat in FORBIDDEN:
        if re.search(pat, status, re.I):
            print(f"FAIL forbidden claim in status: {pat}")
            return 1

    print("PASS hardware OS validation package validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
