# Fab notes — Edge I/O Rings

Updated: 2026-08-08T19:40:00Z  
Board: `edge_io_ring_main`  
Compute/controller: **nRF52840-QIAA-R**  
PHYSICAL_EXECUTION_FREEZE — do **not** send to fab.

## Stackup
See `stackup.yaml` (4-layer target).

## Controlled impedance (MODELED targets)
- USB3 SuperSpeed: 90 Ω diff
- USB4 / high-speed where applicable: 85 Ω diff
- HDMI (dock): 100 Ω diff
- PCIe: 85 Ω diff
- eDP: per panel vendor

## Keep-outs
- Antenna keep-outs per `../electrical/rf_model.yaml` (or gate1 RF notes for rings)
- COM/SoM keep-out and standoff pattern per vendor mechanical drawing (ADLINK/Radxa)

## Outputs pending kicad-cli
Gerbers, drill, IPC-356, pick-and-place: **EDMUND_ACTION_REQUIRED** (`kicad-cli` absent).

## Non-claims
Not fab-ready. Not DFM-signed. Not purchased.
