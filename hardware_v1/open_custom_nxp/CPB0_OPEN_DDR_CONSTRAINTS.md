# CPB0-O DDR constraints register

**Generated:** 2026-09-18T22:17:56Z  
**Campaign:** `NXP2_CPB0_COLLATERAL_UNLOCK_EDA_CONTINUATION` (continues NXP0/NXP1; owner UG10210 still MISSING)  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Constraint | Value | Status | Source |
|---|---|---|---|
| Interface width | x32 | ACCEPTED_PUBLIC | IMX95IEC |
| Max rate (19×19 LPDDR5) | up to 6400 MT/s | ACCEPTED_PUBLIC | IMX95IEC |
| VDD2H_DDR (LPDDR5) | 1.05 V class | ACCEPTED_PUBLIC | IMX95IEC |
| VDDQ_DDR (LPDDR5) | 0.5 V class | ACCEPTED_PUBLIC | IMX95IEC |
| Package escape | 19×19 / 0.7 mm | ACCEPTED_PUBLIC | IMX95IEC |
| Trace length / skew budgets | TBD | **BLOCKED** ACCOUNT_LOGIN UG10210 / EVK | UG10210, EVK layout |
| Impedance targets | TBD | **BLOCKED** | UG10210 |
| Byte-lane mapping | TBD | **BLOCKED** | EVK + RM |
| Vref / ODT policy | training-managed | PENDING | BSP + UG10210 |
| Stackup assumptions | see PCB docs | DRAFT | CPB0_OPEN_STACKUP_REQUIREMENTS.md |

Until blocked rows close: do not set memory topology understood token true.
