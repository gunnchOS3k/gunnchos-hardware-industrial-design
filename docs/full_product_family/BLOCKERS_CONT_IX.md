# Blockers — Continuation IX

Updated: 2026-08-12T21:05:00Z  
STREAM C / HW-002 honesty: DIGITAL is **not** empty. `HW_FIRMWARE_DIGITAL_PACKAGE_COMPLETE=false`.

## DIGITAL
- Handheld production A/B/recovery images unproven vs Outcome A 5.0 GiB slot budgets — `NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001` **OPEN** (`npi/phase_xv/handheld_storage_headroom/`)
- Residual `lib_footprint_mismatch` warnings remain (handheld Cont IX) — digital hygiene still open
- Dock/Student/DS-XL on-target firmware + NDA pin-accurate fanout still open (harness-only digital path)
- COM-HPC/Dock EXTERNAL NDA maps block full digital package completion

### Closed in HW-002 (digital only)
- `NPI_DEFECT-HANDHELD-EDA-DANGLING-SILK-001` **CLOSED** — `track_dangling=0`, `silk_over_copper=0` on handheld
- `RING_ZEPHYR_WEST_BUILD_PASS` **EARNED** — real `west build` in `firmware/edge_io_rings/zephyr_west` (soft-skip forbidden); physical boot **not** claimed

## PHYSICAL
- PHYSICAL_EXECUTION_FREEZE — no fab, purchase, flash, assemble
- No manufacturer DFM sign-off yet (DFM_PRECHECK is digital self-check only)
- Ring physical boot pending despite Zephyr west digital PASS

## EXTERNAL
- COM-HPC Mini 400-pin net map (PICMG/ADLINK NARROW_NDA) — Student/DS-XL
- Dual eDP COM-HPC pin map — DS-XL
- Intel JHL8440 / JHL9040R package ball maps — Dock
- Display panel exact MPNs + hinge bend OEM spec — DS-XL AVL quotes
- Paste/reflow profile vendor values; some fastener torque OEM values
