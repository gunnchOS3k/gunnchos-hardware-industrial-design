# Pick-and-place plan — Student 14.5 carrier

Updated: 2026-08-08T19:40:00Z  
PHYSICAL_EXECUTION_FREEZE ACTIVE

1. Export centroid CSV via `kicad-cli pcb export pos` when CLI available
2. Verify polarity marks for PD/charger/QFN parts
3. Module seats (COM / SODIMM / M.2 / DWM3001C) are **hand-place / press-fit** — not SMT spray
4. DNP lines (optional UWB, WWAN on handheld, etc.) remain unpopulated for EVT0

Status: plan present; machine files pending CLI.
