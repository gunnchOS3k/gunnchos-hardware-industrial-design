# Continuation VII — EDA release-clean summary

Updated: 2026-08-09T17:16:18Z

- Base: `bed14ca7530ce11379d0173d1eff056df2e00d19` (hardware #49)
- KiCad: 10.0.5
- Cont VI entries investigated: **111**
- Ledger: {'FIXED': 98, 'FORMALLY_WAIVED_WARNING': 10, 'EXTERNAL_NDA_BLOCKED': 3}
- NDA decision: `KEEP_ADLINK_AND_ACCEPT_NARROW_EXTERNAL_BLOCK`

## Per-board ERC/DRC (Cont VII re-run)

| Board | ERC err/warn | DRC err/warn | Gerbers | STEP bytes |
|---|---|---|---:|---:|
| student_14_5 | 0/22 | 0/0 | 17 | 14798 |
| ds_xl_coder | 0/15 | 0/0 | 17 | 14796 |
| handheld_hybrid | 0/35 | 0/0 | 17 | 14804 |
| edge_io_rings | 0/22 | 0/0 | 17 | 14752 |
| dock | 0/45 | 0/0 | 17 | 14782 |

## Release-clean tokens

All `*_EDA_RELEASE_CLEAN_PASS` = **FALSE** (structural PCB / vendor pinouts).
`KICAD_CLI_EXECUTION_PASS` = **TRUE**.
