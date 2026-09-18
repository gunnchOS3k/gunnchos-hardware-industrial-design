# OS ↔ Hardware v1 contract (RC1-safe)

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Bound software identity (DO NOT MODIFY in this campaign)
- Device OS / Portal / WAIKE / gunnchAI / HumanValidationFreezeManifest **v1.0.0-rc.1** identity remains frozen.
- This contract only documents hardware interface expectations compatible with RC1.

## Host platforms (mainline)
| SKU | Compute | Display | Storage/Wi-Fi | Optional WWAN |
|---|---|---|---|---|
| Student 14.5 | COM-HPC Mini MTL-class | IPS eDP | M.2 NVMe + M.2 Key E | Telit FN990B40-class |
| DS-XL Coder | same module | Dual IPS eDP | same | same |
| Handheld Hybrid (EVT mule) | COM-HPC Mini mule | IPS (mule panel) | same | optional |
| Handheld Hybrid (production) | PENDING_PHYSICAL_MEASUREMENT | — | — | — |

## Dock
- Gen-1: USB4 40 + PD EPR
- USB4 80: experimental only

## Rings
- MCU: nRF54L15 class
- Sensors: IMU + cap/touch
- Charge EVT: magnetic cradle
- Inductive / sEMG: experimental

## Firmware
- Host: vendor UEFI
- EC / rings: Zephyr
- coreboot / RAUC: experimental

## Non-claims
No physical validation, certification, or manufacturing validation asserted by this contract.
