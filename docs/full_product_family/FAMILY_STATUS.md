# Per-product status table

Updated: 2026-08-08T19:40:00Z  
Evidence class default: **MODELED / DIGITAL** unless noted.  
Release claim: **CANDIDATE** — see `HARDWARE_DESIGN_RELEASE_STATUS.md` / `RELEASE_CRITERIA.md`.

| Product | Exact compute MPN | Electrical arch | BOM | Power | Thermal | Battery | Radios/RF | Drivers | KiCad sources | CLI ERC/DRC | Physical | Release |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Student 14.5 | **COM-HPC-mMTL-155H-32G** | COM+carrier **FROZEN_DIGITAL** | Exact MPN BOM | Yes | Yes | Yes | BE200 + RM520N-GL (+ RF model) | Yes | Carrier hierarchical sch + PCB + mfg | **ABSENT → EDMUND_ACTION_REQUIRED** | PENDING / FREEZE | CANDIDATE (not COMPLETE) |
| DS-XL Coder | **COM-HPC-mMTL-155H-32G** | Shared COM + dual eDP | Exact MPN BOM | Yes | Yes | Shared class | Shared WWAN/Wi-Fi | Yes | Dual-panel sch + ICD + mfg | ABSENT → EDMUND | PENDING / FREEZE | CANDIDATE |
| Handheld Hybrid | **RM121-D8E32** | NX5 SoM + game carrier | Exact MPN BOM | Yes (game) | Yes | 5–6 Ah class | Wi-Fi 6E + opt RM520N-GL | Yes | SoM carrier + mfg | ABSENT → EDMUND | PENDING / FREEZE | CANDIDATE |
| Edge I/O Rings | **nRF52840-QIAA-R** | ADR-FP-008 fusion | Fusion BOM | Yes | Wearable | 40–250 mAh | BLE + opt UWB RF | Yes | KiCad + Fusion CAD package | ABSENT → EDMUND | PENDING / FREEZE | CANDIDATE |
| Dock | **JHL9040** | Full discrete PCB | Expanded | Yes | Passive | N/A AC PD | Opt UWB | Yes | Full digital PCB + mfg | ABSENT → EDMUND | PENDING / FREEZE | CANDIDATE |

## Honesty notes
- No in-house Intel/Rockchip CPU BGA layout.
- Modem is **5G NR Sub-6** Quectel RM520N-GL — **not** 6G; **no NTN** claim (public verify doc).
- `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` **not** earned (placeholder symbols + missing kicad-cli).
