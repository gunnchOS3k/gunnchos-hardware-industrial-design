# Experiments registry

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

All experiments are isolated comparison tracks. Not in mainline BOM.

| ID | Branch | Title | Promotion gate |
|---|---|---|---|
| `EXP-ARM-IQX-001` | `hardware/exp-arm-iqx` | ARM IQX-class SoM vs COM-HPC Mini x86 | All metrics meet or beat baseline on EVT mule sample n>=3 AND Device OS RC1 interface register shows zero P0 breaks |
| `EXP-STUDENT-OLED-001` | `hardware/exp-student-oled` | Student OLED panel vs IPS | Power <= IPS+10% at 200 nits office; burn-in mitigation plan owner-approved |
| `EXP-DSXL-OLED-HYBRID-001` | `hardware/exp-dsxl-oled-hybrid` | DS-XL OLED+IPS hybrid vs dual IPS | Dual-eDP SI margin maintained; EXT-DSXL-DUAL-EDP resolved for both stacks |
| `EXP-DOCK-USB4-80-001` | `hardware/exp-dock-usb4-80` | Dock USB4 80 vs USB4 40 | Measured eye margin at length L with owner cables; no mainline mix until DVT |
| `EXP-RINGS-INDUCTIVE-001` | `hardware/exp-rings-inductive-charge` | Inductive ring charge vs magnetic cradle contacts | Efficiency >=70% at EVT coil; EMI does not fail pre-scan relative to baseline |
| `EXP-RINGS-SEMG-001` | `hardware/exp-rings-semg-wrist` | sEMG wrist band vs IMU/cap ring input | Safety current limits met; youth privacy review pass; not medical claim |
| `EXP-COREBOOT-001` | `hardware/exp-coreboot` | coreboot vs vendor UEFI | Zero P0 RC1 interface breaks; measured boot on EVT mule |
| `EXP-RAUC-001` | `hardware/exp-rauc-update` | RAUC A/B update vs vendor capsule/EC update | Rollback verified on EVT; no secret material in repo |
