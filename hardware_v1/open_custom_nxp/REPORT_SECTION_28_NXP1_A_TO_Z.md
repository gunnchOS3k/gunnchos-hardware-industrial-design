# NXP-1 Final Report A–Z

**Generated:** 2026-09-18T19:19:55Z  
**Campaign:** `NXP1_CPB0_OPEN_DIGITAL_EDA_CLOSURE`  
**Claim boundary:** public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## A. Starting working tree / accepted-main

- Dedicated worktree `hardware/nxp-open-cpb0-eda` from `origin/main` @ `4a8aefb5fd6203842267f5adbd72b8ed324e1fac` (PR #80 merge)
- Original dirty tree left intact (see `NXP1_WORKTREE_MIGRATION_PROOF.*`)
- Experiments #69–#79 remain DRAFT/unmerged (not touched)
- Software RC1 untouched

## B. Safe NXP-0 migration

- 72 NXP-0 paths transferred with **zero loss**
- Proof: `NXP1_WORKTREE_MIGRATION_PROOF.md` / `.json`

## C. NXP-0 foundation commit

- Commit: recorded in git log as `feat(nxp): establish i.MX95 open-custom CPB0 foundation`
- Validators green before/after foundation commit

## D. DRAFT PR

- Title: `NXP open-custom: CPB0-O public-collateral EDA foundation`
- Draft only — **not merged**

## E. Collateral inventory

- `PUBLIC_COLLATERAL_INDEX` upgraded to v3 with retrieved/hash/used_for_design
- IMX95IEC Rev 8 retrieved via Wayback; ballmap/pinlist attachments extracted to CSV facts (xlsx not committed)
- PF09 product page + EVK QSG used for PMIC architecture
- UG10210 / full EVK design ZIP still blockers

## F. Exact SoC OPN

- **Frozen:** `MIMX9596CVZXNAC` (IMX95IEC Table 2 industrial 19×19 no-lid, B0, SDP USB1)
- EVK alias retained: `MIMX9596AVZXN`
- `NXP_EXACT_SOC_OPN_FROZEN=true`

## G. Package / ballmap

- `CPB0_OPEN_SOC_BALLMAP.csv` — **758** balls, primary signals from `i.mx95_19mm_ballmap.xlsx`
- Automated uniqueness check via symbol generator
- `NXP_PUBLIC_PINMAP_UNDERSTOOD=true`

## H. KiCad symbol generation

- `scripts/generate_imx95_kicad_symbol.py`
- `eda/cpb0_open/lib/gunnchos_imx95.kicad_sym` (758 pins)
- `CPB0_OPEN_SOC_SYMBOL_VALIDATED=true`

## I. PMIC selection

- Architecture: **PF09 + PF5301 + PF5302** (EVK QSG)
- Preferred PF09 candidate: `MPF0900AVNA1ES` (OTP still verify-from-EVK-BOM)
- `NXP_OPEN_PMIC_ARCHITECTURE_FROZEN=true`

## J. Power tree / sequence

- `CPB0_OPEN_POWER_TREE.csv`, `CPB0_OPEN_POWER_SEQUENCE.csv`
- Currents not invented
- `NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD=true`

## K. DRAM selection

- LPDDR5 x32; EVK QSG capacity class 16GB
- Exact MPN **not** frozen
- `NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false`

## L. DDR constraints

- Netclass/length CSVs present with **UNRESOLVED** rows pending UG10210
- No invented skew numbers

## M. Peripheral architecture

- `CPB0_OPEN_PERIPHERAL_ARCHITECTURE.md` schematic-level candidates

## N. Schematic completion

- Sheets updated with design notes + SoC/PMIC/LPDDR status
- Full multi-unit wiring not complete
- `CPB0_OPEN_SCHEMATIC_STARTED=true`, `CPB0_OPEN_SCHEMATIC_READY=false`

## O. ERC

- `ERC_REPORT.md` / `ERC_WAIVERS.json`
- `CPB0_OPEN_SCHEMATIC_ERC_PASS=false`

## P. Footprint library

- Generated FCBGA footprint from ballmap coordinates
- Mechanical drawing cross-check pending
- `CPB0_OPEN_FOOTPRINT_LIBRARY_VALIDATED=false`

## Q. Stackup

- 14-layer design stackup `CPB0_OPEN_STACKUP_V1.md` / `.csv`
- `CPB0_OPEN_STACKUP_DEFINED=true` (not fabricator-approved)

## R. Placement

- Outline 170×120 mm + zone comments in PCB
- Review doc present; signoff false
- `CPB0_OPEN_PLACEMENT_PASS=false`

## S. Routing

- High-speed / DDR routing **not** claimed complete
- Explicit block on unresolved DDR rules

## T. SI

- `si/` + `CPB0_OPEN_SI_SIGNOFF_MATRIX.md` — **no SI PASS**

## U. PI

- `pi/` + analytical PDN notes — **no PI PASS / no current claims**

## V. DRC

- `DRC_REPORT.md` — `CPB0_OPEN_PCB_DRC_PASS=false`
- `CPB0_OPEN_PCB_STARTED=true`, `CPB0_OPEN_PCB_READY=false`

## W. BOM / AVL

- Updated with CVZXNAC + PF09 candidate; PF53/DRAM still pending
- `CPB0_OPEN_BOM_AVL_DIGITAL_PASS=false`

## X. DFM / DFT / bring-up

- `manufacturing/CPB0_OPEN_DF{M,A,T}.md`
- `bringup/cpb0_open/` scripts/checklists
- `CPB0_OPEN_DFM_DFA_DFT_PASS=true`
- `CPB0_OPEN_BRINGUP_ENGINEERING_READY=true`

## Y. Manufacturing outputs / fab audit

- Release `A0` manifest with `fab_outputs_present=false`
- `scripts/validate_cpb0_open_fab_release.py` fail-closed
- `CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS=false`
- `CPB0_OPEN_READY_FOR_FAB=false`

## Z. Exact remaining blockers + next action

1. Owner ordinary-account fetch of **UG10210** (+ hash) for DDR length/impedance
2. Owner fetch **EVK BOM** for LPDDR5 MPN + PF5301/PF5302 OPNs + PF09 OTP package
3. Complete multi-unit schematic wiring → ERC pass
4. Validate footprints vs mechanical drawings
5. Place/route under real constraints → DRC pass
6. Only then reconsider fab outputs / READY_FOR_FAB

**NEXT_HARDWARE_ACTION=`CONTINUE_CPB0_OPEN_EDA`**  
**NEXT_OWNER_ACTION=`LOGIN_FETCH_UG10210_AND_EVK_BOM_HASH_PDFS`**  
(Do not quote/fab automatically. Preferred later success path after owner review: `REVIEW_CPB0_OPEN_FAB_PACKAGE` → `AUTHORIZE_CPB0_OPEN_FAB_QUOTE`.)

---

## Printed token block

```
NXP_EXACT_SOC_OPN_FROZEN=true
NXP_PUBLIC_PINMAP_UNDERSTOOD=true
CPB0_OPEN_SOC_SYMBOL_VALIDATED=true
NXP_OPEN_PMIC_ARCHITECTURE_FROZEN=true
NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD=true
NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false
CPB0_OPEN_SCHEMATIC_STARTED=true
CPB0_OPEN_SCHEMATIC_ERC_PASS=false
CPB0_OPEN_SCHEMATIC_READY=false
CPB0_OPEN_FOOTPRINT_LIBRARY_VALIDATED=false
CPB0_OPEN_STACKUP_DEFINED=true
CPB0_OPEN_PLACEMENT_PASS=false
CPB0_OPEN_PCB_DRC_PASS=false
CPB0_OPEN_PCB_READY=false
CPB0_OPEN_BOM_AVL_DIGITAL_PASS=false
CPB0_OPEN_DFM_DFA_DFT_PASS=true
CPB0_OPEN_BRINGUP_ENGINEERING_READY=true
CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS=false
NXP_OPEN_NO_NDA_BOUNDARY_PASS=true
CPB0_OPEN_READY_FOR_FAB=false
EVT_PENDING=true
DVT_PENDING=true
PVT_PENDING=true
PHYSICAL_HARDWARE_VALIDATED=false
```
