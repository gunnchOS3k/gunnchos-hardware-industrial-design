# RP0-A compute platform (ADLINK COTS)

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0B_RP0_COTS_BLOCKER_CLOSURE`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

## Mainline binding
COM-HPC Mini x86 Meteor Lake-class remains mainline.

## RP0-A COTS path
| Item | Selection | Evidence |
|---|---|---|
| Module family | COM-HPC-mMTL | https://www.adlinktech.com/products/computer_on_modules/com-hpc_mini_module/com-hpc-mmtl |
| Module SKU | `COM-HPC-mMTL-155H-32G` | ADLINK ordering information (live page hit) |
| Reference carrier | COM-HPC Mini Base (ATX) | ADLINK reference carrier |
| Cooling | Released heat spreader / fan for mMTL | VERIFY_AT_PURCHASE exact accessory SKU |
| Display interfaces | **1x eDP 1.4b + 2x DDI** (DP/HDMI/DVI) | ADLINK wiki/module docs — **not dual native eDP** |

## Required RP0-A capabilities
gunnchOS boot, NVMe, Wi-Fi, optional M.2 cellular, native eDP test, second-display DDI/DP test,
USB4 test, camera path where carrier supports, audio, GPIO/I2C/SPI, power measurement, debug/recovery.

## EXT-COM-HPC-400PIN
`STILL_VENDOR_GATED_FOR_RP0_B` — COTS base does **not** unlock custom 400-pin net-accurate fab.
`EXT_COM_HPC_400PIN_RP0_A_BLOCKING=false`
`EXT_COM_HPC_400PIN_RP0_B_BLOCKING=true`
