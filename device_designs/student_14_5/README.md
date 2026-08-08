# Student 14.5 — hardware electrical package

Updated: 2026-08-08T01:15:00Z  
ADR compute: ADR-FP-001 (Ultra 7 155H class)  
ADR integration: **ADR-HW-001 COM/carrier**  
PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Exact architecture (honest)
```
[COM-HPC Client Mini — Core Ultra 7 155H class + LPDDR5x on-module]
        │  high-speed connector (vendor pinout)
        ▼
[Carrier PCB — designed in this repo]
  • EC (keyboard/battery/thermal fans)
  • PD (TPS65994) + charger (BQ25792) + fuel gauge (BQ40Z50)
  • M.2 Key E: Intel BE200 Wi-Fi 7
  • M.2 Key B 3052: Quectel RM520N-GL (5G NR Sub-6 — NOT 6G)
  • eDP → 14.5" panel; USB-C/USB4 to dock
  • TPM footprint SLB9672; audio ALC256 class; webcam FPC
```

**Forbidden:** inventing Intel CPU BGA ball map in KiCad.

## Package map
- Architecture: `architecture.md`
- COM/carrier ICD: `docs/com_carrier_icd.md`
- BOM: `bom/assembly_bom.csv`
- Power/thermal/battery: `electrical/*.yaml`
- Radios: `docs/radios.md`
- Drivers: `../` family `DRIVER_CLASSIFICATION.md` + `drivers/README.md`
- KiCad: `kicad/` (mirrored to `electrical/student_14_5/kicad/`)

## Status
`STUDENT_COM_CARRIER_ARCHITECTURE_DOCUMENTED`  
Not claimed: physical bring-up, CLI ERC/DRC pass, fab.
