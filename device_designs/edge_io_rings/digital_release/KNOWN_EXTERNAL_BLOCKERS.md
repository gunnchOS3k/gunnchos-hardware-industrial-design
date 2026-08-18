# Known external blockers — Edge I/O Rings
**Digital release status:** `DIGITAL_RELEASE_READY`
Source of truth: `artifacts/hw_fw_rc_001/EDMUND_EXTERNAL_BLOCKERS.json` and `DIGITAL_MANUFACTURING_READINESS.md`.

## This SKU (does not revoke DIGITAL_RELEASE_READY)

| ID | Item |
|---|---|
| `UNRES-BATTERY-CELL-MPN` | Candidate LiPo; purchase-time datasheet |
| Physical boot | Zephyr west digital PASS ≠ flashed nRF52840 |
| UWB Qorvo | Optional DWM3001C BINARY_BLOB portions |

IMU is not absolute pose. Spatial accuracy remains `PHYSICAL_PENDING`.

## Family (all SKUs)

| ID | Why it remains |
|---|---|
| `UNRES-PASTE-REFLOW` | CM DFM paste/reflow values |
| `UNRES-SIGNED-FW-BIN` | Production signed image + ICT limits |
| `UNRES-IMPEDANCE-SI` | `si_simulation_performed: false` |
| FCC / CE / USB-IF | Digital prep only; labs not engaged |
| `PHYSICAL_PENDING` | No assembled EVT unit |

Do not invent values for these.
