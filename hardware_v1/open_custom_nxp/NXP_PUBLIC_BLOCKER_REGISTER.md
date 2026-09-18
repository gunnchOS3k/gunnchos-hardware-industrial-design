# NXP public-collateral blocker register

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| ID | Blocker | Classification | Notes |
|---|---|---|---|
| BLK-PINMAP | Ball-accurate pin/mux CSV incomplete | EDA_PENDING / TOOLING_REQUIRED | Needs IMX95IEC package assignments + IMX95RM IOMUX extract |
| BLK-UG10210 | Hardware design guide not ingested | ACCOUNT_LOGIN_REQUIRED | Ordinary login OK; content not fetched this campaign |
| BLK-ERRATA | IMX95_P21N not ingested | ACCOUNT_LOGIN_REQUIRED | |
| BLK-IBIS | IBIS/BSDL not ingested | ACCOUNT_LOGIN_REQUIRED | Blocks SI/DFT pass |
| BLK-PMIC-OPN | PMIC exact OPN unknown | EXTERNAL_VENDOR_PENDING / ACCOUNT_LOGIN_REQUIRED | EVK BOM |
| BLK-DDR-DETAIL | Skew/impedance/device OPN | ACCOUNT_LOGIN_REQUIRED / EDA_PENDING | |
| BLK-SCH-SYMBOLS | No authoritative i.MX95 KiCad symbol/footprint yet | EDA_PENDING | Do not copy restricted libs |
| BLK-ERC | ERC pass | EDA_PENDING | |
| BLK-PCB | Layout not started | EDA_PENDING | |
| BLK-DRC | DRC pass | EDA_PENDING | |
| BLK-SHA | Local SHA-256 archive of public PDFs | TOOLING_REQUIRED | Owner fetch |
| BLK-PHYS | EVT bring-up | PHYSICAL_PENDING | |
| BLK-CLOSED-INDEX | Category inventory complete | CLOSED_PUBLIC | Index built from product page + datasheet + MCUX + GS |

**NDA:** none identified as required for essential CPB0-O path. If an essential item unexpectedly requires NDA → stop that subpath; do not invent.
