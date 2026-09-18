# DOCK PRD

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Dock Gen-1 PRD (mainline)
- USB4 40 Gbps host/device path (JHL8440 + JHL9040R)
- USB-C PD EPR-class dual-port controller
- 2.5GbE, USB hub, ESD on exposed ports
- Rings magnetic cradle charge rails
- USB4 80 = EXPERIMENTAL_COMPARE only (EXP-DOCK-USB4-80)

## External blockers
`EXT-JHL8440-BALLMAP`, `EXT-JHL9040R-BALLMAP`

## HW1C classification

**Generated:** 2026-09-18T16:48:39Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.

- Production-intent mainline: `CUSTOM_GUNNCHOS_DOCK_GEN1`
- COTS TB4/USB4 dock: `REFERENCE_CONTROL_DOCK`
- JHL8440/JHL9040R ball maps remain external blockers for pin-accurate custom dock
- Do not demote custom Dock because COTS control is easier
