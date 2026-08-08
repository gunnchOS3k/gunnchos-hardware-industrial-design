# ICD — Radxa NX5 RM121-D8E32 ↔ Handheld game carrier (Continuation VI)

Updated: 2026-08-08T20:58:59Z  
Docs: https://dl.radxa.com/nx5/radxa_nx5_product_brief.pdf · pinout xlsx in-repo evidence  
Evidence rule: **PUBLIC_PINOUT** nets only — no invented remux.

| Group | Direction | SoM pins (public) | Notes | Evidence |
|---|---|---|---|---|
| Power 5V | carrier→SoM | VCC_SYSIN **251–260** | Max 5.2V; brief Vin | PUBLIC_PINOUT + PUBLIC_DOCS |
| GND | — | multiple GND pins (e.g. 1,2,7,8,…) | Return path | PUBLIC_PINOUT |
| Display | SoM→panel | HDMI0/eDP lanes **63,65,69,71,75,77,81,83** and/or MIPI DPHY TX **70,72,76,78,82,84,90,92**; BL PWM **220**; LCD_RESET **126** | Game SKU panel path | PUBLIC_PINOUT |
| USB2 | SoM↔ports | USB20_HOST0_DM **109**, HOST1_DM **121** | Host ports | PUBLIC_PINOUT |
| USB3 SS | SoM↔Type-C | USB30_2_SS* **167,169,172,174** (mux w/ PCIe/SATA) | Follow Func columns | PUBLIC_PINOUT |
| Controls / HID | SoM↔STM32 | I2C0_M2 **185/187**; sticks/buttons on HID MCU | HID USB to SoM host | PUBLIC_PINOUT + MODELED |
| WWAN opt | SoM→M.2 | PCIe2.0 **131,133,134,136** + refclk **160,162** | DNP OK; RM520N-GL; not 6G/NTN | PUBLIC_PINOUT |
| Audio | SoM↔codec | I2S0 **193,195,197,199,212** | | PUBLIC_PINOUT |
| Storage | SoM↔µSD | SDMMC **88,208,219,221,223,225,227,229** | eMMC on-module | PUBLIC_PINOUT |
| Debug | SoM→header | UART2 **236/238** | | PUBLIC_PINOUT |

Connector: **260-pin SODIMM**. Full table: `docs/radxa_nx5_public_pinout_table.csv`.  
No bare RK3588S BGA. COM-HPC NDA **does not block** this product.

## Token
`HANDHELD_PUBLIC_PINOUT_EDA_COMPLETE`
