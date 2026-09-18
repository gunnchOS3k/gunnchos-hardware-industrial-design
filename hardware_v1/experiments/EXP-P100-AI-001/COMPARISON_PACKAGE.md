# EXP-P100-AI-001 comparison package

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Title
Student P132/P132i AI-first vs 8840U mainline

## Hypothesis
Higher NPU prioritization beats 8840U for gunnchAI local workloads without unacceptable GPU/game/battery regression

## Baseline (mainline)
Ryzen Embedded 8840U Platform Core

## Variant
Ryzen AI Embedded P132 / P132i-class (PENDING_VENDOR_CONFIRMATION)

## Metrics
- npu_perf
- gunnchai_local
- cpu
- gpu
- battery
- usb4
- networking
- memory_options
- thermal
- windows_linux
- game_perf
- board_complexity

## Promotion gate
Physical comparison; AI-first SKU only after evidence; does not replace mainline now

## Isolation
`not_in_main_bom=true` — experimental parts must not mix into MAINLINE_CUSTOM with qty>0.
