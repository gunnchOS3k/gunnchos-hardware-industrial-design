# Public collateral gap register

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


| Gap ID | Description | Blocks | Severity | Owner path |
|---|---|---|---|---|
| GAP-HW-DESIGN-GUIDE | Hardware Design Guide appears account-gated on product page | net-accurate power/DDR rules for fab | HIGH | Owner NXP account login (Cursor does not accept NDA) |
| GAP-RM-HASH | IMX95RM not hashed in-repo | reproducible design freeze | MED | Owner fetch + hash commit |
| GAP-DS-HASH | Datasheet PDFs not hashed | AVL / OPN freeze | MED | Owner fetch + hash |
| GAP-PACKAGE-SELECT | 15×15 vs 19×19 package not frozen | PCB outline / fanout | HIGH | Owner decision after public BSDL/IBIS review |
| GAP-EVK-≠-CUSTOM | EVK lessons ≠ custom open-custom board pass | false-green risk | HIGH | Explicit methodology in EVT_PLAN |

No gap may be closed by inventing vendor content.
