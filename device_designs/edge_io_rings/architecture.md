# Edge I/O Rings architecture (fusion)

nRF52840 primary BLE/auth/DFU MCU — **insufficient alone** (ADR-FP-008).

Modalities:
- BMI270 IMU (required)
- IQS7222A capacitive (required footprint)
- DWM3001C UWB (footprint; DNP → UWB_ON_COMPANION on dock)
- BMM350 mag optional
- BHI360 sensor-hub optional
- SE050 identity

Fusion policy: ≥2 modalities before action dispatch.
