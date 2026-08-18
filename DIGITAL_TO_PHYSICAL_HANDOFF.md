# Digital-to-physical handoff — device quartet

**Repo:** `gunnchos-hardware-industrial-design`  
**Audience:** EVT CM, electrical bring-up, prospective supervisor (boundary only).  
**Claim family:** `PHYSICAL_PENDING`. This file does **not** authorize fabrication, RFQ send, purchase, or certification.

Carrier-grade-**targeted** language only: reliability, serviceability, evidence discipline. No carrier approval, FCC, CE, USB-IF, or UN38.3 claim.

Device roles (must not collapse to generic gaming devices):

| SKU | Research / product role |
|---|---|
| Student 14.5 | Sustained desk / learning / work compute |
| Handheld Hybrid | Mobile/docked compute |
| DS-XL Coder | Local create / build / test / deploy |
| Edge I/O Rings | Wearable/body-area sensing and authenticated spatial input |

Dock is supporting continuity hardware, not a fourth research device class.

Authoritative electrical values come from in-tree public datasheets, frozen MPNs, and recorded ERC/DRC runs. Unknown vendor/NDA fields stay unknown. Do not invent rails, pin maps, or antenna numbers.

## This-run digital hygiene (recorded)

Source: `artifacts/supervisor_ready_eda/kicad/*/summary.json` on this branch.

| SKU | ERC errors | ERC warnings | DRC errors | DRC warnings | Fab pass? |
|---|---:|---:|---:|---:|---|
| Student 14.5 | 0 | 40 | 0 | 50 | **false** |
| Handheld Hybrid | 0 | 461 | 0 | 39 | **false** |
| DS-XL Coder | 0 | 45 | 0 | 51 | **false** |
| Edge I/O Rings | 0 | 27 | 0 | 22 | **false** |

Zero ERC/DRC **errors** is digital schematic/PCB hygiene. Warnings remain. `DIGITAL_FABRICATION_PASS` stays **FALSE**. See [DIGITAL_MANUFACTURING_READINESS.md](DIGITAL_MANUFACTURING_READINESS.md).

---

## Student 14.5 — sustained desk compute

| Item | Digital status | Physical / external |
|---|---|---|
| Role | `IMPLEMENTED_DIGITAL` in charter + OS contracts | Role must not regress to a gaming laptop |
| CAD / concept SCAD | Present (`cad/openscad/student_14_5/`) | First-article print `PHYSICAL_PENDING` |
| Schematic / PCB | KiCad present; ERC/DRC 0 errors | EVT board `PHYSICAL_PENDING` |
| Power tree | YAML `MODELED` / public-docs | Measured rails `PHYSICAL_PENDING` |
| COM-HPC pin-accurate fanout | Named MPN; pin map `EXTERNAL_PENDING` | Do not guess NDA balls |
| Digital release package | **not earned** | Owner/CM freeze |
| RF / thermal / battery | Targets documented | Chamber/skin-temp/runtime `PHYSICAL_PENDING` |
| Certification | Digital prep only | `CERTIFICATION_PENDING` |

**Handoff packet:** [docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md](docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md)

---

## Handheld Hybrid — mobile/docked compute

| Item | Digital status | Physical / external |
|---|---|---|
| Role | Mobile/docked compute; dock continuity | Not a generic handheld game console |
| SoM freeze | RM121-D8E32 frozen in BOM | Bring-up `PHYSICAL_PENDING` |
| Digital release package | Earned in `device_designs/handheld_hybrid/digital_release/INDEX.json` | Public-pinout package **is not** EVT/DVT/PVT |
| KiCad ERC/DRC | 0 errors; 461 ERC warnings remain | Warning triage is CM/electrical, not invented fixes |
| Antenna / SI | Design notes | RF validation `PHYSICAL_PENDING` |
| Dock pairing | Contract in OS/hardware traceability | Physical SI `PHYSICAL_PENDING` |

---

## DS-XL Coder — local create/deploy

| Item | Digital status | Physical / external |
|---|---|---|
| Role | Dual-screen learn/build/test/deploy | Not a novelty dual-screen toy |
| COM-HPC + dual-eDP | Topology named | Pin-accurate eDP AVL `EXTERNAL_PENDING` |
| Digital release package | **not earned** | Blocked on pin maps |
| Dual-display compositor contract | OS compatibility docs | Two-panel visual proof `PHYSICAL_PENDING` |
| KiCad ERC/DRC | 0 errors; warnings remain | Same hygiene rule as family |

---

## Edge I/O Rings — sensing / spatial input

| Item | Digital status | Physical / external |
|---|---|---|
| Role | Authenticated spatial/surface input | IMU-only is **not** absolute pose |
| nRF52840 path | Public silicon; BOM present | Physical boot `PHYSICAL_PENDING` |
| Spatial accuracy | Firmware/sim contracts | Absolute registration `PHYSICAL_PENDING` |
| Anti-spoof / comfort | Specs/checklists | Human/lab `PHYSICAL_PENDING` |
| Pixel 6a client | Digital acceptance packet in Edge-I/O repo | Signed on-device session `PHYSICAL_PENDING` |

Do not convert Ring IMU samples into `DEVICE_MEASURED` pose.

---

## What a CM / lab still owns (owner actions — not this agent)

1. NDA pin maps (COM-HPC, JHL8440/JHL9040R where required).  
2. Warning-by-warning ERC/DRC close only with datasheet authority.  
3. RFQ send (`RFQ_SENT` stays false until owner sends).  
4. EVT assembly, rail measurement, RF, thermal, battery, USB-IF/FCC/CE.  

Packets (do not execute from Cursor): [MANUFACTURER_RFQ_SEND_PACKET.md](docs/packets/MANUFACTURER_RFQ_SEND_PACKET.md), [PHYSICAL_EVT_BRINGUP_PACKET.md](docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md).
