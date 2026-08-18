# Known external blockers — Handheld Hybrid
**Digital release status:** `DIGITAL_RELEASE_READY`
Source of truth: `artifacts/hw_fw_rc_001/EDMUND_EXTERNAL_BLOCKERS.json` and `DIGITAL_MANUFACTURING_READINESS.md`.

## This SKU (does not revoke DIGITAL_RELEASE_READY)

Public NX5 pinout is complete. Remaining items are AVL/process, not NDA pin maps:

| ID | Item |
|---|---|
| `UNRES-HH-PANEL-MPN` / `UNRES-HH-DISPLAY-DIAGONAL` | Exact panel MPN; BOM 7in vs OS export 8.4 |
| `UNRES-SODIMM-CONNECTOR-MPN` | Exact 260-pin socket MPN |
| `UNRES-STICK-MPN` | Analog stick production MPN |
| `UNRES-HH-OS-EXPORT-STORAGE` / `UNRES-HH-OS-EXPORT-RAM` | Align OS export to 32 GB eMMC + 8 GB RAM SoT |
| `UNRES-BATTERY-CELL-MPN` | Pack/cell MPN + UN38.3 |

## Family (all SKUs)

| ID | Why it remains |
|---|---|
| `UNRES-PASTE-REFLOW` | CM DFM paste/reflow values |
| `UNRES-SIGNED-FW-BIN` | Production signed image + ICT limits |
| `UNRES-IMPEDANCE-SI` | `si_simulation_performed: false` |
| FCC / CE / USB-IF | Digital prep only; labs not engaged |
| `PHYSICAL_PENDING` | No assembled EVT unit |

Do not invent values for these.
