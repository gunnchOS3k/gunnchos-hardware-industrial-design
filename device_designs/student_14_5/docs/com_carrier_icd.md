# ICD — ADLINK COM-HPC-mMTL-155H-32G ↔ Student carrier

Updated: 2026-08-08T19:40:00Z  
Module docs: https://docs.ipi.wiki/com-hpc/mini-type-meteor-lake/ModuleIntroduction.html

| Group | Direction | Notes | Evidence |
|---|---|---|---|
| VIN 8–20V / AT 12V±5% | carrier→COM | Single-rail per ADLINK COM-HPC-mMTL power section | PUBLIC_DOCS + MODELED carrier |
| eDP 1.4b | COM→panel | 14.5" panel | MODELED |
| USB4 (up to 3 muxed w/ DDI) | COM↔dock Type-C | Custom BIOS/re-timer/PD may be project support | PUBLIC_DOCS note |
| PCIe Gen4 lanes | COM→NVMe / WWAN | Up to 16 lanes total; mux notes in wiki | PUBLIC_DOCS |
| CNVi / PCIe Wi-Fi | COM→BE200 Key E | | MODELED |
| Ethernet I226 | COM→optional / unused in laptop SKU | Available on module | PUBLIC_DOCS |
| LPC/eSPI + I2C | COM↔EC | Keyboard, bat, thermals | MODELED |
| HDA/I2S | COM↔codec on carrier | Realtek on carrier per ADLINK note | PUBLIC_DOCS |
| MIPI CSI | COM←camera FPC | 2× on-module FFC option | PUBLIC_DOCS |
| SEMA / fan | COM↔thermal | ADLINK SEMA board controller | PUBLIC_DOCS |

Connector: COM-HPC Mini 400-pin. Exact mating connector MPN from ADLINK carrier design guide (**NARROW_NDA** — PICMG/ADLINK). **Purchase frozen.**

Continuation V: full pin-by-pin netlist is **not** PUBLIC_DOCS. Carrier schematics must not invent pin numbers. See `docs/full_product_family/COM_HPC_NX5_FEASIBILITY_PINOUT.md`.
