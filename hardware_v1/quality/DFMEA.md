# DFMEA (digital starter)

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

| Item | Failure mode | Effect | Cause | Prevention | Detection | Severity | State |
|---|---|---|---|---|---|---|---|
| COM-HPC connector | Open/short pin | No boot | Pin-map error | Wait EXT-COM-HPC-400PIN | Continuity fixture | 10 | EXTERNAL_PENDING |
| Dock USB4 | Link train fail | No dock video | SI / ball-map | NDA ball maps | BERT/eye | 8 | EXTERNAL_PENDING |
| Rings charge | Intermittent pogo | No charge | Alignment | Magnetic cradle geometry | Charge log | 6 | PENDING_PHYSICAL_MEASUREMENT |
| Battery | Thermal event | Safety | Wrong chemistry | Qualified Li-ion only | Pack protector | 10 | ADOPTED_MAINLINE |
| OLED exp mix | BOM contamination | Yield/cost | Process error | Experiment isolation | BOM linter | 7 | CONTROL |

This is a digital DFMEA starter — not a completed live DFMEA sign-off.
