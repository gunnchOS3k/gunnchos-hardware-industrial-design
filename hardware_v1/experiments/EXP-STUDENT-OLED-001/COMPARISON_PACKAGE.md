# EXP-STUDENT-OLED-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
Student OLED panel vs IPS

## Hypothesis
OLED improves contrast/weight without exceeding power/thermal budget

## Baseline (mainline)
IPS eDP panel on custom Student-MB-v1

## Variant
OLED eDP panel class

## Metrics
- contrast_ratio
- avg_power_w
- burnin_risk_score
- cost_delta_usd
- nit_hdr

## Promotion gate
Power <= IPS+10% at 200 nits office; burn-in mitigation plan owner-approved

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
