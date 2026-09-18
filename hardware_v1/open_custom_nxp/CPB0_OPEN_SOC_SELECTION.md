# CPB0-O SoC / package selection

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Selected OPN (exact)

| Field | Value |
|---|---|
| **Selected part number** | **MIMX9596AVZXN** |
| Device family | MIMX9596 (i.MX 95) |
| Package code | **VZ** — 19 × 19 mm FCBGA, 0.7 mm pitch, no lid (per IMX95IEC nomenclature) |
| Reference EVK proximity | IMX95LPD5EVK-19 (public MCUXpresso SDK documents this OPN on the EVK) |
| Memory class intent | LPDDR5 x32 (19×19 supports up to 6400 MT/s LPDDR5 per IMX95IEC) |
| PCIe | 2× 1-lane PCIe Gen 3.0 (19×19) |
| Ethernet | 2× 1 GbE TSN + 1× 10 GbE TSN (10 GbE on 19×19 / VZ class) |
| USB | 1× USB 3.0 Type-C PHY + 1× USB 2.0 PHY |
| NPU / GPU | Public family features (eTOPS-class NPU; graphics/video cores) — exact SKU feature enablement verified against datasheet Table 2 before fab |
| Thermal envelope | Industrial learning board; heatsink required for high-performance modes; no measured Tj claim |
| Lifecycle | Prefer NXP longevity-backed industrial/commercial grades; confirm OPN status on nxp.com before purchase |

## Selection rationale

1. **Public documentation completeness:** IMX95IEC + IMX95RM + LPD5 EVK getting-started + MCUX board docs are public-class references for this package class.
2. **EVK proximity:** Closest open learning path to IMX95LPD5EVK-19 (SOM + baseboard) without inventing a new memory topology.
3. **Fab learning:** 0.7 mm pitch is more approachable than 15×15 / 0.5 mm VT for CPB0-O first custom attempt.
4. **I/O richness:** Dual PCIe Gen3 x1 + 10 GbE enables NVMe + Wi-Fi M.2 + Ethernet learning without USB4 claims.
5. **No distributor stock invented:** Availability = `VERIFY_AT_PURCHASE` only.

## Known alternatives

| Alternative | When to switch |
|---|---|
| MIMX9596AVTXN (15×15 / VT, LPD4X EVK-15 class) | Prefer smaller form factor / LPDDR4X EVK path; accept single PCIe and no 10 GbE |
| Commercial CVZXN* OPNs from IMX95IEC Table 2 | Need commercial grade / specific feature fuse map |
| Automotive IMX95AEC OPNs | Automotive qualification required (out of CPB0-O scope) |

## Change triggers

- Selected OPN not orderable / wrong feature fuse vs CPB0-O interface matrix
- UG10210 or EVK BOM forces a different package for validated PMIC pairing
- Pinmux impossibility for required interfaces after ball-map extraction
- Thermal solution cannot support chosen frequency bin

## Honesty

- Feature enablement bits must be re-checked against IMX95IEC Table 2 for the exact OPN before schematic freeze.
- No claim that MIMX9596AVZXN is in stock anywhere.
