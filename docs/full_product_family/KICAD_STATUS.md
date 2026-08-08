# KiCad status — hardware family depth

Updated: 2026-08-08T01:15:00Z

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

Until then: **static/text structure only**. No claim of ERC/DRC pass.

## Source locations
| Product | Schematic | PCB |
|---|---|---|
| Student | `device_designs/student_14_5/kicad/` + `electrical/student_14_5/kicad/` | same |
| DS-XL | `device_designs/ds_xl_coder/kicad/` + `electrical/ds_xl_coder/kicad/` | same |
| Handheld | `device_designs/handheld_hybrid/kicad/` + `electrical/handheld_hybrid/kicad/` | same |
| Rings | `gate1_digital_fabrication/edge_io_ring/schematic/kicad/` + `device_designs/edge_io_rings/kicad/` | gate1 pcb/kicad |
| Dock | `device_designs/dock/kicad/` + `gate1_digital_fabrication/dock/kicad/` + `electrical/dock/kicad/` | device_designs/dock/pcb |

## Tokens
Claimed: digital schematic/PCB **structure present**  
Not claimed: `KICAD_CLI_ERC_PASS`, `KICAD_CLI_DRC_PASS`, fab-ready Gerbers
