# Handheld Hybrid architecture

Updated: 2026-08-08T01:15:00Z

```
[RK3588S SoM — 4×A76+4×A55, Mali-G610 MP4, 16GB LPDDR4x, UFS on-SoM or carrier]
        │ board-to-board / SODIMM
        ▼
[Game carrier]
  • 7" 1920×1080 120 Hz IPS + touch
  • Dual sticks + ABXY + L/R + triggers + D-pad (HID MCU)
  • Wi-Fi 6E/BT module (AP6275P / AIC8800D class)
  • Optional M.2 WWAN (thermal-gated; default Wi-Fi-first)
  • USB-C: USB 3.2 Gen1 + DP Alt + PD ↔ Dock (VL108 cost-down path OK)
  • Battery 5000–6000 mAh + protection + fuel gauge
  • Active vapor/heat-spreader path for sustained GPU
```

No bare RK3588S BGA fanout invented without Rockchip PDK.
