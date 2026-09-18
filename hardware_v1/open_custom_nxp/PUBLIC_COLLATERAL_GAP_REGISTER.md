# Public collateral gap register

**Generated:** 2026-09-18T18:50:15Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Gap ID | Description | Classification | Blocks |
|---|---|---|---|
| GAP-UG10210 | Hardware Design Guide content not ingested (account login) | ACCOUNT_LOGIN_REQUIRED | detailed DDR skew/impedance; fab-ready |
| GAP-ERRATA | IMX95_P21N errata not ingested | ACCOUNT_LOGIN_REQUIRED | bring-up risk closure |
| GAP-BSDL-IBIS | 19x19 BSDL/IBIS not ingested | ACCOUNT_LOGIN_REQUIRED | SI/DFT pass claims |
| GAP-BALLMAP | Package contact assignments not extracted into pinmux CSV | TOOLING_REQUIRED / EDA_PENDING | NXP_PUBLIC_PINMAP_UNDERSTOOD |
| GAP-EVK-FILES | EVK schematic/layout binaries not hashed locally | ACCOUNT_LOGIN_REQUIRED | reference cross-check |
| GAP-PMIC-OPN | Exact NXP-recommended PMIC OPN not frozen from public EVK BOM | EDA_PENDING | BOM freeze |
| GAP-LOCAL-SHA | Datasheet/RM SHA-256 pending owner local fetch | TOOLING_REQUIRED | license-safe archive |

No gap is classified as NDA-required at this time.
