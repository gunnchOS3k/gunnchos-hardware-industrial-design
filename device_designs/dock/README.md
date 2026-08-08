# Dock — hardware design release candidate (full PCB, beyond skeleton)

Updated: 2026-08-08T20:15:00Z  
ADR: ADR-FP-006 + **ADR-HW-002**  
Architecture freeze: **USB4 / Thunderbolt 4 @ 40 Gbps** — **not TB5**  
Controller: **JHL8440** · Retimer: **JHL9040R**  
Prior: `DOCK_PCB_DIGITAL_PACKAGE_BEYOND_SKELETON`  
Now also: `DOCK_HARDWARE_DESIGN_RELEASE_CANDIDATE` + `DOCK_ARCHITECTURE_FROZEN_USB4_TB4_NOT_TB5`

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only

## Contents
- Architecture + expanded ICD (corrected silicon roles)
- Assembly BOM (JHL8440 controller, JHL9040R retimer, PD, hub, connectors, UWB companion)
- Explicit reject rows for JHL9480/JHL9580 (TB5)
- Power / thermal models
- KiCad schematic + 4-layer PCB structure + project
- Stackup, netlist JSON, fab notes, Gerber/STEP/PnP plans, ERC/DRC blocker JSON
- Ring cradle charge + optional UWB_ON_COMPANION (ADR-FP-008)

## Not claimed
`FULL_HARDWARE_DESIGN_RELEASE_COMPLETE`, USB-IF / Thunderbolt logo, FCC/CE, CLI ERC/DRC pass, fab, TB5.
