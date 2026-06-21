# DOCKING AND EXTERNAL DISPLAY REQUIREMENTS

USB-C DP alt mode and dock hotplug.

## Implementation artifacts

- firmware/interfaces/docking_external_display_contract.yaml
- firmware/descriptors/acpi/*_dsdt.dsl
- firmware/descriptors/devicetree/*.dts
- firmware/qemu/qemu_device_profiles.yaml
- firmware/tests/test_interface_contracts.py
- scripts/validate_firmware_implementation.py

## Current implementation status

Implemented in manifest/descriptor/interface-contract form and validated in CI.
Physical USB-C DP Alt Mode and dock hotplug validation still requires real hardware.

Implemented in firmware compatibility harness / OS firmware probe / cross-repo contract sync.
Physical-board validation remains pending.
