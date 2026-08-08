# Student 14.5 — hardware design release candidate

Updated: 2026-08-08T19:40:00Z  
ADR compute: ADR-FP-001 (Ultra 7 155H)  
ADR integration: **ADR-HW-001** exact COM MPN  
PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Exact architecture
```
[ADLINK COM-HPC-mMTL-155H-32G — Ultra 7 155H + 32GB LPDDR5x on-module]
        │  COM-HPC Mini connector (vendor pinout / NDA guide)
        ▼
[Carrier PCB — designed in this repo]
  • EC (ITE5570 / NPCX9)
  • PD (TPS65994ADFBRQ1) + charger (BQ25792) + gauge (BQ40Z50-R2)
  • M.2 Key E: Intel BE200
  • M.2 Key B 3052: Quectel RM520N-GL (5G NR Sub-6 — NOT 6G; NO NTN)
  • eDP → 14.5" panel; USB-C/USB4 to dock
  • TPM SLB9672XQ2.0; audio ALC256; webcam FPC
```

**Forbidden:** inventing Intel CPU BGA ball map in KiCad.

## Package map
- Architecture: `architecture.md`
- COM/carrier ICD: `docs/com_carrier_icd.md`
- BOM: `bom/assembly_bom.csv` (exact COM MPN)
- Power/thermal/battery/RF: `electrical/*.yaml`
- Radios: `docs/radios.md`
- Manufacturing: `manufacturing/`
- KiCad: `kicad/` (mirrored to `electrical/student_14_5/kicad/`)

## Status
`STUDENT_HARDWARE_DESIGN_RELEASE_CANDIDATE`  
**Not** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` (placeholder symbols + kicad-cli absent → EDMUND_ACTION_REQUIRED).
