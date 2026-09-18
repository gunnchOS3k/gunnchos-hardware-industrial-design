# CPB0-O PCB architecture

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Topic | Intent |
|---|---|
| Form factor | Debug-friendly learning carrier (EVK-like, not product enclosure) |
| Tentative layers | **12-layer** candidate (may reduce after UG10210) |
| BGA | 19×19 / 0.7 mm escape; dogbone + via-in-pad decision pending fab capability |
| HDI | Prefer **non-HDI first**; escalate only if escape fails |
| High-speed | Outer/inner pairs for PCIe/USB/MIPI with ref planes |
| DDR | Dedicated layers per upcoming UG10210 rules |
| Power | Split planes / shapes for core, DDR, 3V3 |
| DFT | Edge test points; optional pogo zone TBD |
| Fab | No house selected; no quote; capability checklist only |

`CPB0_OPEN_PCB_STARTED=false` until a real board file with outline/placement intent exists beyond empty stub — this campaign creates schematic-first KiCad; PCB file is a non-routed stub for tooling only → token **false** for "started" meaning engineering layout started. Stub present for project integrity.
