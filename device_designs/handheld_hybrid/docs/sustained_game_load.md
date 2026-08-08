# Sustained game load — Handheld Hybrid

Updated: 2026-08-08T01:15:00Z  
Evidence: MODELED

## Target workload
Godot/Vulkan or similar mid-tier 3D at 1080p60–120 on device display for **≥30 minutes** without thermal trip that drops below playable fps floor.

## Power model (MODELED)
| State | Power W | Notes |
|---|---|---|
| Home UI idle | 2.5 | radios on |
| 2D study | 4.0 | |
| Sustained 3D game | 8.5–12.0 | GPU+CPU balanced; fan/heatpipe as designed |
| Peak burst | 15.0 | ≤60 s PL2-like |

## Thermal model (MODELED)
| Metric | Value |
|---|---|
| Skin max sustained | 42 °C target / 45 °C hard |
| SoC throttle onset | ~85–90 °C (vendor DVFS) |
| Cooling | graphite + heatpipe + optional tiny blower |
| Ambient assumption | 25 °C |

## Battery (MODELED)
- 2S or 1S2P Li-ion **5000–6000 mAh** (~19–23 Wh class depending topology)
- Sustained game life target: **≥1.5 h** at 10 W average (MODELED)
- Gauge: BQ27z273 or Maxim class; charger: BQ25792 or single-cell BQ25895 class per pack topology

## Performance floor (software contract)
- fps_floor_playable: 30
- fps_target: 60
- resolution: 1920×1080
- Not claimed MEASURED until device lab

## Dock continuity
On dock: display may move to external; thermal headroom increases; USB3+DP path (not USB4 80G claim).
