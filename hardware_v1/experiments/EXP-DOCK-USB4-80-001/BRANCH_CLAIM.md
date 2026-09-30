# Branch claim — `hardware/exp-dock-usb4-80`

**Experiment:** `EXP-DOCK-USB4-80-001`  
**Base:** `hardware/v1-mainline-ready-for-evt` (@ 628eacd8f35a2a509f36592c392b6aba88b6c4f8)  
**State:** `EXPERIMENTAL_COMPARE`  
**Target PR base:** `hardware/v1-mainline-ready-for-evt` (not `main`)  
**Refreshed:** 2026-09-18T16:50:34Z (HW1C)

This branch isolates the comparison track for: **Dock USB4 80 vs USB4 40**.

Canonical package: `hardware_v1/experiments/EXP-DOCK-USB4-80-001/COMPARISON_PACKAGE.md`

## Rules
- Do not merge experimental MPNs into mainline BOM
- Do not claim physical results
- Promotion only via documented metrics + promotion gate in the comparison package
- Custom AMD Platform Core remains product mainline; this variant cannot silently promote
