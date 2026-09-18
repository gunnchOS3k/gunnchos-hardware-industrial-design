# EXP-DSXL-OLED-HYBRID-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
DS-XL OLED+IPS hybrid vs dual IPS

## Hypothesis
Primary OLED + secondary IPS improves creator UX without dual-OLED cost/thermal

## Baseline (mainline)
IPS eDP + DDI/DP on custom DSXL-MB-v1

## Variant
OLED primary + IPS secondary

## Metrics
- dual_edp_si_margin
- thermal_delta_c
- cost_delta_usd
- color_delta_e

## Promotion gate
SI margin maintained on eDP+DDI/DP; do not mislabel as dual native eDP

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
