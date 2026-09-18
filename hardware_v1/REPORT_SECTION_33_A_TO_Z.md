# Section 33 report A–Z

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## A. Campaign
`HARDWARE_1_0_MASTER_CAMPAIGN` executed digitally under `hardware_v1/`.

## B. Repo / branch
`gunnchOS3k/gunnchos-hardware-industrial-design` · `hardware/v1-mainline-ready-for-evt`

## C. Doctrine
One mainline per decision; experiments isolated; no physical/cert/fab false claims; RC1 untouched.

## D. Decision ledger
`hardware_v1/decisions/DECISION_LEDGER.md`

## E. Compute mainline
COM-HPC Mini Meteor Lake-class for Student/DS-XL/Handheld EVT mule.

## F. Displays
IPS mainline; OLED experiments.

## G. Dock
USB4 40 + PD EPR mainline; USB4 80 experiment.

## H. Rings
nRF54L15 + IMU/cap + magnetic cradle; inductive + sEMG experiments.

## I. Firmware
Vendor UEFI + Zephyr EC; coreboot + RAUC experiments.

## J. Battery / quality
Qualified Li-ion; IPC Class 2 + selective tighter controls.

## K. BOM/AVL
`hardware_v1/bom/` — no experimental mix.

## L. Reference Platform 0
Two-stage: RP0-A COTS packet ready; `REFERENCE_PLATFORM_0_READY_FOR_FAB=false` (= RP0-B).

## M. PRDs / ICDs
`hardware_v1/prd/`, `hardware_v1/icd/`

## N. DFMEA / matrices
`hardware_v1/quality/DFMEA.md`, `hardware_v1/matrices/`

## O. Compliance / human factors
Digital prep only; `CERTIFICATION_COMPLETE=false`.

## P. Experiments
Eight EXP-*-001 packages under `hardware_v1/experiments/`.

## Q. RC1 impact register
`hardware_v1/SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.md`

## R. Owner packet
`hardware_v1/OWNER_ACTION_PACKET.md`

## S. Gates
See `hardware_v1/GATES.json` — EVT/DVT/PVT still pending; physical validated false.

## T. Make validators
`make hardware-v1-validate` and related targets.

## U. Reconciled evidence
Existing DIGITAL_* / device_designs / manufacturing / dvt / pvt retained.

## V. DRAFT PRs
Mainline DRAFT to `main`; experimental DRAFTs to mainline branch when packages present.

## W. Non-actions
No merge, no RFQ send, no purchase, no secrets.

## X. NEXT_OWNER_ACTION
`ORDER_RP0_A_COTS_BRINGUP_KIT`

## Y. Honest blockers (RP0-B)
EXT-COM-HPC-400PIN, EXT-JHL8440-BALLMAP, EXT-JHL9040R-BALLMAP (vendor-gated for custom fab only).

## Z. Evidence root
`hardware_v1/` including `rp0b/`, `reference_platform_0/RP0_*`, `vendor_evidence/nordic/`
