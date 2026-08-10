# Risk / unknowns consumption (WP-010 light)

Source: field-kit `program/operating_model/06_RISK_UNKNOWN_SUPPLY/RISK_REGISTER.json` and `KNOWN_UNKNOWNS.json`.

WP-010 does **not** close risks. It maps each RISK-001..012 and relevant UNK-* to tests, instruments, fixtures, and evidence fields. See `EVT0_RISK_TEST_TRACEABILITY.json`.

| Risk | Primary EVT tests | Residual until physical |
|------|-------------------|-------------------------|
| RISK-001 COM-HPC | EVT-PWR-*, EVT-BOOT-*, EVT-THERM-001 | vendor collateral + unit |
| RISK-002 Dock SI | EVT-DOCK-* | RENT SI + NDA collateral |
| RISK-003 DS-XL flex | EVT-DISP-002/003, EVT-GJ-006 | cycle fixture fab |
| RISK-004 Handheld storage | EVT-BOOT-002 | microSD endurance E5 |
| RISK-005 Battery/thermal | EVT-THERM-*, EVT-BATT-*, EVT-AI-003 | units + cal instruments |
| RISK-006 RF coexistence | EVT-RF-001/003 | rent/lab |
| RISK-007 Ring drift | EVT-RING-*, EVT-GJ-007 | MoCap borrow + rings |
| RISK-008 Local AI | EVT-AI-* | target SoC |
| RISK-009 Graphics/AV/input | EVT-DISP-*, EVT-AUD-001, EVT-CAM-001, EVT-KEY-001/002, EVT-GAME-001 | target GPU + AV path |
| RISK-010 Suspend | EVT-GAME-002 | soak on HW |
| RISK-011 Modem | EVT-RF-004 | vendor/carrier path |
| RISK-012 Human preference | EVT-GJ-* companions | human study (not EVT0 PASS) |
