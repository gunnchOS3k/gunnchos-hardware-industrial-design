# RINGS PRD

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Rings PRD (mainline)
- Nordic nRF54L15 class MCU
- IMU + capacitive/touch
- Magnetic cradle charge for EVT
- Zephyr firmware + DFU
- Authenticated spatial input role preserved (IMU ≠ absolute pose)

## Experiments
- Inductive charge
- sEMG wrist

## Historical
Prior nRF52840 digital package retained under `device_designs/edge_io_rings/` — not mixed into v1 mainline BOM.

## HW1C classification

**Generated:** 2026-09-18T16:48:39Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

- Ring remains fully custom mainline (nRF54L15, IMU, sense, power, antenna, Zephyr, MCUboot, enclosure)
- nRF54L15 DK = `REFERENCE_CONTROL_RING` (not product mainline)
- Keep inductive / sEMG experiments


## Stream E

See `STREAM_E_RINGS_EXHAUSTION.md` and `kicad_nrf54l15/` (2026-09-18T18:37:46Z).
