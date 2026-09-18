# EXP-RAUC-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
RAUC A/B vs vendor capsule/EC update

## Hypothesis
RAUC improves update safety/ops for custom platforms vs vendor capsule-only flows

## Baseline (mainline)
Vendor capsule + custom EC update orchestration

## Variant
RAUC A/B

## Metrics
- update_success_rate
- rollback_time_s
- bandwidth
- field_ops_complexity

## Promotion gate
No P0 Device OS RC1 breaks; measured field-ops improvement

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
