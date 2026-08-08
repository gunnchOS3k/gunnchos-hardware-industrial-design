# ICD — Student COM ↔ carrier

Updated: 2026-08-08T01:15:00Z

| Group | Direction | Notes | Evidence |
|---|---|---|---|
| COM_VIN / VCC_RTC | carrier→COM | Carrier supplies module input rails per COM design guide | MODELED |
| eDP0 | COM→panel | 14.5" eDP 1.4/1.5 | MODELED |
| USB4/TBT | COM↔dock Type-C | 40 Gbps class; no 80G claim | MODELED |
| PCIe M.2 | COM→NVMe / WWAN | NVMe ×4; WWAN per module | MODELED |
| CNVi / PCIe Wi-Fi | COM→BE200 | Key E | MODELED |
| LPC/eSPI + I2C | COM↔EC | Keyboard, bat, thermals | MODELED |
| HDA/I2S | COM↔codec | ALC256 class | MODELED |
| MIPI CSI | COM←camera FPC | Dual cam candidate | MODELED |

Connector: vendor COM-HPC Client Mini (exact pinout from purchased module datasheet — **AVL quote pending**, purchase frozen).
