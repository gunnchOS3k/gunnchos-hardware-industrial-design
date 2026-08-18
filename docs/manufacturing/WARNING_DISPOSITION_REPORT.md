# ERC/DRC warning disposition (this-run)

Generated: 2026-08-18T18:58:38Z
Source artifacts: `artifacts/supervisor_ready_eda/kicad/*/erc.json`, `drc.json`, logs, summaries.
Row-level table: `artifacts/supervisor_ready_eda/WARNING_DISPOSITION.csv`.

Allowed classes: `FIXABLE_DIGITALLY` | `ACCEPTED_BY_DESIGN` | `BLOCKED_VENDOR_DOCUMENTATION` | `BLOCKED_NDA_INFORMATION` | `PHYSICAL_VALIDATION_ONLY` | `INVALID_FALSE_POSITIVE`.

Codes are copied from KiCad JSON `type` fields. No guessed codes.
DRC ignore lists were **not** expanded.

## Counts per class per SKU (this-run remaining warnings)

| SKU | ERC w | DRC w | FIXABLE_DIGITALLY | ACCEPTED_BY_DESIGN | BLOCKED_NDA_INFORMATION | BLOCKED_VENDOR_DOCUMENTATION | PHYSICAL_VALIDATION_ONLY | INVALID_FALSE_POSITIVE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| dock | 19 | 39 | 11 | 43 | 4 | 0 | 0 | 0 |
| ds_xl_coder | 45 | 51 | 11 | 67 | 18 | 0 | 0 | 0 |
| edge_io_rings | 27 | 22 | 11 | 38 | 0 | 0 | 0 | 0 |
| handheld_hybrid | 461 | 39 | 4 | 496 | 0 | 0 | 0 | 0 |
| student_14_5 | 40 | 50 | 11 | 65 | 14 | 0 | 0 | 0 |
| **total** | 592 | 201 | 48 | 709 | 36 | 0 | 0 | 0 |

## What was fixed this pass (FIXABLE_DIGITALLY)

Applied from in-tree geometry / public NX5 pinout CSV only. kicad-cli 10.0.5 post-fix DRC: **0 errors** on all five SKUs; `track_dangling` and `silk_over_copper` cleared. Handheld `multiple_net_names` cleared (0 remaining).

- Deleted no-net (`net 0`) dangling segments: 60 (this-run `track_dangling` 10×4 SKUs).
- Moved REV silkscreen off H1: 4 boards (handheld already clear).
- Deleted SoM net-bridging wires using `radxa_nx5_public_pinout_table.csv`: 6 (`HP_DET_L`/`POWER-EN`, `4A1`/`BBAT`, MIPI D0/D1 and D1P/D2P, `BBAT`/`SLEEP-WAKE`).
- `fp-lib-table` URIs made project-relative (`${KIPRJMOD}/../../_shared_kicad/gunnchos_production.pretty`).

**Tried and reverted (would have weakened the 0-error DRC / broken ERC load):**
- Full JEDEC footprint drop from `gunnchos_production.pretty` onto the 24 mm envelope grid → courtyard/clearance/drill errors. Classified `lib_footprint_mismatch` as `ACCEPTED_BY_DESIGN`.
- Prefixing embedded `lib_id` to `gunnchos:` → kicad-cli `Failed to load schematic`. Classified `lib_symbol_issues` as `ACCEPTED_BY_DESIGN`.
- Handheld `endpoint_off_grid` wires were **not** deleted: ERC '0.0254 mm' is the 1 mil grid residual on 2.54 mm wires.

Not done: inventing COM-HPC or JHL ball maps; adding DRC ignore keys; claiming fab/RFQ/cert.

## What remains blocked and why

### BLOCKED_NDA_INFORMATION

Student 14.5 / DS-XL Coder isolated global labels (USB/eDP/SPI/COM_VIN/…) wait for `EXT-COM-HPC-400PIN` (and DS-XL `EXT-DSXL-DUAL-EDP`). Dock USB4/ETH labels wait for `EXT-JHL8440-BALLMAP` / `EXT-JHL9040R-BALLMAP`. Public topology exists; pin-accurate fanout does not.

### ACCEPTED_BY_DESIGN

- Handheld SODIMM pin / 2.54 mm wire off-grid (public NX5 pitch ≠ default 50 mil ERC grid) and isolated PUBLIC_PINOUT net names on stub far-end connectors.
- Rings named SWD/USB/RF/IMU/CAP nets on stub symbols; **IMU is not absolute pose**.
- Family `lib_footprint_mismatch`: envelope stubs vs in-tree JEDEC library; full drop fails DRC.
- Family `lib_symbol_issues` empty library nickname: embedded symbols; prefixing broke schematic load.

### PHYSICAL_VALIDATION_ONLY / INVALID_FALSE_POSITIVE / BLOCKED_VENDOR_DOCUMENTATION

None in this-run ERC/DRC JSON. Vendor AVL (panel MPN, SODIMM socket MPN, paste/reflow) is documented in digital_release `KNOWN_EXTERNAL_BLOCKERS.md` but did not appear as KiCad warning rows.

## Digital release status

| Device | Role | INDEX status | Missing prerequisite |
|---|---|---|---|
| Student 14.5 | sustained desk/work | `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA` | `EXT-COM-HPC-400PIN` |
| Handheld Hybrid | mobile/docked compute | `DIGITAL_RELEASE_READY` | none (AVL items listed, not NDA) |
| DS-XL Coder | local create/deploy | `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA` | `EXT-COM-HPC-400PIN` + `EXT-DSXL-DUAL-EDP` |
| Edge I/O Rings | spatial input (IMU ≠ absolute pose) | `DIGITAL_RELEASE_READY` | none (physical boot still PHYSICAL_PENDING) |

`DIGITAL_FABRICATION_PASS` remains **FALSE**. `PHYSICAL_PENDING` remains **TRUE**.

