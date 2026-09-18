# HW1D final report A–T

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## A. starting/final #68 SHA
Starting expected: `628eacd8f35a2a509f36592c392b6aba88b6c4f8` (drift at preflight: see `convergence/HW1D_STARTING_STATE.json`).  
Final: `628eacd8f35a2a509f36592c392b6aba88b6c4f8` on `hardware/v1-mainline-ready-for-evt` (DRAFT #68; unmerged).

## B. four-track model
PRODUCT_MAINLINE=`AMD_CUSTOM_X86`; OPEN_ENGINEERING_MAINLINE=`NXP_IMX95_OPEN_CUSTOM`; GREENFIELD_EXPERIMENT=`GXE`; REFERENCE_CONTROL=`COM_HPC_AND_COTS`.

## C. terminology reconciliation
Ambiguous bare “mainline” removed from control-plane docs; track qualifiers required (`CANONICAL_TRACK_MODEL.md`).

## D. experience-first doctrine
`EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE.md` — software must earn additional hardware.

## E. AMD product mainline status
Preserved Platform Core v1 (8840U/8845HS candidates, custom Dock/Rings). `CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false` = external blocker.

## F. NXP open-custom architecture
Full package under `hardware_v1/open_custom_nxp/` with explicit non-equivalence to AMD x86.

## G. NXP public-collateral status
Index + gap register; URLs/metadata/hashes only; design-guide may be account-gated.

## H. GXE integration boundary
`GXE_HARDWARE_INTEGRATION_CONTRACT.md` only; `GXE_IMPLEMENTED_IN_HARDWARE_REPO=false`.

## I. COM-HPC control status
REFERENCE_CONTROL preserved; RP0-A packet ready-to-order optional; not PRODUCT_MAINLINE.

## J. cross-track benchmark model
Per-workload matrix + schema; no overall winner score.

## K. Experience Contract schema
`HARDWARE_EXPERIENCE_CONTRACT_SCHEMA.json` + guide.

## L. decision ledger status
Track / role / evidence_class / promotion / physical / external fields reconciled.

## M. BOM/classification status
PRODUCT_MAINLINE custom BOM isolated; NXP preliminary BOM qty=0 architecture-only; experiments not mixed.

## N. experiment PR status
#69–#79 remain DRAFT; refresh onto final #68 head (see closeout).

## O. validator results
`make hardware-v1-validate` / `make hardware-v1-all` — see closeout log.

## P. software RC1 firewall
`SOFTWARE_RC1_BASELINES_UNTOUCHED=true`.

## Q. merge-readiness result
`HW_ARCHITECTURE_BASELINE_MERGE_READY=true` (architecture definition only).

## R. physical gate truth
All physical EVT/fab/cert gates remain false; `EVT_PENDING/DVT_PENDING/PVT_PENDING=true`.

## S. post-merge plan
`convergence/POST_MERGE_PLAN.md` prepared for `HW1D.1_ACCEPTED_MAIN_REBIND` — not executed.

## T. exactly one owner action
`NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT`

## Printed tokens
```
HW_ARCHITECTURE_BASELINE_MERGE_READY=true
FOUR_TRACK_MODEL_PASS=true
EXPERIENCE_FIRST_CO_DESIGN_DOCTRINE_PASS=true
AMD_PRODUCT_MAINLINE_PRESERVED=true
NXP_OPEN_CUSTOM_TRACK_DEFINED=true
GXE_INTEGRATION_BOUNDARY_DEFINED=true
REFERENCE_CONTROL_TRACK_DEFINED=true
EXPERIMENT_ISOLATION_PASS=true
SOFTWARE_RC1_BASELINES_UNTOUCHED=true
CUSTOM_PLATFORM_VENDOR_ACCESS_READY=false
CPB0_SCHEMATIC_READY=false
CPB0_PCB_READY=false
CPB0_READY_FOR_FAB=false
CUSTOM_MAINLINE_READY_FOR_EVT_BUILD=false
HARDWARE_V1_READY_FOR_EVT_BUILD=false
EVT_PENDING=true
DVT_PENDING=true
PVT_PENDING=true
PHYSICAL_HARDWARE_VALIDATED=false
CERTIFICATION_COMPLETE=false
MANUFACTURING_VALIDATED=false
NEXT_OWNER_ACTION=MERGE_HW_ARCHITECTURE_BASELINE_68_WITH_MERGE_COMMIT
```
