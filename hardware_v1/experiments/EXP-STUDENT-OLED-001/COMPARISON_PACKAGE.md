# Student OLED panel vs IPS

**Generated:** 2026-09-18T16:24:23Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-STUDENT-OLED-001`
- Branch: `hardware/exp-student-oled`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
OLED improves contrast/weight without exceeding power/thermal budget

## Baseline (mainline)
IPS eDP panel

## Variant
OLED eDP panel class

## Measurable comparison criteria
- `contrast_ratio`
- `avg_power_w`
- `burnin_risk_score`
- `cost_delta_usd`
- `nit_hdr`

## Promotion gate
Power <= IPS+10% at 200 nits office; burn-in mitigation plan owner-approved

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
