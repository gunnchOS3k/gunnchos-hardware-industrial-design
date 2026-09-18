# CPB0-O SI / PI plan

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Domain | Pre-layout | Post-layout | Pass claim |
|---|---|---|---|
| DDR | Length/skew rules from UG10210 | HyperLynx/or equiv TBD | **none** |
| PCIe | REFCLK quality, AC couple, loss budget TBD | channel sim TBD | **none** |
| USB | SS mux placement, ESD | eye TBD | **none** |
| Ethernet | magnetics placement | — | **none** |
| MIPI | short flex, common-mode filter TBD | — | **none** |
| PDN | target Z(f) TBD; bulk+mid+HF caps | PI analysis TBD | **none** |
| Decoupling | per datasheet pin groups when ballmap known | — | **none** |
| Return paths | unbroken ref under HS | DRC + visual | **none** |
| Crosstalk | 3W / guided | — | **none** |

IBIS models are account-gated — do not claim SI pass without them.
