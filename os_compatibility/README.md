# OS Compatibility Handoff

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
- OS commit inspected: `7f26faf900039bfcf0618df99defd8489f8a13d3` on `main`

This hardware repo provides OS compatibility assumptions, manifests, and validation checklists. It does not prove real hardware boot, HLK certification, driver certification, UEFI/ACPI implementation, secure boot completion, thermal/battery validation, or production hardware compatibility.
