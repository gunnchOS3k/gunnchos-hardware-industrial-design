# DS-XL OLED+IPS hybrid vs dual IPS

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Identity
- Experiment ID: `EXP-DSXL-OLED-HYBRID-001`
- Branch: `hardware/exp-dsxl-oled-hybrid`
- State: `EXPERIMENTAL_COMPARE`
- `not_in_main_bom`: `True`

## Hypothesis
Primary OLED + secondary IPS improves creator UX without dual-OLED cost/thermal

## Baseline (mainline)
Dual IPS eDP

## Variant
OLED primary + IPS secondary

## Measurable comparison criteria
- `dual_edp_si_margin`
- `thermal_delta_c`
- `cost_delta_usd`
- `color_delta_e`

## Promotion gate
Dual-eDP SI margin maintained; EXT-DSXL-DUAL-EDP resolved for both stacks

## Non-claims
No physical results fabricated. No quotes/lead times invented. No merge to mainline without gate.
