# Owner action packet

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## What Cursor completed (digital)
- Custom-first architecture doctrine + Platform Core v1
- Device SoC selection matrix (8840U / 8845HS candidates)
- CPB0 learning board digital package (not fab-ready)
- AMD custom platform access packet + owner steps
- Firmware ownership boundary; memory topology UNFROZEN
- COM-HPC reclassified REFERENCE_CONTROL; RP0-A packet preserved
- BOM class split MAINLINE_CUSTOM / REFERENCE_CONTROL / EXPERIMENTAL
- Knowledge map, learning gates, complexity register
- Experiment hierarchy + EXP-COM-HPC-MODULAR / EXP-DSXL-X100 / EXP-P100-AI packages
- Gate model: CUSTOM_MAINLINE_READY_FOR_EVT_BUILD (aliases HARDWARE_V1_READY_FOR_EVT_BUILD)
- HW1B public closures preserved

## What Cursor did NOT do
- Send RFQs / purchase / contact suppliers / accept NDAs
- Invent AMD pin/power/DDR restricted collateral
- Claim physical validation, certification, or fab release
- Merge any PR
- Modify software RC1 baselines
- Fabricate Gerbers/ODB++/quotes

## Preferred next action
`NEXT_OWNER_ACTION=ACQUIRE_AMD_CUSTOM_PLATFORM_COLLATERAL`

## Optional parallel action
`OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

## Honest gate highlights
- `CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false`
- `HARDWARE_V1_READY_FOR_EVT_BUILD=false`
- `CPB0_READY_FOR_FAB=false`
- `CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false`
- Learning gates all `false` where collateral missing
- `RP0_A_COTS_PROCUREMENT_PACKET_READY=true` / `RP0_A_READY_TO_ORDER=true` (reference control only)
