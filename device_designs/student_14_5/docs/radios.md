# Student 14.5 radios

Updated: 2026-08-08T19:40:00Z

| Radio | Exact MPN | Band | Driver class | Notes |
|---|---|---|---|---|
| Wi-Fi 7 + BT | Intel BE200 | 2.4/5/6 GHz | BINARY_BLOB+UPSTREAM | M.2 Key E |
| WWAN | Quectel **RM520N-GL** | 5G NR Sub-6 + LTE | OPEN_VENDOR+BINARY_BLOB | **Not 6G**; **no NTN** (public verify) |
| GNSS | modem-integrated | L1 multi-constellation option | via modem | optional enable |
| BLE ring peer | host BT | 2.4 | via BE200 | pairs Edge I/O Rings |

RF model: `electrical/rf_model.yaml` (MODELED — not chamber MEASURED).
