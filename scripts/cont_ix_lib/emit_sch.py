"""Cont IX schematic emission + Handheld hierarchical SODIMM sheets."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

from cont_viii_lib import kicad_emit as K8

from .common import TS, deterministic_uuid, root, write
from .parts import build_parts, mpn_fp, redistribute_lr

REV = "0.6.0-cont-ix"


def load_sodimm_pins():
    path = root() / "device_designs/handheld_hybrid/docs/radxa_nx5_public_pinout_table.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    assert len(rows) == 260, len(rows)
    return rows


def sheet_groups(rows):
    order = [
        "POWER_5V", "GND", "USB", "DISPLAY_HDMI_EDP", "DISPLAY_MIPI_DSI", "DISPLAY_CTRL",
        "CAMERA", "PCIE", "STORAGE_SDMMC", "I2C", "UART_DEBUG", "AUDIO", "WIFI_BT_CTRL",
        "SYS_CTRL", "CLOCK", "ADC", "RTC", "NC", "OTHER",
    ]
    by = defaultdict(list)
    for r in rows:
        by[r["group"] or "OTHER"].append(r)
    groups = []
    for g in order:
        if by.get(g):
            groups.append((g, by[g]))
    for g, lst in by.items():
        if g not in order:
            groups.append((g, lst))
    return groups


def attach_pins(lines, product, p, x, y):
    by = {"L": [], "R": [], "T": [], "B": []}
    for pin in p["pins"]:
        by[pin.get("side", "L")].append(pin)
    if p.get("passive2") or p.get("led"):
        if p.get("led"):
            pin_xy = {"1": (x - 3.81, y), "2": (x + 3.81, y)}
        else:
            pin_xy = {"1": (x, y - 3.81), "2": (x, y + 3.81)}
    else:
        body_w = 20.32 if len(p["pins"]) < 10 else 30.48
        max_lr = max(len(by["L"]), len(by["R"]), 2)
        body_h = max(10.16, max_lr * 2.54 + 2.54)
        pin_xy = {}
        for side, plist in by.items():
            for idx, pin in enumerate(plist):
                px, py, _ = K8.pin_side(side, idx, len(plist), body_w, body_h)
                pin_xy[pin["num"]] = (x + px, y + py)
    wires = p.get("wires", {})
    for num, (px, py) in pin_xy.items():
        if num in wires:
            net = wires[num]
            dx, dy = px - x, py - y
            if abs(dx) > abs(dy):
                lx, ly = px + (2.54 if dx > 0 else -2.54), py
                orient = 0 if dx > 0 else 180
            else:
                lx, ly = px, py + (2.54 if dy > 0 else -2.54)
                orient = 90 if dy > 0 else 270
            lines.append(K8.global_label(net, lx, ly, orient, f"gl-{product}-{p['ref']}-{num}-{net}"))
            lines.append(K8.wire(lx, ly, px, py, f"w-{product}-{p['ref']}-{num}"))
        else:
            lines.append(K8.no_connect(px, py, f"nc-{product}-{p['ref']}-{num}"))


def _place(lines, p, x, y):
    extra = {"MPN": p.get("mpn") or p["val"], "Role": p["role"], "ContIX": "PRODUCTION"}
    if p.get("extra"):
        extra.update(p["extra"])
    block = K8.place_symbol(p["lib"], p["ref"], p["val"], x, y, p["fp"], extra_props=extra)
    block = block.replace('property "ContVIII" "FUNCTIONAL"', 'property "ContIX" "PRODUCTION"')
    lines.append(block)


def emit_schematic(product: str, meta: dict) -> dict:
    if product == "handheld_hybrid":
        return emit_handheld(meta)
    parts = build_parts(product)
    return emit_flat(product, meta, parts)


def emit_flat(product: str, meta: dict, parts: list) -> dict:
    lib_map = {}
    for p in parts:
        if p["lib"] not in ("R", "C", "LED"):
            prev = lib_map.get(p["lib"])
            if prev is None or len(p["pins"]) >= len(prev):
                lib_map[p["lib"]] = p["pins"]
    symbols = [K8.make_passive_r(), K8.make_passive_c(), K8.make_led()]
    for name, plist in lib_map.items():
        bw = 20.32 if len(plist) < 10 else 30.48
        symbols.append(K8.make_lib_symbol(name, plist, body_w=bw))

    lines = [
        '(kicad_sch (version 20230121) (generator "continuation_ix_pre_evt_hardware_lock")',
        f"  (uuid {deterministic_uuid(f'sch-root-{product}')})",
        '  (paper "A3")',
        "  (title_block",
        f'    (title "{meta["title"]}")',
        f'    (date "{TS[:10]}")',
        f'    (rev "{REV}")',
        '    (company "gunnchOS3k / CONTINUATION IX")',
        '    (comment 1 "Production JEDEC/vendor footprints — Cont VIII proxies retired")',
        '    (comment 2 "PHYSICAL_EXECUTION_FREEZE ACTIVE — DRAFT PR only")',
        f'    (comment 3 "Compute MPN: {meta["compute_mpn"]}")',
        f'    (comment 4 "Engineerability: {meta["public_engineerability"]}")',
        "  )",
        "  (lib_symbols",
        "\n".join(symbols),
        "  )",
    ]
    placements = []
    for i, p in enumerate(parts):
        x = 50.8 + (i % 5) * 50.8
        y = 45.72 + (i // 5) * 45.72
        _place(lines, p, x, y)
        placements.append({**p, "x": x, "y": y})
        attach_pins(lines, product, p, x, y)

    notes = [
        "Cont IX functional schematic — production packages + exact MPNs (FuncBlock retired).",
        "SI notes encoded on PCB netclasses — no SI simulation claimed.",
        f"Revision {REV}.",
    ]
    if meta.get("nda_block"):
        notes.append(f"EXTERNAL_NDA_BLOCKED: {meta.get('nda_item')}")
    for i, n in enumerate(notes):
        lines.append(K8.text_note(n, 12.7, 200 + i * 5.08, f"note-{product}-{i}"))
    lines.append('  (sheet_instances\n    (path "/" (page "1"))\n  )')
    lines.append(")")
    text = "\n".join(lines) + "\n"
    kdir = root() / f"device_designs/{product}/kicad"
    write(kdir / f"{product}.kicad_sch", text)
    write(root() / f"electrical/{product}/kicad/{product}.kicad_sch", text)
    return {
        "product": product,
        "parts": len(parts),
        "nets": sum(len(p.get("wires", {})) for p in parts),
        "placements": placements,
        "hierarchical_sheets": 0,
    }


def emit_sodimm_child(gname, grows, sym_name, plist) -> str:
    symbols = [K8.make_lib_symbol(sym_name, plist, body_w=35.56 if len(plist) > 20 else 25.4)]
    lines = [
        '(kicad_sch (version 20230121) (generator "continuation_ix_pre_evt_hardware_lock")',
        f"  (uuid {deterministic_uuid(f'sch-sheet-{gname}')})",
        '  (paper "A3")',
        "  (title_block",
        f'    (title "Handheld SODIMM sheet — {gname}")',
        f'    (date "{TS[:10]}")',
        f'    (rev "{REV}")',
        '    (company "gunnchOS3k / CONTINUATION IX")',
        f'    (comment 1 "Pins in group: {len(grows)}")',
        '    (comment 2 "Evidence: PUBLIC_PINOUT radxa_nx5_260_pinout_v1100")',
        "  )",
        "  (lib_symbols",
        "\n".join(symbols),
        "  )",
    ]
    x, y = 80.0, 100.0
    block = K8.place_symbol(
        sym_name, f"JS_{gname[:10]}", f"SODIMM260_{gname}", x, y, mpn_fp("SODIMM-260"),
        extra_props={"MPN": "SODIMM-260", "Role": "SOM_SOCKET", "Group": gname, "Evidence": "PUBLIC_PINOUT"},
    ).replace('property "ContVIII" "FUNCTIONAL"', 'property "ContIX" "PRODUCTION"')
    lines.append(block)

    by = {"L": [], "R": [], "T": [], "B": []}
    for pin in plist:
        by[pin.get("side", "L")].append(pin)
    body_w = 35.56 if len(plist) > 20 else 25.4
    max_lr = max(len(by["L"]), len(by["R"]), 2)
    body_h = max(10.16, max_lr * 2.54 + 2.54)
    pin_xy = {}
    for side, pl in by.items():
        for idx, pin in enumerate(pl):
            px, py, _ = K8.pin_side(side, idx, len(pl), body_w, body_h)
            pin_xy[pin["num"]] = (x + px, y + py)

    for r in grows:
        num = r["pin"]
        sig = r["signal"]
        px, py = pin_xy[num]
        if sig == "NC" or r["group"] == "NC":
            lines.append(K8.no_connect(px, py, f"nc-hh-{gname}-{num}"))
            continue
        if r["group"] == "GND" or sig == "GND":
            net = "GND"
        elif r["group"] == "POWER_5V" or "VCC_SYSIN" in sig:
            net = "SOM_VIN"
        elif "USB20_HOST0_DM" in sig:
            net = "USB_DM"
        elif "USB20_HOST0_DP" in sig:
            net = "USB_DP"
        elif "UART2_TX" in sig:
            net = "UART_TX"
        elif "UART2_RX" in sig:
            net = "UART_RX"
        elif "I2C0_SCL" in sig:
            net = "I2C_SCL"
        elif "I2C0_SDA" in sig:
            net = "I2C_SDA"
        elif "LCD_BL_PWM" in sig:
            net = "LCD_BL_PWM"
        else:
            net = f"SOM_{sig}"[:48]
        dx, dy = px - x, py - y
        if abs(dx) > abs(dy):
            lx, ly = px + (2.54 if dx > 0 else -2.54), py
            orient = 0 if dx > 0 else 180
        else:
            lx, ly = px, py + (2.54 if dy > 0 else -2.54)
            orient = 90 if dy > 0 else 270
        lines.append(K8.global_label(net, lx, ly, orient, f"gl-hh-{gname}-{num}"))
        lines.append(K8.wire(lx, ly, px, py, f"w-hh-{gname}-{num}"))

    lines.append('  (sheet_instances\n    (path "/" (page "1"))\n  )')
    lines.append(")")
    return "\n".join(lines) + "\n"


def emit_handheld(meta: dict) -> dict:
    rows = load_sodimm_pins()
    groups = sheet_groups(rows)
    parts = [p for p in build_parts("handheld_hybrid") if p["role"] != "SOM_SOCKET"]
    kdir = root() / "device_designs/handheld_hybrid/kicad"
    sdir = kdir / "sheets"
    sdir.mkdir(parents=True, exist_ok=True)
    (root() / "electrical/handheld_hybrid/kicad/sheets").mkdir(parents=True, exist_ok=True)

    lib_map = {}
    for p in parts:
        if p["lib"] not in ("R", "C", "LED"):
            prev = lib_map.get(p["lib"])
            if prev is None or len(p["pins"]) >= len(prev):
                lib_map[p["lib"]] = p["pins"]
    symbols = [K8.make_passive_r(), K8.make_passive_c(), K8.make_led()]
    for name, plist in lib_map.items():
        bw = 20.32 if len(plist) < 10 else 30.48
        symbols.append(K8.make_lib_symbol(name, plist, body_w=bw))

    sheet_metas = []
    for gname, grows in groups:
        plist = redistribute_lr(
            [{"num": r["pin"], "name": r["signal"][:28], "side": "L", "etype": "passive"} for r in grows]
        )
        sym_name = f"SODIMM_{gname}"
        symbols.append(K8.make_lib_symbol(sym_name, plist, body_w=35.56 if len(plist) > 20 else 25.4))
        sheet_metas.append((gname, grows, sym_name, plist))

    lines = [
        '(kicad_sch (version 20230121) (generator "continuation_ix_pre_evt_hardware_lock")',
        f"  (uuid {deterministic_uuid('sch-root-handheld_hybrid')})",
        '  (paper "A2")',
        "  (title_block",
        f'    (title "{meta["title"]}")',
        f'    (date "{TS[:10]}")',
        f'    (rev "{REV}")',
        '    (company "gunnchOS3k / CONTINUATION IX")',
        '    (comment 1 "FULL Radxa NX5 260-pin PUBLIC_PINOUT hierarchical sheets")',
        '    (comment 2 "PHYSICAL_EXECUTION_FREEZE ACTIVE — DRAFT PR only")',
        '    (comment 3 "Production JEDEC/vendor footprints — no Block_SMD_safe")',
        "  )",
        "  (lib_symbols",
        "\n".join(symbols),
        "  )",
    ]
    placements = []
    for i, p in enumerate(parts):
        x = 40.64 + (i % 5) * 50.8
        y = 38.1 + (i // 5) * 40.64
        _place(lines, p, x, y)
        placements.append({**p, "x": x, "y": y})
        attach_pins(lines, "handheld_hybrid", p, x, y)

    # Keep a root SODIMM public-key symbol for carrier wiring + full sheets below
    from .parts import pins_tuple
    from cont_viii_lib import circuits as C8
    som = {
        "lib": "SODIMM260", "ref": "JSOM1", "val": "SODIMM-260", "fp": mpn_fp("SODIMM-260"),
        "role": "SOM_SOCKET", "mpn": "SODIMM-260", "extra": {"Evidence": "PUBLIC_PINOUT"},
        "pins": redistribute_lr(C8.sodimm_public_pins()),
        "wires": {"251": "SOM_VIN", "1": "GND", "109": "USB_DM", "111": "USB_DP",
                  "236": "UART_TX", "238": "UART_RX", "185": "I2C_SCL", "187": "I2C_SDA",
                  "220": "LCD_BL_PWM"},
    }
    # add symbol if missing
    if "SODIMM260" not in lib_map:
        lines[lines.index("  (lib_symbols") + 1]  # noop safety
        # inject symbol before closing — rebuild symbols already include from parts; add now
        pass
    # Ensure SODIMM260 symbol exists in lib_symbols block: append via separate place using existing make
    # Re-emit: insert symbol definition by rewriting is hard; place_symbol needs lib. Add to symbols earlier.
    # Actually symbols don't include SODIMM260 — fix by adding:
    # We'll re-open: simplest patch — add symbol text before placements
    sodimm_sym = K8.make_lib_symbol("SODIMM260", som["pins"], body_w=30.48)
    # inject after (lib_symbols
    text_so_far = "\n".join(lines)
    if 'symbol "SODIMM260"' not in text_so_far:
        lines = []
        for ln in text_so_far.splitlines():
            lines.append(ln)
            if ln.strip() == "(lib_symbols":
                lines.append(sodimm_sym)

    sx0, sy0 = 40.64, 120.0
    _place(lines, som, sx0, sy0)
    placements.append({**som, "x": sx0, "y": sy0})
    attach_pins(lines, "handheld_hybrid", som, sx0, sy0)

    sheet_infos = []
    for gi, (gname, grows, sym_name, plist) in enumerate(sheet_metas):
        sx = 40.64 + (gi % 4) * 55.88
        sy = 155.0 + (gi // 4) * 30.48
        sheet_path = f"sheets/sodimm_{gname.lower()}.kicad_sch"
        uid = deterministic_uuid(f"sheet-hh-{gname}")
        lines.append(
            f'  (sheet (at {sx} {sy}) (size 45.72 22.86)\n'
            f"    (stroke (width 0.1524) (type solid)) (fill (color 0 0 0 0.0000))\n"
            f"    (uuid {uid})\n"
            f'    (property "Sheetname" "{gname}" (at {sx} {sy - 1.27} 0)\n'
            f"      (effects (font (size 1.27 1.27)) (justify left bottom)))\n"
            f'    (property "Sheetfile" "{sheet_path}" (at {sx} {sy + 24.13} 0)\n'
            f"      (effects (font (size 1.27 1.27)) (justify left top)))\n"
            f"  )"
        )
        child = emit_sodimm_child(gname, grows, sym_name, plist)
        write(kdir / sheet_path, child)
        write(root() / f"electrical/handheld_hybrid/kicad/{sheet_path}", child)
        sheet_infos.append({"group": gname, "pins": len(grows), "file": sheet_path})

    for i, n in enumerate([
        "Cont IX: production footprints + full 260-pin hierarchical SODIMM sheets.",
        "All pin numbers from radxa_nx5_public_pinout_table.csv (PUBLIC_PINOUT).",
        f"Hierarchical sheets: {len(sheet_infos)}. Revision {REV}.",
    ]):
        lines.append(K8.text_note(n, 12.7, 280 + i * 5.08, f"note-hh-{i}"))

    inst = ['  (sheet_instances', '    (path "/" (page "1"))']
    for gi, (gname, *_r) in enumerate(sheet_metas):
        inst.append(f'    (path "/{gname}" (page "{gi + 2}"))')
    inst.append("  )")
    lines.extend(inst)
    lines.append(")")
    text = "\n".join(lines) + "\n"
    write(kdir / "handheld_hybrid.kicad_sch", text)
    write(root() / "electrical/handheld_hybrid/kicad/handheld_hybrid.kicad_sch", text)
    return {
        "product": "handheld_hybrid",
        "parts": len(placements),
        "nets": sum(len(p.get("wires", {})) for p in placements),
        "placements": placements,
        "hierarchical_sheets": len(sheet_infos),
        "sodimm_pins": 260,
        "sheet_infos": sheet_infos,
    }
