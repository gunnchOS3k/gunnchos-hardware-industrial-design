# AMD platform block diagram (public)

**Generated:** 2026-09-18T18:37:46Z
**Campaign:** `STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION`
**Claim boundary:** digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps.


```
[USB-C PD]--[EC]--[SoC AMD_CUSTOM]
              |        |-- LPDDR5x (VENDOR_GATED)
              |        |-- NVMe
              |        |-- Wi-Fi/BT module
              |        |-- eDP / USB4 path (dock)
              +-- battery / chargers
```
All SoC-adjacent nets marked `VENDOR_GATED` until AMD custom collateral lands.
