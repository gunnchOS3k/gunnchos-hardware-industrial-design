# Memory topology decision (UNFROZEN)

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


Do **not** freeze until AMD topology rules are available.

## Evaluation axes

routing difficulty, SI margin, capacity, repairability, power, board area, cost, availability, production assembly, product thickness.

## Intent by board (not frozen)

| Board | Preference if vendor allows |
|---|---|
| CPB0 | easiest to instrument/debug (prefer SO-DIMM if supported) |
| Student | serviceability favored if physically practical |
| DS-XL | capacity favored |
| Handheld | compactness/power favored |

Evaluate SO-DIMM vs soldered DDR5; LPDDR only if selected SoC/platform supports it.

`CUSTOM_DDR_TOPOLOGY_UNDERSTOOD=false`
