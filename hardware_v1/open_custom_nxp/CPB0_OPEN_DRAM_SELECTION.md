# CPB0-O DRAM device / topology freeze attempt

**Generated:** 2026-09-18T19:17:34Z  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## What is public

| Item | Value | Source | Confidence |
|---|---|---|---|
| Technology | LPDDR5 | IMX95IEC; EVK QSG | HIGH |
| Width | x32 | IMX95IEC 19×19 | HIGH |
| EVK capacity class | 16GB on IMX95LPD5EVK-19 | EVK QSG | HIGH (EVK), not a CPB0 MPN freeze |
| SoC balls | DRAM_* package assignments | IMX95IEC ballmap | HIGH |
| VDD2H / VDDQ | 1.05 V / 0.5 V class (LPDDR5) | IMX95IEC | HIGH |

## What is NOT frozen (honest)

- Exact DRAM vendor MPN / package
- Byte-lane swap map beyond package names
- Length/skew tables (need **UG10210** / EVK layout)
- ODT/Vref implementation details beyond datasheet class

`NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false` until UG10210 or EVK layout constraints are retrieved.
