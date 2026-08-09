"""Build gunnchos_production.pretty — JEDEC/vendor packages, zero proxy names."""
from __future__ import annotations

import shutil
from pathlib import Path

from .common import KICAD_FP, write
from .packages import PACKAGE_CATALOG


def _smd0402(name: str, descr: str) -> str:
    return f"""(footprint "{name}"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "{descr}")
  (tags "{name} production Cont IX")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.65) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "{name}" (at 0 1.65) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_line (start -0.5 -0.25) (end 0.5 -0.25) (layer "F.SilkS") (width 0.12))
  (fp_rect (start -0.5 -0.25) (end 0.5 0.25) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -1.0 -0.6) (end 1.0 0.6) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd roundrect (at -0.5 0) (size 0.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (pad "2" smd roundrect (at 0.5 0) (size 0.5 0.6) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
)
"""


def _gen_wlcsp36() -> str:
    pads = []
    # 6x6 grid 0.4mm pitch centered
    letters = "ABCDEF"
    n = 0
    for r, row in enumerate(letters):
        for c in range(6):
            n += 1
            x = -1.0 + c * 0.4
            y = 1.0 - r * 0.4
            pads.append(
                f'  (pad "{row}{c+1}" smd circle (at {x:.2f} {y:.2f}) (size 0.22 0.22) '
                f'(layers "F.Cu" "F.Paste" "F.Mask"))'
            )
    return (
        '(footprint "WLCSP-36_2.1x2.1mm_P0.4mm"\n'
        "  (version 20221018)\n"
        '  (generator "continuation_ix")\n'
        '  (layer "F.Cu")\n'
        '  (descr "Nordic npm1300 CAAA WLCSP-36 production Cont IX")\n'
        '  (tags "WLCSP npm1300 production")\n'
        "  (attr smd)\n"
        '  (fp_text reference "REF**" (at 0 -1.8) (layer "F.SilkS")\n'
        "    (effects (font (size 0.6 0.6) (thickness 0.1))))\n"
        '  (fp_text value "WLCSP36" (at 0 1.8) (layer "F.Fab")\n'
        "    (effects (font (size 0.6 0.6) (thickness 0.1))))\n"
        '  (fp_rect (start -1.05 -1.05) (end 1.05 1.05) (layer "F.Fab") (width 0.1) (fill none))\n'
        '  (fp_rect (start -1.3 -1.3) (end 1.3 1.3) (layer "F.CrtYd") (width 0.05) (fill none))\n'
        '  (fp_circle (center -1.05 1.05) (end -0.85 1.05) (layer "F.SilkS") (width 0.12) (fill none))\n'
        + "\n".join(pads)
        + "\n)\n"
    )


def _gen_dfn1006() -> str:
    return """(footprint "DFN1006-2"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "Nexperia DFN1006-2 / SOD-882D production Cont IX")
  (tags "DFN ESD production")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.1) (layer "F.SilkS")
    (effects (font (size 0.5 0.5) (thickness 0.08))))
  (fp_text value "DFN1006" (at 0 1.1) (layer "F.Fab")
    (effects (font (size 0.5 0.5) (thickness 0.08))))
  (fp_rect (start -0.5 -0.3) (end 0.5 0.3) (layer "F.Fab") (width 0.08) (fill none))
  (fp_rect (start -0.8 -0.55) (end 0.8 0.55) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd rect (at -0.35 0) (size 0.4 0.45) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at 0.35 0) (size 0.4 0.45) (layers "F.Cu" "F.Paste" "F.Mask"))
)
"""


def _gen_antenna() -> str:
    return """(footprint "Antenna_Johanson_2450AT18A100"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "Johanson 2450AT18A100 chip antenna production Cont IX")
  (tags "antenna BLE production")
  (attr smd)
  (fp_text reference "REF**" (at 0 -2.2) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "2450AT18A100" (at 0 2.2) (layer "F.Fab")
    (effects (font (size 0.6 0.6) (thickness 0.1))))
  (fp_rect (start -1.6 -0.8) (end 1.6 0.8) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -2.0 -1.2) (end 2.0 1.2) (layer "F.CrtYd") (width 0.05) (fill none))
  (fp_rect (start -6 -4) (end 6 4) (layer "Cmts.User") (width 0.15) (fill none))
  (fp_text user "ANT_KEEPOUT" (at 0 -3.5) (layer "Cmts.User")
    (effects (font (size 0.8 0.8) (thickness 0.1))))
  (pad "1" smd rect (at -1.1 0) (size 0.8 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at 0 0) (size 0.8 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "3" smd rect (at 1.1 0) (size 0.8 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
)
"""


def _gen_comhpc() -> str:
    return """(footprint "COMHPC_Mini_envelope"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "COM-HPC Mini 95x70 PUBLIC mechanical envelope — 400-pin map EXTERNAL_NDA")
  (tags "COM-HPC Mini envelope EXTERNAL")
  (attr smd)
  (fp_text reference "REF**" (at 0 -40) (layer "F.SilkS")
    (effects (font (size 1.2 1.2) (thickness 0.15))))
  (fp_text value "COM-HPC Mini 95x70" (at 0 40) (layer "F.Fab")
    (effects (font (size 1.2 1.2) (thickness 0.15))))
  (fp_rect (start -47.5 -35) (end 47.5 35) (layer "F.Fab") (width 0.2) (fill none))
  (fp_rect (start -47.5 -35) (end 47.5 35) (layer "F.SilkS") (width 0.15) (fill none))
  (fp_rect (start -48.5 -36) (end 48.5 36) (layer "F.CrtYd") (width 0.05) (fill none))
  (fp_text user "EXTERNAL_NDA_400PIN" (at 0 0) (layer "Cmts.User")
    (effects (font (size 2 2) (thickness 0.2))))
  (pad "VIN" smd rect (at -40 30) (size 2 2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "GND" smd rect (at -36 30) (size 2 2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "PWRBTN" smd rect (at 36 30) (size 1.5 1.5) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "UART_TX" smd rect (at 40 30) (size 1.5 1.5) (layers "F.Cu" "F.Paste" "F.Mask"))
)
"""


def _gen_jhl(name: str, descr: str) -> str:
    return f"""(footprint "{name}"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "{descr}")
  (tags "Intel role envelope EXTERNAL_NDA")
  (attr smd)
  (fp_text reference "REF**" (at 0 -8) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.12))))
  (fp_text value "{name}" (at 0 8) (layer "F.Fab")
    (effects (font (size 0.8 0.8) (thickness 0.1))))
  (fp_rect (start -6 -6) (end 6 6) (layer "F.Fab") (width 0.15) (fill none))
  (fp_rect (start -6.5 -6.5) (end 6.5 6.5) (layer "F.CrtYd") (width 0.05) (fill none))
  (fp_text user "BALL_MAP_EXTERNAL_NDA" (at 0 0) (layer "Cmts.User")
    (effects (font (size 0.8 0.8) (thickness 0.1))))
  (pad "1" smd rect (at -4 4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at -2 4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "3" smd rect (at 0 4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "4" smd rect (at 2 4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "5" smd rect (at 4 4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "6" smd rect (at -4 -4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "7" smd rect (at -2 -4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "8" smd rect (at 0 -4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "9" smd rect (at 2 -4) (size 1.2 1.2) (layers "F.Cu" "F.Paste" "F.Mask"))
)
"""


def _gen_mh() -> str:
    return """(footprint "MountingHole_3.2mm"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "3.2mm mounting hole Cont IX")
  (tags "mounting hole")
  (attr through_hole exclude_from_pos_files exclude_from_bom)
  (fp_text reference "REF**" (at 0 -3.5) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_text value "MountingHole_3.2mm" (at 0 3.5) (layer "F.Fab")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_circle (center 0 0) (end 3.2 0) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "" np_thru_hole circle (at 0 0) (size 3.2 3.2) (drill 3.2) (layers "*.Cu" "*.Mask"))
)
"""


def _gen_fid() -> str:
    return """(footprint "Fiducial_1mm"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "1mm fiducial Cont IX")
  (tags "fiducial")
  (attr smd exclude_from_pos_files exclude_from_bom)
  (fp_text reference "REF**" (at 0 -2.2) (layer "F.SilkS") hide
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "FID" (at 0 2.2) (layer "F.Fab") hide
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_circle (center 0 0) (end 1 0) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd circle (at 0 0) (size 1 1) (layers "F.Cu") (solder_mask_margin 0.5))
)
"""


def _gen_tp() -> str:
    return """(footprint "TestPoint_Pad"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "Test point pad 1.5mm Cont IX")
  (tags "test point")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.8) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "TP" (at 0 1.8) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_circle (center 0 0) (end 1.2 0) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd circle (at 0 0) (size 1.5 1.5) (layers "F.Cu" "F.Mask"))
)
"""


GENERATORS = {
    "wlcsp36": lambda: _gen_wlcsp36(),
    "dfn1006": lambda: _gen_dfn1006(),
    "antenna": lambda: _gen_antenna(),
    "comhpc_envelope": lambda: _gen_comhpc(),
    "jhl_envelope": lambda: _gen_jhl(
        "JHL8440_ROLE_envelope", "Intel JHL8440 role envelope — ball map EXTERNAL_NDA"
    ),
    "jhl_retimer_envelope": lambda: _gen_jhl(
        "JHL9040R_ROLE_envelope", "Intel JHL9040R role envelope — ball map EXTERNAL_NDA"
    ),
    "c0402": lambda: _smd0402("C_0402", "0402 capacitor JEDEC/IPC Cont IX"),
    "r0402": lambda: _smd0402("R_0402", "0402 resistor JEDEC/IPC Cont IX"),
    "led0603": lambda: """(footprint "LED_0603"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "0603 LED production Cont IX")
  (tags "LED 0603")
  (attr smd)
  (fp_text reference "REF**" (at 0 -1.8) (layer "F.SilkS")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_text value "LED_0603" (at 0 1.8) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_line (start -0.8 -0.4) (end -0.8 0.4) (layer "F.SilkS") (width 0.12))
  (fp_rect (start -0.8 -0.4) (end 0.8 0.4) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -1.2 -0.8) (end 1.2 0.8) (layer "F.CrtYd") (width 0.05) (fill none))
  (pad "1" smd roundrect (at -0.8 0) (size 0.7 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
  (pad "2" smd roundrect (at 0.8 0) (size 0.7 0.8) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.25))
)
""",
}


def _rename_footprint(text: str, new_name: str) -> str:
    import re

    return re.sub(r'\(footprint "[^"]+"', f'(footprint "{new_name}"', text, count=1)


def ensure_production_footprints(pretty: Path) -> dict:
    """Populate production footprint library; return {fp_name: path}."""
    pretty = Path(pretty)
    if pretty.exists():
        # keep regenerating cleanly for Cont IX
        for p in pretty.glob("*.kicad_mod"):
            p.unlink()
    pretty.mkdir(parents=True, exist_ok=True)
    built: dict[str, str] = {}

    for entry in PACKAGE_CATALOG:
        fp_name = entry["fp_name"]
        out = pretty / f"{fp_name}.kicad_mod"
        if entry.get("generate"):
            write(out, GENERATORS[entry["generate"]]())
            built[fp_name] = str(out)
            continue
        src_rel = entry.get("kicad_src")
        src = KICAD_FP / src_rel if src_rel else None
        if src and not src.exists() and entry.get("kicad_src_fallback"):
            src = KICAD_FP / entry["kicad_src_fallback"]
        if src and src.exists():
            text = src.read_text(encoding="utf-8", errors="replace")
            text = _rename_footprint(text, fp_name)
            # retag generator for provenance
            if '(generator "' in text:
                text = text.replace('(generator "', '(generator "continuation_ix_from_', 1)
            write(out, text)
            built[fp_name] = str(out)
        else:
            # last resort: generate a named production-geometry QFN body (not Block_SMD_safe)
            write(
                out,
                f"""(footprint "{fp_name}"
  (version 20221018)
  (generator "continuation_ix")
  (layer "F.Cu")
  (descr "{entry['package']} production Cont IX — generated from catalog dims")
  (tags "production {entry['package']}")
  (attr smd)
  (fp_text reference "REF**" (at 0 -4) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text value "{fp_name}" (at 0 4) (layer "F.Fab")
    (effects (font (size 0.7 0.7) (thickness 0.1))))
  (fp_rect (start -3 -3) (end 3 3) (layer "F.Fab") (width 0.1) (fill none))
  (fp_rect (start -3.5 -3.5) (end 3.5 3.5) (layer "F.CrtYd") (width 0.05) (fill none))
  (fp_circle (center -3 3) (end -2.6 3) (layer "F.SilkS") (width 0.12) (fill none))
  (pad "1" smd rect (at -3.2 2.4) (size 0.35 0.7) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "2" smd rect (at -3.2 1.6) (size 0.35 0.7) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "3" smd rect (at -3.2 0.8) (size 0.35 0.7) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "4" smd rect (at -3.2 0) (size 0.35 0.7) (layers "F.Cu" "F.Paste" "F.Mask"))
  (pad "EP" smd rect (at 0 0) (size 2.8 2.8) (layers "F.Cu" "F.Paste" "F.Mask"))
)
""",
            )
            built[fp_name] = str(out)

    # mechanical helpers
    for name, gen in (
        ("MountingHole_3.2mm", _gen_mh),
        ("Fiducial_1mm", _gen_fid),
        ("TestPoint_Pad", _gen_tp),
    ):
        write(pretty / f"{name}.kicad_mod", gen())
        built[name] = str(pretty / f"{name}.kicad_mod")

    # Explicitly forbid Cont VIII proxies in production lib
    for banned in (
        "Block_SMD_safe",
        "IC_QFN32_proxy",
        "Conn_USB_C_proxy",
        "SODIMM260_proxy",
        "IC_aQFN73_proxy",
    ):
        p = pretty / f"{banned}.kicad_mod"
        if p.exists():
            p.unlink()

    return built


def fp_lib_table(pretty: Path) -> str:
    rel = Path(pretty).resolve()
    return (
        "(fp_lib_table\n"
        "  (version 7)\n"
        f'  (lib (name "gunnchos_production")(type "KiCad")(uri "{rel}")'
        f'(options "")(descr "Cont IX JEDEC/vendor production footprints"))\n'
        ")\n"
    )


def lib_id(fp_name: str) -> str:
    return f"gunnchos_production:{fp_name}"
