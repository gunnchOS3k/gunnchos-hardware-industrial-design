# Hardware to OS Traceability

Cross-repo traceability from hardware artifacts to OS compatibility layer.

| Hardware artifact | OS repo artifact | Device class impact | Compatibility implication | Evidence status | Blocking before release? |
|---|---|---|---|---|---|
| product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md | hardware_compat/device_profiles/*.yaml | All four SKUs | Defines capabilities OS mirrors | documented | Yes |
| architecture/PRODUCT_LINE_ARCHITECTURE.md | docs/DEVICE_ARCHITECTURE.md | All | System context for boot/policy | documented | Yes |
| architecture/DEVICE_COMPARISON_MATRIX.md | hardware_compat/DEVICE_CLASS_COMPATIBILITY_MATRIX.md | All | SKU feature differences | documented | Yes |
| architecture/OS_HARDWARE_CONTRACT.md | hardware_compat/HARDWARE_COMPATIBILITY_CONTRACT.md | All | Architecture contract | documented | Yes |
| io/PORT_IO_MASTER_MATRIX.md | docs/HARDWARE_STORAGE_NETWORK_POLICY.md | All | Port/storage/network policy | documented | Yes |
| power/POWER_BUDGET_MASTER.md | docs/HARDWARE_POWER_THERMAL_POLICY.md | All | Power assumptions | simulated | Yes |
| battery/BATTERY_REQUIREMENTS.md | docs/HARDWARE_POWER_THERMAL_POLICY.md | All | Battery runtime evidence | needs_real_hardware | Yes |
| thermal/THERMAL_REQUIREMENTS.md | docs/HARDWARE_POWER_THERMAL_POLICY.md | All | Thermal throttle evidence | needs_real_hardware | Yes |
| compliance/REGULATORY_MATRIX.md | hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md | All | Regulatory rows | needs_external_review | Yes |
| dvt/DVT_STATUS.md | hardware_release/HARDWARE_COMPATIBILITY_STATUS.md | All | DVT blocks release | blocked | Yes |
| pvt/PVT_STATUS.md | hardware_release/HARDWARE_COMPATIBILITY_RELEASE_REQUIREMENTS.md | All | PVT required | blocked | Yes |
| certification/CERTIFICATION_STATUS.md | hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md | All | Cert evidence | blocked | Yes |
| production_release/PRODUCTION_RELEASE_STATUS.md | hardware_release/HARDWARE_COMPATIBILITY_STATUS.md | All | Production gate | blocked | Yes |
| versions/prototype_evt1/README.md | boot_readiness/DEVICE_BOOT_SEQUENCE.md | EVT-1 | Prototype boot plan | documented | Yes |
| versions/production_candidate/README.md | hardware_release/HARDWARE_PILOT_TEST_PLAN.md | Production track | Pilot test alignment | documented | Yes |
| os_compatibility/device_class_exports/*.yaml | hardware_compat/device_profiles/*.yaml | All | Reciprocal profile export | documented | Yes |
| firmware_os_interface/ | boot_readiness/ | All | Firmware/boot requirements | documented | Yes |
| hardware_os_validation/ | hardware_release/HARDWARE_VALIDATION_LAB_CHECKLIST.md | All | Lab validation plan | documented | Yes |
| hlk_readiness/ | hardware_release/HARDWARE_COMPATIBILITY_EVIDENCE_MATRIX.md | Windows path | HLK-style future path | documented | No |


## Evidence status legend

| Status | Meaning |
|--------|---------|
| documented | Artifact exists and is linked |
| simulated | Software-only or planning assumption |
| needs_real_hardware | Requires physical device evidence |
| needs_external_review | Requires lab/vendor/reviewer signoff |
| blocked | Gate not met — blocks release |
| passed | Lab evidence linked (**none in this matrix**) |

This hardware repo provides OS compatibility assumptions, manifests, and validation checklists. It does not prove real hardware boot, HLK certification, driver certification, UEFI/ACPI implementation, secure boot completion, thermal/battery validation, or production hardware compatibility.
