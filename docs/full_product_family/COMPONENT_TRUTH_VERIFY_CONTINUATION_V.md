# Component truth verification — Continuation V

Updated: 2026-08-08T20:15:00Z  
Branch: `cursor/full-product-continuation-v-hardware-release`  
Base: `origin/main` @ `7e1658e63052e7baa2e9f4ab58113a91e4165c72` (#47)  
PHYSICAL_EXECUTION_FREEZE ACTIVE — verification only; no fab / purchase.

Independent re-check of compute + dock silicon against **public vendor pages** (not prior PR text alone).

## 1. ADLINK COM-HPC-mMTL-155H-32G — VERIFIED

| Field | Public evidence |
|---|---|
| Orderable MPN | **COM-HPC-mMTL-155H-32G** listed on ADLINK iPi wiki Ordering Information |
| CPU | Intel Core Ultra 7 **155H** (Meteor Lake-H), 28W class |
| Memory | **32GB** LPDDR5x soldered (module SKU); family up to 64GB |
| Form factor | PICMG COM-HPC Mini, **95 × 70 mm** |
| Power | AT 12V±5%; Vin **8–20V** single rail |
| USB4 | Up to **3× USB4** (muxed with DDI / USB3 port 2); project BIOS/re-timer/PD notes |
| Source | https://docs.ipi.wiki/com-hpc/mini-type-meteor-lake/ModuleIntroduction.html |
| Evidence class | **PUBLIC_VENDOR_DOCS** |

**Not invented:** bare Ultra 7 BGA ball map. Carrier uses COM-HPC Mini connector only.

## 2. Radxa NX5 RM121-D8E32 — VERIFIED

| Field | Public evidence |
|---|---|
| Orderable MPN | **RM121-D8E32** in NX5 product brief Rev 1.1 SKU table |
| SoC | Rockchip **RK3588S** |
| Memory/storage | **8GB** LPDDR4X + **32GB** eMMC |
| Connector | **260-pin** SODIMM golden finger, 70 × 45 mm |
| Power | **5V DC**, max 5.2V |
| Lifecycle | Availability stated until **≥ September 2033** |
| Pinout | Public XLSX: https://dl.radxa.com/nx5/radxa_nx5_260_pinout_v1100.xlsx (+ v1.1) |
| Schematic | Public PDF: https://dl.radxa.com/nx5/radxa_nx5_schematic_v1100.pdf |
| Source brief | https://dl.radxa.com/nx5/radxa_nx5_product_brief.pdf |
| Evidence class | **PUBLIC_VENDOR_DOCS** |

**Honesty:** brief does **not** list a 16GB RAM SKU row; do not freeze distributor “16GB NX5” marketing as orderable.

## 3. Intel JHL9040 vs Thunderbolt 5 — CORRECTED

| MPN | Intel product class | Generation | Role |
|---|---|---|---|
| **JHL9040R** | Thunderbolt **4 Retimer** (Hayden Bridge) | TB4 / USB4 **40 Gbps** | Signal re-timer — **not** a dock controller |
| **JHL8440** | Thunderbolt **4** peripheral/device controller (Goshen Ridge) | TB4 / USB4 **40 Gbps** | Typical **dock/hub** controller |
| **JHL8540** | Thunderbolt **4** host controller (Maple Ridge) | TB4 / USB4 **40 Gbps** | Host/PC side — not dock primary |
| **JHL9480** | Thunderbolt **5** accessory controller (Barlow Ridge) | **TB5** | Out of normative dock scope |
| **JHL9580** | Thunderbolt **5** controller (Barlow Ridge) | **TB5** | Out of normative dock scope |

Sources (public Intel ARK / product pages):
- JHL9040R: https://www.intel.com/content/www/us/en/products/sku/211299/intel-jhl9040r-thunderbolt-4-retimer/specifications.html
- JHL8540 (Maple Ridge): Intel ARK Thunderbolt 4 Controllers
- JHL8440 (Goshen Ridge): Intel ARK — peripheral Thunderbolt/USB4 support @ 40G
- JHL9480 / JHL9580: Intel Thunderbolt **5** Controllers (Barlow Ridge)

### Prior labeling defect (PR #47 era)
`JHL9040` was described as “Maple Ridge class USB4 controller.” That is **incorrect**:
- Maple Ridge ≠ Hayden Bridge
- JHL9040R is a **retimer**, not the dock protocol controller

Continuation V **corrects** this without shifting scope to TB5.

## Normative dock bandwidth (field-kit ADR-FP-001 / ADR-FP-006)
- Student/DS-XL: **USB4 40 Gbps** Type-C path
- Explicit non-claim: **no 80 Gbps / TB5** unless silicon + ADR amendment
- Handheld dock path may cost-down to USB3 + DP Alt (VL108 class)

→ See `DOCK_ARCHITECTURE_FREEZE_USB4_TB4.md` and `docs/adr/ADR-HW-002-dock-usb4-tb4-not-tb5.md`.
