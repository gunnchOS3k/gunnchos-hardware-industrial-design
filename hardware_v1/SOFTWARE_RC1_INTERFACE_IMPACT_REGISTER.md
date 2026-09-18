# Software RC1 interface impact register

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Freeze
Device OS / Portal / WAIKE / gunnchAI / HumanValidationFreezeManifest **v1.0.0-rc.1** must not be modified by this hardware campaign.

## Hardware deltas vs prior digital packages
| Area | Delta | RC1 software impact | Disposition |
|---|---|---|---|
| Handheld EVT mule compute | Radxa NX5 historical → COM-HPC Mini mule | Boot/ACPI/device-tree expectations may differ | Document only; no RC1 code change in this campaign |
| Rings MCU | nRF52840 → nRF54L15 class | BLE stack / DFU descriptors may need future SW rev | Register only; keep RC1 freeze |
| WWAN preferred | Quectel → Telit FN990B40-class preferred | Modem manager IDs may differ | Optional SKU; RC1 untouched |
| Dock | USB4 40 unchanged mainline | None | — |
| Firmware | Vendor UEFI + Zephyr EC affirmed | None if vendor paths already assumed | coreboot/RAUC experimental only |

## Rule
Future software changes require a separate software campaign after hardware measurements — not silent edits here.
