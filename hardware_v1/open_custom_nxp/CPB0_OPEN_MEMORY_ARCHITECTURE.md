# CPB0-O memory architecture

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Decision (high level)

| Item | Choice | Evidence |
|---|---|---|
| Technology | **LPDDR5** (primary) | Align to IMX95LPD5EVK-19; IMX95IEC 19×19 supports LPDDR5 up to 6400 MT/s |
| Bus | **x32**, one LPDDR channel with inline ECC | IMX95IEC |
| Device count / density | **PENDING_EVK_BOM_CROSSCHECK** | Do not invent density/rank |
| LPDDR4X fallback | Supported by silicon; not preferred for CPB0-O | IMX95IEC |

## Token

`NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false` until UG10210 / EVK layout constraints (length, skew, impedance, byte-lane mapping) are ingested and cited row-by-row in `CPB0_OPEN_DDR_CONSTRAINTS.md`.

## Boot / training

- Rely on NXP BSP DDR training path as control reference.
- No claim of stable training without hardware.
