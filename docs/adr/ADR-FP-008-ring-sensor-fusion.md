# ADR-FP-008 — Ring spatial-input sensor fusion (MCU alone insufficient)

- Status: **ACCEPTED (engineering baseline)**
- Date: 2026-08-08T00:50:00Z
- Canonical: field-kit `program/decisions/full_product/ADR-FP-008-ring-sensor-fusion.md`

## Verdict
**nRF52840 alone is insufficient** for the spatial-input promise.

Keep nRF52840 as primary BLE/auth/DFU MCU. Add footprints: BMI270 (already), IQS7222A capacitive (REQUIRED), DWM3001C/DW3000 UWB (DNP→UWB_ON_COMPANION), BMM350 optional, BHI360 optional sensor-hub.

Fusion policy: ≥2 modalities before action dispatch.

## KiCad
`kicad-cli` ABSENT → `EDMUND_ACTION_REQUIRED`. No fab.

## Family-depth follow-up (2026-08-08T01:15:00Z)
Native EDA sources updated to include IQS7222A / DWM3001C / BHI360 / BMM350 / SE050 symbols:
- `gate1_digital_fabrication/edge_io_ring/schematic/kicad/edge_io_ring_evt0.kicad_sch`
- `device_designs/edge_io_rings/kicad/`
`kicad-cli` still ABSENT → `EDMUND_ACTION_REQUIRED`. No fab.
