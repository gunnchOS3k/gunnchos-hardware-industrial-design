# Firmware Implementation Status

| Area | Implemented artifact | Runs today? | Evidence | Physical hardware status |
|---|---|---|---|---|
| firmware manifests | `firmware/manifests/*.yaml` | Yes | CI validation | Pending |
| ACPI descriptors | `firmware/descriptors/acpi/*_dsdt.dsl` | Yes | CI validation | Pending |
| DeviceTree descriptors | `firmware/descriptors/devicetree/*.dts` | Yes | CI validation | Pending |
| UEFI variable templates | `firmware/descriptors/uefi_vars/` | Yes | CI validation | Pending |
| QEMU/OVMF smoke harness | `firmware/qemu/run_device_profile_vm.py` | Yes (dry run) | Smoke report | Pending |
| capsule update simulation | `firmware/capsule_update/simulate_capsule_update.py` | Yes | CI + smoke | Pending |
| boot/recovery contracts | `firmware/boot/*.yaml` | Yes | CI validation | Pending |
| docking/external display interface | `firmware/interfaces/docking_external_display_contract.yaml` | Yes | CI validation | Pending |
| power state interface | `firmware/interfaces/power_state_contract.yaml` | Yes | CI validation | Pending |
| thermal sensor interface | `firmware/interfaces/thermal_sensor_contract.yaml` | Yes | CI validation | Pending |
| battery status interface | `firmware/interfaces/battery_status_contract.yaml` | Yes | CI validation | Pending |
| input/display/storage/network enumeration | `firmware/interfaces/*_contract.yaml` | Yes | CI validation | Pending |
