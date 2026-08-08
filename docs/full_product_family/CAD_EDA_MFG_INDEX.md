# CAD / EDA / Manufacturing index

Updated: 2026-08-08T20:15:00Z

| Product | EDA | CAD | Manufacturing |
|---|---|---|---|
| Student | `device_designs/student_14_5/kicad/` | `device_designs/student_14_5/cad/` + OpenSCAD | `manufacturing/` + Gerber/STEP/PnP plans + ERC_DRC_STATUS.json |
| DS-XL | `device_designs/ds_xl_coder/kicad/` | `device_designs/ds_xl_coder/cad/` + OpenSCAD | same deepen |
| Handheld | `device_designs/handheld_hybrid/kicad/` | cad + Radxa STP reference | same deepen |
| Rings | device_designs + gate1 KiCad | **Fusion package** `cad/fusion/` + OpenSCAD twin | same deepen + `docs/BOM_SCH_FW_PARITY.md` |
| Dock | device_designs/dock/kicad + pcb | enclosure params + SCAD | same deepen; USB4/TB4 freeze |

KiCad CLI: **ABSENT → EDMUND_ACTION_REQUIRED** (brew admin; does not stall other product deepening).
