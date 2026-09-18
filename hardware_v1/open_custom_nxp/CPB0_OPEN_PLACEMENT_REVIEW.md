# CPB0-O placement review

**Generated:** 2026-09-18T19:17:34Z  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

## Board concept

Learning/bring-up form factor (~170×120 mm class — not thin-device packaging): accessible TPs, short DDR, connector banks on edges.

## Zones

1. Center-left: SoC FCBGA + LPDDR5
2. Adjacent: PF09/PF53 power island + sense TPs
3. East: M.2 M/E (+ B DNP)
4. South: USB-C, GbE, debug USB, JTAG
5. North: display/camera FPC
6. West: EC, fan, status LEDs, recovery

## Automated checks (digital)

| Check | Result |
|---|---|
| Outline present in PCB | STARTED (see kicad_pcb) |
| SoC/DRAM/PMIC courtyard collision engine | NOT RUN (tooling/layout incomplete) |
| DDR length-driven placement | BLOCKED on UG10210 |

`CPB0_OPEN_PLACEMENT_PASS=false` — placement documented and stubbed, not signed off.
