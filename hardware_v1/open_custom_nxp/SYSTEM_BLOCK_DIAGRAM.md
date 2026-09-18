# System block diagram (architecture)

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


```
[USB-C PD / DC-in] -> [PMIC tree] -> [i.MX95]
                         |              |-- LPDDR
                         |              |-- eMMC / NVMe (SKU option)
                         |              |-- Wi-Fi/BT M.2 or SDIO module
                         |              |-- Ethernet PHY
                         |              |-- Display (MIPI/LVDS/eDP class per public mux)
                         |              |-- Camera CSI
                         |              |-- PCIe slot/endpoint (SKU-dependent)
                         |              |-- USB host/device
[EC / supervisory MCU] <- SMBus/UART/GPIO -> [i.MX95]
[Debug] SWD/JTAG + UART console + USB gadget recovery
```
Not a netlist. Interfaces pending public RM / design-guide confirmation.

