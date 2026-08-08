# ADR-HW-001 — COM / SoM + carrier strategy (no fake proprietary CPU BGA)

- Status: **ACCEPTED (hardware engineering baseline)**
- Date: 2026-08-08T01:15:00Z
- Relates: field-kit ADR-FP-001 / ADR-FP-002 / ADR-FP-003 (compute freezes remain; **implementation form factor refined**)

## Context
Full-product electrical design must not invent proprietary Intel/AMD/Rockchip **CPU BGA fanout** without vendor PDK/NDA package files. Prior BOM lines saying “Application processor BGA (COM-like / soldered)” are ambiguous and risk false tokens.

## Decision
1. **Student 14.5 & DS-XL Coder:** purchase a commercial **COM-HPC Client Mini** (or equivalent documented Meteor Lake / Core Ultra 7 H-series COM) that already integrates CPU + LPDDR5x + critical high-speed power islands. gunnchOS designs the **carrier PCB** only: PD, EC, WWAN/Wi-Fi M.2, audio, sensors, display connectors, battery charger, I/O, dock USB-C.
2. **Handheld Hybrid:** purchase an **RK3588S SoM** (industry SODIMM/board-to-board) and design the **game carrier** (display, controls, power, radios, USB-C/DP).
3. Reject any schematic that places a bare `Core Ultra 7 155H` BGA with invented ball map.

## Consequences
- Student/DS-XL KiCad projects are **carrier + COM connector** designs.
- BOM lists COM as a **module line item** with vendor MPN class, not a fake die BGA.
- Field-kit ADR-FP-001 compute freeze (Ultra 7 155H class) remains the performance target; this ADR freezes the **honest integration method**.

## Non-claims
No statement that a specific COM vendor is under contract. AVL quote required before purchase (purchase frozen anyway).
