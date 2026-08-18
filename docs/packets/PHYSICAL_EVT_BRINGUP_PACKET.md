# Physical EVT bring-up packet

**Status:** `PHYSICAL_PENDING`

**Owner-only.** This packet is a checklist for a human with assembled hardware, ESD-safe lab power, and matching firmware. This agent does not power boards, flash devices, or invent measured voltages.

## Why blocked

Digital KiCad ERC/DRC, OpenSCAD parse, BOM CSVs, and QEMU/firmware harnesses cannot substitute for an assembled EVT unit. Family state remains `PHYSICAL_PENDING`. Successful digital hygiene is **not** `DIGITAL_FABRICATION_PASS`.

## Prerequisite

| Item | Source | Must be true |
|---|---|---|
| Fabricated/assembled EVT unit | CM / owner fab — **not done from this repo** | Board matches a tagged hardware SHA |
| Hardware revision | `git rev-parse HEAD` in this repo at fab time | Recorded on the traveler |
| Firmware image | `gunnchos-device-os` + `firmware/manifests/` for that SKU | Hash recorded; harness YAML is not a board image |
| ESD / current-limited PSU | Lab | Before any connector mate |
| Modeled rail *references* | `device_designs/<sku>/electrical/power_tree.yaml` | Use as **expected class only**; evidence_class is `PUBLIC_DOCS` / `MODELED` / `PUBLIC_PINOUT+MODELED` |

Do **not** copy YAML `volts` fields into a bring-up log as measured values. Measure, then record.

## Modeled rails (reference only — not measured)

Cited from in-tree YAML. Unresolved NDA rails are marked. Do not invent replacements.

### handheld_hybrid (`evidence_class: PUBLIC_PINOUT+MODELED`)

From `device_designs/handheld_hybrid/electrical/power_tree.yaml` and ICD `device_designs/handheld_hybrid/docs/som_carrier_icd.md`:

| Rail name | YAML volts | Notes in source |
|---|---|---|
| VBUS | 5.0 | USB-C PD |
| VSYS | 3.8 | regulator_mpn BQ25895RTWR |
| SOM_VIN | 5.0 | VCC_SYSIN pins 251–260 PUBLIC_PINOUT; ICD max 5.2 V from brief |
| VDD_3V3 | 3.3 | TPS62864 |
| VDD_DISPLAY_BL | 12.0 | boost **modeled** |

### student_14_5 (`evidence_class: PUBLIC_DOCS`)

From `device_designs/student_14_5/electrical/power_tree.yaml`:

| Rail name | YAML volts | Notes in source |
|---|---|---|
| ADAPTER_19V | 19.0 | |
| COM_VIN | 12.0 | AT 12 V ±5% PUBLIC_DOCS |
| VDD_3V3 | 3.3 | TPS62864 |
| VBAT | 7.6 | BQ25792RQMR |

Pin-accurate COM-HPC fanout remains `UNRES-COM-HPC-400PIN`. Do not probe invented module pins.

### ds_xl_coder (`evidence_class: PUBLIC_DOCS`)

From `device_designs/ds_xl_coder/electrical/power_tree.yaml`:

| Rail name | YAML volts | Notes in source |
|---|---|---|
| ADAPTER_19V | 19.0 | |
| COM_VIN | 12.0 | AT 12 V ±5% PUBLIC_DOCS |
| VDD_3V3 | 3.3 | |
| BL_MAIN | 12.0 | primary panel backlight |
| BL_SECONDARY | 12.0 | secondary panel + hinge flex |

Dual-eDP pin map remains `UNRES-COM-HPC-DUAL-EDP`.

### edge_io_rings (`evidence_class: PUBLIC_DOCS`)

From `device_designs/edge_io_rings/electrical/power_tree.yaml`:

| Rail name | YAML volts | Notes in source |
|---|---|---|
| VBUS_CRADLE | 5.0 | pogo cradle |
| VBAT | 3.7 | LiPo 250 mAh **candidate** |
| VDD | 3.0 | npm1300-CAAA-R |

Zephyr west digital build ≠ physical boot.

### dock (`evidence_class: PUBLIC_DOCS+MODELED`)

From `device_designs/dock/electrical/power_tree.yaml`:

| Rail name | YAML volts | Notes in source |
|---|---|---|
| VBUS_IN | 20.0 | USB-C PD sink/source |
| VDD_3V3 | 3.3 | TPS62864 |
| VDD_USB4 | 0.8 | JHL8440 rails **MODELED — package NDA** (`UNRES-DOCK-0V8`) |

Do not treat 0.8 V as a measured Intel rail.

## Owner action (bring-up sequence)

1. Identify SKU and traveler: board ID / serial, hardware SHA, firmware hash.
2. Visual / mechanical: polarity, shorts, connector seating. Photograph optional.
3. Apply current-limited power appropriate to the SKU **input** named in the power tree (USB-C vs adapter). Stop on overcurrent.
4. For each YAML rail that is **on the carrier and publicly documented**, measure with a meter and write **measured_V**, instrument, and timestamp. Skip NDA-only module internals.
5. Debug UART where documented (handheld UART2 pins 236/238 per ICD). Capture boot log. No log → no boot PASS.
6. Run only tests that have a written procedure (display, input, dock enumerate). Record pass/fail per test point.
7. Stop and quarantine on smoke, thermal runaway, or missing current limit.

Firmware hooks for rings (digital): `device_designs/edge_io_rings/docs/FIRMWARE_HOOKS.md` (SWD Tag-Connect TC2030, DFU, ship mode). Physical use still `PHYSICAL_PENDING`.

## Expected evidence

Create `artifacts/evt/<sku>/<serial>/` when physical work happens:

- `traveler.json` — board ID, SHAs, operator
- `rails.csv` — rail name, modeled_V (citation only), measured_V, pass/fail
- `boot.log` — required for any boot claim
- `failures.md` — explicit skips for `UNRES-*` specs

Photos optional. Logs required.

## Status transition

Recorded rail + boot procedures may support `DEVICE_MEASURED` for **those test points only**. That still is not FCC/CE/USB-IF, not DVT/PVT, not manufacturing release.
