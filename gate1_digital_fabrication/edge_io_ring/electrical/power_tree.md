# Edge I/O Ring — Power Tree (digital)

Generated: 2026-08-07T22:20:56Z
Board: `edge_io_ring_evt0` v0.1.0-dev

```
[J2 CHARGE_5V pogo]──ESD D1──►[U4 BQ25100]──► VBAT ──►[U5 protect]──► VBAT_SYS
     │                              │                      │
     └──────── GND ─────────────────┴──────────────────────┤
                                                           ▼
                                                    [U6 TLV70033]──► 3V3
                                                           │
             ┌─────────────┬──────────────┬────────────────┤
             ▼             ▼              ▼                ▼
           [U1 SoC]     [U2 BMI270]   [U3 DRV2605L]     pull-ups/SWD
             │
          RF path → match → ANT1
```

| Rail | Nom | Source | Loads | Notes |
|---|---|---|---|---|
| CHARGE_5V | 5.0 V | Cradle pogo | U4 IN | Present only when docked |
| VBAT | 3.0–4.2 V | Cell | U4 BAT, U6 IN | After PCM |
| VBAT_SYS | ≈VBAT | U5 OUT | U1 VDD/VDDH | Direct SoC supply allowed |
| 3V3 | 3.3 V | U6 | IMU, haptic, IO pull-ups | Always-on when VBAT present |

Voltage domain checks: SWD/I2C at 3V3; RF path AC-coupled/passive; CHARGE_5V never routed to 3V3 IO.
