#!/usr/bin/env python3
"""Validate OS compatibility handoff package."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    "os_compatibility/README.md",
    "os_compatibility/OS_COMPATIBILITY_HANDOFF.md",
    "os_compatibility/HARDWARE_TO_OS_TRACEABILITY.md",
    "os_compatibility/OS_PROFILE_EXPORT_MANIFEST.md",
    "os_compatibility/OS_HARDWARE_CONTRACT_V2.md",
    "os_compatibility/DEVICE_CLASS_OS_SUPPORT_MATRIX.md",
    "os_compatibility/OS_BOOT_EXPECTATIONS.md",
    "os_compatibility/OS_MODE_SUPPORT_REQUIREMENTS.md",
    "os_compatibility/OS_INPUT_DISPLAY_REQUIREMENTS.md",
    "os_compatibility/OS_POWER_THERMAL_REQUIREMENTS.md",
    "os_compatibility/OS_STORAGE_NETWORK_REQUIREMENTS.md",
    "os_compatibility/OS_ACCESSIBILITY_REQUIREMENTS.md",
    "os_compatibility/OS_RELEASE_EVIDENCE_REQUIREMENTS.md",
    "os_compatibility/OS_COMPATIBILITY_CLAIM_BOUNDARY.md",
    "os_compatibility/OS_COMPATIBILITY_LAYER_AUDIT.md",
    "os_compatibility/device_class_exports/DEVICE_EXPORT_SCHEMA.md",
]

EXPORTS = [
    "os_compatibility/device_class_exports/student_14_5_os_export.yaml",
    "os_compatibility/device_class_exports/handheld_hybrid_os_export.yaml",
    "os_compatibility/device_class_exports/ds_xl_coder_os_export.yaml",
    "os_compatibility/device_class_exports/wearables_arena_set_os_export.yaml",
]

EXPORT_FIELDS = [
    "device_id",
    "hardware_repo_device_name",
    "os_repo_profile_name",
    "display",
    "input",
    "audio",
    "camera_mic",
    "network",
    "storage",
    "memory",
    "battery",
    "thermal",
    "ports",
    "dock",
    "sensors",
    "controller",
    "keyboard",
    "touch",
    "accessibility",
    "supported_modes",
    "unsupported_modes",
    "supported_journey_presets",
    "supported_app_packs",
    "developer_features",
    "gaming_media_features",
    "creator_features",
    "research_features",
    "school_library_features",
    "guardian_features",
    "offline_features",
    "boot_expectations",
    "recovery_expectations",
    "firmware_interface_expectations",
    "power_management_expectations",
    "thermal_management_expectations",
    "known_gaps",
    "required_real_hardware_evidence",
    "claim_boundary",
    "source_artifacts",
]

EVIDENCE_PLACEHOLDERS = [
    "os_compatibility_evidence/OS_BOOT_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/DEVICE_ENUMERATION_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/INPUT_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/DISPLAY_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/POWER_THERMAL_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/BATTERY_STATUS_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/NETWORK_STORAGE_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/RECOVERY_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/EDGE_IO_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/WAIKE_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/HLK_TEST_LOG_PLACEHOLDER.md",
    "os_compatibility_evidence/EXTERNAL_REVIEW_SIGNOFF_PLACEHOLDER.md",
]

FORBIDDEN = [
    r"\bHLK (?:passed|certified)\b",
    r"\breal hardware boot proven\b",
    r"\bproduction hardware compatibility proven\b",
]

README_LINK = "os_compatibility/"


def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore

        return yaml.safe_load(path.read_text()) or {}
    except ImportError:
        data: dict = {}
        for line in path.read_text().splitlines():
            if ":" in line and not line.strip().startswith("#"):
                k, _, v = line.partition(":")
                data[k.strip()] = v.strip()
        return data


def main() -> int:
    missing = [f for f in REQUIRED_DOCS + EXPORTS + EVIDENCE_PLACEHOLDERS if not (ROOT / f).exists()]
    if missing:
        print("Missing OS compatibility handoff files:", missing)
        return 1

    readme = (ROOT / "README.md").read_text()
    if README_LINK not in readme:
        print("FAIL README must link to os_compatibility handoff")
        return 1

    readme_os = (ROOT / "os_compatibility/README.md").read_text()
    required_phrase = "reciprocal handoff to gunnchos-device-os"
    if required_phrase not in readme_os:
        print("FAIL os_compatibility/README.md missing required handoff phrase")
        return 1

    for export in EXPORTS:
        data = load_yaml(ROOT / export)
        for field in EXPORT_FIELDS:
            if field not in data:
                print(f"FAIL {export} missing field {field}")
                return 1

    matrix = (ROOT / "production_release/PRODUCTION_RELEASE_EVIDENCE_MATRIX.md").read_text()
    if "OS compatibility" not in matrix or "os_compatibility" not in matrix.lower():
        print("FAIL production release matrix must include OS compatibility blocking gate")
        return 1
    if re.search(r"OS compatibility.*\|\s*pass(ed)?\s*\|", matrix, re.I):
        print("FAIL OS compatibility gate must not be marked passed")
        return 1

    for pat in FORBIDDEN:
        for doc in REQUIRED_DOCS:
            if re.search(pat, (ROOT / doc).read_text(), re.I):
                print(f"FAIL forbidden claim in {doc}: {pat}")
                return 1

    for ph in EVIDENCE_PLACEHOLDERS:
        text = (ROOT / ph).read_text()
        if "No real hardware evidence submitted yet" not in text:
            print(f"FAIL placeholder text missing in {ph}")
            return 1

    print("PASS OS compatibility handoff validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
