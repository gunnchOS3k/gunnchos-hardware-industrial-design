# EXP-RINGS-SEMG-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
sEMG wrist band vs IMU/cap ring input

## Hypothesis
sEMG adds gesture bandwidth without unsafe skin current / privacy regression

## Baseline (mainline)
IMU + capacitive/touch custom ring

## Variant
sEMG wrist accessory

## Metrics
- gesture_f1
- skin_current_ua
- false_positive_rate
- privacy_review_pass

## Promotion gate
Safety current limits met; youth privacy review pass; not medical claim

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
