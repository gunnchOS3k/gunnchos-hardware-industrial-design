# OS / hardware interface traceability

Interface-level map from this hardware repo to `gunnchos-device-os`. Complements the document-level matrix in [HARDWARE_TO_OS_TRACEABILITY.md](HARDWARE_TO_OS_TRACEABILITY.md).

**Evidence class:** documented / harness / modeled. **No physical boot, HLK, or certification is claimed.**

Device-os counterparts below are the paths that exist in the sibling checkout (`hardware_compat/`, `docs/HARDWARE_SOFTWARE_CONTRACT.md`, `docs/HARDWARE_OS_TRACEABILITY.md`). If a device-os file is renamed, update this table; do not invent OS APIs.

## Contract surfaces

| Hardware | Device OS | Status |
|---|---|---|
| `docs/OS_HARDWARE_CONTRACT.md` | `docs/HARDWARE_SOFTWARE_CONTRACT.md` | documented |
| `architecture/OS_HARDWARE_CONTRACT.md` | `hardware_compat/HARDWARE_COMPATIBILITY_CONTRACT.md` | documented |
| `os_compatibility/OS_HARDWARE_CONTRACT_V2.md` | same + firmware obligations | documented; flash layout TBD on hardware side |
| `product/CLAIM_BOUNDARY.md` | `hardware_compat/HARDWARE_CLAIM_BOUNDARY.md` | documented |
| `os_compatibility/device_class_exports/*.yaml` | `hardware_compat/device_profiles/*.yaml` | profile_mirror; see unresolved export mismatches |
| `mechanical_correctness/device_mechanical_targets.json` | profile `hardware_repo_source_paths` | documented, not physically proven |

## Firmware interface YAML → requirements → OS

| `firmware/interfaces/` | `firmware_os_interface/` | Harness fields (source) | Physical |
|---|---|---|---|
| `power_state_contract.yaml` | `POWER_STATE_REQUIREMENTS.md` | states S0, S3, S4, S5; `implemented_in_harness: true` | pending |
| `battery_status_contract.yaml` | `BATTERY_STATUS_INTERFACE_REQUIREMENTS.md` | `smart_battery_stub: true` | pending |
| `thermal_sensor_contract.yaml` | `THERMAL_SENSOR_INTERFACE_REQUIREMENTS.md` | zones cpu, skin; stub | pending |
| `display_enumeration_contract.yaml` | `DISPLAY_ENUMERATION_REQUIREMENTS.md` | internal true; external_optional true | pending |
| `input_device_contract.yaml` | `INPUT_DEVICE_ENUMERATION_REQUIREMENTS.md` | keyboard/touch; controller_optional | pending |
| `docking_external_display_contract.yaml` | `DOCKING_AND_EXTERNAL_DISPLAY_REQUIREMENTS.md` | USB-C DP Alt Mode required; `physical_hardware_validated: false` | pending |
| `storage_enumeration_contract.yaml` | (handoff via OS storage docs) | `nvme_or_emmc: true` | pending; SKU SoT may be eMMC-only |
| `network_enumeration_contract.yaml` | (handoff via OS network docs) | `wifi_stub: true` | pending |
| `edge_io_contract.yaml` | ring firmware hooks | `companion_session_stub: true` | pending |

Boot / recovery: `firmware/boot/safe_mode_boot_contract.yaml`, `firmware_os_interface/BOOT_DISCOVERY_REQUIREMENTS.md`, `RECOVERY_BOOT_REQUIREMENTS.md`, `os_compatibility/OS_BOOT_EXPECTATIONS.md` ↔ device-os `boot_readiness/` (OS-side; not proven on silicon).

Secure boot / TPM: `firmware_os_interface/SECURE_BOOT_REQUIREMENTS.md`, `TPM_AND_MEASURED_BOOT_REQUIREMENTS.md`, `secure_boot/` — simulation only.

Capsule update: `firmware/capsule_update/` `simulated_only: true` in handheld manifest.

## Electrical → OS power/thermal policy

| Hardware | Device OS (documented consumer) | Evidence |
|---|---|---|
| `device_designs/handheld_hybrid/electrical/power_tree.yaml` | `docs/HARDWARE_POWER_THERMAL_POLICY.md` | MODELED + PUBLIC_PINOUT; not measured |
| `device_designs/student_14_5/electrical/power_tree.yaml` | same | PUBLIC_DOCS; COM-HPC NDA remaining |
| `device_designs/ds_xl_coder/electrical/power_tree.yaml` | same | PUBLIC_DOCS |
| `device_designs/edge_io_rings/electrical/power_tree.yaml` | same | PUBLIC_DOCS; candidate cell |
| `device_designs/dock/electrical/power_tree.yaml` | same | MODELED NDA rail `VDD_USB4` |
| `power/POWER_TREE.md` | same | EVT-1 skeleton mermaid |
| `power/*_power_budget.csv` | same | schema-validated; not lab runtime |
| `thermal/*` | same | plans; `needs_real_hardware` |

## BOM / compute SoT → OS profiles

Hardware SoT for compute is the per-SKU assembly BOM and digital release JSON, not the OS export if they disagree.

| SKU | Hardware SoT | Hardware OS export | Device-os profile (sibling) | Trace status |
|---|---|---|---|---|
| handheld_hybrid | BOM `RM121-D8E32` 8GB + 32GB eMMC; `artifacts/hw_fw_rc_001/products/handheld_hybrid/DIGITAL_RELEASE_PACKAGE.json` | `handheld_hybrid_os_export.yaml`: display 8.4, storage nvme 512GB, ram 12 | `hardware_compat/device_profiles/handheld_hybrid.yaml`: 8.4", eMMC 32GB, ram 8 | **UNRES-HH-DISPLAY-DIAGONAL**, **UNRES-HH-OS-EXPORT-STORAGE**, **UNRES-HH-OS-EXPORT-RAM** |
| student_14_5 | ADLINK COM-HPC-mMTL-155H-32G (named); NDA pin map | `student_14_5_os_export.yaml`: ram_gb 8, display 14.5 | `device_profiles/student_14_5.yaml` | **UNRES-COM-HPC-400PIN**, **UNRES-STUDENT-RAM-EXPORT** |
| ds_xl_coder | shared COM-HPC + dual eDP ICD | `ds_xl_coder_os_export.yaml` | `device_profiles/ds_xl_coder.yaml` | **UNRES-COM-HPC-DUAL-EDP**, **UNRES-DSXL-PANEL-MPN** |
| edge_io_rings / wearables | nRF52840-QIAA-R BOM | `wearables_arena_set_os_export.yaml` | `device_profiles/wearables_arena_set.yaml` | digital DT/west; physical boot pending |
| dock | JHL8440 + JHL9040R topology | (dock is accessory; no separate OS SKU export) | dock enumeration via USB-C contract | **UNRES-JHL8440-BALLS**, **UNRES-JHL9040R-BALLS** |

This pass does **not** rewrite OS export numbers to invent a freeze. Mismatches stay unresolved until a single cited source wins.

## CAD → OS mechanical class

| Hardware | OS |
|---|---|
| `cad/openscad/*.scad` | mechanical class assumptions only |
| `mechanical_correctness/device_mechanical_targets.json` | `hardware_compat/device_profiles/*.yaml` |
| `exports/stl/*_placeholder.stl` | not a fit proof |

## Validation hooks

| Check | Script |
|---|---|
| OS handoff files | `scripts/validate_os_compatibility_handoff.py` |
| Firmware OS interface docs | `scripts/validate_firmware_os_interface.py` |
| Firmware manifests | `scripts/validate_firmware_manifests.py` |
| This packet + UML + claim boundary | `scripts/validate_digital_manufacturing.py` |

## Claim boundary

This map proves **path alignment**. It does not prove real hardware boot, driver certification, UEFI/ACPI on silicon, secure boot production, thermal/battery validation, or production compatibility.
