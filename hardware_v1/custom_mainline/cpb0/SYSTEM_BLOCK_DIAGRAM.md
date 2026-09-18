# CPB0 system block diagram (logical)

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


```
                 +---------------------------+
 Bench PSU / Batt Emulator ----> | Power tree / VRM / PD    |
                 +-------------+-------------+
                               |
                 +-------------v-------------+
                 | AMD Ryzen Emb. 8845HS BGA |
                 | Platform Core SoC         |
                 +--+----+----+----+----+----+
                    |    |    |    |    |
                 DDR5  PCIe USB4 Display Debug
                    |    |    |    |    |
                 SODIMM NVMe USB-C eDP/DDI UART/JTAG
                 /solder Wi-Fi Dock DP    EC / TPM / SPI
                         (opt 5G)
```

Logical only — not a netlist. Pin/rail names require AMD collateral.
