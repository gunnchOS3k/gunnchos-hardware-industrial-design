# Stream F — Section 15 Mechanical Digital Engineering

**Generated:** 2026-09-18T18:35:47Z  
**Gate:** `MECHANICAL_DIGITAL_ENGINEERING_EXHAUSTED`  
**Claim boundary:** digital enclosure/CAD/DFM prep only.

## Honesty
- `ERGONOMIC_PASS` = **FALSE** (CAD cannot grant ergonomic pass)
- `PHYSICAL_FIT_PASS` = **FALSE**
- `FIRST_ARTICLE_PRINT_PASS` = **FALSE**
- Antenna keepouts are ICD placeholders pending RF/electrical freeze (Stream E owns KiCad; this tree does not edit `.kicad_*`)

## SKUs covered
Student 14.5, Handheld Hybrid, DS-XL Coder, Edge I/O Rings, First-party Dock.

## Package layout
Per SKU under `hardware_v1/mechanical/skus/<sku>/`:
enclosure, tolerances, connectors, service, thermal/vents, antenna keepouts, exploded views, DFM/DFA, drawing package.

Family schemas under `hardware_v1/mechanical/family/`.

## Coordination with Stream E
Mechanical keepouts and connector envelopes reference electrical ICDs by path only.
Do not modify `device_designs/**/_shared_kicad` or `hardware_v1/electrical/**` in Stream F.
