# Per-product status table

Updated: 2026-08-08T01:15:00Z  
Evidence class default: **MODELED / DIGITAL** unless noted.

| Product | Electrical arch | BOM | Power model | Thermal model | Battery model | Radios | Drivers classified | KiCad sources | CLI ERC/DRC | Physical |
|---|---|---|---|---|---|---|---|---|---|---|
| Student 14.5 | COM-HPC Mini Meteor Lake class + carrier **FROZEN_DIGITAL** | Carrier+module BOM present | Yes | Yes | Yes (60–70 Wh) | Wi-Fi 7 BE200 + RM520N-GL | Yes | Carrier hierarchical sch + PCB structure | **ABSENT → EDMUND_ACTION_REQUIRED** | PENDING / FREEZE |
| DS-XL Coder | Shared COM + dual eDP carrier | Yes | Yes | Yes | Shared pack class | Shared with Student | Yes | Dual-panel sch structure + 2nd display ICD | ABSENT → EDMUND_ACTION_REQUIRED | PENDING / FREEZE |
| Handheld Hybrid | RK3588S SoM + game carrier | Yes | Yes (sustained game) | Yes (sustained) | 5000–6000 mAh | Wi-Fi 6E + optional WWAN | Yes | SoM carrier sch + PCB structure | ABSENT → EDMUND_ACTION_REQUIRED | PENDING / FREEZE |
| Edge I/O Rings | nRF52840 + ADR-FP-008 fusion | Fusion BOM synced | Yes | Wearable envelope | 40–250 mAh class | BLE + opt UWB | Yes | Schematic/PCB **updated with fusion parts** | ABSENT → EDMUND_ACTION_REQUIRED | PENDING / FREEZE |
| Dock | JHL9040 + PD + hub PCB | Expanded | Yes | Passive dock | N/A (AC PD) | Opt UWB companion | Yes | Full digital PCB package beyond skeleton | ABSENT → EDMUND_ACTION_REQUIRED | PENDING / FREEZE |

## Honesty notes
- Student/DS-XL do **not** claim in-house Intel CPU BGA layout; COM vendor module supplies CPU/DRAM/PCH power islands.
- Modem is **5G NR Sub-6** Quectel RM520N-GL class — **not** 6G.
