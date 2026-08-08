# FULL_HARDWARE_DESIGN_RELEASE_COMPLETE — criteria

Updated: 2026-08-08T20:58:59Z

A product may claim `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` only if **all** are true:

1. Exact orderable compute/SoM/MCU MPN frozen with vendor+docs+lifecycle+procurement note
2. Native EDA package: hierarchical schematic + PCB with **real library symbols/footprints** (not Device:R placeholders) for all non-DNP BOM lines
3. Manufacturing package: stackup, netlist, fab notes, paste/pick-place plan, BOM AVL fields
4. Driver/firmware classification complete for every high-risk subsystem
5. Battery + thermal + RF models present (MODELED allowed under freeze; must not be empty)
6. `kicad-cli` ERC **and** DRC executed with reports checked in (or CI artifact)
7. CAD: enclosure package native to stated toolchain (Fusion for Rings) with exportable STEP/STL
8. No forbidden claims (fake CPU BGA, 6G modem, NTN inference, fab/purchase, TB4 mislabeled as TB5)
9. Dock (if applicable): architecture generation matches ADR-HW-002 (USB4/TB4 40G) with correct controller vs retimer roles
10. COM-HPC carriers: either PUBLIC_PINOUT nets or documented **NARROW_NDA** pinout intake — no invented pins

## Cont VI additions
- Student/DS-XL: Option3 gate → `*_BLOCKED_NDA` until NDA pinout intake; criteria #10 fails for COMPLETE
- Handheld: PUBLIC_PINOUT carrier EDA may claim `HANDHELD_PUBLIC_PINOUT_EDA_COMPLETE` without claiming FULL COMPLETE
- `*_DESIGN_RELEASE_COMPLETE` (short token) also requires criteria #2 and #6 — **not earned** while Device:R + CLI absent

## Current environment blockers
- `kicad-cli` ABSENT → `EDMUND_ACTION_REQUIRED` / resume via `make kicad-validate-family`
- Device:R structural placeholders remain
- COM-HPC Mini full pinout remains NARROW_NDA
