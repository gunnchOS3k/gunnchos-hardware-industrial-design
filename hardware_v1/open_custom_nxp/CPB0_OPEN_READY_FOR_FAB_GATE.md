# CPB0_OPEN_READY_FOR_FAB gate definition

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



Set `CPB0_OPEN_READY_FOR_FAB=true` **only** when all are true:

1. public pin map complete (`NXP_PUBLIC_PINMAP_UNDERSTOOD`)
2. power architecture complete
3. memory topology complete (`NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD`)
4. schematic complete
5. ERC pass
6. PCB complete
7. DRC pass
8. stackup defined (fab-capable)
9. SI/PI requirements satisfied (analysis, not wishlist)
10. BOM/AVL complete with non-PENDING critical MPNs
11. fabrication outputs generated
12. assembly outputs generated
13. programming/recovery plan complete
14. bring-up plan complete
15. unresolved blockers = 0

## This campaign

**`CPB0_OPEN_READY_FOR_FAB=false`** (allowed).
