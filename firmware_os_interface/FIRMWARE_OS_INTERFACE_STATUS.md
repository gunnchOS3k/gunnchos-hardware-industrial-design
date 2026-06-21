# Firmware OS Interface Status

Current status: implemented in emulation/host harness.
Implemented in firmware compatibility harness: manifests, ACPI/DeviceTree descriptors, interface contracts, QEMU/OVMF dry-run harness, capsule update simulation.

Not yet proven on physical hardware: UEFI/ACPI on silicon, secure boot production readiness, TPM/measured boot on board, real hardware profile discovery, driver enumeration on board, firmware handoff on board, recovery boot on board, USB-C DP Alt Mode physical validation, or HLK certification.

Physical-board validation remains pending.
