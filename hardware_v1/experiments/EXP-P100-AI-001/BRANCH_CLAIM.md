# Branch claim — `hardware/exp-student-p100-ai`

**Experiment:** `EXP-P100-AI-001`  
**Base:** `hardware/v1-mainline-ready-for-evt` (@ 628eacd8f35a2a509f36592c392b6aba88b6c4f8)  
**State:** `EXPERIMENTAL_COMPARE`  
**Target PR base:** `hardware/v1-mainline-ready-for-evt` (not `main`)  
**Refreshed:** 2026-09-18T16:50:34Z (HW1C)

This branch isolates the comparison track for: **Student P132/P132i AI-first vs 8840U mainline**.

Canonical package: `hardware_v1/experiments/EXP-P100-AI-001/COMPARISON_PACKAGE.md`

## Rules
- Do not merge experimental MPNs into mainline BOM
- Do not claim physical results
- Promotion only via documented metrics + promotion gate in the comparison package
- Custom AMD Platform Core remains product mainline; this variant cannot silently promote
