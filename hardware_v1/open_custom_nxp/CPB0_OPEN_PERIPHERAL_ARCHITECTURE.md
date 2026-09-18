# CPB0-O peripheral architecture (schematic-level candidates)

**Generated:** 2026-09-18T19:17:34Z  
**Claim boundary:** architecture / public-collateral digital EDA only — not physical pass, not certification, not fab order, not purchased, not NDA, not GXE execution, not software RC1 change.

| Block | Interface | Voltage | Reset/clock/power | MPN class | DNP | Source |
|---|---|---|---|---|---|---|
| Boot flash | FlexSPI / Octal SPI NOR | 1.8 | SoC XSPI + POR | 1Gb NOR class (EVK) | no | EVK QSG |
| Debug UART | LPUART | 1.8/3.3 | — | USB-UART bridge class | no | bring-up |
| JTAG | dedicated debug | NVCC_CCM_DAP | — | 10/20-pin header | no | IMX95IEC |
| Board ID EEPROM | I2C | 1.8/3.3 | — | 2kb EEPROM class | no | DFT |
| EC | SWD/UART/I2C | 3.3 | EC_RESET | open Zephyr MCU class | no | CPB0_OPEN_EC |
| NVMe | PCIe1 x1 M.2 M-key | 3.3 | PERST/CLKREQ | M.2 connector | no | arch |
| Wi-Fi | PCIe2 x1 M.2 E-key | 3.3 | — | M.2 E-key | no | EVK-like |
| Cellular | USB/PCIe M.2 B-key | 3.3 | — | M.2 B-key | **yes default** | optional |
| GbE | ENET RGMII + PHY | 1.8/3.3 | PHY_RST | 1G PHY class | no | arch |
| 10GbE | 10G TSN MAC pins | PHY-dependent | — | module/PHY TBD | optional | 19×19 feature |
| USB-C | USB1 SS+USB2 | USB rails | CC controller class | USB-C + ESD | no | arch |
| Display | MIPI-DSI / LVDS | MIPI/LVDS rails | — | FPC connector class | no | media |
| Camera | MIPI-CSI | MIPI | — | FPC | no | media |
| Audio | SAI + codec | 1.8/3.3 | — | codec class | no | media |
| Fan | PWM/TACH header | 12/5 | EC | header | no | thermal |
| Thermal sense | I2C TMP class | 1.8/3.3 | — | TMP117-class | no | bring-up |
| Status LEDs | GPIO | 1.8/3.3 | — | LED | no | DFT |
| Recovery btn | POR/ONOFF | BBSM | — | tactile | no | IMX95IEC |
| Test | TP + tags | — | — | — | no | DFT |
