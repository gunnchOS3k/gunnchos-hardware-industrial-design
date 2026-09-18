# Firmware ownership boundary (custom mainline)

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Mainline firmware stack

- custom motherboard
- vendor-supported AMD silicon-init path
- UEFI
- Secure Boot
- TPM 2.0 / fTPM where supported
- measured boot
- signed updates
- custom EC firmware (Zephyr + MCUboot)

coreboot / AMD openSIL are **experimental only** — not production blockers.

## We own

- board configuration
- ACPI/platform tables where accessible
- EC
- boot policy
- recovery UX
- Secure Boot keys/policy
- update orchestration
- telemetry
- hardware inventory
- board-revision configuration

## Silicon vendor / IBV owns or supplies

- proprietary silicon initialization not publicly implementable
- vendor binary firmware where required
- AGESA or equivalent supported silicon-init path
