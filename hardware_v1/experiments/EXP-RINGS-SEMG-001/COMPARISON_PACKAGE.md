# sEMG wrist band vs IMU/cap ring input

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-RINGS-SEMG-001`
- Branch: `hardware/exp-rings-semg-wrist`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
sEMG adds gesture bandwidth without unsafe skin current / privacy regression

## Baseline (mainline)
IMU + capacitive/touch ring

## Variant
sEMG wrist accessory

## Measurable comparison criteria
- `gesture_f1`
- `skin_current_ua`
- `false_positive_rate`
- `privacy_review_pass`

## Promotion gate
Safety current limits met; youth privacy review pass; not medical claim

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
