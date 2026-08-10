# EVT0 Master Test Matrix (summary)
Canonical JSON: `EVT0_MASTER_TEST_MATRIX.json`.
| Test ID | Priority | Name | Risks | Journeys |
|---|---|---|---|---|
| EVT-PWR-000 | P0 | Pre-power inspection + ESD/dimensional | RISK-001, RISK-003 | — |
| EVT-PWR-001 | P0 | Rail resistance / short screen | RISK-001 | — |
| EVT-PWR-002 | P0 | Current-limited first power | RISK-001, RISK-005 | — |
| EVT-PWR-003 | P0 | Rail voltage sequence | RISK-001 | — |
| EVT-PWR-004 | P1 | Idle vs load input power | RISK-005, RISK-008 | GOLDEN-08 |
| EVT-BOOT-001 | P0 | Bootloader + serial console | RISK-001 | — |
| EVT-BOOT-002 | P0 | Storage enumerate + OS image boot | RISK-001, RISK-004 | GOLDEN-01, GOLDEN-05 |
| EVT-DISP-001 | P1 | Primary display + touch | RISK-009 | GOLDEN-01, GOLDEN-06 |
| EVT-DISP-002 | P1 | DS-XL dual-display enumeration | RISK-003, RISK-009 | GOLDEN-06 |
| EVT-DISP-003 | P1 | DS-XL flex/hinge continuity + cycle plan start | RISK-003 | GOLDEN-06 |
| EVT-DOCK-001 | P3 | Dock PD negotiation | RISK-002, RISK-005 | GOLDEN-04, GOLDEN-05 |
| EVT-DOCK-002 | P3 | Dock USB/Ethernet/audio enumerate | RISK-002 | GOLDEN-04, GOLDEN-05 |
| EVT-DOCK-003 | P3 | Dock display hotplug | RISK-002, RISK-009 | GOLDEN-04, GOLDEN-05 |
| EVT-DOCK-004 | P3 | Dock high-speed link integrity | RISK-002 | GOLDEN-04, GOLDEN-05 |
| EVT-RF-001 | P2 | Wi-Fi/BT association + throughput smoke | RISK-006 | GOLDEN-02 |
| EVT-RF-002 | P2 | Ethernet docking path | RISK-002 | GOLDEN-04 |
| EVT-RF-003 | P2 | Antenna/RF coexistence pre-scan | RISK-006 | GOLDEN-02, GOLDEN-07 |
| EVT-RF-004 | P2 | RM520N-GL modem attach smoke | RISK-011 | GOLDEN-02 |
| EVT-THERM-001 | P5 | Idle/office thermal map | RISK-005, RISK-001 | GOLDEN-01, GOLDEN-04, GOLDEN-06 |
| EVT-THERM-002 | P5 | AI+game combined thermal/power | RISK-005, RISK-008, RISK-009 | GOLDEN-01, GOLDEN-05, GOLDEN-08 |
| EVT-BATT-001 | P5 | Battery discharge under office profile | RISK-005 | GOLDEN-01 |
| EVT-BATT-002 | P5 | Charge + PD charge path | RISK-005, RISK-002 | GOLDEN-04 |
| EVT-BATT-003 | P5 | Limited cycle characterization | RISK-005 | — |
| EVT-RING-001 | P6 | Ring power/current + FW program | RISK-007 | GOLDEN-07 |
| EVT-RING-002 | P6 | Packet transport latency/loss | RISK-007 | GOLDEN-07 |
| EVT-RING-003 | P6 | Spatial drift vs reference pose | RISK-007 | GOLDEN-07 |
| EVT-RING-004 | P6 | Wrong-target / low-confidence rejection | RISK-007 | GOLDEN-07 |
| EVT-RING-005 | P6 | Long-session runtime + SE/provisioning smoke | RISK-007 | GOLDEN-07 |
| EVT-AI-001 | P7 | Local AI TTFT / tokens-s | RISK-008 | GOLDEN-08, GOLDEN-03 |
| EVT-AI-002 | P7 | Local AI RAM/power under tutoring | RISK-008, RISK-005 | GOLDEN-08 |
| EVT-AI-003 | P7 | AI thermal under sustained tutoring | RISK-008, RISK-005 | GOLDEN-08 |
| EVT-GAME-001 | P7 | GPU/game profile FPS + frame time | RISK-009 | GOLDEN-01, GOLDEN-05 |
| EVT-GAME-002 | P7 | Suspend/resume soak | RISK-010 | GOLDEN-01, GOLDEN-05 |
| EVT-GJ-001 | P7 | Golden Student Day physical companion | RISK-005, RISK-008, RISK-012 | GOLDEN-01, GOLDEN-02, GOLDEN-08 |
| EVT-GJ-004 | P7 | Office dock Golden physical companion | RISK-002, RISK-010 | GOLDEN-04, GOLDEN-05 |
| EVT-GJ-006 | P7 | DS-XL dual-screen Golden physical companion | RISK-003, RISK-009 | GOLDEN-06, GOLDEN-03 |
| EVT-GJ-007 | P7 | Ring real-input Golden physical companion | RISK-007 | GOLDEN-07 |
