"""Cont IX part lists with production footprints."""
from __future__ import annotations

from cont_viii_lib import circuits as C8
from .packages import catalog_by_mpn

LIB = "gunnchos_production"


def mpn_fp(mpn: str) -> str:
    cat = catalog_by_mpn().get(mpn)
    if not cat:
        # allow footprint name passthrough for helpers
        if mpn in ("TestPoint_Pad", "QFN-16-1EP_3x3mm_P0.5mm", "FFC_40P_0.5mm"):
            return f"{LIB}:{mpn}"
        raise KeyError(f"No production package catalog entry for {mpn}")
    return f"{LIB}:{cat['fp_name']}"


def redistribute_lr(pins):
    out = []
    for i, p in enumerate(pins):
        q = dict(p)
        q["etype"] = "passive"
        q["side"] = "L" if i % 2 == 0 else "R"
        out.append(q)
    return out


def pins_tuple(*items):
    raw = [{"num": n, "name": nm, "side": sd, "etype": "passive"} for n, nm, sd in items]
    return redistribute_lr(raw)


def build_parts(product: str) -> list[dict]:
    parts = []

    def add(**kwargs):
        parts.append(kwargs)

    add(
        lib="USB_C", ref="JUSB1", val="TYPE-C-31-M-12",
        fp=mpn_fp("HRO TYPE-C-31-M-12"), role="USB_C", mpn="HRO TYPE-C-31-M-12",
        pins=pins_tuple(("A1", "GND", "L"), ("A4", "VBUS", "L"), ("A5", "CC1", "L"),
                        ("A6", "DP", "R"), ("A7", "DM", "R"), ("B5", "CC2", "R"), ("S1", "SHIELD", "B")),
        wires={"A4": "VBUS", "A1": "GND", "A5": "CC1", "B5": "CC2", "A6": "USB_DP", "A7": "USB_DM", "S1": "GND"},
    )
    pd_mpn = "TPS65987DDHRSHR" if product == "handheld_hybrid" else "TPS65994ADFBRQ1"
    add(
        lib="PD_CTRL", ref="UPD1", val=pd_mpn, fp=mpn_fp(pd_mpn), role="PD", mpn=pd_mpn,
        pins=pins_tuple(("1", "VBUS", "L"), ("2", "CC1", "L"), ("3", "CC2", "L"), ("4", "GND", "L"),
                        ("5", "SCL", "R"), ("6", "SDA", "R"), ("7", "VSYS", "R"), ("8", "3V3", "R")),
        wires={"1": "VBUS", "2": "CC1", "3": "CC2", "4": "GND", "7": "VSYS", "5": "I2C_SCL",
               "6": "I2C_SDA", "8": "VDD_3V3"},
    )
    chg = "BQ25895RTWR" if product == "handheld_hybrid" else "BQ25792RQMR"
    add(
        lib="CHARGER", ref="UCHG1", val=chg, fp=mpn_fp(chg), role="CHARGER", mpn=chg,
        pins=pins_tuple(("1", "VBUS", "L"), ("2", "SYS", "L"), ("3", "BAT", "L"), ("4", "GND", "R"),
                        ("5", "SCL", "R"), ("6", "SDA", "R")),
        wires={"1": "VBUS", "2": "VSYS", "3": "VBAT", "4": "GND", "5": "I2C_SCL", "6": "I2C_SDA"},
    )
    add(
        lib="BUCK", ref="U3V3", val="TPS62864", fp=mpn_fp("TPS62864"), role="BUCK_3V3", mpn="TPS62864",
        pins=pins_tuple(("1", "VIN", "L"), ("2", "EN", "L"), ("3", "GND", "L"), ("4", "VOUT", "R")),
        wires={"1": "VSYS", "3": "GND", "4": "VDD_3V3", "2": "VDD_3V3"},
    )
    add(lib="C", ref="C1", val="CL05A104KA5NNNC", fp=mpn_fp("CL05A104KA5NNNC"), role="DECAP",
        mpn="CL05A104KA5NNNC", pins=pins_tuple(("1", "1", "T"), ("2", "2", "B")),
        wires={"1": "VDD_3V3", "2": "GND"}, passive2=True)
    add(lib="C", ref="C2", val="GRM188R60J106ME47D", fp=mpn_fp("CL05A104KA5NNNC"), role="BULK",
        mpn="GRM188R60J106ME47D", pins=pins_tuple(("1", "1", "T"), ("2", "2", "B")),
        wires={"1": "VSYS", "2": "GND"}, passive2=True)
    add(lib="R", ref="R1", val="RC0402FR-0710KL", fp=mpn_fp("RC0402FR-0710KL"), role="PULLUP",
        mpn="RC0402FR-0710KL", pins=pins_tuple(("1", "1", "T"), ("2", "2", "B")),
        wires={"1": "VDD_3V3", "2": "I2C_SCL"}, passive2=True)
    add(lib="R", ref="R2", val="RC0402FR-071K0L", fp=mpn_fp("RC0402FR-0710KL"), role="LED_R",
        mpn="RC0402FR-071K0L", pins=pins_tuple(("1", "1", "T"), ("2", "2", "B")),
        wires={"1": "VDD_3V3", "2": "LED_A"}, passive2=True)
    add(lib="LED", ref="D1", val="APTD1608LCGCK", fp=mpn_fp("APTD1608LCGCK"), role="STATUS_LED",
        mpn="APTD1608LCGCK", pins=pins_tuple(("1", "K", "L"), ("2", "A", "R")),
        wires={"1": "GND", "2": "LED_A"}, led=True)
    add(lib="ESD", ref="DESD1", val="PESD5V0S1UL", fp=mpn_fp("PESD5V0S1UL"), role="ESD",
        mpn="PESD5V0S1UL", pins=pins_tuple(("1", "IO", "T"), ("2", "GND", "B")),
        wires={"1": "CC1", "2": "GND"})

    if product == "handheld_hybrid":
        add(
            lib="SODIMM260", ref="JSOM1", val="SODIMM-260", fp=mpn_fp("SODIMM-260"),
            role="SOM_SOCKET", mpn="SODIMM-260", extra={"Evidence": "PUBLIC_PINOUT"},
            pins=redistribute_lr(C8.sodimm_public_pins()),
            wires={"251": "SOM_VIN", "1": "GND", "109": "USB_DM", "111": "USB_DP",
                   "236": "UART_TX", "238": "UART_RX", "185": "I2C_SCL", "187": "I2C_SDA",
                   "220": "LCD_BL_PWM"},
        )
        add(
            lib="HID_MCU", ref="UHID1", val="STM32F103C8T6", fp=mpn_fp("STM32F103C8T6"),
            role="HID_MCU", mpn="STM32F103C8T6",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "USB_DP", "R"),
                            ("4", "USB_DM", "R"), ("5", "SCL", "T"), ("6", "SDA", "T")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "USB_DP", "4": "USB_DM",
                   "5": "I2C_SCL", "6": "I2C_SDA"},
        )
        for ref, role, net in (
            ("JDISP1", "DISPLAY_MIPI", "LCD_BL_PWM"),
            ("JTP1", "TOUCH", "I2C_SCL"),
            ("JAUD1", "AUDIO", "I2C_SCL"),
            ("JCAM1", "CAMERA", "I2C_SCL"),
            ("JKEY1", "KEYBOARD", "I2C_SCL"),
            ("JTRK1", "TRACKPAD", "I2C_SCL"),
            ("JWWAN1", "WWAN", "USB_DP"),
            ("JGNSS1", "GNSS", "UART_TX"),
            ("JWIFI1", "WIFI", "I2C_SCL"),
            ("JBAT1", "BATTERY", "VBAT"),
            ("JSEC1", "SECURITY", "I2C_SCL"),
            ("JDBG1", "DEBUG", "UART_TX"),
            ("JHAP1", "HAPTICS", "I2C_SCL"),
            ("JFAN1", "EC_FAN", "I2C_SCL"),
        ):
            fp = mpn_fp("PANEL_AVL_PENDING") if role in ("DISPLAY_MIPI", "CAMERA") else mpn_fp("PESD5V0S1UL")
            add(
                lib="PERIPH", ref=ref, val=role, fp=fp, role=role, mpn=f"{role}_CONN",
                pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SIG", "R"), ("4", "CTRL", "R")),
                wires={"1": "VDD_3V3", "2": "GND",
                       "3": net if net in ("LCD_BL_PWM", "I2C_SCL", "UART_TX", "VBAT", "USB_DP") else "VDD_3V3",
                       "4": "GND"},
            )
    elif product == "edge_io_rings":
        add(lib="NRF52840", ref="U1", val="nRF52840-QIAA-R", fp=mpn_fp("nRF52840-QIAA-R"), role="MCU",
            mpn="nRF52840-QIAA-R", extra={"Evidence": "PUBLIC_PINOUT"},
            pins=redistribute_lr(C8.nrf52840_pins()),
            wires={"13": "VDD_3V3", "15": "GND", "42": "SWDIO", "43": "SWDCLK",
                   "32": "I2C_SCL", "33": "I2C_SDA", "49": "GND"})
        add(lib="NPM1300", ref="U2", val="npm1300-CAAA-R", fp=mpn_fp("npm1300-CAAA-R"), role="PMIC",
            mpn="npm1300-CAAA-R", pins=redistribute_lr(C8.npm1300_pins()),
            wires={"1": "VBUS", "2": "VBAT", "3": "GND", "4": "VDD_3V3", "5": "I2C_SCL", "6": "I2C_SDA"})
        add(lib="IQS7222A", ref="U3", val="IQS7222A", fp=mpn_fp("IQS7222A"), role="CAP_TOUCH",
            mpn="IQS7222A", pins=redistribute_lr(C8.iqs7222_pins()),
            wires={"1": "VDD_3V3", "2": "GND", "3": "I2C_SCL", "4": "I2C_SDA", "5": "CAP_RX0", "6": "CAP_TX0"})
        add(lib="BMI270", ref="U4", val="BMI270", fp=mpn_fp("BMI270"), role="IMU",
            mpn="BMI270", pins=redistribute_lr(C8.bmi270_pins()),
            wires={"1": "VDD_3V3", "2": "VDD_3V3", "3": "GND", "4": "I2C_SCL", "5": "I2C_SDA", "6": "IMU_INT1"})
        add(lib="SE050", ref="U5", val="SE050C1HQ1", fp=mpn_fp("SE050C1HQ1"), role="SE",
            mpn="SE050C1HQ1",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SCL", "R"), ("4", "SDA", "R")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "I2C_SCL", "4": "I2C_SDA"})
        add(lib="ANT", ref="ANT1", val="2450AT18A100", fp=mpn_fp("2450AT18A100"), role="BLE_ANT",
            mpn="2450AT18A100",
            pins=pins_tuple(("1", "FEED", "L"), ("2", "GND", "L"), ("3", "NC", "R")),
            wires={"1": "RF_2G4", "2": "GND"})
        add(lib="UWB", ref="UWBDNP", val="DWM3001C", fp=mpn_fp("TPS62864"), role="UWB_DNP",
            mpn="DWM3001C", extra={"DNP": "TRUE"},
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SPI_CS", "R"), ("4", "SPI_CLK", "R")),
            wires={"2": "GND"})
        add(lib="HAP", ref="UHAP1", val="DRV2605LDGSR", fp=mpn_fp("TPS62864"), role="HAPTICS",
            mpn="DRV2605LDGSR",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SCL", "R"), ("4", "SDA", "R")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "I2C_SCL", "4": "I2C_SDA"})
        add(lib="ELEC", ref="JE1", val="CAP_ELECTRODE", fp=f"{LIB}:TestPoint_Pad", role="ELECTRODE",
            mpn="ELECTRODE_GEO",
            pins=pins_tuple(("1", "RX", "T"), ("2", "GND", "B")),
            wires={"1": "CAP_RX0", "2": "GND"})
        add(lib="CHGPOGO", ref="JP1", val="POGO_CHARGE", fp=f"{LIB}:TestPoint_Pad", role="CHARGE_CONTACT",
            mpn="Mill-Max-319",
            pins=pins_tuple(("1", "VBUS", "T"), ("2", "GND", "B")),
            wires={"1": "VBUS", "2": "GND"})
    elif product == "dock":
        add(lib="JHL8440_ROLE", ref="UUSB4", val="JHL8440", fp=mpn_fp("JHL8440"), role="USB4_CTRL",
            mpn="JHL8440", extra={"Evidence": "ROLE_PUBLIC", "NDA": "PACKAGE_BALL_MAP"},
            pins=redistribute_lr(C8.jhl8440_role_pins()),
            wires={"1": "VDD_3V3", "2": "GND", "3": "USB4_UP", "4": "USB4_UP", "7": "I2C_SCL", "8": "I2C_SDA"})
        add(lib="JHL9040R_ROLE", ref="URET1", val="JHL9040R", fp=mpn_fp("JHL9040R"), role="TB4_RETIMER",
            mpn="JHL9040R", extra={"Evidence": "ROLE_PUBLIC", "NDA": "PACKAGE_BALL_MAP"},
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "RX", "R"), ("4", "TX", "R")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "USB4_UP", "4": "USB4_DN"})
        add(lib="RTL8156", ref="UETH1", val="RTL8156", fp=mpn_fp("RTL8156"), role="ETHERNET",
            mpn="RTL8156", pins=redistribute_lr(C8.rtl8156_pins()),
            wires={"1": "VDD_3V3", "2": "GND", "3": "USB_DP", "4": "USB_DM", "5": "ETH_TD_P", "6": "ETH_TD_N"})
        add(lib="VL817", ref="UHUB1", val="VL817", fp=mpn_fp("VL817"), role="USB_HUB",
            mpn="VL817",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "UP_DP", "R"), ("4", "UP_DM", "R"),
                            ("5", "DN1_DP", "T"), ("6", "DN1_DM", "T")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "USB_DP", "4": "USB_DM",
                   "5": "HUB_DN1_DP", "6": "HUB_DN1_DM"})
        add(lib="USB_C", ref="JUSB2", val="TYPE-C-31-M-12", fp=mpn_fp("HRO TYPE-C-31-M-12"),
            role="USB_C_DN", mpn="HRO TYPE-C-31-M-12",
            pins=pins_tuple(("A1", "GND", "L"), ("A4", "VBUS", "L"), ("A5", "CC1", "L"),
                            ("A6", "DP", "R"), ("A7", "DM", "R"), ("B5", "CC2", "R"), ("S1", "SHIELD", "B")),
            wires={"A4": "VBUS", "A1": "GND", "A5": "CC1", "B5": "CC2",
                   "A6": "HUB_DN1_DP", "A7": "HUB_DN1_DM", "S1": "GND"})
    else:
        add(lib="COMHPC_PUBLIC", ref="UCOM1", val="COM-HPC-mMTL-155H-32G",
            fp=mpn_fp("COM-HPC-mMTL-155H-32G"), role="COM_MODULE", mpn="COM-HPC-mMTL-155H-32G",
            extra={"Evidence": "PUBLIC_DOCS", "NDA": "400PIN_EXTERNAL"},
            pins=redistribute_lr(C8.comhpc_public_feature_pins()),
            wires={"VIN": "COM_VIN", "GND": "GND", "PWRBTN": "PWRBTN", "UART_TX": "UART_TX"})
        add(lib="TPM", ref="UTPM1", val="SLB9672XQ2.0", fp=mpn_fp("SLB9672XQ2.0"), role="TPM",
            mpn="SLB9672XQ2.0",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SPI_CS", "R"),
                            ("4", "SPI_CLK", "R"), ("5", "SPI_MOSI", "R"), ("6", "SPI_MISO", "T")),
            wires={"1": "VDD_3V3", "2": "GND", "3": "SPI_CS", "4": "SPI_CLK",
                   "5": "SPI_MOSI", "6": "SPI_MISO"})
        add(lib="PANEL_EDP", ref="JDISP1", val="eDP_primary_panel", fp=mpn_fp("PANEL_AVL_PENDING"),
            role="DISPLAY", mpn="PANEL_AVL_PENDING",
            pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "EDP_TX0N", "R"),
                            ("4", "EDP_TX0P", "R"), ("5", "BL_EN", "T"), ("6", "BL_PWM", "T"),
                            ("7", "T_SCL", "B"), ("8", "T_SDA", "B")),
            wires={"1": "VDD_3V3", "2": "GND", "4": "EDP0_P", "3": "EDP0_N", "6": "BL_PWM",
                   "7": "I2C_SCL", "8": "I2C_SDA", "5": "BL_EN"})
        for ref, role in (
            ("JNVME1", "NVME"), ("JWWAN1", "WWAN"), ("JSIM1", "SIM"), ("JWIFI1", "WIFI"),
            ("JETH1", "ETHERNET"), ("JAUD1", "AUDIO"), ("JCAM1", "CAMERA"),
            ("JKEY1", "KEYBOARD"), ("JTRK1", "TRACKPAD"), ("JEC1", "EC_FAN"),
            ("JBAT1", "BATTERY_BMS"), ("JSEC1", "SECURITY"), ("JDBG1", "DEBUG"),
        ):
            fp = mpn_fp("PANEL_AVL_PENDING") if role in ("NVME", "WWAN", "CAMERA") else mpn_fp("PESD5V0S1UL")
            add(
                lib="PERIPH", ref=ref, val=role, fp=fp, role=role, mpn=f"{role}_CONN",
                pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "SIG", "R"), ("4", "CTRL", "R")),
                wires={"1": "VDD_3V3", "2": "GND", "3": "VDD_3V3", "4": "GND"},
            )
        if product == "ds_xl_coder":
            add(lib="PANEL_EDP2", ref="JDISP2", val="eDP_secondary_panel",
                fp=mpn_fp("PANEL_AVL_PENDING"), role="DISPLAY2", mpn="PANEL2_AVL_PENDING",
                pins=pins_tuple(("1", "VDD", "L"), ("2", "GND", "L"), ("3", "EDP_TX0N", "R"),
                                ("4", "EDP_TX0P", "R"), ("5", "HINGE", "T"), ("6", "BL_PWM", "B")),
                wires={"1": "VDD_3V3", "2": "GND", "4": "EDP1_P", "3": "EDP1_N",
                       "5": "HINGE_FLEX", "6": "BL_PWM2"})
    return parts
