# Branch claim — `hardware/exp-rauc-update`

**Experiment:** `EXP-RAUC-001`  
**Base:** `hardware/v1-mainline-ready-for-evt` (@ bd65bc67b413597a7d5534bc8dddaa9d7513b0c3)  
**State:** `EXPERIMENTAL_COMPARE`  
**Target PR base:** `hardware/v1-mainline-ready-for-evt` (not `main`)

This branch isolates the comparison track for: **RAUC A/B vs vendor capsule/EC update**.

Canonical package: `hardware_v1/experiments/EXP-RAUC-001/COMPARISON_PACKAGE.md`

## Rules
- Do not merge experimental MPNs into mainline BOM
- Do not claim physical results
- Promotion only via documented metrics + promotion gate in the comparison package
