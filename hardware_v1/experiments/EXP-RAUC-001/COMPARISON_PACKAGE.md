# RAUC A/B update vs vendor capsule/EC update

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-RAUC-001`
- Branch: `hardware/exp-rauc-update`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
RAUC improves field update reliability for rings/EC and optional host slotting

## Baseline (mainline)
Vendor UEFI capsule + Zephyr DFU

## Variant
RAUC A/B (rings/EC primary; host optional)

## Measurable comparison criteria
- `update_success_rate`
- `rollback_success_rate`
- `brick_rate`
- `rc1_interface_breaks`

## Promotion gate
Rollback verified on EVT; no secret material in repo

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
