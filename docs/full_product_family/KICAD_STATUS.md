# KiCad status — hardware design release

Updated: 2026-08-08T19:40:00Z

## Environment
```
which kicad-cli → not found
which kicad → not found
```

## EDMUND_ACTION_REQUIRED
Approve macOS administrator / Homebrew install for KiCad so `kicad-cli` can run:

1. `kicad-cli sch erc` on each `*.kicad_sch`
2. `kicad-cli pcb drc` on each `*.kicad_pcb`
3. Optional Gerber/drill export for digital package completeness checks
4. Replace structural `Device:R` placeholders with vendor-accurate symbols/footprints (COM-HPC Mini connector, SODIMM-260, QFN/BGA modules)

Until then: **static/text structure only**. No claim of ERC/DRC pass. Source EDA continues to deepen under freeze.

## Source locations
| Product | Schematic / PCB / Mfg |
|---|---|
| Student | `device_designs/student_14_5/kicad/` + `electrical/student_14_5/kicad/` + `device_designs/student_14_5/manufacturing/` |
| DS-XL | `device_designs/ds_xl_coder/kicad/` + `electrical/ds_xl_coder/kicad/` + mfg |
| Handheld | `device_designs/handheld_hybrid/kicad/` + `electrical/handheld_hybrid/kicad/` + mfg |
| Rings | `device_designs/edge_io_rings/kicad/` + `gate1_digital_fabrication/edge_io_ring/` + Fusion CAD package |
| Dock | `device_designs/dock/kicad/` + `device_designs/dock/pcb/` + mfg |

## Tokens
Claimed: digital schematic/PCB **structure present** + exact MPN values in sources  
Not claimed: `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`, fab-ready Gerbers, production lib completeness
