# CPB0-O PCIe / USB / network architecture

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Lane / port allocation (19×19 MIMX9596AVZXN class)

| Resource | Assignment | Notes |
|---|---|---|
| PCIe0 Gen3 x1 | M.2 M-key NVMe | REFCLK + PERST# + CLKREQ# + 3V3 enable |
| PCIe1 Gen3 x1 | M.2 E-key Wi-Fi/BT | same clocking discipline |
| Optional M.2 B-key 5G | USB3 or PCIe mux TBD; SIM + WWAN disables | antenna **unvalidated**; product-specific |
| USB3 Type-C PHY | USB-C connector via mux/PD controller | **No USB4** |
| USB2 PHY | shared on Type-C or debug hub | |
| ENET 1G #0/#1 | onboard PHY + magnetics | TSN silicon capability ≠ product claim |
| ENET 10G | optional / DNP footprint | 19×19 only |

## Common requirements

- AC coupling / ESD on SerDes and USB.
- Hot-plug: NVMe treated as boot-time present for EVT; no surprise-hotplug claim.
- Power enables gated by EC after SoC PG.
- SIM interface only if 5G option stuffed — keep DNP by default.

## Non-claims

- No USB4/TBT.
- No antenna certification.
- No fabricated insertion-loss budgets until SI plan runs.
