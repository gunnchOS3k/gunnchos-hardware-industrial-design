# EVT0 Bring-Up Sequence (Risk-First)

Status: DIGITAL procedure only. `PHYSICAL_EXECUTION_FREEZE`. Do not energize hardware under freeze.

Hardware rev baseline: `0.6.0-cont-ix`.

## Order (mandatory)

1. **pre_power** — `EVT-PWR-000` ESD, silk/rev, dimensional, visual damage
2. **rail_resistance** — `EVT-PWR-001` resistance / short screen before applying power
3. **current_limited_power** — `EVT-PWR-002`, `EVT-PWR-003` CC PSU, rail sequence, console alive
4. **boot_debug** — `EVT-BOOT-001` bootloader, FW SHA, debug harness
5. **storage** — `EVT-BOOT-002` storage + OS image; Handheld microSD path
6. **display_input** — `EVT-DISP-001..003` panels/touch; DS-XL dual + hinge continuity
7. **network** — `EVT-RF-001..004` Wi-Fi/BT/ETH smoke; coexistence/modem via rent/lab/vendor
8. **dock** — `EVT-DOCK-001..004` PD → enumerate → hotplug → SI (RENT tooling)
9. **thermal** — `EVT-THERM-001..002` idle/office then AI+game combined
10. **battery** — `EVT-BATT-001..003` discharge/charge/limited cycles (safety plan first)
11. **rings** — `EVT-RING-001..005` power → transport → drift → wrong-target → long session
12. **game_ai** — `EVT-AI-001..003`, `EVT-GAME-001..002`
13. **golden_journeys** — `EVT-GJ-001/004/006/007` physical companions for E4→E5

## Damaging-order prohibitions

- Never apply unrestricted PSU before `EVT-PWR-001`.
- Never run battery cycler without `EVT0_SAFETY_PLAN.md` Li-ion controls.
- Never radiated RF transmit without RF safety checklist.
- Never force DS-XL hinge past stop; use cycle fixture concept limits.
- Dock SI (`EVT-DOCK-004`) after basic PD/enumerate success — avoid frying link with bad cables.

## Evidence

Every step writes an `EVT0EvidenceRecord`. Default `pass_fail=NOT_RUN` / `physical_execution_status=PHYSICAL_PENDING` until real execution.
