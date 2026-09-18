# CPB0-O BOM risk

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Risk | Severity | Mitigation |
|---|---|---|
| SoC OPN availability unknown | HIGH | VERIFY_AT_PURCHASE; keep alt VZ OPNs |
| PMIC OPN not frozen | HIGH | Account-login EVK BOM / UG10210; do not invent |
| LPDDR5 density/rank unknown | HIGH | Cross-check EVK BOM before schematic freeze |
| 10 GbE magnetics long-lead | MED | Keep DNP option |
| WWAN antenna unvalidated | MED | Option DNP; no RF claim |
| No live distributor quotes | — | Intentional; stock/price = VERIFY_AT_PURCHASE |

Update preliminary BOM pointer:
