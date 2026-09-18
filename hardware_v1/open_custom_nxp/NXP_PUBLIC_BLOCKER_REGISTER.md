# NXP public blocker register (NXP-1)

**Generated:** 2026-09-18T19:19:08Z

| ID | Blocker | Class | Blocks gate | Resolution |
|---|---|---|---|---|
| BLK-UG10210 | Hardware design guide length/impedance tables | ACCOUNT_LOGIN | NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD, PCB_READY, FAB | Owner ordinary-account fetch + hash |
| BLK-EVK-BOM | Exact PF53 + LPDDR5 + OTP MPNs | ACCOUNT_OR_PUBLIC_ZIP | BOM_AVL_DIGITAL_PASS, PMIC OTP freeze | Owner fetch EVK BOM |
| BLK-IBIS | IBIS models for sim | ACCOUNT_MAYBE | SI PASS | Optional; not required for digital docs |
| BLK-ERC | Full schematic wiring + ERC zero | EDA | SCHEMATIC_ERC_PASS / READY | Continue EDA after MPNs |
| BLK-DRC | Routed PCB + DRC | EDA | PCB_DRC_PASS / READY | After DDR rules |
| BLK-NDA | — | NONE | — | No NDA required items identified |

Minimal digital blockers keeping `CPB0_OPEN_READY_FOR_FAB=false`:
1. UG10210 (or EVK layout) DDR constraint tables
2. Exact DRAM + PF53 OPNs / PF09 OTP package from EVK BOM
3. Complete schematic ERC pass with real parts
4. Footprint library validation vs mechanical drawings
5. Placement/routing/DRC complete under those constraints
