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
