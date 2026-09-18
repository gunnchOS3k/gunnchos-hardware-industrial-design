# i.MX95 platform profile (public-class)

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Silicon family

NXP **i.MX 95** applications processor family (public product page: https://www.nxp.com/products/i.MX95).

## Public-class characteristics (architecture intent only)

- Heterogeneous AP + real-time / safety domains (see public RM / datasheet)
- LPDDR memory class (exact topology pending design-guide rules)
- High-speed SerDes / PCIe / USB / Ethernet class interfaces (SKU-dependent)
- Display / camera pipeline suitable for embedded UI + vision learning boards
- EdgeLock / secure-enclave class security features (public docs)
- Industrial / commercial / automotive grade variants exist — selection PENDING_OWNER_DECISION

## Role vs PRODUCT_MAINLINE

| Aspect | OPEN_ENGINEERING (i.MX95) | PRODUCT_MAINLINE (AMD x86) |
|---|---|---|
| Primary goal | Board ownership + fab learning | Product performance + x86 compat |
| NDA dependency | Prefer public path | AMD custom collateral often gated |
| Windows / games | Not a target claim | Explicit target |
| USB4 | Not assumed | Product Dock / platform intent |

## Non-claims

- No pin-accurate ball map invented here
- No fabricated power-sequence numbers
- No “product mainline replacement” claim
