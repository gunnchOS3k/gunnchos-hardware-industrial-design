# Hardware v1.0 decision ledger

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

One mainline per decision. Alternatives are EXPERIMENTAL_COMPARE only.

| ID | Topic | State | Mainline | Experiment / gate |
|---|---|---|---|---|
| `DEC-COMPUTE-001` | Student 14.5 / DS-XL compute module | `ADOPTED_MAINLINE` | COM-HPC Mini x86 Meteor Lake-class module (ADLINK COM-HPC-mMTL-155H-32G class) for EVT | EXP-ARM-IQX (ARM IQX-class SoM) |
| `DEC-COMPUTE-002` | Handheld Hybrid compute for EVT | `ADOPTED_MAINLINE` | COM-HPC Mini EVT mule (shared Meteor Lake-class module) for electrical/thermal bring-up | — |
| `DEC-COMPUTE-003` | Handheld production board | `PENDING_PHYSICAL_MEASUREMENT` | Production handheld carrier/board geometry PENDING_PHYSICAL_MEASUREMENT after EVT mule data | EVT mule bring-up measurements |
| `DEC-DISPLAY-001` | Student / DS-XL display technology | `ADOPTED_MAINLINE` | IPS LCD panels (Student: single eDP; DS-XL: one native eDP + DDI/DP second display). Not dual native eDP unless authoritative module docs prove it. | EXP-STUDENT-OLED, EXP-DSXL-OLED-HYBRID |
| `DEC-STORAGE-001` | Storage / Wi-Fi | `ADOPTED_MAINLINE` | M.2 NVMe storage + M.2 Key E Wi-Fi (Intel BE200 class) | — |
| `DEC-CELLULAR-001` | Optional cellular | `ADOPTED_MAINLINE` | Optional Telit FN990B40 M.2 5G Sub-6 module exact MPN FN990B40W01T010300; Quectel RM520N-GL approved alternate | PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING |
| `DEC-DOCK-001` | Dock Gen-1 link rate | `ADOPTED_MAINLINE` | USB4 40 Gbps (Intel JHL8440 + JHL9040R retimer) + USB-C PD EPR-class controller | EXP-DOCK-USB4-80 |
| `DEC-RINGS-001` | Rings MCU | `ADOPTED_MAINLINE` | Nordic nRF54L15 (BLE + LE Audio). RING_EVT_ELECTRICAL_PLATFORM=QFN48/DK reference (PCA10156); RING_FORM_FACTOR_CANDIDATE=CSP47 | CSP47 wearable HDI/assembly feasibility before form-factor board |
| `DEC-RINGS-002` | Rings sensing + charge EVT | `ADOPTED_MAINLINE` | IMU + capacitive/touch + magnetic cradle charge contacts for EVT | EXP-RINGS-INDUCTIVE-CHARGE, EXP-RINGS-SEMG-WRIST |
| `DEC-FW-001` | Host firmware stack | `ADOPTED_MAINLINE` | Vendor UEFI on COM-HPC module + Zephyr EC on companion MCU | EXP-COREBOOT, EXP-RAUC-UPDATE |
| `DEC-BATT-001` | Battery chemistry | `ADOPTED_MAINLINE` | Qualified Li-ion / LiPo only; no experimental chemistries in mainline | solid-state / Na-ion = DEFERRED_GEN2 |
| `DEC-QA-001` | PCB assembly quality class | `ADOPTED_MAINLINE` | IPC Class 2 baseline with selective tighter controls on BGA/COM connector / RF keepouts (not blanket Class 3) | — |
| `DEC-RP0-001` | Reference Platform 0 scope | `ADOPTED_MAINLINE` | Two-stage RP0: RP0-A COTS Integration Bench (ADLINK Mini Base + mMTL + nRF54L15 DK + COTS USB4 dock) then RP0-B custom gunnchOS carrier/dock/ring EVT electronics | ORDER_RP0_A_COTS_BRINGUP_KIT (Cursor does not purchase) |
