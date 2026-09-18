# NXP → AMD product-mainline transfer map

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



| Subsystem | Directly transferable | Conceptually transferable | Vendor-specific / nontransferable | Revalidation required |
|---|---|---|---|---|
| BGA escape | Via strategies, dogbone lessons | Escape budgeting | Ballmap, pitch, HDI rules | Yes — AMD package |
| DDR | Length matching discipline, DFT | Topology decision process | LPDDR5 vs DDR5/LPDDR on AMD | Yes |
| PDN | Sense points, sequencing mindset | Rail partitioning | Rail names, PMIC | Yes |
| PCIe | REFCLK/PERST hygiene, M.2 | Lane budgeting | Controllers, retimers | Yes |
| USB | ESD, Type-C basics | Type-C policy | USB4/TBT on AMD product | Yes |
| Display | MIPI bring-up habits | Panel power seq | eDP/USB4 display paths | Yes |
| Camera | CSI debug hooks | ISP pipeline differences | Vendor ISP | Yes |
| Audio | Codec bring-up | — | HDA vs SAI | Yes |
| EC | Zephyr EC architecture, PG/fan/board-ID | **High transfer** | MCU choice, host interface | Partial |
| Boot | Recovery/debug culture | A/B mindset | x86 UEFI vs i.MX ROM/U-Boot | Yes |
| Security | Lifecycle discipline | Secure boot concepts | EdgeLock vs AMD PSP/fTPM | Yes |
| Thermal | Sensor/fan loop | Skin temp budgets | TDP envelope | Yes |
| Manufacturing | DFT, fixture mindset | — | Different ICT nets | Yes |
| Bring-up | Scripted rail checks | — | Different tools | Yes |

NXP open-custom remains **non-equivalent** to AMD PRODUCT_MAINLINE.
