# Fab notes — Dock main PCB

Updated: 2026-08-08T20:15:00Z  
Board: `dock_main_pcb`  
Controller: **Intel JHL8440** (USB4/TB4 @ 40G)  
Retimer: **Intel JHL9040R**  
Forbidden: **JHL9480 / JHL9580** (TB5)  
PHYSICAL_EXECUTION_FREEZE — do **not** send to fab.

## Stackup
See `stackup.yaml` (4-layer target).

## Controlled impedance (MODELED targets)
- USB3 SuperSpeed: 90 Ω diff
- USB4 / TB4 40G: 85 Ω diff
- HDMI (dock): 100 Ω diff
- Do **not** apply TB5 80G stackup assumptions

## Keep-outs
- Antenna keep-outs per `../electrical/rf_model.yaml` (or gate1 RF notes for rings)
- Ring pogo ESD keep-out

## Outputs pending kicad-cli
Gerbers, drill, IPC-356, pick-and-place, STEP: **EDMUND_ACTION_REQUIRED** (`kicad-cli` absent).  
See `GERBER_EXPORT_PLAN.md`, `STEP_EXPORT_STATUS.md`, `ERC_DRC_STATUS.json`.

## Non-claims
Not fab-ready. Not DFM-signed. Not purchased. Not Thunderbolt-certified. Not TB5.
