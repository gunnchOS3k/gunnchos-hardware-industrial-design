# Custom mainline complexity register

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


No dollar estimates without sourced quotes.

| Area | Complexity | Likely failure | Mitigation | Expertise | Tooling | External dependency | Validation stage |
|---|---|---|---|---|---|---|---|
| BGA SoC escape | high | open/short, SI | fanout rules + review | PCB layout | CAD + microscope | AMD package data | EVT |
| DDR routing | high | training fail | length match + sim | SI eng | SI tools | AMD DDR rules | EVT |
| high-current power | high | brownout | sense + margin | power eng | electronic load | VRM docs | EVT |
| VRM tuning | high | instability | vendor design guide | power eng | scope | AMD VRM req | EVT |
| boot firmware | high | no-POST | IBV path + serial | FW eng | SPI programmer | AGESA/IBV | EVT |
| SI/PI | high | eye collapse | sim + measurement | SI eng | VNA/scope | vendor constraints | DVT |
| USB4 | high | link fail | retimer strategy | SI/FW | USB4 analyzer | AMD+USB-IF | EVT |
| display | high | no image | eDP+DDI bring-up | display eng | panel fixture | AMD display guide | EVT |
| EMI | high | fail pre-scan | filter/stackup | EMC eng | chamber | lab | DVT |
| thermal | high | throttle | chamber + skin | thermal eng | TC/IR | heatsink fab | EVT |
| bring-up | high | stuck rail | CPB0 instrumentation | systems | bench | debug tools | EVT |
| debug | high | blind failure | headers/LEDs | systems | JTAG/UART | vendor tools | EVT |
| manufacturing | high | yield loss | DFT/fixtures | NPI | ICT/FCT | CM | PVT |
| BIOS/IBV | high | enablement gap | engage IBV early | FW | build env | IBV | EVT |
| board spins | high | schedule slip | CPB0 first | PM | fab house | CM | EVT |
