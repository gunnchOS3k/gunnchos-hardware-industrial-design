# Known external blockers — Student 14.5
**Digital release status:** `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA`
**INDEX missing prerequisite:** `EXT-COM-HPC-400PIN` — COM-HPC Mini 400-pin net-accurate pin map (PICMG / ADLINK).
Also open: `UNRES-COM-HPC-400PIN`
Source of truth: `artifacts/hw_fw_rc_001/EDMUND_EXTERNAL_BLOCKERS.json` and `DIGITAL_MANUFACTURING_READINESS.md`.

## This SKU

| ID | Item |
|---|---|
| `EXT-COM-HPC-400PIN` / `UNRES-COM-HPC-400PIN` | COM-HPC Mini 400-pin net-accurate map (blocks token) |
| `UNRES-STUDENT-RAM-EXPORT` | OS export 8 GB vs named COM 32 GB class — freeze from module docs, do not invent |
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
