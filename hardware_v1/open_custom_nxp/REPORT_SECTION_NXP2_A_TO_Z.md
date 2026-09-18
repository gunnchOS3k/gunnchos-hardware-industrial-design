# NXP-2 Final Report A–Z

**Generated:** 2026-09-18T22:17:56Z  
**Campaign:** `NXP2_CPB0_COLLATERAL_UNLOCK_EDA_CONTINUATION`  
**Claim boundary:** public-collateral / owner-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change

## A. accepted main

- SHA: `56125d1738a437f413ee4418c51c2f3a82bcbac8`
- Merge of PR #83: NXP open-custom CPB0-O public-collateral EDA foundation
- Historical NXP-1 branch/head **not** used as baseline
- Preflight: fetch + ff-only pull; `BASELINE_OK`

## B. branch / final SHA

- Branch: `hardware/nxp-open-cpb0-collateral-unlock`
- Final tip SHA: _(filled at commit/PR time)_

## C. owner collateral index

- Local intake: `/Users/gunnchos/Downloads/owner_collateral/nxp_imx95` (outside git)
- Committed metadata:
  - `hardware/nxp_open/owner_collateral/NXP_OWNER_COLLATERAL_INDEX.{json,md}`
  - `hardware_v1/open_custom_nxp/owner_collateral/NXP_OWNER_COLLATERAL_INDEX.{json,md}`
- **Authoritative UG10210 / EVK BOM: MISSING** (0 files)

## D. DDR evidence

- `CPB0_OPEN_DDR_CONSTRAINT_EVIDENCE.json`
- `ug10210_present=false`; extracted authoritative length/impedance rows = 0
- No invented values

## E. DDR constraints

- `CPB0_OPEN_DDR_CONSTRAINTS.csv` + updated `.md`
- Public class rows retained; UG10210-dependent rows **UNRESOLVED**

## F. memory topology

- `CPB0_OPEN_DDR_TOPOLOGY.md`
- `NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false`

## G. EVK BOM reconciliation

- `CPB0_OPEN_BOM_RECONCILIATION.md`
- EVK BOM missing; no wholesale copy

## H. LPDDR MPN

- **Not frozen** (`CPB0_OPEN_MEMORY_COMPONENT_EVIDENCE.json` status UNRESOLVED)

## I. PMIC OPNs / OTP

- Architecture still PF09+PF5301+PF5302
- PF09 candidate `MPF0900AVNA1ES` — OTP **not** frozen
- PF5301/PF5302 OPNs **UNRESOLVED**

## J. schematic completion

- Multi-unit wiring still incomplete on accepted-main sheets
- `CPB0_OPEN_SCHEMATIC_STARTED=true`, `CPB0_OPEN_SCHEMATIC_READY=false`

## K. ERC

- `CPB0_OPEN_ERC_REPORT.{json,md}` (kicad-cli 10.0.5)
- `CPB0_OPEN_SCHEMATIC_ERC_PASS=false`

## L. footprints

- `CPB0_OPEN_FOOTPRINT_VALIDATION.{json,md}`
- Mechanical drawing missing → `CPB0_OPEN_FOOTPRINT_LIBRARY_VALIDATED=false`

## M. placement

- `CPB0_OPEN_PLACEMENT_REPORT.{json,md}`
- `CPB0_OPEN_PLACEMENT_PASS=false`

## N. routing

- `CPB0_OPEN_NETCLASS_RULES.csv`, `CPB0_OPEN_LENGTH_TUNING_REPORT.csv`, `CPB0_OPEN_HIGHSPEED_ROUTING_AUDIT.md`
- High-speed routing **not** complete

## O. SI

- `CPB0_OPEN_SI_AUDIT.json` — `SI_PASS=false`

## P. PI

- `CPB0_OPEN_PI_AUDIT.json` — `PI_PASS=false` (no invented currents)

## Q. DRC

- `CPB0_OPEN_DRC_REPORT.{json,md}`
- `CPB0_OPEN_PCB_DRC_PASS=false`

## R. BOM

- Critical MPNs still PENDING/UNRESOLVED for DRAM + PF53x
- `CPB0_OPEN_BOM_AVL_DIGITAL_PASS=false`

## S. AVL

- Accepted-main AVL retained; no false freezes

## T. DFM / DFA / DFT

- Prior digital prep retained: `CPB0_OPEN_DFM_DFA_DFT_PASS=true` (engineering docs only)

## U. bring-up

- Prior bring-up engineering retained: `CPB0_OPEN_BRINGUP_ENGINEERING_READY=true`

## V. fab outputs

- **Not generated** (prerequisites not green)

## W. release manifest

- `release/cpb0_open/A0/MANIFEST.json` with `fab_outputs_present=false`

## X. fab audit

- `make cpb0-open-fab-audit` expected FAIL (honest)
- `CPB0_OPEN_DIGITAL_FAB_AUDIT_PASS=false`

## Y. final gate tokens

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
CPB0_OPEN_PCB_STARTED=true
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

## Z. next action

Remaining blockers:
1. Owner provide **UG10210** (hash into index; keep PDF out of git unless redistribution explicit)
2. Owner provide **EVK BOM** (LPDDR5 MPN, PF5301/PF5302 OPNs, PF09 OTP/package)
3. Then resume schematic → ERC → footprints → place/route → SI/PI → DRC → BOM → fab outputs

**`NEXT_OWNER_ACTION=PROVIDE_MISSING_AUTHORITATIVE_NXP_COLLATERAL`**  
**`NEXT_HARDWARE_ACTION=CONTINUE_CPB0_OPEN_EDA`**

Do not RFQ / purchase / fab / merge automatically.
