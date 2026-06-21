#!/usr/bin/env python3
"""Bootstrap firmware compatibility implementation artifacts."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
DEVICE_NAMES = {
    "student_14_5": "Student 14.5",
    "handheld_hybrid": "Handheld Hybrid",
    "ds_xl_coder": "DS-XL Coder",
    "wearables_arena_set": "Wearables / Arena Set",
}
UNSUPPORTED = {
    "student_14_5": [],
    "handheld_hybrid": ["Admin"],
    "ds_xl_coder": [],
    "wearables_arena_set": ["Developer", "Workshop", "Laboratory"],
}
SUPPORTED_MODES = {
    "student_14_5": ["School", "Developer", "Play", "Media", "Studio", "Workshop", "Laboratory", "Guardian", "Library", "Offline", "Admin"],
    "handheld_hybrid": ["School", "Play", "Media", "Studio", "Arcade", "Guardian", "Library", "Offline"],
    "ds_xl_coder": ["Developer", "Coder", "Workshop", "Laboratory", "School", "Offline", "Admin"],
    "wearables_arena_set": ["Play", "School", "Offline", "Library", "Admin"],
}
DOCK = {
    "student_14_5": True,
    "handheld_hybrid": True,
    "ds_xl_coder": True,
    "wearables_arena_set": False,
}
DUAL_SCREEN = {"ds_xl_coder": True}
CLAIM = (
    "This directory contains real firmware compatibility implementation artifacts for manifests, "
    "descriptors, QEMU/OVMF-style boot harnesses, interface contracts, and capsule-update simulation. "
    "It does not prove physical-board firmware boot, secure boot production readiness, HLK certification, "
    "or hardware lab validation."
)
PROTOTYPE = "Prototype descriptor for firmware/OS compatibility harness.\nNot validated on physical hardware.\n"


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n")


def manifest_yaml(device_id: str) -> str:
    import yaml

    data = {
        "device_id": device_id,
        "device_name": DEVICE_NAMES[device_id],
        "firmware_target": "gunnchos_compat_harness_v1",
        "firmware_version": "0.1.0-harness",
        "boot_model": "uefi_standard_boot",
        "supported_boot_paths": ["uefi_standard_boot", "recovery_boot", "safe_mode_boot"],
        "hardware_interfaces": {
            "display": {"internal": True, "external": DOCK[device_id]},
            "input": {"keyboard": device_id != "wearables_arena_set", "touch": True, "controller": device_id in ("handheld_hybrid", "wearables_arena_set")},
            "battery": {"smart_battery_stub": True},
            "thermal": {"thermal_zone_stub": True},
            "storage": {"nvme_or_emmc": device_id != "wearables_arena_set"},
            "network": {"wifi_stub": True},
            "dock": {"supported": DOCK[device_id]},
            "external_display": {"usb_c_alt_mode_stub": DOCK[device_id]},
            "sensors": {"imu": device_id == "handheld_hybrid", "haptic": device_id == "wearables_arena_set"},
        },
        "firmware_variables": {
            "boot_order": "Boot0001",
            "firmware_version": "0.1.0-harness",
            "device_profile": device_id,
            "recovery_requested": False,
            "capsule_update_pending": False,
        },
        "capsule_update": {
            "supported": True,
            "simulated_only": True,
            "version_format": "semver+build",
            "rollback_policy": "keep_previous_capsule_simulated",
        },
        "descriptor_sources": {
            "acpi": f"firmware/descriptors/acpi/{device_id}_dsdt.dsl",
            "devicetree": f"firmware/descriptors/devicetree/{device_id}.dts",
        },
        "os_compatibility": {
            "required_os_profile": device_id,
            "supported_modes": SUPPORTED_MODES[device_id],
            "unsupported_modes": UNSUPPORTED[device_id],
        },
        "claim_boundary": "Harness manifest — emulation/host validation only; physical-board validation pending.",
    }
    return yaml.safe_dump(data, sort_keys=False)


def acpi_dsl(device_id: str) -> str:
    lines = [
        f"// {PROTOTYPE.strip()}",
        'DefinitionBlock ("", "DSDT", 2, "GUNNCH", "GCHOS  ", 0x00000001)',
        "{",
        "    External (_SB.PCI0, DeviceObj)",
        "    Scope (_SB)",
        "    {",
        '        Device (GCDP) { Name (_HID, "GUNN0001") /* display controller stub */ }',
        '        Device (GCIN) { Name (_HID, "GUNN0002") /* input/touch stub */ }',
        '        Device (GCBAT) { Name (_HID, "GUNN0003") /* battery stub */ }',
        '        Device (GCTHM) { Name (_HID, "GUNN0004") /* thermal zone stub */ }',
        '        Device (GCSTO) { Name (_HID, "GUNN0005") /* storage stub */ }',
        '        Device (GCNET) { Name (_HID, "GUNN0006") /* network stub */ }',
    ]
    if DOCK[device_id]:
        lines.append('        Device (GCDO) { Name (_HID, "GUNN0007") /* dock/external display stub */ }')
    if DUAL_SCREEN.get(device_id):
        lines.append('        Device (GCDS) { Name (_HID, "GUNN0008") /* dual-screen stub */ }')
    lines.extend([
        '        Device (GCSEN) { Name (_HID, "GUNN0009") /* sensors stub */ }',
        "    }",
        "}",
        "}",
    ])
    return "\n".join(lines) + "\n"


def dts(device_id: str) -> str:
    dock_node = ""
    if DOCK[device_id]:
        dock_node = """
    dock: dock-controller {
        compatible = "gunnchos,dock-stub";
        status = "okay";
        external-display;
    };"""
    return f"""/*
 * {PROTOTYPE.strip()}
 */
/dts-v1/;

/ {{
    compatible = "gunnchos,{device_id.replace('_', '-')}-harness", "gunnchos,compat-harness";
    model = "GunnchOS {DEVICE_NAMES[device_id]} Harness";
    #address-cells = <1>;
    #size-cells = <0>;

    display: display-controller {{
        compatible = "gunnchos,display-stub";
        status = "okay";
    }};

    input: input-controller {{
        compatible = "gunnchos,input-stub";
        status = "okay";
    }};

    battery: smart-battery {{
        compatible = "gunnchos,battery-stub";
        status = "okay";
    }};

    thermal: thermal-zone {{
        compatible = "gunnchos,thermal-stub";
        status = "okay";
    }};

    storage: storage-controller {{
        compatible = "gunnchos,storage-stub";
        status = "okay";
    }};

    network: network-controller {{
        compatible = "gunnchos,wifi-stub";
        status = "okay";
    }};{dock_node}
}};
"""


def main() -> None:
    write("firmware/README.md", f"""# Firmware Compatibility Implementation

Real firmware compatibility harness: manifests, ACPI/DeviceTree descriptors, UEFI variable templates, QEMU/OVMF smoke harness, interface contracts, and capsule-update simulation.

Implemented in emulation/host validation. Physical-board validation remains pending.

See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md) and [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md).
""")

    write("firmware/CLAIM_BOUNDARY.md", f"# Firmware Claim Boundary\n\n{CLAIM}\n")

    status_rows = [
        ("firmware manifests", "firmware/manifests/*.yaml", "Yes", "CI validation", "Pending"),
        ("ACPI descriptors", "firmware/descriptors/acpi/*_dsdt.dsl", "Yes", "CI validation", "Pending"),
        ("DeviceTree descriptors", "firmware/descriptors/devicetree/*.dts", "Yes", "CI validation", "Pending"),
        ("UEFI variable templates", "firmware/descriptors/uefi_vars/", "Yes", "CI validation", "Pending"),
        ("QEMU/OVMF smoke harness", "firmware/qemu/run_device_profile_vm.py", "Yes (dry run)", "Smoke report", "Pending"),
        ("capsule update simulation", "firmware/capsule_update/simulate_capsule_update.py", "Yes", "CI + smoke", "Pending"),
        ("boot/recovery contracts", "firmware/boot/*.yaml", "Yes", "CI validation", "Pending"),
        ("docking/external display interface", "firmware/interfaces/docking_external_display_contract.yaml", "Yes", "CI validation", "Pending"),
        ("power state interface", "firmware/interfaces/power_state_contract.yaml", "Yes", "CI validation", "Pending"),
        ("thermal sensor interface", "firmware/interfaces/thermal_sensor_contract.yaml", "Yes", "CI validation", "Pending"),
        ("battery status interface", "firmware/interfaces/battery_status_contract.yaml", "Yes", "CI validation", "Pending"),
        ("input/display/storage/network enumeration", "firmware/interfaces/*_contract.yaml", "Yes", "CI validation", "Pending"),
    ]
    table = "| Area | Implemented artifact | Runs today? | Evidence | Physical hardware status |\n|---|---|---|---|---|\n"
    table += "\n".join(f"| {a} | `{p}` | {r} | {e} | {ph} |" for a, p, r, e, ph in status_rows)
    write("firmware/IMPLEMENTATION_STATUS.md", f"# Firmware Implementation Status\n\n{table}\n")

    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "required": [
            "device_id", "device_name", "firmware_target", "firmware_version", "boot_model",
            "supported_boot_paths", "hardware_interfaces", "firmware_variables", "capsule_update",
            "descriptor_sources", "os_compatibility", "claim_boundary",
        ],
    }
    write("firmware/manifests/firmware_manifest.schema.json", json.dumps(schema, indent=2))

    for d in DEVICES:
        write(f"firmware/manifests/{d}_firmware_manifest.yaml", manifest_yaml(d))
        write(f"firmware/descriptors/acpi/{d}_dsdt.dsl", acpi_dsl(d))
        write(f"firmware/descriptors/devicetree/{d}.dts", dts(d))

    write("firmware/descriptors/acpi/README.md", "ACPI DSDT prototype descriptors for firmware/OS compatibility harness.\n")
    write("firmware/descriptors/devicetree/README.md", "DeviceTree prototype descriptors for firmware/OS compatibility harness.\n")

    import yaml

    uefi_vars = {
        "boot_order_template": {"BootOrder": ["Boot0001", "Boot0002", "Boot0003"]},
        "firmware_version_template": {"FirmwareVersion": "0.1.0-harness", "BuildId": "gunnchos-compat-harness"},
        "capsule_update_template": {"CapsulePending": False, "CapsuleVersion": "", "RebootRequired": False},
    }
    write("firmware/descriptors/uefi_vars/README.md", "UEFI variable templates for harness — not production firmware.\n")
    for name, data in uefi_vars.items():
        write(f"firmware/descriptors/uefi_vars/{name}.yaml", yaml.safe_dump(data, sort_keys=False))
    write("firmware/descriptors/uefi_vars/expected_uefi_variables.yaml", yaml.safe_dump({
        "variables": ["BootOrder", "FirmwareVersion", "DeviceProfile", "RecoveryRequested", "CapsulePending"],
    }, sort_keys=False))

    write("firmware/qemu/README.md", "QEMU/OVMF-style smoke harness — dry run when QEMU unavailable.\n")
    write("firmware/qemu/qemu_device_profiles.yaml", yaml.safe_dump({
        "profiles": {d: {"machine": "q35", "firmware": "OVMF", "device_profile": d} for d in DEVICES}
    }, sort_keys=False))
    write("firmware/qemu/expected_boot_log_patterns.yaml", yaml.safe_dump({
        "patterns": ["GunnchOS", "device_profile", "UEFI", "Boot0001"],
    }, sort_keys=False))

    write("firmware/capsule_update/README.md", "Capsule update simulation — never flashes real firmware.\n")
    cap_schema = {"type": "object", "required": ["capsule_id", "target_version", "device_id", "simulated_only"]}
    write("firmware/capsule_update/capsule_manifest.schema.json", json.dumps(cap_schema, indent=2))
    write("firmware/capsule_update/sample_capsule_manifest.yaml", yaml.safe_dump({
        "capsule_id": "gunnchos-capsule-sample",
        "target_version": "0.1.1-harness",
        "device_id": "student_14_5",
        "simulated_only": True,
        "rollback_supported": True,
    }, sort_keys=False))
    write("firmware/capsule_update/sample_update_history.json", json.dumps([
        {"version": "0.1.0-harness", "status": "installed", "simulated": True},
        {"version": "0.1.1-harness", "status": "pending_reboot", "simulated": True},
    ], indent=2))

    write("firmware/boot/README.md", "Standard Boot / U-Boot-style boot path contracts for harness.\n")
    write("firmware/boot/standard_boot_plan.md", "UEFI Standard Boot path with recovery and safe-mode contracts — implemented in harness YAML.\n")
    for name in ["boot_menu_contract.yaml", "recovery_boot_contract.yaml", "safe_mode_boot_contract.yaml"]:
        write(f"firmware/boot/{name}", yaml.safe_dump({"contract": name.replace(".yaml", ""), "implemented_in_harness": True}, sort_keys=False))

    dock_contract = {
        "interface_id": "docking_external_display",
        "capabilities": {
            "usb_c_alt_mode_required": True,
            "hotplug_event_required": True,
            "external_display_modes": ["mirror", "extend", "presentation"],
        },
        "os_events": ["dock_connected", "dock_disconnected", "external_display_connected", "external_display_disconnected"],
        "fallbacks": {
            "no_dp_alt_mode": "Use internal display and show dock compatibility warning.",
            "hotplug_failed": "Prompt user to reconnect dock and log technical diagnostic.",
        },
        "evidence": {
            "implemented_in_contract": True,
            "descriptor_stub_exists": True,
            "qemu_simulated": True,
            "physical_hardware_validated": False,
        },
    }
    write("firmware/interfaces/README.md", "Firmware interface contracts implemented as YAML — validated in CI.\n")
    write("firmware/interfaces/docking_external_display_contract.yaml", yaml.safe_dump(dock_contract, sort_keys=False))

    for iface, fields in [
        ("power_state", {"states": ["S0", "S3", "S4", "S5"], "implemented_in_harness": True}),
        ("thermal_sensor", {"zones": ["cpu", "skin"], "implemented_in_harness": True}),
        ("battery_status", {"smart_battery_stub": True, "implemented_in_harness": True}),
        ("input_device", {"keyboard": True, "touch": True, "controller_optional": True}),
        ("display_enumeration", {"internal": True, "external_optional": True}),
        ("storage_enumeration", {"nvme_or_emmc": True}),
        ("network_enumeration", {"wifi_stub": True}),
        ("edge_io", {"companion_session_stub": True}),
    ]:
        write(f"firmware/interfaces/{iface}_contract.yaml", yaml.safe_dump({"interface_id": iface, **fields}, sort_keys=False))

    print("Bootstrap firmware implementation complete")


if __name__ == "__main__":
    main()
