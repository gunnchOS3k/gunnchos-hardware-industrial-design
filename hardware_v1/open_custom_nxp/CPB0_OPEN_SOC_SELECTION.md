# CPB0-O SoC / package selection (NXP-1 freeze)

**Generated:** 2026-09-18T19:17:34Z  
**Campaign:** `NXP1_CPB0_OPEN_DIGITAL_EDA_CLOSURE`  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## Selected OPN (exact)

| Field | Value |
|---|---|
| **Board design freeze OPN** | **MIMX9596CVZXNAC** |
| EVK / MCUX PartNumber alias | **MIMX9596AVZXN** (documented on IMX95LPD5EVK-19 MCUX docs; retained for continuity) |
| Device family | MIMX9596 (i.MX 95 full-featured, 6x A55) |
| Temp / qual | **C** Industrial (−40°C Ta to 105°C Tj) per IMX95IEC nomenclature |
| Package | **VZ** — 19×19 mm FCBGA, 0.7 mm pitch, **no lid** |
| Ball count (populated + DEPOP entries in package map) | **758** contacts in `i.mx95_19mm_ballmap.xlsx` SPN sheet |
| Pitch | 0.7 mm |
| Silicon revision (Table 2) | **B0** |
| A-core freq | 1.8 GHz class |
| Special config | SDP on USB1 |
| Lifecycle | Mass-production class per Table 2 listing; confirm on nxp.com before purchase |
| Public sources | IMX95IEC Rev 8 Table 2; MCUX IMX95LPD5EVK-19 PartNumber MIMX9596AVZXN |

## Why CVZXNAC (not root AVZXN alone)

1. IMX95IEC Table 2 publishes complete industrial orderable codes (`MIMX9596CVZXNAC` / `…NBC`).
2. MCUX still lists EVK PartNumber `MIMX9596AVZXN` — treated as EVK alias / root family identifier, not a conflicting second design.
3. `NXP_EXACT_SOC_OPN_FROZEN=true` uses the Table 2 complete code for CPB0-O board planning.

## Honesty

- Feature fuse map must be re-checked against IMX95IEC Table 2 before fab.
- No stock/price invented (`VERIFY_AT_PURCHASE`).
- Gate `NXP_EXACT_SOC_OPN_FROZEN=true`.
