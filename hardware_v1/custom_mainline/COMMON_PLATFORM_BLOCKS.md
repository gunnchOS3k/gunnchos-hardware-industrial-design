# Common Platform Core schematic/architecture blocks

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


Reusable blocks intended for Student-MB-v1 / Handheld-MB-v1 / DSXL-MB-v1 / CPB0:

- SoC power
- DDR5
- SPI/boot flash
- TPM
- EC
- USB4
- PCIe/NVMe
- Wi-Fi
- optional 5G
- audio
- camera
- display
- USB-C/PD
- debug/recovery

## Ownership rule

Each block is MAINLINE_CUSTOM architecture documentation until vendor collateral + EDA make nets accurate.
Block reuse does **not** imply identical PCB layout or proven SI/PI closure.
