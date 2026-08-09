"""Product circuit definitions for Cont VIII functional schematics."""
from __future__ import annotations

# Pin dictionaries for multi-pin functional symbols. Exact MPNs from EXACT_MPN_MATRIX.
# Student/DS-XL COM-HPC pin-accurate map remains EXTERNAL_NDA_BLOCKED — only PUBLIC feature groups.


def sodimm_public_pins() -> list[dict]:
    """Key Radxa NX5 PUBLIC_PINOUT pins for Handheld carrier (subset of 260)."""
    return [
        {"num": "251", "name": "VCC_SYSIN", "side": "L", "etype": "power_in"},
        {"num": "252", "name": "VCC_SYSIN2", "side": "L", "etype": "power_in"},
        {"num": "1", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "109", "name": "USB20_HOST0_DM", "side": "L", "etype": "bidirectional"},
        {"num": "111", "name": "USB20_HOST0_DP", "side": "L", "etype": "bidirectional"},
        {"num": "236", "name": "UART2_TX", "side": "R", "etype": "output"},
        {"num": "238", "name": "UART2_RX", "side": "R", "etype": "input"},
        {"num": "185", "name": "I2C0_SCL", "side": "R", "etype": "bidirectional"},
        {"num": "187", "name": "I2C0_SDA", "side": "R", "etype": "bidirectional"},
        {"num": "220", "name": "LCD_BL_PWM", "side": "R", "etype": "output"},
        {"num": "126", "name": "LCD_RESET_L", "side": "R", "etype": "output"},
        {"num": "63", "name": "HDMI0_TX2N", "side": "T", "etype": "output"},
        {"num": "65", "name": "HDMI0_TX2P", "side": "T", "etype": "output"},
        {"num": "219", "name": "SDMMC_D0", "side": "B", "etype": "bidirectional"},
        {"num": "227", "name": "SDMMC_CMD", "side": "B", "etype": "bidirectional"},
        {"num": "229", "name": "SDMMC_CLK", "side": "B", "etype": "output"},
    ]


def usbc_pins() -> list[dict]:
    return [
        {"num": "A1", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "A4", "name": "VBUS", "side": "L", "etype": "passive"},
        {"num": "A5", "name": "CC1", "side": "L", "etype": "bidirectional"},
        {"num": "A6", "name": "D+", "side": "L", "etype": "bidirectional"},
        {"num": "A7", "name": "D-", "side": "L", "etype": "bidirectional"},
        {"num": "A9", "name": "VBUS2", "side": "R", "etype": "passive"},
        {"num": "B1", "name": "GND2", "side": "R", "etype": "passive"},
        {"num": "B5", "name": "CC2", "side": "R", "etype": "bidirectional"},
        {"num": "S1", "name": "SHIELD", "side": "B", "etype": "passive"},
    ]


def pd_controller_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VBUS", "side": "L", "etype": "passive"},
        {"num": "2", "name": "CC1", "side": "L", "etype": "bidirectional"},
        {"num": "3", "name": "CC2", "side": "L", "etype": "bidirectional"},
        {"num": "4", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "5", "name": "I2C_SCL", "side": "R", "etype": "bidirectional"},
        {"num": "6", "name": "I2C_SDA", "side": "R", "etype": "bidirectional"},
        {"num": "7", "name": "VSYS", "side": "R", "etype": "passive"},
        {"num": "8", "name": "3V3", "side": "R", "etype": "power_in"},
    ]


def charger_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VBUS", "side": "L", "etype": "passive"},
        {"num": "2", "name": "PMID", "side": "L", "etype": "passive"},
        {"num": "3", "name": "SYS", "side": "L", "etype": "passive"},
        {"num": "4", "name": "BAT", "side": "L", "etype": "passive"},
        {"num": "5", "name": "GND", "side": "R", "etype": "passive"},
        {"num": "6", "name": "SCL", "side": "R", "etype": "bidirectional"},
        {"num": "7", "name": "SDA", "side": "R", "etype": "bidirectional"},
        {"num": "8", "name": "STAT", "side": "R", "etype": "output"},
    ]


def buck_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VIN", "side": "L", "etype": "power_in"},
        {"num": "2", "name": "EN", "side": "L", "etype": "input"},
        {"num": "3", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "4", "name": "SW", "side": "R", "etype": "passive"},
        {"num": "5", "name": "FB", "side": "R", "etype": "input"},
        {"num": "6", "name": "VOUT", "side": "R", "etype": "power_out"},
    ]


def nrf52840_pins() -> list[dict]:
    """Nordic nRF52840 public pin subset for Ring."""
    return [
        {"num": "13", "name": "VDD", "side": "L", "etype": "power_in"},
        {"num": "14", "name": "VDDH", "side": "L", "etype": "power_in"},
        {"num": "15", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "16", "name": "DEC1", "side": "L", "etype": "passive"},
        {"num": "17", "name": "DEC2", "side": "L", "etype": "passive"},
        {"num": "42", "name": "SWDIO", "side": "R", "etype": "bidirectional"},
        {"num": "43", "name": "SWDCLK", "side": "R", "etype": "input"},
        {"num": "1", "name": "P0.00_XL1", "side": "T", "etype": "bidirectional"},
        {"num": "2", "name": "P0.01_XL2", "side": "T", "etype": "bidirectional"},
        {"num": "32", "name": "P0.06_I2C_SCL", "side": "B", "etype": "bidirectional"},
        {"num": "33", "name": "P0.08_I2C_SDA", "side": "B", "etype": "bidirectional"},
        {"num": "49", "name": "EPAD", "side": "B", "etype": "passive"},
    ]


def npm1300_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VBUS", "side": "L", "etype": "passive"},
        {"num": "2", "name": "VBAT", "side": "L", "etype": "passive"},
        {"num": "3", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "4", "name": "VOUTLDO1", "side": "R", "etype": "power_out"},
        {"num": "5", "name": "SCL", "side": "R", "etype": "bidirectional"},
        {"num": "6", "name": "SDA", "side": "R", "etype": "bidirectional"},
    ]


def iqs7222_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VDD", "side": "L", "etype": "power_in"},
        {"num": "2", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "3", "name": "SCL", "side": "R", "etype": "bidirectional"},
        {"num": "4", "name": "SDA", "side": "R", "etype": "bidirectional"},
        {"num": "5", "name": "RX0", "side": "T", "etype": "passive"},
        {"num": "6", "name": "TX0", "side": "T", "etype": "passive"},
        {"num": "7", "name": "RDY", "side": "B", "etype": "output"},
    ]


def bmi270_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VDD", "side": "L", "etype": "power_in"},
        {"num": "2", "name": "VDDIO", "side": "L", "etype": "power_in"},
        {"num": "3", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "4", "name": "SCL", "side": "R", "etype": "bidirectional"},
        {"num": "5", "name": "SDA", "side": "R", "etype": "bidirectional"},
        {"num": "6", "name": "INT1", "side": "R", "etype": "output"},
    ]


def comhpc_public_feature_pins() -> list[dict]:
    """PUBLIC_DOCS feature-group ports only — NO invented COM-HPC pin numbers."""
    return [
        {"num": "VIN", "name": "VIN_12V", "side": "L", "etype": "power_in"},
        {"num": "GND", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "PWRBTN", "name": "PWRBTN", "side": "R", "etype": "input"},
        {"num": "UART_TX", "name": "UART_TX", "side": "R", "etype": "output"},
    ]


def jhl8440_role_pins() -> list[dict]:
    """Dock USB4/TB4 controller ROLE pins — package ball map EXTERNAL_NDA."""
    return [
        {"num": "1", "name": "VDD", "side": "L", "etype": "power_in"},
        {"num": "2", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "3", "name": "USB4_UP_RX", "side": "L", "etype": "input"},
        {"num": "4", "name": "USB4_UP_TX", "side": "L", "etype": "output"},
        {"num": "5", "name": "DP_OUT", "side": "R", "etype": "output"},
        {"num": "6", "name": "PCIE_DN", "side": "R", "etype": "bidirectional"},
        {"num": "7", "name": "I2C_SCL", "side": "R", "etype": "bidirectional"},
        {"num": "8", "name": "I2C_SDA", "side": "R", "etype": "bidirectional"},
        {"num": "9", "name": "NOTE_NDA", "side": "B", "etype": "passive"},
    ]


def rtl8156_pins() -> list[dict]:
    return [
        {"num": "1", "name": "VDD33", "side": "L", "etype": "power_in"},
        {"num": "2", "name": "GND", "side": "L", "etype": "passive"},
        {"num": "3", "name": "USB_D+", "side": "R", "etype": "bidirectional"},
        {"num": "4", "name": "USB_D-", "side": "R", "etype": "bidirectional"},
        {"num": "5", "name": "TD+", "side": "T", "etype": "output"},
        {"num": "6", "name": "TD-", "side": "T", "etype": "output"},
        {"num": "7", "name": "RD+", "side": "B", "etype": "input"},
        {"num": "8", "name": "RD-", "side": "B", "etype": "input"},
    ]


def esd_pins() -> list[dict]:
    return [
        {"num": "1", "name": "IO", "side": "T", "etype": "passive"},
        {"num": "2", "name": "GND", "side": "B", "etype": "passive"},
    ]


BOARD_OUTLINES = {
    "handheld_hybrid": (220.0, 110.0),
    "edge_io_rings": (80.0, 60.0),
    "dock": (180.0, 120.0),
    "student_14_5": (280.0, 180.0),
    "ds_xl_coder": (300.0, 200.0),
}


PRODUCT_META = {
    "handheld_hybrid": {
        "title": "Handheld Hybrid SoM Carrier — Cont VIII PUBLIC_PINOUT",
        "rev": "0.5.0-cont-viii",
        "compute_mpn": "RM121-D8E32",
        "public_engineerability": "PUBLIC_PINOUT",
        "nda_block": False,
    },
    "edge_io_rings": {
        "title": "Edge I/O Ring EVT1 — Cont VIII Nordic Public",
        "rev": "0.5.0-cont-viii",
        "compute_mpn": "nRF52840-QIAA-R",
        "public_engineerability": "PUBLIC_PINOUT",
        "nda_block": False,
    },
    "dock": {
        "title": "Dock Main PCB — USB4/TB4 Cont VIII",
        "rev": "0.5.0-cont-viii",
        "compute_mpn": "JHL8440",
        "public_engineerability": "ROLE_PUBLIC_PACKAGE_NDA",
        "nda_block": True,
        "nda_item": "Intel JHL8440 / JHL9040R package ball maps",
    },
    "student_14_5": {
        "title": "Student 14.5 Carrier — Cont VIII Option B",
        "rev": "0.5.0-cont-viii",
        "compute_mpn": "COM-HPC-mMTL-155H-32G",
        "public_engineerability": "PUBLIC_DOCS_FEATURE_GROUPS",
        "nda_block": True,
        "nda_item": "COM-HPC Mini 400-pin net-accurate map",
    },
    "ds_xl_coder": {
        "title": "DS-XL Coder Carrier — Cont VIII Option B + dual display",
        "rev": "0.5.0-cont-viii",
        "compute_mpn": "COM-HPC-mMTL-155H-32G",
        "public_engineerability": "PUBLIC_DOCS_FEATURE_GROUPS",
        "nda_block": True,
        "nda_item": "COM-HPC Mini 400-pin + dual eDP pin map",
    },
}


def force_passive(pins):
    return redistribute_lr(pins)


def redistribute_lr(pins):
    """Place pins on L/R only for reliable schematic wire/NC attach."""
    out = []
    for i, p in enumerate(pins):
        q = dict(p)
        q["etype"] = "passive"
        q["side"] = "L" if i % 2 == 0 else "R"
        out.append(q)
    return out
