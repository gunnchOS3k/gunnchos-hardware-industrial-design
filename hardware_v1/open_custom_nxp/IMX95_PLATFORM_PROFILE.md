# i.MX95 platform profile (public-class)


**Generated:** 2026-09-18T18:55:43Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.

## Silicon selection (CPB0-O)

**MIMX9596AVZXN** — 19×19 mm FCBGA (VZ), public EVK proximity IMX95LPD5EVK-19.

## Public-class characteristics

- Heterogeneous AP + real-time / safety domains (IMX95IEC / IMX95RM)
- LPDDR5 x32 class on 19×19 (up to 6400 MT/s per IMX95IEC)
- 2× PCIe Gen3 x1, USB3 Type-C + USB2, 2×1GbE + 10GbE (19×19)
- Display/camera MIPI class; EdgeLock Secure Enclave (Advanced Profile) public description
- Industrial/commercial/automotive grades exist — CPB0-O uses documented EVK OPN pending Table-2 fuse verify

## Role vs PRODUCT_MAINLINE

| Aspect | OPEN_ENGINEERING (i.MX95) | PRODUCT_MAINLINE (AMD x86) |
|---|---|---|
| Primary goal | Board ownership + fab learning | Product performance + x86 compat |
| NDA dependency | Prefer public path | AMD custom collateral often gated |
| Windows / games | Not a target claim | Explicit target |
| USB4 | Not assumed | Product Dock / platform intent |

## Non-claims

- No pin-accurate ball map completed in NXP-0
- No fabricated power-sequence currents
- No product-mainline replacement claim
