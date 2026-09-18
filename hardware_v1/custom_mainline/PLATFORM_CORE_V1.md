# gunnchOS Platform Core v1

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Definition

**gunnchOS Platform Core v1** is the custom motherboard platform family built around AMD embedded x86 SoCs.

## Primary silicon family

`AMD Ryzen Embedded 8000 Series — FP7r2 BGA`

### Why this family (decision rationale)

- x86 compatibility with Windows/Linux ecosystem
- integrated RDNA 3 graphics
- integrated NPU (public product-brief class)
- up to four displays (vendor-confirmed topology required before freeze)
- USB4
- PCIe Gen4
- DDR5 with ECC capability (topology pending vendor rules)
- BGA package suitable for custom boards
- low-to-mid power envelopes suitable for portable devices
- embedded lifecycle / longevity positioning

### Explicit non-claims

- Pin compatibility among SKUs is **NOT assumed** until AMD design collateral proves it.
- No net-accurate pinout, ball map, power sequencing, or DDR rules are present in this repo.
- Platform Core v1 is architecture doctrine + learning/EVT plan, not fab release.

### Product boards sharing Platform Core blocks

| Board | Role |
|---|---|
| `Student-MB-v1` | Student 14.5 production-intent mainboard |
| `Handheld-MB-v1` | Handheld Hybrid production-intent mainboard |
| `DSXL-MB-v1` | DS-XL Coder production-intent mainboard |
| `CPB0` | Custom Platform Board 0 — debug-friendly learning/reference board |

Replaces previous product mainline label: `COM-HPC Mini x86` (now REFERENCE_CONTROL only).
