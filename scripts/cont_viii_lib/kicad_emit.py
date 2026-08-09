"""KiCad schematic/PCB emitters for Cont VIII functional designs."""
from __future__ import annotations

from pathlib import Path

from .common import deterministic_uuid, write


def pin_side(side: str, idx: int, total: int, body_w: float, body_h: float):
    spacing = 2.54
    if side == "L":
        y = (total - 1) * spacing / 2 - idx * spacing
        return (-body_w / 2 - 2.54, y, 0)
    if side == "R":
        y = (total - 1) * spacing / 2 - idx * spacing
        return (body_w / 2 + 2.54, y, 180)
    if side == "T":
        x = -(total - 1) * spacing / 2 + idx * spacing
        return (x, body_h / 2 + 2.54, 270)
    x = -(total - 1) * spacing / 2 + idx * spacing
    return (x, -body_h / 2 - 2.54, 90)


def make_lib_symbol(
    name: str, pins: list, body_w: float = 20.32, body_h: float | None = None
) -> str:
    by: dict[str, list] = {"L": [], "R": [], "T": [], "B": []}
    for p in pins:
        by[p.get("side", "L")].append(p)
    max_lr = max(len(by["L"]), len(by["R"]), 2)
    if body_h is None:
        body_h = max(10.16, max_lr * 2.54 + 2.54)
    lines = [
        f'    (symbol "{name}"',
        "      (pin_numbers (hide no))",
        "      (pin_names (offset 0.254))",
        "      (in_bom yes) (on_board yes)",
        f'      (property "Reference" "U" (at 0 {body_h / 2 + 1.27} 0)',
        "        (effects (font (size 1.27 1.27))))",
        f'      (property "Value" "{name}" (at 0 {-body_h / 2 - 1.27} 0)',
        "        (effects (font (size 1.27 1.27))))",
        '      (property "Footprint" "" (at 0 0 0)',
        "        (effects (font (size 1.27 1.27)) hide))",
        '      (property "Datasheet" "" (at 0 0 0)',
        "        (effects (font (size 1.27 1.27)) hide))",
        f'      (symbol "{name}_0_1"',
        f"        (rectangle (start {-body_w / 2} {-body_h / 2}) (end {body_w / 2} {body_h / 2})",
        "          (stroke (width 0.254) (type default)) (fill (type background)))",
        "      )",
        f'      (symbol "{name}_1_1"',
    ]
    for side, plist in by.items():
        for i, p in enumerate(plist):
            x, y, orient = pin_side(side, i, len(plist), body_w, body_h)
            et = p.get("etype", "passive")
            pname = p["name"]
            pnum = p["num"]
            lines.append(
                f"        (pin {et} line (at {x} {y} {orient}) (length 2.54)\n"
                f'          (name "{pname}" (effects (font (size 1.016 1.016))))\n'
                f'          (number "{pnum}" (effects (font (size 1.016 1.016)))))'
            )
    lines.append("      )")
    lines.append("    )")
    return "\n".join(lines)


def _two_pin(name: str, footprint: str, shape_body: str) -> str:
    return (
        f'    (symbol "{name}"\n'
        "      (pin_numbers (hide yes))\n"
        "      (pin_names (offset 0.254))\n"
        "      (in_bom yes) (on_board yes)\n"
        f'      (property "Reference" "{name[0]}" (at 0.635 2.54 0)\n'
        "        (effects (font (size 1.27 1.27)) (justify left)))\n"
        f'      (property "Value" "{name}" (at 0.635 -2.54 0)\n'
        "        (effects (font (size 1.27 1.27)) (justify left)))\n"
        f'      (property "Footprint" "{footprint}" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (property "Datasheet" "" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        f'      (symbol "{name}_0_1"\n'
        f"{shape_body}\n"
        "      )\n"
        f'      (symbol "{name}_1_1"\n'
        "        (pin passive line (at 0 3.81 270) (length 2.54)\n"
        '          (name "~" (effects (font (size 1.27 1.27))))\n'
        '          (number "1" (effects (font (size 1.27 1.27)))))\n'
        "        (pin passive line (at 0 -3.81 90) (length 2.54)\n"
        '          (name "~" (effects (font (size 1.27 1.27))))\n'
        '          (number "2" (effects (font (size 1.27 1.27)))))\n'
        "      )\n"
        "    )"
    )


def make_passive_r() -> str:
    body = (
        "        (rectangle (start -1.016 -2.54) (end 1.016 2.54)\n"
        "          (stroke (width 0.254) (type default)) (fill (type none)))"
    )
    return _two_pin("R", "gunnchos_functional:R_0402", body)


def make_passive_c() -> str:
    body = (
        "        (polyline (pts (xy -1.524 -0.508) (xy 1.524 -0.508))\n"
        "          (stroke (width 0.371) (type default)) (fill (type none)))\n"
        "        (polyline (pts (xy -1.524 0.508) (xy 1.524 0.508))\n"
        "          (stroke (width 0.371) (type default)) (fill (type none)))"
    )
    return _two_pin("C", "gunnchos_functional:C_0402", body)


def make_led() -> str:
    return (
        '    (symbol "LED"\n'
        "      (pin_numbers (hide yes))\n"
        "      (pin_names (offset 1.016) (hide yes))\n"
        "      (in_bom yes) (on_board yes)\n"
        '      (property "Reference" "D" (at 0 2.54 0)\n'
        "        (effects (font (size 1.27 1.27))))\n"
        '      (property "Value" "LED" (at 0 -2.54 0)\n'
        "        (effects (font (size 1.27 1.27))))\n"
        '      (property "Footprint" "gunnchos_functional:LED_0603" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (property "Datasheet" "" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (symbol "LED_0_1"\n'
        "        (polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27))\n"
        "          (stroke (width 0.254) (type default)) (fill (type none)))\n"
        "        (polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27) (xy -1.27 0) (xy 1.27 -1.27))\n"
        "          (stroke (width 0.254) (type default)) (fill (type none)))\n"
        "      )\n"
        '      (symbol "LED_1_1"\n'
        "        (pin passive line (at -3.81 0 0) (length 2.54)\n"
        '          (name "K" (effects (font (size 1.27 1.27))))\n'
        '          (number "1" (effects (font (size 1.27 1.27)))))\n'
        "        (pin passive line (at 3.81 0 180) (length 2.54)\n"
        '          (name "A" (effects (font (size 1.27 1.27))))\n'
        '          (number "2" (effects (font (size 1.27 1.27)))))\n'
        "      )\n"
        "    )"
    )


def make_pwr_flag() -> str:
    return (
        '    (symbol "PWR_FLAG"\n'
        "      (power)\n"
        "      (pin_numbers (hide yes))\n"
        "      (pin_names (offset 0) (hide yes))\n"
        "      (in_bom yes) (on_board yes)\n"
        '      (property "Reference" "#FLG" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (property "Value" "PWR_FLAG" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (property "Footprint" "" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (property "Datasheet" "" (at 0 0 0)\n'
        "        (effects (font (size 1.27 1.27)) hide))\n"
        '      (symbol "PWR_FLAG_0_1"\n'
        "        (polyline (pts (xy 0 0) (xy 0 1.27) (xy 1.27 1.27) "
        "(xy 0 2.54) (xy -1.27 1.27) (xy 0 1.27))\n"
        "          (stroke (width 0) (type default)) (fill (type none)))\n"
        "      )\n"
        '      (symbol "PWR_FLAG_1_1"\n'
        "        (pin power_in line (at 0 0 90) (length 0) (hide yes)\n"
        '          (name "~" (effects (font (size 1.27 1.27))))\n'
        '          (number "1" (effects (font (size 1.27 1.27)))))\n'
        "      )\n"
        "    )"
    )


def _smd0402(name: str, descr: str) -> str:
    return f"""(footprint "{name}"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "{descr}")
  (tags "{name}")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.65) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "{name}" (at 0 1.65) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_rect (start -0.5 -0.25) (end 0.5 0.25) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -1.0 -0.6) (end 1.0 0.6) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd roundrect (at -0.5 0) (size 0.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (pad "2" smd roundrect (at 0.5 0) (size 0.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
)
"""


def ensure_functional_footprints(pretty: Path) -> None:
    pretty = Path(pretty)
    pretty.mkdir(parents=True, exist_ok=True)
    write(pretty / "R_0402.kicad_mod", _smd0402("R_0402", "0402 resistor Cont VIII"))
    write(pretty / "C_0402.kicad_mod", _smd0402("C_0402", "0402 capacitor Cont VIII"))
    write(
        pretty / "LED_0603.kicad_mod",
        """(footprint "LED_0603"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "0603 LED Cont VIII")
  (tags "LED 0603")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.8) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "LED_0603" (at 0 1.8) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_rect (start -0.8 -0.4) (end 0.8 0.4) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -1.2 -0.8) (end 1.2 0.8) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd roundrect (at -0.8 0) (size 0.7 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (pad "2" smd roundrect (at 0.8 0) (size 0.7 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
)
""",
    )
    # Multi-pad IC / connector proxies — functional layout, not production package claims for NDA parts
    qfn_pads = ['  (pad "33" smd rect (at 0 0) (size 2.8 2.8) (layers "F.Cu" "F.Paste" "F.Mask"))']
    for i in range(1, 25):
        if i <= 6:
            y = 1.75 - (i - 1) * 0.7
            qfn_pads.append(
                f'  (pad "{i}" smd rect (at -2.75 {y:.2f}) (size 0.35 0.7) '
                f'(layers "F.Cu" "F.Paste" "F.Mask"))'
            )
        elif i <= 12:
            x = -1.75 + (i - 7) * 0.7
            qfn_pads.append(
                f'  (pad "{i}" smd rect (at {x:.2f} -2.75) (size 0.7 0.35) '
                f'(layers "F.Cu" "F.Paste" "F.Mask"))'
            )
        elif i <= 18:
            y = -1.75 + (i - 13) * 0.7
            qfn_pads.append(
                f'  (pad "{i}" smd rect (at 2.75 {y:.2f}) (size 0.35 0.7) '
                f'(layers "F.Cu" "F.Paste" "F.Mask"))'
            )
        else:
            x = 1.75 - (i - 19) * 0.7
            qfn_pads.append(
                f'  (pad "{i}" smd rect (at {x:.2f} 2.75) (size 0.7 0.35) '
                f'(layers "F.Cu" "F.Paste" "F.Mask"))'
            )
    write(
        pretty / "IC_QFN32_proxy.kicad_mod",
        '(footprint "IC_QFN32_proxy"\n'
        "  (version 20221018)\n"
        '  (generator "continuation_viii")\n'
        '  (layer "F.Cu")\n'
        '  (descr "Cont VIII functional QFN-32 proxy")\n'
        '  (tags "QFN proxy")\n'
        "  (attr smd)\n"
        '  (fp_text reference "REF**" (at 0 -4.5) (layer "F.SilkS")\n'
        "    (effects (font (size 0.8 0.8) (thickness 0.12))))\n"
        '  (fp_text value "IC_QFN32_proxy" (at 0 4.5) (layer "F.Fab")\n'
        "    (effects (font (size 0.8 0.8) (thickness 0.12))))\n"
        '  (fp_rect (start -2.5 -2.5) (end 2.5 2.5) (layer "F.Fab") (width 0.1) (fill none))\n'
        '  (fp_rect (start -3.2 -3.2) (end 3.2 3.2) (layer "F.CrtYd") (width 0.05) (fill none))\n'
        + "\n".join(qfn_pads)
        + "\n)\n",
    )
    write(
        pretty / "Conn_USB_C_proxy.kicad_mod",
        """(footprint "Conn_USB_C_proxy"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "USB-C receptacle proxy Cont VIII")
  (tags "USB-C")
  (attr smd)
  (fp_text reference "REF**" (at 0 -5) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text value "USB_C" (at 0 5) (layer "F.Fab")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_rect (start -4.5 -3.5) (end 4.5 3.5) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -5 -4) (end 5 4) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "A1" smd rect (at -3.5 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "A4" smd rect (at -2.1 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "A5" smd rect (at -0.7 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "A6" smd rect (at 0.7 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "A7" smd rect (at 2.1 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "A9" smd rect (at 3.5 -2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B9" smd rect (at -3.5 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B4" smd rect (at -2.1 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B5" smd rect (at -0.7 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B6" smd rect (at 0.7 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B7" smd rect (at 2.1 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "B1" smd rect (at 3.5 2.2) (size 0.6 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "S1" smd rect (at -4.2 0) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "S2" smd rect (at 4.2 0) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
)
""",
    )
    write(
        pretty / "SODIMM260_proxy.kicad_mod",
        """(footprint "SODIMM260_proxy"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "SODIMM-260 edge connector proxy PUBLIC_PINOUT")
  (tags "SODIMM")
  (attr smd)
  (fp_text reference "REF**" (at 0 -8) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_text value "SODIMM260" (at 0 8) (layer "F.Fab")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_rect (start -35 -6) (end 35 6) (layer "F.Fab") (width 0.15) (fill none))
  (fp_rect (start -36 -7) (end 36 7) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "251" smd rect (at -30 4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "252" smd rect (at -27 4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "1" smd rect (at -30 -4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "109" smd rect (at -10 -4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "111" smd rect (at -7 -4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "236" smd rect (at 10 -4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "238" smd rect (at 13 -4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "185" smd rect (at 20 4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "187" smd rect (at 23 4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "220" smd rect (at 28 4.5) (size 1.2 2.0) (layers "F.Cu" "F.Paste" "F.Mask"))
)
""",
    )
    write(
        pretty / "MountingHole_3.2mm.kicad_mod",
        """(footprint "MountingHole_3.2mm"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "3.2mm mounting hole")
  (tags "mounting hole")
  (attr through_hole exclude_from_pos_files exclude_from_bom)
  (fp_text reference "REF**" (at 0 -3.5) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_text value "MountingHole_3.2mm" (at 0 3.5) (layer "F.Fab")
    (effects (font (size 1 1) (thickness 0.15))))
  (pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu" "*.Mask"))
)
""",
    )
    write(
        pretty / "Fiducial_1mm.kicad_mod",
        """(footprint "Fiducial_1mm"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "1mm fiducial")
  (tags "fiducial")
  (attr smd exclude_from_pos_files exclude_from_bom)
  (fp_text reference "REF**" (at 0 -2.2) (layer "F.SilkS") hide
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "FID" (at 0 2.2) (layer "F.Fab") hide
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_circle (center 0 0) (end 1 0) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd circle (at 0 0) (size 1 1) (layers "F.Cu") (solder_mask_margin 0.5))
)
""",
    )
    write(
        pretty / "TestPoint_Pad.kicad_mod",
        """(footprint "TestPoint_Pad"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "Test point pad 1.5mm")
  (tags "test point")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.8) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "TP" (at 0 1.8) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (pad "1" smd circle (at 0 0) (size 1.5 1.5) (layers "F.Cu" "F.Mask"))
)
""",
    )
    write(
        pretty / "IC_aQFN73_proxy.kicad_mod",
        """(footprint "IC_aQFN73_proxy"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "nRF52840 aQFN-73 mechanical proxy Cont VIII")
  (tags "aQFN nRF")
  (attr smd)
  (fp_text reference "REF**" (at 0 -5) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text value "aQFN73" (at 0 5) (layer "F.Fab")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_rect (start -3.5 -3.5) (end 3.5 3.5) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -4 -4) (end 4 4) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "49" smd rect (at 0 0) (size 3.5 3.5) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "13" smd rect (at -3.7 0) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "14" smd rect (at -3.7 0.6) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "15" smd rect (at -3.7 1.2) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "16" smd rect (at -3.7 1.8) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "17" smd rect (at -3.7 2.4) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "42" smd rect (at 3.7 0) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "43" smd rect (at 3.7 0.6) (size 0.35 0.55) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "1" smd rect (at -2.4 3.7) (size 0.55 0.35) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at -1.8 3.7) (size 0.55 0.35) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "32" smd rect (at 0 -3.7) (size 0.55 0.35) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "33" smd rect (at 0.6 -3.7) (size 0.55 0.35) (layers "F.Cu" "F.Paste" "F.Mask"))
)
""",
    )
    write(
        pretty / "COMHPC_Mini_envelope.kicad_mod",
        """(footprint "COMHPC_Mini_envelope"
  (version 20221018)
  (generator "continuation_viii")
  (layer "F.Cu")
  (descr "COM-HPC Mini 95x70 mechanical envelope — pin map EXTERNAL_NDA_BLOCKED")
  (tags "COM-HPC Mini envelope")
  (attr smd)
  (fp_text reference "REF**" (at 0 -40) (layer "F.SilkS")
    (effects (font (size 1.2 1.2) (thickness 0.15))))
  (fp_text value "COM-HPC Mini 95x70" (at 0 40) (layer "F.Fab")
    (effects (font (size 1.2 1.2) (thickness 0.15))))
  (fp_rect (start -47.5 -35) (end 47.5 35) (layer "F.Fab") (width 0.2) (fill none))
  (fp_rect (start -48 -36) (end 48 36) (layer "F.CrtYd") (width 0.05) (fill none))
  (fp_text user "NDA_PINOUT_EXTERNAL" (at 0 0) (layer "Cmts.User")
    (effects (font (size 2 2) (thickness 0.2))))
  (pad "VIN" smd rect (at -40 30) (size 2 2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "GND" smd rect (at -36 30) (size 2 2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "PWRBTN" smd rect (at 36 30) (size 1.5 1.5) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "UART_TX" smd rect (at 40 30) (size 1.5 1.5) (layers "F.Cu" "F.Paste" "F.Mask"))
)
""",
    )


def fp_lib_table(pretty: Path) -> str:
    rel = Path(pretty).resolve()
    return (
        "(fp_lib_table\n"
        "  (version 7)\n"
        f'  (lib (name "gunnchos_functional")(type "KiCad")(uri "{rel}")'
        f'(options "")(descr "Cont VIII functional footprints"))\n'
        ")\n"
    )


def place_symbol(
    lib_id: str,
    ref: str,
    value: str,
    x: float,
    y: float,
    footprint: str,
    extra_props=None,
    rot: int = 0,
) -> str:
    uid = deterministic_uuid(f"sch-{ref}-{value}")
    props = [
        f'    (property "Reference" "{ref}" (at {x} {y - 5.08} 0)\n'
        "      (effects (font (size 1.27 1.27))))",
        f'    (property "Value" "{value}" (at {x} {y + 5.08} 0)\n'
        "      (effects (font (size 1.27 1.27))))",
        f'    (property "Footprint" "{footprint}" (at {x} {y} 0)\n'
        "      (effects (font (size 1.27 1.27)) hide))",
        f'    (property "Datasheet" "" (at {x} {y} 0)\n'
        "      (effects (font (size 1.27 1.27)) hide))",
        f'    (property "ContVIII" "FUNCTIONAL" (at {x} {y} 0)\n'
        "      (effects (font (size 1.27 1.27)) hide))",
    ]
    if extra_props:
        for k, v in extra_props.items():
            props.append(
                f'    (property "{k}" "{v}" (at {x} {y} 0)\n'
                "      (effects (font (size 1.27 1.27)) hide))"
            )
    return (
        f'  (symbol (lib_id "{lib_id}") (at {x} {y} {rot}) (unit 1)\n'
        "    (in_bom yes) (on_board yes) (dnp no)\n"
        f"    (uuid {uid})\n" + "\n".join(props) + "\n  )"
    )


def wire(x1, y1, x2, y2, seed: str) -> str:
    return (
        f"  (wire (pts (xy {x1} {y1}) (xy {x2} {y2}))\n"
        f"    (stroke (width 0) (type default)) (uuid {deterministic_uuid(seed)}))"
    )


def global_label(
    name: str, x: float, y: float, orient: int, seed: str, shape: str = "input"
) -> str:
    return (
        f'  (global_label "{name}" (shape {shape}) (at {x} {y} {orient}) (fields_autoplaced)\n'
        "    (effects (font (size 1.27 1.27)) (justify left))\n"
        f"    (uuid {deterministic_uuid(seed)})\n"
        '    (property "Inferred Net Class" "Defaultnetclass" (at 0 -1.5 0)\n'
        "      (effects (font (size 1.27 1.27)) hide))\n"
        "  )"
    )


def no_connect(x: float, y: float, seed: str) -> str:
    return f"  (no_connect (at {x} {y}) (uuid {deterministic_uuid(seed)}))"


def text_note(txt: str, x: float, y: float, seed: str) -> str:
    safe = txt.replace('"', "'")
    return (
        f'  (text "{safe}" (at {x} {y} 0)\n'
        "    (effects (font (size 1.27 1.27)) (justify left bottom))\n"
        f"    (uuid {deterministic_uuid(seed)}))"
    )
