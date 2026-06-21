#!/usr/bin/env python3
"""Bootstrap OS compatibility handoff package for gunnchos-hardware-industrial-design."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OS_COMMIT = "7f26faf900039bfcf0618df99defd8489f8a13d3"
OS_BRANCH = "main"
PLACEHOLDER = (
    "No real hardware evidence submitted yet.\n"
    "Do not mark hardware-compatible release as passed until reviewed evidence is committed.\n"
)
CLAIM_BOUNDARY = (
    "This hardware repo provides OS compatibility assumptions, manifests, and validation checklists. "
    "It does not prove real hardware boot, HLK certification, driver certification, UEFI/ACPI "
    "implementation, secure boot completion, thermal/battery validation, or production hardware compatibility."
)
HLK_BOUNDARY = (
    "This repo documents an HLK-style future readiness path. It does not claim Windows HLK testing "
    "has been run, that any device has passed HLK tests, or that the product qualifies for the "
    "Windows Hardware Compatibility Program."
)


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n")


def export_yaml(
    device_id: str,
    hw_name: str,
    os_profile: str,
    profile: dict,
    unsupported_modes: list[str],
    boot: str,
    recovery: str,
    firmware: str,
    power_mgmt: str,
    thermal_mgmt: str,
    gaps: list[str],
    evidence: list[str],
    sources: list[str],
) -> str:
    import yaml  # noqa: PLC0415 — optional; fall back to manual if missing

    data = {
        "device_id": device_id,
        "hardware_repo_device_name": hw_name,
        "os_repo_profile_name": os_profile,
        "display": profile.get("display", {}),
        "input": profile.get("input", {}),
        "audio": profile.get("audio", {}),
        "camera_mic": profile.get("camera_mic", {}),
        "network": profile.get("network", {}),
        "storage": profile.get("storage", {}),
        "memory": profile.get("memory", {}),
        "battery": profile.get("battery", {}),
        "thermal": profile.get("thermal", {}),
        "ports": profile.get("ports", []),
        "dock": profile.get("dock", {}),
        "sensors": profile.get("sensors", []),
        "controller": profile.get("controller", {}),
        "keyboard": profile.get("keyboard", {}),
        "touch": profile.get("touch", {}),
        "accessibility": profile.get("accessibility", {}),
        "supported_modes": profile.get("supported_modes", []),
        "unsupported_modes": unsupported_modes,
        "supported_journey_presets": profile.get("supported_journey_presets", []),
        "supported_app_packs": profile.get("supported_app_packs", []),
        "developer_features": profile.get("developer_features", {}),
        "gaming_media_features": profile.get("gaming_media_features", {}),
        "creator_features": profile.get("creator_features", {}),
        "research_features": profile.get("research_features", {}),
        "school_library_features": profile.get("school_library_features", {}),
        "guardian_features": profile.get("guardian_features", {}),
        "offline_features": profile.get("offline_features", {}),
        "boot_expectations": boot,
        "recovery_expectations": recovery,
        "firmware_interface_expectations": firmware,
        "power_management_expectations": power_mgmt,
        "thermal_management_expectations": thermal_mgmt,
        "known_gaps": gaps,
        "required_real_hardware_evidence": evidence,
        "claim_boundary": "Hardware export manifest — profile-based compatibility only; requires real hardware validation.",
        "source_artifacts": sources,
    }
    try:
        return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    except ImportError:
        lines = [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in data.items()]
        return "\n".join(lines) + "\n"


PROFILES = {
    "student_14_5": {
        "hw_name": "Student 14.5",
        "unsupported": [],
        "boot": "UEFI-style profile discovery placeholder; OS binds student_14_5 profile on first run.",
        "recovery": "Recovery partition and safe-mode entry via firmware menu — requirements only.",
        "firmware": "ACPI battery/thermal/ALS placeholders; USB-C dock enumeration.",
        "power": "School-day battery target; S3/S0ix assumptions documented in power/POWER_BUDGET_MASTER.md.",
        "thermal": "Passive fanless throttle policy per thermal/student_14_5/os_thermal_policy.yaml.",
        "gaps": ["physical_thermal_validation_pending", "hlk_not_run", "real_boot_not_proven"],
        "evidence": ["boot_log", "display_touch_test", "dock_enumeration", "battery_runtime", "thermal_readings"],
        "sources": [
            "product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md",
            "io/student_14_ports.md",
            "power/student_14_power_budget.csv",
            "battery/BATTERY_REQUIREMENTS.md",
            "thermal/student_14_5/thermal_test_plan.md",
            "mechanical_correctness/device_mechanical_targets.json#student_14",
        ],
    },
    "handheld_hybrid": {
        "hw_name": "Handheld Hybrid",
        "unsupported": ["Admin"],
        "boot": "Handheld profile with controller-first input; dock/TV mode hotplug expectations.",
        "recovery": "Controller-navigable recovery; USB-C firmware recovery path — requirements only.",
        "firmware": "Gamepad HID enumeration; active cooling fan curve interface placeholder.",
        "power": "Portable extended battery; gaming-balanced throttle.",
        "thermal": "Active cooling per thermal/handheld_hybrid/os_thermal_policy.yaml.",
        "gaps": ["steam_compatibility_not_certified", "battery_validation_pending", "real_boot_not_proven"],
        "evidence": ["boot_log", "controller_input_test", "tv_mode_display", "thermal_fan_curve"],
        "sources": [
            "io/handheld_hybrid_ports.md",
            "power/handheld_hybrid_power_budget.csv",
            "thermal/handheld_hybrid/thermal_test_plan.md",
            "mechanical_correctness/device_mechanical_targets.json#handheld_hybrid",
        ],
    },
    "ds_xl_coder": {
        "hw_name": "DS-XL Coder",
        "unsupported": [],
        "boot": "Dual-screen profile discovery; developer workstation binding.",
        "recovery": "Dual-screen safe mode layout; deploy-source recovery — requirements only.",
        "firmware": "Dual display enumeration; USB-C host role for deploy target.",
        "power": "Workstation portable battery; developer throttle policy.",
        "thermal": "Active cooling per thermal/ds_xl_coder/os_thermal_policy.yaml.",
        "gaps": ["dual_screen_os_shell_not_proven_on_hardware", "real_boot_not_proven"],
        "evidence": ["boot_log", "dual_display_test", "deploy_usb_host_test", "keyboard_touch_matrix"],
        "sources": [
            "io/ds_xl_coder_ports.md",
            "power/ds_xl_coder_power_budget.csv",
            "thermal/ds_xl_coder/thermal_test_plan.md",
            "mechanical_correctness/device_mechanical_targets.json#ds_xl_coder",
        ],
    },
    "wearables_arena_set": {
        "hw_name": "Wearables / Arena Set",
        "unsupported": ["Developer", "Workshop", "Laboratory"],
        "boot": "Wearable/arena profile; marshal supervision flags on first run.",
        "recovery": "Arena-safe recovery; haptic/audio cue path — requirements only.",
        "firmware": "Strict throttle; haptic/motion sensor placeholders; no dock.",
        "power": "Short-cycle wearable battery; arena-safe power caps.",
        "thermal": "Strict throttle per thermal/wearables_arena_set/os_thermal_policy.yaml.",
        "gaps": ["arena_safety_rules_not_field_validated", "no_wsl_workstation", "real_boot_not_proven"],
        "evidence": ["boot_log", "haptic_test", "arena_session_log", "marshal_controls_test"],
        "sources": [
            "io/wearables_arena_ports.md",
            "power/wearables_arena_power_budget.csv",
            "thermal/wearables_arena_set/thermal_test_plan.md",
            "mechanical_correctness/device_mechanical_targets.json#wearables_arena_set",
        ],
    },
}


def main() -> None:
    write(
        "os_compatibility/README.md",
        f"""# OS Compatibility Handoff

This package is the hardware repo's reciprocal handoff to gunnchos-device-os. It documents how the hardware device families are expected to support the OS compatibility layer, and what evidence is still required before hardware-compatible release can be claimed.

## Contents

- [OS_COMPATIBILITY_HANDOFF.md](OS_COMPATIBILITY_HANDOFF.md)
- [HARDWARE_TO_OS_TRACEABILITY.md](HARDWARE_TO_OS_TRACEABILITY.md)
- [OS_PROFILE_EXPORT_MANIFEST.md](OS_PROFILE_EXPORT_MANIFEST.md)
- [OS_HARDWARE_CONTRACT_V2.md](OS_HARDWARE_CONTRACT_V2.md)
- [DEVICE_CLASS_OS_SUPPORT_MATRIX.md](DEVICE_CLASS_OS_SUPPORT_MATRIX.md)
- [OS_COMPATIBILITY_CLAIM_BOUNDARY.md](OS_COMPATIBILITY_CLAIM_BOUNDARY.md)
- [OS_COMPATIBILITY_LAYER_AUDIT.md](OS_COMPATIBILITY_LAYER_AUDIT.md)
- [device_class_exports/](device_class_exports/)

## Cross-repo

- OS repo: https://github.com/gunnchOS3k/gunnchos-device-os
- OS commit inspected: `{OS_COMMIT}` on `{OS_BRANCH}`

{CLAIM_BOUNDARY}
""",
    )

    write(
        "os_compatibility/OS_COMPATIBILITY_LAYER_AUDIT.md",
        f"""# OS Compatibility Layer Audit

Audit of gunnchos-device-os hardware compatibility execution layer from the hardware repo perspective.

## OS repo input inspected

| Field | Value |
|-------|-------|
| Repository | gunnchos-device-os |
| Branch | {OS_BRANCH} |
| Commit | `{OS_COMMIT}` |
| Merge | PR #27 hardware-compatibility-execution-layer |

## Hardware profiles found

| Profile | Path |
|---------|------|
| student_14_5 | `hardware_compat/device_profiles/student_14_5.yaml` |
| handheld_hybrid | `hardware_compat/device_profiles/handheld_hybrid.yaml` |
| ds_xl_coder | `hardware_compat/device_profiles/ds_xl_coder.yaml` |
| wearables_arena_set | `hardware_compat/device_profiles/wearables_arena_set.yaml` |

## Device profiles found

Four YAML profiles under `hardware_compat/device_profiles/` mirror hardware device families. Schema: `hardware_compat/hardware_manifest.schema.json`.

## Demos found

- `scripts/run_hardware_compatibility_demo.py`
- `scripts/run_hardware_boot_readiness_demo.py`
- `scripts/run_device_specific_mode_demo.py`

## Validators found

- `scripts/validate_hardware_manifests.py`
- `scripts/validate_hardware_compatibility.py`
- `scripts/validate_hardware_release_evidence.py`

## Release evidence status

- Config: `config/hardware_release_evidence.yaml`
- Matrix: `hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md`
- Status doc: `hardware_release/HARDWARE_COMPATIBILITY_STATUS.md`
- Generated `results/HARDWARE_COMPATIBILITY_EXECUTION_LAYER_REPORT.md` may be gitignored — regenerate locally with demos if absent.

## Known claim boundary

OS layer provides **simulated** hardware capability detection and profile-based compatibility. It does not prove physical boot, driver certification, or HLK.

## Missing items from OS repo

None blocking for reciprocal handoff. Future hardware evidence intake paths (`os_compatibility_evidence/`) are hardware-side placeholders awaiting lab logs.

## Reciprocal hardware artifacts created

This pass adds `os_compatibility/`, `firmware_os_interface/`, `hardware_os_validation/`, `hlk_readiness/`, and `os_compatibility_evidence/` in the hardware repo.
""",
    )

    handoff_docs = {
        "OS_COMPATIBILITY_HANDOFF.md": "Handoff summary: hardware exports device-class manifests consumed by gunnchos-device-os hardware_compat profiles.",
        "OS_PROFILE_EXPORT_MANIFEST.md": "Index of `device_class_exports/*.yaml` — source of truth remains hardware product, I/O, power, thermal, battery docs.",
        "OS_HARDWARE_CONTRACT_V2.md": "Extends architecture/OS_HARDWARE_CONTRACT.md with firmware interface and boot discovery obligations for OS alpha.",
        "DEVICE_CLASS_OS_SUPPORT_MATRIX.md": "Four device classes × modes, journeys, app packs — aligned with OS config/hardware_*_matrix.yaml files.",
        "OS_BOOT_EXPECTATIONS.md": "Boot sequence expectations per device class; requirements only — not proven on silicon.",
        "OS_MODE_SUPPORT_REQUIREMENTS.md": "Mode allow/block lists per device; wearables block Developer/Workshop/Laboratory.",
        "OS_INPUT_DISPLAY_REQUIREMENTS.md": "Input/display enumeration requirements from io/ and mechanical_correctness/ plans.",
        "OS_POWER_THERMAL_REQUIREMENTS.md": "Power/thermal interfaces from power/ and thermal/ packages.",
        "OS_STORAGE_NETWORK_REQUIREMENTS.md": "Storage class and network assumptions for OS policy modules.",
        "OS_ACCESSIBILITY_REQUIREMENTS.md": "Accessibility feature flags expected by OS hardware_accessibility_policy.",
        "OS_RELEASE_EVIDENCE_REQUIREMENTS.md": "Evidence required before hardware-compatible release — cross-links os_compatibility_evidence/.",
        "OS_COMPATIBILITY_CLAIM_BOUNDARY.md": CLAIM_BOUNDARY,
    }
    for name, summary in handoff_docs.items():
        write(
            f"os_compatibility/{name}",
            f"# {name.replace('_', ' ').replace('.md', '')}\n\n{summary}\n\nSee [HARDWARE_TO_OS_TRACEABILITY.md](HARDWARE_TO_OS_TRACEABILITY.md).\n\n{CLAIM_BOUNDARY}\n",
        )

    trace_rows = [
        ("product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md", "hardware_compat/device_profiles/*.yaml", "All four SKUs", "Defines capabilities OS mirrors", "documented", "Yes"),
        ("architecture/PRODUCT_LINE_ARCHITECTURE.md", "docs/DEVICE_ARCHITECTURE.md", "All", "System context for boot/policy", "documented", "Yes"),
        ("architecture/DEVICE_COMPARISON_MATRIX.md", "hardware_compat/DEVICE_CLASS_COMPATIBILITY_MATRIX.md", "All", "SKU feature differences", "documented", "Yes"),
        ("architecture/OS_HARDWARE_CONTRACT.md", "hardware_compat/HARDWARE_COMPATIBILITY_CONTRACT.md", "All", "Architecture contract", "documented", "Yes"),
        ("io/PORT_IO_MASTER_MATRIX.md", "docs/HARDWARE_STORAGE_NETWORK_POLICY.md", "All", "Port/storage/network policy", "documented", "Yes"),
        ("power/POWER_BUDGET_MASTER.md", "docs/HARDWARE_POWER_THERMAL_POLICY.md", "All", "Power assumptions", "simulated", "Yes"),
        ("battery/BATTERY_REQUIREMENTS.md", "docs/HARDWARE_POWER_THERMAL_POLICY.md", "All", "Battery runtime evidence", "needs_real_hardware", "Yes"),
        ("thermal/THERMAL_REQUIREMENTS.md", "docs/HARDWARE_POWER_THERMAL_POLICY.md", "All", "Thermal throttle evidence", "needs_real_hardware", "Yes"),
        ("compliance/REGULATORY_MATRIX.md", "hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md", "All", "Regulatory rows", "needs_external_review", "Yes"),
        ("dvt/DVT_STATUS.md", "hardware_release/HARDWARE_COMPATIBILITY_STATUS.md", "All", "DVT blocks release", "blocked", "Yes"),
        ("pvt/PVT_STATUS.md", "hardware_release/HARDWARE_COMPATIBILITY_RELEASE_REQUIREMENTS.md", "All", "PVT required", "blocked", "Yes"),
        ("certification/CERTIFICATION_STATUS.md", "hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md", "All", "Cert evidence", "blocked", "Yes"),
        ("production_release/PRODUCTION_RELEASE_STATUS.md", "hardware_release/HARDWARE_COMPATIBILITY_STATUS.md", "All", "Production gate", "blocked", "Yes"),
        ("versions/prototype_evt1/README.md", "boot_readiness/DEVICE_BOOT_SEQUENCE.md", "EVT-1", "Prototype boot plan", "documented", "Yes"),
        ("versions/production_candidate/README.md", "hardware_release/HARDWARE_PILOT_TEST_PLAN.md", "Production track", "Pilot test alignment", "documented", "Yes"),
        ("os_compatibility/device_class_exports/*.yaml", "hardware_compat/device_profiles/*.yaml", "All", "Reciprocal profile export", "documented", "Yes"),
        ("firmware_os_interface/", "boot_readiness/", "All", "Firmware/boot requirements", "documented", "Yes"),
        ("hardware_os_validation/", "hardware_release/HARDWARE_VALIDATION_LAB_CHECKLIST.md", "All", "Lab validation plan", "documented", "Yes"),
        ("hlk_readiness/", "hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md", "Windows path", "HLK-style future path", "documented", "No"),
    ]
    table = "| Hardware artifact | OS repo artifact | Device class impact | Compatibility implication | Evidence status | Blocking before release? |\n"
    table += "|---|---|---|---|---|---|\n"
    for row in trace_rows:
        table += "| " + " | ".join(row) + " |\n"
    write(
        "os_compatibility/HARDWARE_TO_OS_TRACEABILITY.md",
        f"""# Hardware to OS Traceability

Cross-repo traceability from hardware artifacts to OS compatibility layer.

{table}

## Evidence status legend

| Status | Meaning |
|--------|---------|
| documented | Artifact exists and is linked |
| simulated | Software-only or planning assumption |
| needs_real_hardware | Requires physical device evidence |
| needs_external_review | Requires lab/vendor/reviewer signoff |
| blocked | Gate not met — blocks release |
| passed | Lab evidence linked (**none in this matrix**) |

{CLAIM_BOUNDARY}
""",
    )

    write(
        "os_compatibility/device_class_exports/DEVICE_EXPORT_SCHEMA.md",
        """# Device Export Schema

Hardware-side export manifests under `device_class_exports/` are the source of truth for device-class assumptions consumed by gunnchos-device-os `hardware_compat/device_profiles/`.

## Required fields

- `device_id`, `hardware_repo_device_name`, `os_repo_profile_name`
- Capability blocks: `display`, `input`, `audio`, `camera_mic`, `network`, `storage`, `memory`, `battery`, `thermal`, `ports`, `dock`, `sensors`, `controller`, `keyboard`, `touch`, `accessibility`
- OS mapping: `supported_modes`, `unsupported_modes`, `supported_journey_presets`, `supported_app_packs`
- Feature flags: `developer_features`, `gaming_media_features`, `creator_features`, `research_features`, `school_library_features`, `guardian_features`, `offline_features`
- Boot/firmware: `boot_expectations`, `recovery_expectations`, `firmware_interface_expectations`, `power_management_expectations`, `thermal_management_expectations`
- Evidence: `known_gaps`, `required_real_hardware_evidence`, `claim_boundary`, `source_artifacts`

## Sync rule

When hardware I/O, power, thermal, or product docs change, update the export YAML and notify OS repo to refresh profile mirrors.
""",
    )

    # Minimal inline profiles for export generation (mirrors OS YAML)
    inline = {
        "student_14_5": {
            "supported_modes": ["School", "Developer", "Play", "Media", "Studio", "Workshop", "Laboratory", "Guardian", "Library", "Offline", "Admin"],
            "supported_journey_presets": ["scooter", "bicycle", "car", "studio", "workshop", "laboratory", "guardian", "classroom", "library", "offline", "spaceship"],
            "supported_app_packs": ["learn_pack", "write_pack", "cs_student_pack", "stem_lab_pack", "research_pack", "offline_essentials_pack"],
            "display": {"size_inches": 14.5, "resolution": "1920x1200", "touch": True},
            "input": {"keyboard": True, "touch": True, "controller": False},
            "audio": {"speakers": True},
            "camera_mic": {"webcam": True, "mic": True},
            "network": {"wifi": "wifi_6e", "offline_capable": True},
            "storage": {"class": "nvme", "min_gb": 256},
            "memory": {"ram_gb": 8},
            "battery": {"class": "school_day"},
            "thermal": {"class": "passive_fanless"},
            "ports": ["usb_c", "usb_a"],
            "dock": {"supported": True},
            "sensors": [],
            "controller": {"supported": False},
            "keyboard": {"built_in": True},
            "touch": {"supported": True},
            "accessibility": {"screen_reader_labels": True},
            "developer_features": {"wsl_path": True},
            "gaming_media_features": {"steam_path": True},
            "creator_features": {"writer_studio": True},
            "research_features": {"edge_io_companion": True},
            "school_library_features": {"classroom_mode": True},
            "guardian_features": {"guardian_mode": True},
            "offline_features": {"offline_lessons": True},
        },
        "handheld_hybrid": {
            "supported_modes": ["School", "Play", "Media", "Studio", "Arcade", "Guardian", "Library", "Offline"],
            "supported_journey_presets": ["scooter", "bicycle", "arcade", "car", "studio", "offline", "library"],
            "supported_app_packs": ["learn_pack", "game_pack", "music_pack", "offline_essentials_pack"],
            "display": {"size_inches": 8.4, "resolution": "1920x1200", "touch": True},
            "input": {"keyboard": "dock_optional", "touch": True, "controller": True},
            "audio": {"speakers": True, "haptic": True},
            "camera_mic": {"mic": True},
            "network": {"wifi": "wifi_6e", "offline_capable": True},
            "storage": {"class": "nvme", "min_gb": 512},
            "memory": {"ram_gb": 12},
            "battery": {"class": "portable_extended"},
            "thermal": {"class": "active_cooling"},
            "ports": ["usb_c"],
            "dock": {"supported": True, "tv_mode": True},
            "sensors": ["imu_placeholder"],
            "controller": {"supported": True},
            "keyboard": {"built_in": False},
            "touch": {"supported": True},
            "accessibility": {"controller_navigation": True},
            "developer_features": {"light_coding": True},
            "gaming_media_features": {"steam_path": True},
            "creator_features": {"light_studio": True},
            "research_features": {"limited_measurement": True},
            "school_library_features": {"community_kiosk": True},
            "guardian_features": {"play_time_window": True},
            "offline_features": {"offline_games": True},
        },
        "ds_xl_coder": {
            "supported_modes": ["Developer", "Coder", "Workshop", "Laboratory", "School", "Offline", "Admin"],
            "supported_journey_presets": ["workshop", "laboratory", "spaceship", "bicycle", "offline"],
            "supported_app_packs": ["cs_student_pack", "game_dev_pack", "learn_pack", "research_pack", "offline_essentials_pack"],
            "display": {"size_inches": 7.0, "dual_screen": True, "touch": True},
            "input": {"keyboard": True, "touch": True},
            "audio": {"speakers": True},
            "camera_mic": {"mic": True},
            "network": {"wifi": "wifi_6e", "offline_capable": True},
            "storage": {"class": "nvme", "min_gb": 1024},
            "memory": {"ram_gb": 16},
            "battery": {"class": "workstation_portable"},
            "thermal": {"class": "active_cooling"},
            "ports": ["usb_c"],
            "dock": {"supported": True},
            "sensors": [],
            "controller": {"supported": False},
            "keyboard": {"built_in": True},
            "touch": {"supported": True, "dual_screen_touch": True},
            "accessibility": {"keyboard_navigation": True},
            "developer_features": {"wsl_path": True, "dual_screen_workflow": True},
            "gaming_media_features": {"game_dev_preview": True},
            "creator_features": {"coding_lessons": True},
            "research_features": {"research_notebook_authoring": True},
            "school_library_features": {"classroom_coding": True},
            "guardian_features": {"deploy_approval": True},
            "offline_features": {"offline_coding": True},
        },
        "wearables_arena_set": {
            "supported_modes": ["Play", "School", "Offline", "Library", "Admin"],
            "supported_journey_presets": ["scooter", "bicycle", "arcade", "guardian", "offline"],
            "supported_app_packs": ["learn_pack", "game_pack", "accessibility_essentials_pack", "offline_essentials_pack"],
            "display": {"size_class": "wearable_or_arena", "touch": True},
            "input": {"keyboard": False, "touch": True, "controller": True},
            "audio": {"speakers": True, "haptic": True},
            "camera_mic": {"mic": "arena_marshal_only"},
            "network": {"wifi": "wifi_6", "offline_capable": True},
            "storage": {"class": "emmc", "min_gb": 64},
            "memory": {"ram_gb": 4},
            "battery": {"class": "wearable_short_cycle"},
            "thermal": {"class": "strict_throttle"},
            "ports": ["usb_c_charge"],
            "dock": {"supported": False},
            "sensors": ["haptic"],
            "controller": {"supported": True},
            "keyboard": {"built_in": False},
            "touch": {"supported": True},
            "accessibility": {"audio_cues": True, "haptic_cues": True},
            "developer_features": {"wsl_path": False},
            "gaming_media_features": {"venue_arcade": True},
            "creator_features": {"haptic_learning": True},
            "research_features": {"arena_research_placeholder": True},
            "school_library_features": {"supervised_session": True},
            "guardian_features": {"marshal_mode": True},
            "offline_features": {"offline_arena_games": True},
        },
    }

    for key, meta in PROFILES.items():
        prof = inline[key]
        content = export_yaml(
            device_id=key,
            hw_name=meta["hw_name"],
            os_profile=key,
            profile=prof,
            unsupported_modes=meta["unsupported"],
            boot=meta["boot"],
            recovery=meta["recovery"],
            firmware=meta["firmware"],
            power_mgmt=meta["power"],
            thermal_mgmt=meta["thermal"],
            gaps=meta["gaps"],
            evidence=meta["evidence"],
            sources=meta["sources"],
        )
        write(f"os_compatibility/device_class_exports/{key}_os_export.yaml", content)

    fw_docs = [
        ("README.md", "Firmware/OS interface requirements package — requirements only."),
        ("FIRMWARE_OS_INTERFACE_REQUIREMENTS.md", "Top-level firmware obligations for OS handoff."),
        ("BOOT_DISCOVERY_REQUIREMENTS.md", "Device identity and profile discovery at boot."),
        ("DEVICE_IDENTITY_AND_PROFILE_DISCOVERY.md", "Stable device_id mapping to OS profiles."),
        ("UEFI_ACPI_READINESS_PLAN.md", "Future UEFI/ACPI implementation plan — not implemented."),
        ("SECURE_BOOT_REQUIREMENTS.md", "Secure boot requirements — not implemented."),
        ("TPM_AND_MEASURED_BOOT_REQUIREMENTS.md", "TPM/measured boot requirements — not implemented."),
        ("POWER_STATE_REQUIREMENTS.md", "S-states and battery interface requirements."),
        ("THERMAL_SENSOR_INTERFACE_REQUIREMENTS.md", "Thermal sensor ACPI/firmware interface."),
        ("BATTERY_STATUS_INTERFACE_REQUIREMENTS.md", "Smart battery status interface."),
        ("INPUT_DEVICE_ENUMERATION_REQUIREMENTS.md", "HID/touch/controller enumeration."),
        ("DISPLAY_ENUMERATION_REQUIREMENTS.md", "Internal/external display enumeration."),
        ("DOCKING_AND_EXTERNAL_DISPLAY_REQUIREMENTS.md", "USB-C DP alt mode and dock hotplug."),
        ("RECOVERY_BOOT_REQUIREMENTS.md", "Recovery partition and safe mode entry."),
    ]
    for name, body in fw_docs:
        write(f"firmware_os_interface/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\nRequirements defined only — no firmware implementation claimed.\n")

    write(
        "firmware_os_interface/FIRMWARE_OS_INTERFACE_STATUS.md",
        """# Firmware OS Interface Status

Current status: requirements defined only.
Not yet proven: UEFI/ACPI implementation, secure boot, TPM/measured boot, real hardware profile discovery, driver enumeration, firmware handoff, recovery boot, or HLK certification.
""",
    )

    val_docs = [
        ("README.md", "Hardware-side OS validation package."),
        ("HARDWARE_OS_VALIDATION_PLAN.md", "Master validation plan for OS compatibility on real hardware."),
        ("DEVICE_CLASS_VALIDATION_CHECKLIST.md", "Per-class checklist template."),
        ("STUDENT_14_5_OS_VALIDATION.md", "Student 14.5 OS validation scenarios."),
        ("HANDHELD_HYBRID_OS_VALIDATION.md", "Handheld hybrid OS validation scenarios."),
        ("DS_XL_CODER_OS_VALIDATION.md", "DS-XL Coder OS validation scenarios."),
        ("WEARABLES_ARENA_OS_VALIDATION.md", "Wearables/arena OS validation scenarios."),
        ("INPUT_VALIDATION_PLAN.md", "Input device validation plan."),
        ("DISPLAY_VALIDATION_PLAN.md", "Display validation plan."),
        ("POWER_THERMAL_VALIDATION_PLAN.md", "Power/thermal validation plan."),
        ("STORAGE_NETWORK_VALIDATION_PLAN.md", "Storage/network validation plan."),
        ("ACCESSIBILITY_VALIDATION_PLAN.md", "Accessibility validation plan."),
        ("BOOT_RECOVERY_VALIDATION_PLAN.md", "Boot/recovery validation plan."),
        ("EDGE_IO_VALIDATION_PLAN.md", "Edge-IO session validation plan."),
        ("WAIKE_VALIDATION_PLAN.md", "WAIKE workflow validation plan."),
    ]
    for name, body in val_docs:
        write(f"hardware_os_validation/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\nReal hardware validation not started.\n")

    write(
        "hardware_os_validation/HARDWARE_OS_VALIDATION_STATUS.md",
        """# Hardware OS Validation Status

Current status: hardware-side validation plan exists.
Real hardware validation status: Not started.
Required evidence: physical boot logs, input/display tests, power/thermal readings, battery status readings, recovery test logs, Edge-IO session tests, WAIKE workflow tests, and reviewer signoff.
""",
    )

    hlk_docs = [
        ("README.md", "HLK-style future readiness path — not certification."),
        ("HLK_STYLE_READINESS_PLAN.md", "Staged plan toward future Windows HLK-style testing."),
        ("WINDOWS_HARDWARE_COMPATIBILITY_PROGRAM_NOTES.md", "WHCP notes — no qualification claimed."),
        ("DRIVER_AND_DEVICE_TEST_REQUIREMENTS.md", "Driver/device test requirements for future HLK-style runs."),
        ("SYSTEM_TEST_REQUIREMENTS.md", "System-level test requirements."),
        ("GRAPHICS_MEDIA_PERFORMANCE_TEST_NOTES.md", "Graphics/media performance test notes."),
        ("HLK_EVIDENCE_REQUIRED.md", "Evidence required before any HLK-style claim."),
    ]
    for name, body in hlk_docs:
        write(f"hlk_readiness/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{body}\n\n{HLK_BOUNDARY}\n")

    write("hlk_readiness/HLK_CLAIM_BOUNDARY.md", f"# HLK Claim Boundary\n\n{HLK_BOUNDARY}\n")
    write(
        "hlk_readiness/HLK_READINESS_STATUS.md",
        """# HLK Readiness Status

Current status: HLK-style readiness path documented.
HLK testing status: Not started.
Windows Hardware Compatibility Program qualification: Not claimed.
""",
    )

    evidence_files = [
        "README.md",
        "EVIDENCE_INTAKE_PROCESS.md",
        "OS_BOOT_LOG_PLACEHOLDER.md",
        "DEVICE_ENUMERATION_LOG_PLACEHOLDER.md",
        "INPUT_TEST_LOG_PLACEHOLDER.md",
        "DISPLAY_TEST_LOG_PLACEHOLDER.md",
        "POWER_THERMAL_LOG_PLACEHOLDER.md",
        "BATTERY_STATUS_LOG_PLACEHOLDER.md",
        "NETWORK_STORAGE_TEST_LOG_PLACEHOLDER.md",
        "RECOVERY_TEST_LOG_PLACEHOLDER.md",
        "EDGE_IO_TEST_LOG_PLACEHOLDER.md",
        "WAIKE_TEST_LOG_PLACEHOLDER.md",
        "HLK_TEST_LOG_PLACEHOLDER.md",
        "EXTERNAL_REVIEW_SIGNOFF_PLACEHOLDER.md",
    ]
    for name in evidence_files:
        if name == "README.md":
            write("os_compatibility_evidence/README.md", "# OS Compatibility Evidence Intake\n\nPlaceholders for real hardware evidence.\n\n" + PLACEHOLDER)
        elif name == "EVIDENCE_INTAKE_PROCESS.md":
            write(
                "os_compatibility_evidence/EVIDENCE_INTAKE_PROCESS.md",
                "# Evidence Intake Process\n\n1. Run lab test\n2. Commit log under os_compatibility_evidence/\n3. Update HARDWARE_TO_OS_TRACEABILITY evidence status\n4. Obtain reviewer signoff\n\n" + PLACEHOLDER,
            )
        else:
            write(f"os_compatibility_evidence/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\n{PLACEHOLDER}")

    write(
        "hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md",
        """# Hardware Compatibility Evidence Matrix (Hardware Repo)

| Gate | Required evidence | Current evidence | Status | Blocking? |
|------|-------------------|------------------|--------|-----------|
| OS profile export manifest | device_class_exports/*.yaml | Created this pass | documented | Yes |
| OS repo consumed profiles | hardware_compat/device_profiles/*.yaml | OS PR #27 merged | documented | Yes |
| Simulated OS compatibility | OS compatibility engine demos | OS-side simulated | simulated | Yes |
| Hardware-side validation plan | hardware_os_validation/ | Created this pass | documented | Yes |
| Real hardware boot | Boot logs in os_compatibility_evidence/ | Placeholder only | needs_real_hardware | Yes |
| Firmware/OS interface | firmware_os_interface/ | Requirements only | documented | Yes |
| HLK-style readiness | hlk_readiness/ | Plan only | documented | No |
| Real hardware compatibility | Lab signoff | Not started | blocked | Yes |

Production hardware-compatible release: **not claimed**.
""",
    )

    print("Bootstrap complete")


if __name__ == "__main__":
    main()
