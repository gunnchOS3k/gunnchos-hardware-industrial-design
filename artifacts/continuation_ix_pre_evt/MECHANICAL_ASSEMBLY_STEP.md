# Mechanical assembly STEP — Cont IX

Updated: 2026-08-09T20:50:52Z

Board STEP exports from KiCad CLI are board-level. Major body assembly STEP intent:
- Student/DS-XL: COM-HPC module envelope 95×70 + display panel bodies (panel MPN EXTERNAL) + hinge (EXTERNAL)
- Handheld: RM121 module body + display/battery envelopes
- Ring: band + electrode + antenna keepout solids
- Dock: enclosure + USB-C shells

Where vendor STEP missing: request listed in EXTERNAL_VENDOR_COLLATERAL_REQUIRED.
Board STEP bytes: {'handheld_hybrid': 14828, 'edge_io_rings': 14776, 'dock': 14806, 'student_14_5': 14822, 'ds_xl_coder': 14820}
