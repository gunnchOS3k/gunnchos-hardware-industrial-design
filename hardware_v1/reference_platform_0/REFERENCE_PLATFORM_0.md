# Reference Platform 0 (reclassified)

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Role after HW1C

ADLINK COM-HPC Mini mMTL + Mini Base is **`REFERENCE_CONTROL_MODULAR_X86`**, not product mainline.

Uses:

- validate gunnchOS
- validate Windows compatibility
- establish USB4 behavior
- validate NVMe/Wi-Fi/cellular
- compare thermals/performance
- isolate custom motherboard failures
- provide fallback/demo platform

## Gates preserved

- `RP0_A_COTS_PROCUREMENT_PACKET_READY=true`
- `RP0_A_READY_TO_ORDER=true`

Owner intent rename: `OPTIONAL_REFERENCE_CONTROL_PURCHASE` / `OPTIONAL_OWNER_ACTION=ORDER_RP0_A_COTS_CONTROL_KIT`

This is **no longer** the main hardware milestone. Mainline learning board is **CPB0** (custom AMD).

## Stages

- **RP0-A:** COTS Integration Bench (unchanged procurement packet)
- **RP0-B:** historical custom COM-HPC carrier path — still vendor-gated; subordinated to Platform Core / CPB0 custom-first path

Do not delete HW1B public closures.
