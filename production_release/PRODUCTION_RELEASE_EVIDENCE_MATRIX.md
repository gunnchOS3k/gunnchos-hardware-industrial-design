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
| DVT pass | DVT report | Not complete | not_started | QA | Yes |
| PVT pass | PVT report | Not complete | not_started | CM/QA | Yes |
| compliance/certification | Lab reports | Not certified | not_started | Compliance | Yes |
| packaging/labeling | Approved art/manual | Plan only | planned | Program | Yes |
| repair/service | Service manual | Plan only | planned | Service | Yes |
| production test fixture | Fixture design + validation | Plan only | planned | EE/CM | Yes |
| CM signoff | CM release letter | None | not_started | CM | Yes |
