# Driver classification — five-product family

Updated: 2026-08-08T01:15:00Z

Classes: `UPSTREAM` | `OPEN_VENDOR` | `BINARY_BLOB` | `NDA_ONLY` | `UNAVAILABLE`

## Student 14.5 / DS-XL (Intel Core Ultra 7 155H class via COM)
| Subsystem | MPN / class | Classification | Notes |
|---|---|---|---|
| CPU/iGPU/NPU | Ultra 7 155H on COM | `BINARY_BLOB` + `UPSTREAM` mix | i915/xe + firmware blobs (`linux-firmware`); NPU via intel_vpu + FW |
| ME/CSE/CSME | on-module | `BINARY_BLOB` | Required for bring-up; no open replacement |
| Wi-Fi/BT | Intel BE200 | `BINARY_BLOB` + `UPSTREAM` | iwlwifi + FW |
| WWAN | Quectel RM520N-GL | `OPEN_VENDOR` + `BINARY_BLOB` | MBIM/QMI open userspace; modem FW blob |
| eSIM/eUICC | GSMA SGP.22 path | `OPEN_VENDOR` / `NDA_ONLY` carrier profiles | No compliance claim |
| TPM | SLB9672 | `UPSTREAM` | tpm_tis_spi |
| USB4 | JHL9040 / on-COM USB4 | `UPSTREAM` + `BINARY_BLOB` FW | thunderbolt stack |
| Audio codec | ALC256/ALC245 class | `UPSTREAM` | SOF/HDA |
| EC | ITE/NPCX class on carrier | `OPEN_VENDOR` / `UPSTREAM` | ChromeEC or vendor EC FW |
| Touch | panel controller OEM | `BINARY_BLOB` or `OPEN_VENDOR` | HID |
| Webcam ISP | MIPI → on-COM | `BINARY_BLOB` common | libcamera path preferred |

## Handheld Hybrid (RK3588S SoM)
| Subsystem | MPN / class | Classification | Notes |
|---|---|---|---|
| CPU/GPU/NPU | RK3588S | `OPEN_VENDOR` + `BINARY_BLOB` | Vendor kernel trees common; Mali blob; NPU vendor SDK |
| Wi-Fi/BT | AP6275P / AIC8800D | `BINARY_BLOB` / `OPEN_VENDOR` | Module-dependent |
| WWAN optional | RM520N-GL | same as Student | Thermal may force Wi-Fi-first SKU |
| GPU Vulkan | Mali-G610 | `BINARY_BLOB` | Panfrost improving but not sole claim |
| Gamepad MCU | STM32/nRF class | `UPSTREAM` | HID |

## Edge I/O Rings
| Subsystem | MPN | Classification | Notes |
|---|---|---|---|
| BLE MCU | nRF52840 | `UPSTREAM` | Zephyr/NCS |
| SoftDevice/controller | Nordic | `BINARY_BLOB` (if SoftDevice) / `UPSTREAM` (Zephyr controller) | Prefer Zephyr open controller |
| IMU | BMI270 | `UPSTREAM` | IIO |
| Cap | IQS7222A | `OPEN_VENDOR` | Azoteq host lib; may need vendor notes |
| UWB | DWM3001C | `OPEN_VENDOR` + `BINARY_BLOB` | Qorvo UWB stack portions |
| BHI360 | BHI360 | `OPEN_VENDOR` | Bosch BSX / SH2 |
| SE | SE050 | `OPEN_VENDOR` | Plug & Trust middleware |

## Dock
| Subsystem | MPN | Classification | Notes |
|---|---|---|---|
| USB4 | JHL9040 | `BINARY_BLOB` + `UPSTREAM` host | Dock side mostly firmware-less silicon; host drivers matter |
| PD | TPS65994 | `OPEN_VENDOR` | TI config tools; runtime mostly HW |
| Ethernet | RTL8156 | `UPSTREAM` | r8152 |
| USB hub | VL817 | n/a silicon | Host xHCI |
| UWB companion | DWM3001C | same as ring | ADR-FP-008 escape |

## Unavailable / rejected claims
- Open-source Ultra 7 ME replacement: `UNAVAILABLE`
- Fully open Mali-free game path as sole handheld GPU: `UNAVAILABLE` as sole strategy (Panfrost tracked as stretch)
- 6G modem driver stack: `UNAVAILABLE` — not in architecture
