## Summary
- Stream E digital hardware exhaustion for NXP open-custom, AMD public, Rings (nRF54L15), and Dock no-NDA paths.
- Gates set exhausted under public collateral + local EDA; fab-ready flags remain **false**.
- USB4/TB and AMD/NXP pin-accurate content explicitly not invented.

## Test plan
- [ ] `python3 scripts/generate_stream_e_digital_exhaustion.py` idempotent
- [ ] `bash hardware_v1/open_custom_nxp/scripts/export_imx95_open_kicad.sh`
- [ ] `bash hardware_v1/rings/scripts/export_rings_kicad.sh`
- [ ] `bash hardware_v1/dock/scripts/export_dock_no_nda_kicad.sh`
- [ ] Confirm `CPB0_OPEN_READY_FOR_FAB=false` in `hardware_v1/GATES.json`

## Claim boundary
digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps
