# ICD — First-party Dock (full digital)

Updated: 2026-08-08T20:15:00Z  
ADR: ADR-FP-006 + **ADR-HW-002**  
Freeze: **USB4 / Thunderbolt 4 @ 40 Gbps** — **not Thunderbolt 5**

| Interface | Direction | Protocol | Hosts | Notes |
|---|---|---|---|---|
| Upstream USB-C | bidirectional | USB4 **40G** (JHL8440) or USB3+DP Alt (VL108) + PD | Student, DS-XL, Handheld | Controller **JHL8440**; SI retimer **JHL9040R**; TB5 forbidden |
| Downstream USB-C ×2 | dock→peripherals | USB3 / DP | all | |
| USB-A 3.2 ×2 | dock→peripherals | USB3 | all | VL817 |
| HDMI/DP | dock→display | HDMI 2.1 or DP 1.4 | all | no logo claim |
| RJ45 | dock↔network | 2.5GbE | all | RTL8156 |
| 3.5mm optional | audio | USB audio ALC4050 class | optional | |
| Ring pogo | dock→ring | 5V charge | Edge I/O Rings | ESD required |
| UWB companion | dock↔ring/host | UWB SPI/UART to MCU or host | ADR-FP-008 escape | DWM3001C optional |

Continuity software: existing `dock_manager` — expand automated suite (software repo).  
Controller package pinout: **NDA / Intel design kit** — do not invent nets.
