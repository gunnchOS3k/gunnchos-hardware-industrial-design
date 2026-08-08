# ICD — Radxa NX5 RM121-D8E32 ↔ Handheld game carrier

Updated: 2026-08-08T19:40:00Z  
Docs: https://dl.radxa.com/nx5/radxa_nx5_product_brief.pdf · https://docs.radxa.com/en/som/nx/nx5

| Group | Direction | Notes | Evidence |
|---|---|---|---|
| 5V DC (max 5.2V) | carrier→SoM | NX5 power input | PUBLIC_DOCS |
| HDMI / eDP / DP+USB3 combo / MIPI DSI | SoM→display path | Game SKU uses eDP or MIPI DSI to 7" panel | PUBLIC_DOCS + MODELED |
| USB3 OTG / Host | SoM↔Type-C / dock | | MODELED |
| PCIe2.0 / SATA mux notes | SoM→optional WWAN or storage | Follow Radxa pinout mux | PUBLIC_DOCS |
| SDMMC | SoM↔µSD | | PUBLIC_DOCS |
| I2C/SPI/UART/GPIO/PWM | SoM↔HID MCU, sticks, SE | | MODELED |
| Gigabit Ethernet PHY on SoM | optional unused in handheld | | PUBLIC_DOCS |

Connector: **260-pin SODIMM**. No bare RK3588S BGA. Lifecycle: brief availability ≥ Sep 2033.
