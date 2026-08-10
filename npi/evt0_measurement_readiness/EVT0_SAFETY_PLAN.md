# EVT0 Safety Plan

Digital readiness only. Operators must complete this checklist before any future physical EVT energization.

## Li-ion handling

- Use fused, polarity-keyed battery harness (`FIX-BATT`).
- Charge/discharge only with current-limited supply or rated charger path.
- Never leave cycling cells unattended; fire-safe container; sand/Class D extinguisher available.
- Damaged/swollen pack: power disconnect → isolate → do not puncture → quarantine → scrap procedure.

## ESD

- ESD mat + wrist strap verified before board handling.
- Bags/foam for boards and Rings; ionizer optional for plastics.

## Thermal limits

- Abort if skin/hotspot exceeds draft abort threshold (finalize with WP-008 when frozen); until then use conservative 45 °C skin / 85 °C SOC abort defaults for bring-up only.
- Thermocouple placement per `fixtures/THERMAL_SENSOR_MAP.md`.

## Current limiting

- First power always CC-limited (`EVT-PWR-002`).
- Emergency power disconnect within reach of operator (bench E-stop or PSU output kill).

## RF safety

- Conducted fixtures preferred for EVT0.
- Radiated tests: EXTERNAL_LAB or controlled shield box; SAR/exposure not claimed in EVT0.
- No indefinite high-power transmit into open air on bench.

## Mechanical / hinge / pinch

- DS-XL cycle fixture: pinch guards; keep fingers clear of hinge.
- Do not exceed mechanical design open angle.

## Emergency power disconnect

- Labelled E-stop / PSU kill for every energized setup.
- Dock PD fault: unplug VBUS immediately; log defect.

## Training / roles

- Operator + safety observer for first power and battery tests.
- Record operator ID on every evidence record.
