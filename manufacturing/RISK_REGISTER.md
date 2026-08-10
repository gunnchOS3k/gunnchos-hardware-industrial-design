# Risk Register

| Risk | Mitigation |
|------|------------|
| EE skeleton only | Hire/review EE |
| Phase XV Handheld 32GB eMMC operational headroom unsafe for reduced OS profile (`NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001`) | Keep `PHYSICAL_EXECUTION_FREEZE`; prefer system-only eMMC + µSD/user-media policy (see `npi/phase_xv/handheld_storage_headroom/`). Do not invent larger Radxa eMMC SKUs. |
