# Risk Register

| Risk | Mitigation |
|------|------------|
| EE skeleton only | Hire/review EE |
| Phase XV Handheld 32GB eMMC operational headroom unsafe for reduced OS profile (`NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001`) | WP-002 Outcome A (pending V1): system-only eMMC + µSD policy, capacity model, reserves/reclamation, E2E sim — see `npi/phase_xv/handheld_storage_headroom/`. Do not invent larger Radxa eMMC SKUs; NVMe remux remains deferred Class E spike only. |
| STREAM C Handheld production A/B image fit unproven (`NPI_DEFECT-HANDHELD-IMAGE-SLOT-FIT-001`) | OPEN — device-os #107 IMAGE_FIT_MANIFEST measures stub realm sizes (numeric fit); MLP/production A/B disk images still required before close. Outcome A retained; no invented eMMC SKU. |
| COM-HPC / Dock NDA pin & ball maps | EXTERNAL — cannot close digitally; keep public packages conditional |
| Dock TB4 SI (RISK-002) | NDA collateral + EVT measurement; TB5 rejected |
