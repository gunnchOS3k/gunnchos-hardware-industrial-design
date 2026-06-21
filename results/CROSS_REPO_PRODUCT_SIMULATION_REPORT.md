# Cross-Repo Product Simulation Report

## Component stacks (hardware repo simulation)

| Device | Recommended stack | Evidence |
|---|---|---|
| student_14_5 | x86 mobile APU, 16-32GB, NVMe, Wi-Fi 6E/7, DP Alt Mode | component_selection/results/ |
| handheld_hybrid | x86 handheld APU, 16GB, active cooling, dock | simulated |
| ds_xl_coder | dual-screen module, 8-16GB | simulated |
| wearables_arena_set | low-power MCU/SoC, BLE/UWB class | simulated |

## Firmware harness

Manifests, descriptors, QEMU dry-run, capsule simulation — PASS (see FIRMWARE_COMPATIBILITY_SMOKE_REPORT.md).

## Secure boot simulation

Test keys in secure_boot/keys/ — simulated_pass (non-production).

## OS runtime compatibility

hardware_component_runtime/results/os_component_runtime_simulation.json — 4 devices evaluated.

## Persona/workload fit

component_selection/results/user_persona_fit.json, workload_fit_results.json

## Unresolved physical validation

See implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md (hardware) and OS REAL_DEVICE_VALIDATION_ISSUES.md.

## Validators run

validate_component_selection, validate_secure_boot_simulation, validate_firmware_*, run_full_hardware_simulation, pytest

## Claim boundary

Host/emulated implementation complete. Physical-board validation and certification not claimed.
