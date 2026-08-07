# Interface / Voltage Domain Check

Generated: 2026-08-07T22:20:56Z

| Interface | Domain | Compatible? | Notes |
|---|---|---|---|
| SWD | 3V3 | YES | Vtref from 3V3; ESD D2 on SWDIO |
| I2C | 3V3 | YES | BMI270 + DRV2605L on 3V3; 10k pull-ups |
| RF | AC / 50Ω | YES | Match network seed values; tune after enclosure |
| CHARGE_5V | 5V | YES | Isolated to charger IN + ESD; not on GPIO |
| VBAT → SoC | 1.7–3.6 | YES | nRF52840 VDD accepts LiPo range |
| Haptic drive | driver out | YES | Not connected to GPIO rails |

**Pin conflict check:** I2C pins P0.26/P0.27 dedicated; IMU_INT on P0.11; CHG on P0.02; SWD dedicated; no dual-use conflicts in netlist.
