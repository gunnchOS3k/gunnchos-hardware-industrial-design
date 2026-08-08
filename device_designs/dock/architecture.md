# Dock architecture

Updated: 2026-08-08T01:15:00Z

```
[AC PD adapter ≤100W]
        │
        ▼
[TPS65994 PD] ←→ upstream USB-C to Student/DS-XL/Handheld
        │
        ├─ JHL9040 USB4/TBT dock controller (Student/DS-XL path)
        │     or VL108 USB3+DP cost-down (Handheld-first SKU)
        ├─ VL817 USB hub → USB-A ×2 + downstream USB-C ×2
        ├─ RTL8156 2.5GbE
        ├─ HDMI 2.1 / DP 1.4 egress (via dock controller)
        ├─ TPS55288 VBUS buck-boost + TPS62864 5V + TLV75533 3V3
        └─ Ring cradle: CHARGE_5V/GND pogo + optional DWM3001C UWB companion
```
