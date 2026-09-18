# Experiments registry

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Hierarchy

### Mainline
`CUSTOM AMD EMBEDDED X86 MOTHERBOARD` (gunnchOS Platform Core v1)

### Simpler/reference alternatives
- COM-HPC Mini modular x86
- ARM/IQ-X SoM
- ODM-customized x86
- COTS dock
- nRF54L15 DK

### Product experiments
- OLED, USB4 80, inductive ring charging, sEMG, coreboot/openSIL, RAUC, DS-XL X100, Student P100 AI-first

> Does the simpler or specialized variant outperform the custom mainline enough to justify giving up some control or increasing specialization?

| ID | Branch | Baseline | Variant |
|---|---|---|---|
| EXP-ARM-IQX-001 | `hardware/exp-arm-iqx` | CUSTOM AMD Platform Core v1 (8840U/8845HS) | ARM IQX-class SoM (vendor TBD — PENDING_VENDOR_CONFIRMATION) |
| EXP-STUDENT-OLED-001 | `hardware/exp-student-oled` | IPS eDP panel on custom Student-MB-v1 | OLED eDP panel class |
| EXP-DSXL-OLED-HYBRID-001 | `hardware/exp-dsxl-oled-hybrid` | IPS eDP + DDI/DP on custom DSXL-MB-v1 | OLED primary + IPS secondary |
| EXP-DOCK-USB4-80-001 | `hardware/exp-dock-usb4-80` | CUSTOM_GUNNCHOS_DOCK_GEN1 USB4 40 (JHL8440 + JHL9040R class) | USB4 80-class controller (vendor TBD — PENDING_VENDOR_CONFIRMATION) |
| EXP-RINGS-INDUCTIVE-001 | `hardware/exp-rings-inductive-charge` | Magnetic cradle pogo/contacts (custom ring mainline) | Qi-class or proprietary inductive coil |
| EXP-RINGS-SEMG-001 | `hardware/exp-rings-semg-wrist` | IMU + capacitive/touch custom ring | sEMG wrist accessory |
| EXP-COREBOOT-001 | `hardware/exp-coreboot` | Vendor-supported UEFI + AGESA on custom AMD motherboard | coreboot and/or AMD openSIL when production-capable for selected platform |
| EXP-RAUC-001 | `hardware/exp-rauc-update` | Vendor capsule + custom EC update orchestration | RAUC A/B |
| EXP-COM-HPC-MODULAR-001 | `hardware/exp-com-hpc-modular-product` | CUSTOM AMD Platform Core v1 (8840U/8845HS) | ADLINK COM-HPC Mini mMTL + Mini Base REFERENCE_CONTROL_MODULAR_X86 |
| EXP-DSXL-X100-001 | `hardware/exp-dsxl-x100` | Ryzen Embedded 8845HS Platform Core | Ryzen AI Embedded X168i-class (PENDING_VENDOR_CONFIRMATION) |
| EXP-P100-AI-001 | `hardware/exp-student-p100-ai` | Ryzen Embedded 8840U Platform Core | Ryzen AI Embedded P132 / P132i-class (PENDING_VENDOR_CONFIRMATION) |
