# Edge I/O Rings — sensing → action map (HW-FW-RC-001)

Machine-readable twin: `artifacts/hw_fw_rc_001/RING_SENSING_MAP.json`

## Required modalities
- IMU: BMI270
- Capacitive / proximity: IQS7222A
- Secure identity: SE050
- BLE MCU: nRF52840
- PMIC: nPM1300

## Optional
- UWB: DW3000 / DWM3001C
- Sensor hub: BHI360
- Mag: BMM350

## Fusion policy
≥2 modalities before action dispatch (ADR-FP-008). **IMU-only absolute position is rejected.**

## Action mapping
| Action | Primary | Gate |
|---|---|---|
| pointer | IMU delta + CAP hover | confidence |
| click | CAP touch / IMU tap | confidence |
| text | CAP gesture | SE auth optional |
| delete | CAP hold | confidence **required** |
| shortcut | CAP multi + BLE HID | confidence |
| gaming | IMU rate + CAP trigger | confidence |

## Non-claims
Spatial accuracy = `PHYSICAL_PENDING`. No physical tracking PASS.
