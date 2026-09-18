# EXP-DOCK-USB4-80-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
Dock USB4 80 vs USB4 40

## Hypothesis
USB4 80 improves external display/storage UX enough to justify controller cost/SI risk

## Baseline (mainline)
CUSTOM_GUNNCHOS_DOCK_GEN1 USB4 40 (JHL8440 + JHL9040R class)

## Variant
USB4 80-class controller (vendor TBD — PENDING_VENDOR_CONFIRMATION)

## Metrics
- link_rate_gbps
- eye_margin
- bom_delta_usd
- cable_interop_pass_rate

## Promotion gate
Measured eye margin; no mainline mix until DVT

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
