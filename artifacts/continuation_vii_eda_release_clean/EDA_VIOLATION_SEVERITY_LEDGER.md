# EDA Violation Severity Ledger — Continuation VII

Updated: 2026-08-09T17:16:18Z  
Branch: `cursor/full-product-continuation-vii-eda-release-clean`  
Base: `bed14ca7530ce11379d0173d1eff056df2e00d19` (#49)

Allowed outcomes only: `FIXED` | `FORMALLY_WAIVED_WARNING` | `EXTERNAL_NDA_BLOCKED`.

| board | check | rule_id | severity | object/net | status | digitally_fixable | fix |
|---|---|---|---|---|---|---|---|
| student_14_5 | ERC | label_dangling | error | Global Label 'VSYS' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | label_dangling | error | Global Label 'COM_VIN' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | label_dangling | error | Global Label 'VDD_3V3' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | label_dangling | error | Global Label 'VBUS_PD' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | label_dangling | error | Global Label 'eDP0' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | label_dangling | error | Global Label 'I2C_EC' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol UCOM1 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_CHG [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_TPM [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_5V [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol JCOM1 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_FG [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_AUD [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_3V3 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_EC [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_WIFI [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol J_EDP [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol SSD1 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_PD [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol U_WWAN [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol J_USB4 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | ERC | footprint_link_issues | warning | Symbol BT1 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint UCOM1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_PD | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_CHG | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_WIFI | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_WWAN | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_EC | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint SSD1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | DRC | lib_footprint_issues | warning | Footprint U_TPM | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | ERC | label_dangling | error | Global Label 'eDP0' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| ds_xl_coder | ERC | label_dangling | error | Global Label 'eDP1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| ds_xl_coder | ERC | label_dangling | error | Global Label 'VSYS' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| ds_xl_coder | ERC | label_dangling | error | Global Label 'BL_PWM_U' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| ds_xl_coder | ERC | label_dangling | error | Global Label 'BL_PWM_L' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint UCOM1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint J_EDP0 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint J_EDP1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint U_BRG | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint U_PD | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| ds_xl_coder | DRC | lib_footprint_issues | warning | Footprint U_WWAN | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | ERC | label_dangling | error | Global Label 'SOM_VIN' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| handheld_hybrid | ERC | label_dangling | error | Global Label 'VDD_3V3' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| handheld_hybrid | ERC | label_dangling | error | Global Label 'USB_SS' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| handheld_hybrid | ERC | label_dangling | error | Global Label 'MIPI_DSI' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| handheld_hybrid | ERC | label_dangling | error | Global Label 'I2C_HID' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint USOM1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint U_WIFI | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint U_HID | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint U_PD | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint U_CHG | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| handheld_hybrid | DRC | lib_footprint_issues | warning | Footprint U_WWAN | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | ERC | label_dangling | error | Global Label 'VDD_3V3' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | label_dangling | error | Global Label 'I2C_SDA' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | label_dangling | error | Global Label 'I2C_SCL' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | label_dangling | error | Global Label 'SPI_UWB' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | label_dangling | error | Global Label 'IMU_INT' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | label_dangling | error | Global Label 'CAP_RDY' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| edge_io_rings | ERC | footprint_link_issues | warning | Symbol U4 [R] | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U2 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U3 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U4 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U5 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| edge_io_rings | DRC | lib_footprint_issues | warning | Footprint U7 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | ERC | label_dangling | error | Global Label 'VBUS_UPSTREAM' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_TX_UP' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'I2C_PD' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'VBUS_DS1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_RX_UP' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'I2C_RETIMER' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'VBUS_DS2' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_TX_DS1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'USB_A1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'VSYS_5V' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_RX_DS1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'USB_A2' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'VDD_3V3' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_TX_DS2' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'MDI' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'VDD_1V8' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_RX_DS2' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'HDMI_TX' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_TX_HOST' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'CC1' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'RING_CHARGE_5V' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SS_RX_HOST' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'CC2' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | ERC | label_dangling | error | Global Label 'SPI_UWB' | **FIXED** | True | Embed gunnchos_block symbol pin + wire to global l |
| dock | DRC | lib_footprint_issues | warning | Footprint U1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint U2 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint U3 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint U4 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint U5 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint U8 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint J1 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint J6 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| dock | DRC | lib_footprint_issues | warning | Footprint J5 | **FIXED** | True | Project fp-lib-table + local gunnchos_structural.p |
| student_14_5 | RELEASE | com_hpc_pin_accurate_nets | error | COM-HPC Mini 400-pin map | **EXTERNAL_NDA_BLOCKED** | False |  |
| ds_xl_coder | RELEASE | com_hpc_pin_accurate_nets | error | COM-HPC Mini 400-pin map + dual eDP | **EXTERNAL_NDA_BLOCKED** | False |  |
| dock | RELEASE | intel_tb4_package_pinout | error | JHL8440 / JHL9040R package pins | **EXTERNAL_NDA_BLOCKED** | False |  |
| student_14_5 | ERC | lib_symbol_issues | warning | count=16 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| student_14_5 | ERC | isolated_pin_label | warning | count=6 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| ds_xl_coder | ERC | lib_symbol_issues | warning | count=10 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| ds_xl_coder | ERC | isolated_pin_label | warning | count=5 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| handheld_hybrid | ERC | lib_symbol_issues | warning | count=18 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| handheld_hybrid | ERC | isolated_pin_label | warning | count=17 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| edge_io_rings | ERC | lib_symbol_issues | warning | count=12 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| edge_io_rings | ERC | isolated_pin_label | warning | count=10 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| dock | ERC | isolated_pin_label | warning | count=24 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
| dock | ERC | lib_symbol_issues | warning | count=21 | **FORMALLY_WAIVED_WARNING** | False | Production vendor footprints/models required for c |
