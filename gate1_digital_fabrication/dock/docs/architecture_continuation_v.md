# Dock architecture

Updated: 2026-08-08T20:15:00Z  
Freeze: **USB4 / Thunderbolt 4 @ 40 Gbps** (ADR-HW-002) — **not Thunderbolt 5**

```
[AC PD adapter ≤100W]
        │
        ▼
[TPS65994 PD] ←→ upstream USB-C to Student/DS-XL/Handheld
        │
        ├─ JHL8440 USB4/TB4 dock controller (Student/DS-XL path)  ← corrected
        │     + JHL9040R TB4 retimer for SI (NOT the controller)
        │     or VL108 USB3+DP cost-down (Handheld-first SKU)
        ├─ VL817 USB hub → USB-A ×2 + downstream USB-C ×2
        ├─ RTL8156 2.5GbE
        ├─ HDMI 2.1 / DP 1.4 egress (via dock controller)
        ├─ TPS55288 VBUS buck-boost + TPS62864 5V + TLV75533 3V3
        └─ Ring cradle: CHARGE_5V/GND pogo + optional DWM3001C UWB companion
```

## Forbidden
- JHL9480 / JHL9580 (Thunderbolt **5**)
- Labeling JHL9040R as Maple Ridge / dock controller
- 80 Gbps / TB5 marketing claims
