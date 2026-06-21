# Production Release Evidence Matrix

| Gate | Required evidence | Current evidence | Status | Signoff role | Blocking? |
|------|-------------------|------------------|--------|--------------|-----------|
| mechanical correctness | Engineer review + fit check | STL + validation report | planned | ME | Yes |
| printability | First-article print + mesh check | STL only | planned | ME/Vendor | Yes |
| electrical schematic review | EE-reviewed schematics | Skeleton only | not_started | EE | Yes |
| routed PCB | Layout files | Not started | not_started | EE | Yes |
| Gerbers/drill/CPL | Fabrication outputs | None | not_started | EE/CM | Yes |
| DFM review | Vendor report | Not performed | not_started | CM | Yes |
| DFT review | Test coverage report | Not performed | not_started | EE | Yes |
| BOM lock | Locked BOM + AVL | Draft BOM | planned | Program | Yes |
| supplier quotes | ≥3 quotes | Tracker only | planned | Program | Yes |
| battery safety | EE review + cert path | Planning docs | planned | Battery EE | Yes |
| thermal validation | Sim or measured data | Assumptions only | not_started | Thermal EE | Yes |
| firmware/OS integration | Integration test report | OS alpha external | planned | SW/HW | Yes |
| OS compatibility handoff | os_compatibility/device_class_exports/*.yaml + traceability | Handoff package created; OS PR #27 consumed profiles | documented | SW/HW | Yes |
| OS profile export manifest | Four device class export YAMLs | Exports in os_compatibility/ | documented | Program | Yes |
| simulated OS compatibility | OS hardware_compat engine demos | OS-side simulated only | simulated | SW | Yes |
| hardware-side OS validation plan | hardware_os_validation/ package | Plan exists; real HW not started | documented | QA | Yes |
| real hardware boot | os_compatibility_evidence/OS_BOOT_LOG_PLACEHOLDER.md | Placeholder only — not proven | needs_real_hardware | QA | Yes |
| HLK-style readiness | hlk_readiness/ package | Plan only; HLK not run | documented | Compliance | No |
| real hardware compatibility | Lab signoff + evidence intake | Not started | blocked | QA | Yes |
| DVT pass | DVT report | Not complete | not_started | QA | Yes |
| PVT pass | PVT report | Not complete | not_started | CM/QA | Yes |
| compliance/certification | Lab reports | Not certified | not_started | Compliance | Yes |
| packaging/labeling | Approved art/manual | Plan only | planned | Program | Yes |
| repair/service | Service manual | Plan only | planned | Service | Yes |
| production test fixture | Fixture design + validation | Plan only | planned | EE/CM | Yes |
| CM signoff | CM release letter | None | not_started | CM | Yes |
