# Hardware design release status matrix — Continuation VI

Updated: 2026-08-08T20:58:59Z  
Branch: `cursor/full-product-continuation-vi-eda-closure`  
Base: `origin/main` @ `38b37221074446730709af5682a06cb4cefd39fc` (#48)

PHYSICAL_EXECUTION_FREEZE ACTIVE — no fab, no purchase, draft digital only.

| Product | Exact compute MPN | Public-engineerability | EDA Cont VI | KiCad CLI | Status token |
|---|---|---|---|---|---|
| Student 14.5 | ADLINK **COM-HPC-mMTL-155H-32G** | Option3 — NDA nets external | Architecture only; **no fake pinout** | ABSENT → resume scripts | `STUDENT_BLOCKED_NDA` |
| DS-XL Coder | Shared **COM-HPC-mMTL-155H-32G** | Option3 | Dual-eDP ICD; NDA pin map external | ABSENT → resume | `DSXL_BLOCKED_NDA` |
| Handheld Hybrid | Radxa **RM121-D8E32** | **PUBLIC_PINOUT 260-pin** | True carrier nets/power/display/USB/controls/WWAN/audio/storage/debug | ABSENT → resume | `HANDHELD_PUBLIC_PINOUT_EDA_COMPLETE` (not FULL COMPLETE) |
| Edge I/O Rings | **nRF52840-QIAA-R** | Public Nordic + fusion BOM | EDA + DT parity notes | ABSENT → resume | `RING_EDA_DT_PARITY_NOTES_COMPLETE` (not FULL COMPLETE) |
| Dock | **JHL8440** + **JHL9040R** | Role PUBLIC; package pins NDA | TB4 topology EDA complete | ABSENT → resume | `DOCK_TB4_EDA_COMPLETE` (not FULL COMPLETE) |

## Family claim
- Claimed: Cont VI tokens below; candidate package retained
- **Not claimed:** `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE`
- **Not claimed:** `HANDHELD_DESIGN_RELEASE_COMPLETE` / `RING_DESIGN_RELEASE_COMPLETE` / `DOCK_DESIGN_RELEASE_COMPLETE`  
  (RELEASE_CRITERIA #2 Device:R + #6 kicad-cli ERC/DRC still open)

## Why DESIGN_RELEASE_COMPLETE not earned for Handheld/Ring/Dock
1. Structural `Device:R` placeholders (criteria #2)
2. `kicad-cli` absent → no ERC/DRC/Gerber/PnP/STEP execution (criteria #6)
3. Dock Intel package ball maps still NDA (topology OK; pin-accurate controller fanout not public)
