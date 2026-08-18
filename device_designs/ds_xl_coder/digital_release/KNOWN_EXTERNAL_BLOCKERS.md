# Known external blockers — DS-XL Coder
**Digital release status:** `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA`
**INDEX missing prerequisite:** `EXT-COM-HPC-400PIN` — COM-HPC Mini 400-pin net-accurate pin map AND dual eDP lane map (PICMG / ADLINK).
Also open: `EXT-DSXL-DUAL-EDP`, `UNRES-COM-HPC-DUAL-EDP`, `UNRES-DSXL-PANEL-MPN`
Source of truth: `artifacts/hw_fw_rc_001/EDMUND_EXTERNAL_BLOCKERS.json` and `DIGITAL_MANUFACTURING_READINESS.md`.

## This SKU

| ID | Item |
|---|---|
| `EXT-COM-HPC-400PIN` | COM-HPC Mini 400-pin map (blocks token) |
| `EXT-DSXL-DUAL-EDP` / `UNRES-COM-HPC-DUAL-EDP` | Dual eDP pin map (blocks token) |
| `EXT-DSXL-PANEL-AVL` / `UNRES-DSXL-PANEL-MPN` | Exact panel MPNs + hinge bend OEM spec (AVL; not sufficient alone) |

## Family (all SKUs)

| ID | Why it remains |
|---|---|
| `UNRES-PASTE-REFLOW` | CM DFM paste/reflow values |
| `UNRES-SIGNED-FW-BIN` | Production signed image + ICT limits |
| `UNRES-IMPEDANCE-SI` | `si_simulation_performed: false` |
| FCC / CE / USB-IF | Digital prep only; labs not engaged |
| `PHYSICAL_PENDING` | No assembled EVT unit |

Do not invent values for these.
