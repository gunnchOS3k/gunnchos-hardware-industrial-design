# EXP-COREBOOT-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
coreboot/openSIL vs vendor UEFI on custom Platform Core

## Hypothesis
Reproducible host firmware is achievable without blocking production on vendor UEFI/AGESA path

## Baseline (mainline)
Vendor-supported UEFI + AGESA on custom AMD motherboard

## Variant
coreboot and/or AMD openSIL when production-capable for selected platform

## Metrics
- boot_time_s
- secure_boot_coverage
- repro_build
- platform_enablement_gaps

## Promotion gate
Must not block mainline; only promote after production-capable platform support

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
