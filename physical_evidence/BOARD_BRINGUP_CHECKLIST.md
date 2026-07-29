# Board Bring-Up Checklist (Gate 6 harness)

Status boundary: **DESIGN_ONLY** / **HARDWARE_PROTOTYPE_PENDING**. Completing checklist items in dry-run does **not** create physical bring-up evidence.

## Pre-power

- [ ] ESD precautions documented
- [ ] Correct revision board identified (`board_revision`)
- [ ] BOM vs assembly reconciliation recorded
- [ ] Programming / debug header continuity checked (when hardware present)
- [ ] Power rail shorts screened (when hardware present)

## First power

- [ ] Current-limited supply set
- [ ] Rail voltages within design tolerance
- [ ] No unexpected thermal hotspots at idle
- [ ] Clock / reset observed (when hardware present)
- [ ] Serial console or LED heartbeat observed (when hardware present)

## Post bring-up

- [ ] Power/thermal/battery log started (`power_thermal_battery_log.schema.json`)
- [ ] Mechanical fit record drafted if enclosure present
- [ ] Defects logged in defect registry (none invented)
- [ ] Evidence label remains `BLOCKED_HARDWARE` or `SYNTHETIC_EXPERIMENT` until real measurements exist

## Dry-run note

Emulated / synthetic checklist ticks are harness-only. Physical claims stay `HARDWARE_PROTOTYPE_PENDING`.
