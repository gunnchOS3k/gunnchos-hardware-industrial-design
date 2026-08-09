# Assembly work instruction — handheld_hybrid

Updated: 2026-08-09T19:46:44Z  
PHYSICAL_EXECUTION_FREEZE — document only; do not assemble under freeze.

## Sequence
1. SMT top: passives → ICs → connectors (reflow profile per paste vendor — **EXTERNAL: paste MPN + profile**).
2. SoM press-fit / SODIMM insert after SMT inspection.
3. Bottom SMT if required (Cont VIII single-side primary).
4. Manual: USB-C mechanical check; torque fasteners per table.
5. ICT / flying probe on TP1–TP4 (GND, 3V3, VBUS, VSYS).
6. Firmware programming / recovery pads (see firmware hooks doc).
7. Functional QC checklist.

## Torque / adhesive
See `FASTENER_TORQUE_TABLE.csv` and `ADHESIVE_THERMAL_MATERIAL_TABLE.csv`.
Where vendor value unknown: marked **EXTERNAL_BLOCKER**.
