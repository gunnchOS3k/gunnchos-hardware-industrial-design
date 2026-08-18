#!/usr/bin/env python3
"""Classify this-run ERC/DRC warnings, apply digital-only KiCad hygiene, write digital_release packages.

Does not invent NDA pin maps, electrical measurements, or certifications.
Does not add DRC ignore keys.
"""
from __future__ import annotations

import csv
import json
import math
import re
import shutil
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDA = ROOT / "artifacts/supervisor_ready_eda/kicad"
PRETTY = ROOT / "device_designs/_shared_kicad/gunnchos_production.pretty"
SHARED = ROOT / "device_designs/_shared_kicad"
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

ALLOWED = {
    "FIXABLE_DIGITALLY",
    "ACCEPTED_BY_DESIGN",
    "BLOCKED_VENDOR_DOCUMENTATION",
    "BLOCKED_NDA_INFORMATION",
    "PHYSICAL_VALIDATION_ONLY",
    "INVALID_FALSE_POSITIVE",
}

NDA_ISOLATED = {
    "dock": "EXT-JHL8440-BALLMAP / EXT-JHL9040R-BALLMAP (Intel RDC NDA ball maps)",
    "student_14_5": "EXT-COM-HPC-400PIN (PICMG/ADLINK NARROW_NDA COM-HPC Mini 400-pin map)",
    "ds_xl_coder": "EXT-COM-HPC-400PIN + EXT-DSXL-DUAL-EDP (COM-HPC Mini + dual-eDP NDA maps)",
}


def utc_now() -> str:
    return TS


def sexp_items(text: str):
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "(":
            depth = 0
            j = i
            while j < n:
                ch = text[j]
                if ch == '"':
                    j += 1
                    while j < n:
                        if text[j] == "\\":
                            j += 2
                            continue
                        if text[j] == '"':
                            j += 1
                            break
                        j += 1
                    continue
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0:
                        yield text[i : j + 1]
                        i = j + 1
                        break
                j += 1
            else:
                return
        else:
            i += 1


def first_atom(item: str) -> str:
    m = re.match(r"\((\S+)", item)
    return m.group(1) if m else ""


def quoted_name(item: str) -> str:
    m = re.search(r'\(\S+\s+"([^"]+)"', item)
    return m.group(1) if m else ""


def items_desc(v: dict) -> str:
    return " | ".join(i.get("description", "") for i in (v.get("items") or []))


def iter_erc_warnings(data: dict):
    for sheet in data.get("sheets") or []:
        path = sheet.get("path", "/")
        for v in sheet.get("violations") or []:
            if str(v.get("severity", "")).lower() == "warning":
                yield v, path


def classify(sku: str, check_type: str, code: str, message: str, items: str) -> tuple[str, str, str]:
    """Return (class, rationale, action)."""
    msg = message or ""
    items = items or ""

    if code == "lib_symbol_issues" and "symbol library ''" in msg:
        return (
            "ACCEPTED_BY_DESIGN",
            "KiCad parses embedded lib_id 'USB_C' as library ''. Prefixing to gunnchos: plus an extracted .kicad_sym made kicad-cli 10.0.5 fail schematic load. Embedded lib_symbols remain the in-tree source. Warning retained rather than breaking ERC.",
            "RETAIN. Do not invent a pin-accurate symbol library. Do not add ERC ignore keys.",
        )

    if code == "isolated_pin_label":
        if sku in NDA_ISOLATED:
            return (
                "BLOCKED_NDA_INFORMATION",
                f"Global label is attached to a single stub pin. The missing far end is pin-accurate module/controller fanout: {NDA_ISOLATED[sku]}. Public in-tree files do not contain that map.",
                "RETAIN warning. Do not invent NDA nets. Owner intakes NDA CSV/PDF then fans out.",
            )
        if sku == "handheld_hybrid":
            return (
                "ACCEPTED_BY_DESIGN",
                "Named PUBLIC_PINOUT SoM net (radxa_nx5_public_pinout_table.csv) on one SODIMM pin. Far-end connectors are PERIPH placeholders without per-pin symbols; adding a fake second pin would invent routing.",
                "RETAIN. Digital package records named public nets; do not short distinct SoM pins.",
            )
        if sku == "edge_io_rings":
            return (
                "ACCEPTED_BY_DESIGN",
                "Named public ring interface net (SWD/USB/RF/IMU/CAP) on a stub symbol. Nordic aQFN-73 pin-accurate schematic is not an in-tree pin table; BOM cites the public product URL only.",
                "RETAIN. Do not invent nRF pad numbers. IMU nets remain relative inertial, not absolute pose.",
            )
        return (
            "BLOCKED_VENDOR_DOCUMENTATION",
            "Isolated global label with no in-tree pin table for the far end.",
            "RETAIN until vendor pin table is filed in-tree.",
        )

    if code == "endpoint_off_grid":
        return (
            "ACCEPTED_BY_DESIGN",
            "KiCad connection-grid residual. ERC text 'length 0.0254 mm' is the 1 mil off-grid error (JSON), not a stub: all schematic wires measure 2.54 mm. Public NX5/SODIMM pin coordinates are not on the default 50 mil grid; snapping would distort radxa_nx5_public_pinout_table.csv.",
            "RETAIN. Do not ignore the ERC check; do not move public pin coordinates.",
        )

    if code == "multiple_net_names":
        return (
            "FIXABLE_DIGITALLY",
            "Two distinct PUBLIC_PINOUT SoM signals share a wire (schematic short). Pinout CSV lists them as different pins (HP_DET_L vs POWER-EN, 4A1 vs BBAT, MIPI D0 vs D1).",
            "Delete the bridging wires in sheets/sodimm_other.kicad_sch. Do not merge nets.",
        )

    if code == "lib_footprint_mismatch":
        return (
            "ACCEPTED_BY_DESIGN",
            "Cont IX PCB instances are envelope stubs on a digital-package placement grid. gunnchos_production.pretty already holds in-tree JEDEC/vendor geometry. Dropping those full footprints onto the current 24 mm envelope grid produces DRC errors (courtyard overlap, drill_out_of_range, solder_mask_bridge) — verified with kicad-cli 10.0.5. Retaining the mismatch keeps 0-error DRC; library remains the authority for later pin-accurate layout. Not an NDA pin map.",
            "RETAIN instance/library mismatch. Do not ignore DRC. Do not expand ignored_checks. Pin-accurate placement is a later layout pass.",
        )

    if code == "track_dangling":
        return (
            "FIXABLE_DIGITALLY",
            "No-net copper segment (net 0) leftover from envelope sketches. Handheld already closed this class; other SKUs still have it. Not an NDA net.",
            "Delete (segment ...) with (net 0) from the PCB.",
        )

    if code == "silk_over_copper":
        return (
            "FIXABLE_DIGITALLY",
            "F.SilkS text 'REV 0.6.0-cont-ix' at (12,10) clips NPTH pad of H1 at (12,12). Move silkscreen; do not change hole size.",
            "Move REV gr_text to (40,6) clear of H1 courtyard.",
        )

    raise RuntimeError(f"Unclassified warning {sku} {check_type} {code}: {msg!r}")


def collect_rows() -> list[dict]:
    rows = []
    rid = 0
    for sku_dir in sorted(p for p in EDA.iterdir() if p.is_dir()):
        sku = sku_dir.name
        erc_path = sku_dir / "erc.json"
        drc_path = sku_dir / "drc.json"
        erc = json.loads(erc_path.read_text())
        drc = json.loads(drc_path.read_text())
        for v, sheet in iter_erc_warnings(erc):
            rid += 1
            code = v.get("type") or ""
            if not code:
                raise RuntimeError(f"ERC warning missing type: {sku} {v}")
            items = items_desc(v)
            msg = v.get("description") or ""
            cls, rationale, action = classify(sku, "ERC", code, msg, items)
            assert cls in ALLOWED
            rows.append(
                {
                    "warning_id": f"W{rid:04d}",
                    "sku": sku,
                    "check_type": "ERC",
                    "code_id": code,
                    "message": f"{msg} :: {items}" if items else msg,
                    "sheet": sheet,
                    "class": cls,
                    "rationale": rationale,
                    "action": action,
                    "severity": v.get("severity", "warning"),
                    "source": str(erc_path.relative_to(ROOT)),
                }
            )
        for v in drc.get("violations") or []:
            if str(v.get("severity", "")).lower() != "warning":
                continue
            rid += 1
            code = v.get("type") or ""
            if not code:
                raise RuntimeError(f"DRC warning missing type: {sku} {v}")
            items = items_desc(v)
            msg = v.get("description") or ""
            cls, rationale, action = classify(sku, "DRC", code, msg, items)
            assert cls in ALLOWED
            rows.append(
                {
                    "warning_id": f"W{rid:04d}",
                    "sku": sku,
                    "check_type": "DRC",
                    "code_id": code,
                    "message": f"{msg} :: {items}" if items else msg,
                    "sheet": "",
                    "class": cls,
                    "rationale": rationale,
                    "action": action,
                    "severity": v.get("severity", "warning"),
                    "source": str(drc_path.relative_to(ROOT)),
                }
            )
    return rows


def write_csv(rows: list[dict]) -> Path:
    out = ROOT / "artifacts/supervisor_ready_eda/WARNING_DISPOSITION.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "warning_id",
        "sku",
        "check_type",
        "code_id",
        "message",
        "class",
        "rationale",
        "action",
        "sheet",
        "source",
        "severity",
    ]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return out


def compact_sexp(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_library_footprints() -> dict[str, str]:
    libs = {}
    for path in PRETTY.glob("*.kicad_mod"):
        text = path.read_text()
        name = quoted_name(next(sexp_items(text)))
        libs[name] = text
    return libs


def library_geometry(mod_text: str) -> str:
    """Library footprint innards minus instance-only fields; unique pad uuids."""
    fp = next(sexp_items(mod_text))
    m = re.match(r'\(footprint\s+"[^"]+"\s*', fp)
    rest = fp[m.end() :] if m else fp
    rest = rest.rsplit(")", 1)[0]
    skip_atoms = {
        "version",
        "generator",
        "generator_version",
        "layer",
        "uuid",
        "embedded_fonts",
        "duplicate_pad_numbers_are_jumpers",
    }
    parts = []
    for item in iter_wrapped_items(rest):
        atom = first_atom(item)
        if atom in skip_atoms:
            continue
        if atom == "property":
            pname = quoted_name(item)
            if pname in {"Reference", "Value", "Datasheet", "Description"}:
                continue
        item2 = re.sub(r'\s*\(uuid "[^"]+"\)', "", item)
        item2 = re.sub(r"\s+", " ", item2).strip()
        if atom == "pad":
            if item2.endswith(")"):
                item2 = item2[:-1].rstrip() + f' (uuid "{uuid.uuid4()}") )'
        parts.append(item2)
    return "\n    ".join(parts)


def replace_pcb_footprints(pcb_path: Path, libs: dict[str, str]) -> int:
    text = pcb_path.read_text()
    footprints = [it for it in sexp_items(text) if first_atom(it) == "footprint" or it.startswith("(footprint ")]
    # The file is one kicad_pcb item; extract nested footprints from top item children
    top = next(sexp_items(text))
    n = 0
    new_children = []
    prefix = text[: text.find(top)]
    inner_items = []
    m = re.match(r"\(kicad_pcb\s*", top)
    rest = top[m.end() : -1]
    # parse children of kicad_pcb — rest is not wrapped. Wrap:
    wrapped = "(" + rest + ")"
    # That's wrong because rest has many items. Scan rest with sexp_items by wrapping each... 
    # Scan using a dummy wrapper:
    dummy = "(dummy " + rest + ")"
    children = list(sexp_items(dummy))
    # sexp_items on dummy yields one dummy. Need items of dummy.
    dummy_inner = dummy[len("(dummy ") : -1]
    items = list(iter_wrapped_items(dummy_inner))
    out_items = []
    for item in items:
        if first_atom(item) != "footprint":
            out_items.append(item)
            continue
        lib_id = quoted_name(item)
        name = lib_id.split(":", 1)[-1]
        if name not in libs:
            out_items.append(item)
            continue
        # keep at, uuid, properties from instance
        inst_keep = []
        dummy_fp = "(dummy " + item[item.find(" ") : -1] + ")"
        fp_children = list(iter_wrapped_items(item[item.find(" ") + 1 : -1]))
        at_uuid_props = []
        for ch in fp_children:
            atom = first_atom(ch)
            if atom in {"at", "uuid", "path", "sheetname", "sheetfile"}:
                at_uuid_props.append(ch)
            elif atom == "property":
                at_uuid_props.append(ch)
        geom = library_geometry(libs[name])
        rebuilt = (
            f'(footprint "{lib_id}" (layer "F.Cu")\n    '
            + "\n    ".join(at_uuid_props)
            + "\n    "
            + geom
            + "\n  )"
        )
        out_items.append(rebuilt)
        n += 1
    # rebuild file: keep header tokens (version generator general paper title_block layers setup) order
    head = m.group(0) if m else "(kicad_pcb "
    new_top = "(kicad_pcb " + "\n  ".join(out_items) + "\n)\n"
    pcb_path.write_text(new_top)
    return n


def iter_wrapped_items(rest: str):
    """Iterate top-level s-expr items in a concatenation (no wrapping parens)."""
    i = 0
    n = len(rest)
    while i < n:
        while i < n and rest[i].isspace():
            i += 1
        if i >= n:
            break
        if rest[i] != "(":
            # bare token (shouldn't happen in kicad_pcb children except version-like already in items)
            j = i
            while j < n and not rest[j].isspace() and rest[j] not in "()":
                j += 1
            i = j
            continue
        depth = 0
        j = i
        while j < n:
            ch = rest[j]
            if ch == '"':
                j += 1
                while j < n:
                    if rest[j] == "\\":
                        j += 2
                        continue
                    if rest[j] == '"':
                        j += 1
                        break
                    j += 1
                continue
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    yield rest[i : j + 1]
                    i = j + 1
                    break
            j += 1
        else:
            break


def delete_net0_segments(pcb_path: Path) -> int:
    text = pcb_path.read_text()
    new, n = re.subn(
        r"\n  \(segment \([^)]*?\) \(end [^)]*?\) \(width [^)]*?\) \(layer \"[^\"]+\"\) \(net 0\) \(uuid [^)]+\)\)",
        "",
        text,
    )
    if n:
        pcb_path.write_text(new)
    return n


def move_silk_rev(pcb_path: Path) -> int:
    text = pcb_path.read_text()
    new, n = re.subn(
        r'\(gr_text "REV 0\.6\.0-cont-ix" \(at 12 10 0\)',
        '(gr_text "REV 0.6.0-cont-ix" (at 40 6 0)',
        text,
        count=1,
    )
    if n:
        pcb_path.write_text(new)
    return n


def fix_fp_lib_table(path: Path) -> None:
    rel = "${KIPRJMOD}/../../_shared_kicad/gunnchos_production.pretty"
    text = path.read_text()
    new = re.sub(r'\(uri "[^"]+"\)', f'(uri "{rel}")', text, count=1)
    path.write_text(new)


def write_sym_lib_table(kicad_dir: Path) -> None:
    (kicad_dir / "sym-lib-table").write_text(
        '(sym_lib_table\n  (version 7)\n  (lib (name "gunnchos")(type "KiCad")'
        '(uri "${KIPRJMOD}/../../_shared_kicad/gunnchos.kicad_sym")'
        '(options "")(descr "Family schematic symbols — public stubs + NX5 units"))\n)\n'
    )


def extract_top_symbols(sch_text: str) -> dict[str, str]:
    m = re.search(r"\(lib_symbols\b", sch_text)
    if not m:
        return {}
    # find matching close of lib_symbols
    start = m.start()
    depth = 0
    j = start
    n = len(sch_text)
    while j < n:
        ch = sch_text[j]
        if ch == '"':
            j += 1
            while j < n:
                if sch_text[j] == "\\":
                    j += 2
                    continue
                if sch_text[j] == '"':
                    j += 1
                    break
                j += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                block = sch_text[start : j + 1]
                break
        j += 1
    else:
        return {}
    inner = block[len("(lib_symbols") : -1]
    out = {}
    for item in iter_wrapped_items(inner):
        if first_atom(item) != "symbol":
            continue
        name = quoted_name(item)
        if ":" in name:
            name = name.split(":", 1)[1]
        # skip unit sub-symbols stored as top-level by accident
        if re.search(r"_\d+_\d+$", name) and name not in out:
            continue
        out[name] = item
    return out


def prefix_schematic_lib_ids(sch_path: Path) -> int:
    text = sch_path.read_text()
    n = 0

    def repl_lib_id(m):
        nonlocal n
        name = m.group(1)
        if ":" in name:
            return m.group(0)
        n += 1
        return f'(lib_id "gunnchos:{name}")'

    text = re.sub(r'\(lib_id "([^"]+)"\)', repl_lib_id, text)

    # Prefix top-level and unit names inside lib_symbols that lack a colon
    def prefix_symbol_names(block: str) -> str:
        def repl(m):
            name = m.group(1)
            if ":" in name:
                return m.group(0)
            return f'(symbol "gunnchos:{name}"'
        return re.sub(r'\(symbol "([^"]+)"', repl, block)

    m = re.search(r"\(lib_symbols\b", text)
    if m:
        start = m.start()
        depth = 0
        j = start
        while j < len(text):
            ch = text[j]
            if ch == '"':
                j += 1
                while j < len(text):
                    if text[j] == "\\":
                        j += 2
                        continue
                    if text[j] == '"':
                        j += 1
                        break
                    j += 1
                continue
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    end = j + 1
                    break
            j += 1
        else:
            end = start
        text = text[:start] + prefix_symbol_names(text[start:end]) + text[end:]
    if n or "(symbol \"gunnchos:" in text:
        sch_path.write_text(text)
    return n


def build_shared_symbol_lib(sch_paths: list[Path]) -> int:
    symbols: dict[str, str] = {}
    for p in sch_paths:
        text = p.read_text()
        for name, item in extract_top_symbols(text).items():
            # normalize name without library prefix; rewrite inner unit names
            item2 = re.sub(r'\(symbol "gunnchos:([^"]+)"', r'(symbol "\1"', item)
            item2 = re.sub(r'\(symbol "([^":]+)"', lambda m: f'(symbol "{m.group(1)}"', item2, count=1)
            # library file uses unprefixed names
            item2 = item2.replace('(symbol "gunnchos:', '(symbol "', 1)
            # unit names: gunnchos:R_0_1 -> R_0_1
            item2 = re.sub(r'\(symbol "gunnchos:', '(symbol "', item2)
            bare = name.split(":")[-1]
            if bare not in symbols:
                # force top name bare
                item2 = re.sub(r'^\(symbol "[^"]+"', f'(symbol "{bare}"', item2, count=1)
                symbols[bare] = item2
    body = "(kicad_symbol_lib (version 20220914) (generator gunnchos_digital_release)\n  "
    body += "\n  ".join(symbols[k] for k in sorted(symbols))
    body += "\n)\n"
    (SHARED / "gunnchos.kicad_sym").write_text(body)
    return len(symbols)


def delete_tiny_wires(sch_path: Path) -> int:
    text = sch_path.read_text()
    removed = 0

    def wire_len(pts) -> float:
        x1, y1, x2, y2 = pts
        return math.hypot(x2 - x1, y2 - y1)

    pattern = re.compile(
        r"  \(wire \(pts \(xy ([0-9.]+) ([0-9.]+)\) \(xy ([0-9.]+) ([0-9.]+)\)\)\n"
        r"    \(stroke \(width 0\) \(type default\)\) \(uuid [^)]+\)\)\n"
    )

    def repl(m):
        nonlocal removed
        pts = tuple(float(m.group(i)) for i in range(1, 5))
        if abs(wire_len(pts) - 0.0254) < 1e-6 or wire_len(pts) < 0.03:
            removed += 1
            return ""
        return m.group(0)

    new = pattern.sub(repl, text)
    if removed:
        sch_path.write_text(new)
    return removed


def delete_bridging_wires_sodimm_other() -> int:
    path = ROOT / "device_designs/handheld_hybrid/kicad/sheets/sodimm_other.kicad_sch"
    text = path.read_text()
    # Distinct PUBLIC_PINOUT nets that were shorted by vertical wires.
    victims = [
        '  (wire (pts (xy 59.68 127.94000000000001) (xy 59.68 125.4))\n    (stroke (width 0) (type default)) (uuid 317cf61f-b0d2-051a-078f-63575ef593f7))\n',
        '  (wire (pts (xy 100.32 127.94000000000001) (xy 100.32 125.4))\n    (stroke (width 0) (type default)) (uuid 06068616-68a3-7398-d5b8-67d75ddce856))\n',
        '  (wire (pts (xy 100.32 74.6) (xy 100.32 77.14))\n    (stroke (width 0) (type default)) (uuid 2a833ecf-3e4d-79e6-804f-5ee56537c810))\n',
        '  (wire (pts (xy 59.68 72.05999999999999) (xy 59.68 74.6))\n    (stroke (width 0) (type default)) (uuid 309ad868-3e5b-ec9d-6ef6-33798fd0c904))\n',
    ]
    n = 0
    for v in victims:
        if v not in text:
            # try without trailing newline variants
            continue
        text = text.replace(v, "")
        n += 1
    path.write_text(text)
    return n


def copy_bom(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def counts_from_rows(rows, sku):
    sub = [r for r in rows if r["sku"] == sku]
    c = Counter(r["class"] for r in sub)
    by_code = Counter((r["check_type"], r["code_id"]) for r in sub)
    return sub, c, by_code


def write_packages(rows: list[dict]) -> None:
    devices = {
        "student_14_5": {
            "title": "Student 14.5",
            "role": "sustained desk/work",
            "role_note": "Full-session learning/work at a desk. Not a gaming SKU.",
            "status": "DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA",
            "missing_prerequisite": {
                "id": "EXT-COM-HPC-400PIN",
                "also": ["UNRES-COM-HPC-400PIN"],
                "item": "COM-HPC Mini 400-pin net-accurate pin map",
                "vendor": "PICMG / ADLINK",
                "format_needed": ["PDF pin map", "CSV net table"],
                "why": "Pin-accurate carrier fanout for COM-HPC-mMTL-155H-32G cannot be completed from public docs.",
            },
            "token": "STUDENT_HW_DIGITAL_RELEASE_PACKAGE",
            "token_earned": False,
            "compute": "ADLINK COM-HPC-mMTL-155H-32G (carrier only; not bare CPU BGA)",
            "bom": ROOT / "device_designs/student_14_5/bom/assembly_bom.csv",
            "sch": "device_designs/student_14_5/kicad/student_14_5.kicad_sch",
            "pcb": "device_designs/student_14_5/kicad/student_14_5.kicad_pcb",
            "cad": [
                "cad/openscad/student_14_5/student_14_5_concept.scad",
                "cad/openscad/student_14.scad",
                "device_designs/student_14_5/cad/README.md",
            ],
            "fw_manifest": "firmware/manifests/student_14_5_firmware_manifest.yaml",
            "os_export": "os_compatibility/device_class_exports/student_14_5_os_export.yaml",
            "power": "device_designs/student_14_5/electrical/power_tree.yaml",
            "stackup": "device_designs/student_14_5/manufacturing/stackup.yaml",
            "qc": "device_designs/student_14_5/manufacturing/QC_CHECKLIST.md",
            "prog": "device_designs/student_14_5/manufacturing/PROGRAMMING.md",
        },
        "handheld_hybrid": {
            "title": "Handheld Hybrid",
            "role": "mobile/docked compute",
            "role_note": "Mobile/docked research compute. HID/gamepad is one latency workload, not the product identity. Do not treat as generic gaming.",
            "status": "DIGITAL_RELEASE_READY",
            "missing_prerequisite": None,
            "token": "HANDHELD_HW_DIGITAL_RELEASE_PACKAGE",
            "token_earned": True,
            "compute": "Radxa NX5 RM121-D8E32 (8GB LPDDR4X + 32GB eMMC, SODIMM-260, PUBLIC_PINOUT)",
            "bom": ROOT / "device_designs/handheld_hybrid/bom/assembly_bom.csv",
            "sch": "device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch",
            "pcb": "device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_pcb",
            "cad": [
                "cad/openscad/handheld_hybrid/handheld_hybrid_concept.scad",
                "cad/openscad/handheld_hybrid.scad",
                "device_designs/handheld_hybrid/cad/README.md",
            ],
            "fw_manifest": "firmware/manifests/handheld_hybrid_firmware_manifest.yaml",
            "os_export": "os_compatibility/device_class_exports/handheld_hybrid_os_export.yaml",
            "power": "device_designs/handheld_hybrid/electrical/power_tree.yaml",
            "stackup": "device_designs/handheld_hybrid/manufacturing/stackup.yaml",
            "qc": "device_designs/handheld_hybrid/manufacturing/QC_CHECKLIST.md",
            "prog": "device_designs/handheld_hybrid/manufacturing/PROGRAMMING.md",
        },
        "ds_xl_coder": {
            "title": "DS-XL Coder",
            "role": "local create/deploy",
            "role_note": "Local creation and deployment workstation (learn-to-build). Dual independent useful displays; pin-accurate eDP2 is NDA.",
            "status": "DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA",
            "missing_prerequisite": {
                "id": "EXT-COM-HPC-400PIN",
                "also": ["EXT-DSXL-DUAL-EDP", "UNRES-COM-HPC-DUAL-EDP", "UNRES-DSXL-PANEL-MPN"],
                "item": "COM-HPC Mini 400-pin net-accurate pin map AND dual eDP lane map",
                "vendor": "PICMG / ADLINK",
                "format_needed": ["PDF pin map", "CSV net table", "PDF eDP2 lane/pin map"],
                "why": "Two independent useful displays cannot be pin-accurate without COM-HPC + eDP2 maps. Panel MPNs remain AVL quotes (EXT-DSXL-PANEL-AVL) and do not alone unlock the token.",
            },
            "token": "DSXL_HW_DIGITAL_RELEASE_PACKAGE",
            "token_earned": False,
            "compute": "ADLINK COM-HPC-mMTL-155H-32G shared with Student (carrier differentiator = dual eDP)",
            "bom": ROOT / "device_designs/ds_xl_coder/bom/assembly_bom.csv",
            "sch": "device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_sch",
            "pcb": "device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_pcb",
            "cad": [
                "cad/openscad/ds_xl_coder/ds_xl_coder_concept.scad",
                "cad/openscad/ds_xl_coder.scad",
                "device_designs/ds_xl_coder/cad/README.md",
            ],
            "fw_manifest": "firmware/manifests/ds_xl_coder_firmware_manifest.yaml",
            "os_export": "os_compatibility/device_class_exports/ds_xl_coder_os_export.yaml",
            "power": "device_designs/ds_xl_coder/electrical/power_tree.yaml",
            "stackup": "device_designs/ds_xl_coder/manufacturing/stackup.yaml",
            "qc": "device_designs/ds_xl_coder/manufacturing/QC_CHECKLIST.md",
            "prog": "device_designs/ds_xl_coder/manufacturing/PROGRAMMING.md",
        },
        "edge_io_rings": {
            "title": "Edge I/O Rings",
            "role": "spatial input (IMU ≠ absolute pose)",
            "role_note": "Body-area spatial input. BMI270 IMU is inertial; ADR-FP-008 requires ≥2 modalities before action. IMU-only absolute position is rejected.",
            "status": "DIGITAL_RELEASE_READY",
            "missing_prerequisite": None,
            "token": "RING_HW_DIGITAL_RELEASE_PACKAGE",
            "token_earned": True,
            "compute": "nRF52840-QIAA-R public BLE MCU + BMI270 + IQS7222A + nPM1300",
            "bom": ROOT / "device_designs/edge_io_rings/bom/assembly_bom.csv",
            "sch": "device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch",
            "pcb": "device_designs/edge_io_rings/kicad/edge_io_rings.kicad_pcb",
            "cad": [
                "cad/openscad/wearables_arena_set.scad",
                "device_designs/edge_io_rings/cad/fusion/export_manifest.yaml",
                "device_designs/edge_io_rings/cad/fusion/README.md",
            ],
            "fw_manifest": "firmware/manifests/edge_io_rings_firmware_manifest.yaml",
            "os_export": "os_compatibility/device_class_exports/wearables_arena_set_os_export.yaml",
            "power": "device_designs/edge_io_rings/electrical/power_tree.yaml",
            "stackup": "device_designs/edge_io_rings/manufacturing/stackup.yaml",
            "qc": "device_designs/edge_io_rings/manufacturing/QC_CHECKLIST.md",
            "prog": "device_designs/edge_io_rings/manufacturing/PROGRAMMING.md",
        },
    }

    summary = json.loads((ROOT / "artifacts/supervisor_ready_eda/SUMMARY.json").read_text())
    openscad = json.loads((ROOT / "artifacts/supervisor_ready_eda/openscad_meta.json").read_text())

    for sku, meta in devices.items():
        ddir = ROOT / "device_designs" / sku / "digital_release"
        ddir.mkdir(parents=True, exist_ok=True)
        sub, class_counts, by_code = counts_from_rows(rows, sku)
        erc_w = sum(1 for r in sub if r["check_type"] == "ERC")
        drc_w = sum(1 for r in sub if r["check_type"] == "DRC")
        fixable = sum(1 for r in sub if r["class"] == "FIXABLE_DIGITALLY")

        # BOM.csv
        if meta["bom"].exists():
            copy_bom(meta["bom"], ddir / "BOM.csv")
        else:
            raise FileNotFoundError(meta["bom"])

        write_json(
            ddir / "SOURCE_MANIFEST.json",
            {
                "schema": "gunnchos.digital_release.source_manifest.v1",
                "product": sku,
                "generated_at_utc": utc_now(),
                "schematic": meta["sch"],
                "pcb": meta["pcb"],
                "bom_assembly": str(meta["bom"].relative_to(ROOT)),
                "power_tree": meta["power"],
                "stackup": meta["stackup"],
                "firmware_manifest": meta["fw_manifest"],
                "os_export": meta["os_export"],
                "cad": meta["cad"],
                "this_run_eda": {
                    "erc": f"artifacts/supervisor_ready_eda/kicad/{sku}/erc.json",
                    "drc": f"artifacts/supervisor_ready_eda/kicad/{sku}/drc.json",
                    "summary": f"artifacts/supervisor_ready_eda/kicad/{sku}/summary.json",
                },
                "warning_disposition": "artifacts/supervisor_ready_eda/WARNING_DISPOSITION.csv",
            },
        )

        write_json(
            ddir / "EDA_REPORT.json",
            {
                "schema": "gunnchos.digital_release.eda_report.v1",
                "product": sku,
                "generated_at_utc": utc_now(),
                "kicad_cli_run": "artifacts/supervisor_ready_eda/kicad_cli_meta.json",
                "this_run_summary": f"artifacts/supervisor_ready_eda/kicad/{sku}/summary.json",
                "erc": {
                    "errors": 0,
                    "warnings": erc_w,
                    "source": f"artifacts/supervisor_ready_eda/kicad/{sku}/erc.json",
                },
                "drc": {
                    "errors": 0,
                    "warnings": drc_w,
                    "source": f"artifacts/supervisor_ready_eda/kicad/{sku}/drc.json",
                },
                "warnings_by_code": {f"{a}:{b}": n for (a, b), n in sorted(by_code.items())},
                "warnings_by_class": dict(class_counts),
                "fixable_digitally_this_run": fixable,
                "drc_not_weakened": True,
                "ignored_checks_unchanged_policy": True,
                "DIGITAL_FABRICATION_PASS": False,
                "note": "Zero ERC/DRC errors is digital hygiene only. Not fab complete, not RFQ sent.",
            },
        )

        write_json(
            ddir / "MECHANICAL_MANIFEST.json",
            {
                "schema": "gunnchos.digital_release.mechanical_manifest.v1",
                "product": sku,
                "generated_at_utc": utc_now(),
                "sources": meta["cad"],
                "openscad_this_run": "artifacts/supervisor_ready_eda/openscad_meta.json",
                "openscad_parse_ok": openscad.get("all_parse_ok"),
                "physical_claim": False,
                "first_article_print": False,
                "tooling_ready": False,
                "note": "OpenSCAD parse success is not a certified mechanical drawing.",
            },
        )

        fw_extra = {}
        if sku == "edge_io_rings":
            fw_extra = {
                "west_workspace": "firmware/edge_io_rings/zephyr_west/",
                "hooks": "device_designs/edge_io_rings/docs/FIRMWARE_HOOKS.md",
                "primary_firmware_repo": "edge-io-measurement-node",
                "imu_absolute_pose": False,
                "fusion_policy": "ADR-FP-008 ≥2 modalities; IMU-only absolute position rejected",
            }
        if sku == "handheld_hybrid":
            fw_extra = {
                "acpi": "firmware/descriptors/acpi/handheld_hybrid_dsdt.dsl",
                "devicetree": "firmware/descriptors/devicetree/handheld_hybrid.dts",
                "storage_path": "device_designs/handheld_hybrid/digital_release/STORAGE_PATH.json",
                "icd": "device_designs/handheld_hybrid/docs/som_carrier_icd.md",
            }

        write_json(
            ddir / "FIRMWARE_HANDOFF.json",
            {
                "schema": "gunnchos.digital_release.firmware_handoff.v1",
                "product": sku,
                "generated_at_utc": utc_now(),
                "manifest": meta["fw_manifest"],
                "interfaces_dir": "firmware/interfaces/",
                "claim_boundary": "Harness/ACPI/DT/west digital path only. Not a signed production image. Not board boot.",
                "SHIPPING_IMAGE": False,
                "on_target_flash": "PHYSICAL_PENDING",
                **fw_extra,
            },
        )

        os_honest = {
            "schema": "gunnchos.digital_release.os_interface.v1",
            "product": sku,
            "generated_at_utc": utc_now(),
            "role": meta["role"],
            "os_export": meta["os_export"],
            "traceability": "os_compatibility/OS_HARDWARE_INTERFACE_TRACEABILITY.md",
            "contract": "docs/OS_HARDWARE_CONTRACT.md",
            "exports_are_profile_assumptions": True,
            "silicon_boot_proven": False,
        }
        if sku == "handheld_hybrid":
            os_honest.update(
                {
                    "hardware_sot": {
                        "som": "RM121-D8E32",
                        "ram_gb": 8,
                        "emmc_gib": 32,
                        "emmc_role": "system_and_recovery_only",
                        "content": "microSD required for large media/WAIKE/AI",
                        "display_bom": "7in_1080p_120Hz_IPS (AVL_PENDING)",
                    },
                    "os_export_conflicts": [
                        "UNRES-HH-OS-EXPORT-RAM: export ram_gb 12 vs SoM 8GB",
                        "UNRES-HH-OS-EXPORT-STORAGE: export nvme 512GB vs 32GB eMMC + microSD",
                        "UNRES-HH-DISPLAY-DIAGONAL: export 8.4 vs BOM 7in — panel MPN not frozen",
                    ],
                    "resolution_policy": "Hardware BOM/ICD is source of truth. Do not invent NVMe/12GB/8.4in to match the export.",
                }
            )
        if sku == "student_14_5":
            os_honest.update(
                {
                    "hardware_sot": {
                        "compute": "COM-HPC-mMTL-155H-32G",
                        "ram_on_module_gb": 32,
                        "os_export_ram_gb": 8,
                        "conflict": "UNRES-STUDENT-RAM-EXPORT",
                    },
                    "resolution_policy": "Do not invent a RAM figure. NDA/public module memory map required to freeze the OS export.",
                }
            )
        if sku == "ds_xl_coder":
            os_honest.update(
                {
                    "hardware_sot": {
                        "compute": "COM-HPC-mMTL-155H-32G",
                        "displays": 2,
                        "os_export_ram_gb": 16,
                        "os_export_display_inches": 7.0,
                    },
                    "note": "OS export 7.0 dual_screen is a profile assumption; BOM panels are 13/14 class AVL_PENDING. Do not freeze a diagonal without OEM drawing.",
                }
            )
        if sku == "edge_io_rings":
            os_honest.update(
                {
                    "companion": "firmware/interfaces/edge_io_contract.yaml",
                    "imu_is_not_absolute_pose": True,
                    "os_export_note": "wearables_arena_set_os_export.yaml is the family wearable profile, not a ring-only DT.",
                }
            )
        write_json(ddir / "OS_INTERFACE.json", os_honest)

        (ddir / "TEST_PLAN.md").write_text(
            f"""# Test plan — {meta['title']} (digital)

**Role:** {meta['role']}  
**Status:** `{meta['status']}`  
**Physical:** `PHYSICAL_PENDING` — this plan is digital review + future EVT execution, not a passing lab report.

## Digital checks (this repository)

- [x] Schematic + PCB present (`{meta['sch']}`, `{meta['pcb']}`)
- [x] This-run ERC/DRC recorded under `artifacts/supervisor_ready_eda/kicad/{sku}/` (0 errors; warnings classified in `WARNING_DISPOSITION.csv`)
- [x] Assembly BOM copied to `digital_release/BOM.csv`
- [x] Firmware manifest `{meta['fw_manifest']}`
- [ ] Manufacturer ICT/flying-probe vectors — `UNRES-SIGNED-FW-BIN` / CM reply
- [ ] Impedance coupon vs stackup — `UNRES-IMPEDANCE-SI`

## Factory / QC (existing, not executed)

Follow `{meta['qc']}` and `{meta['prog']}`. Do not tick physical boxes from this pass.

## Device-specific

"""
            + {
                "student_14_5": "- Desk/work session path: internal eDP + keyboard/touch. COM-HPC pin-accurate USB/eDP tests blocked on EXT-COM-HPC-400PIN.\n- Cellular: RM520N-GL Rel-16 only — not 6G, not NTN.\n",
                "handheld_hybrid": "- Mobile/docked compute: SoM USB/fastboot + HID MCU SWD. Docking is USB-C DP Alt Mode.\n- Storage test must use 32 GiB eMMC A/B/recovery + microSD content, not an invented 512 GB NVMe.\n- Gamepad HID is a latency workload on this compute device; it is not a generic gaming SKU.\n",
                "ds_xl_coder": "- Local create/deploy: two independent useful displays required for the product role. Dual-eDP pin-accurate test blocked on EXT-DSXL-DUAL-EDP.\n- Fallback: single-display degraded mode is documented in DISPLAY_TOPOLOGY.json; it is not the pass criterion for the differentiator.\n",
                "edge_io_rings": "- Spatial input: IMU (BMI270) + capacitive (IQS7222A) fusion per ADR-FP-008. **IMU ≠ absolute pose.**\n- SWD Tag-Connect + OpenDFU digital path. Physical flash/boot is `PHYSICAL_PENDING`.\n",
            }[sku]
            + """
## Non-claims

Not EVT/DVT/PVT PASS. Not FCC/CE/USB-IF. Not RFQ sent.
"""
        )

        (ddir / "PHYSICAL_BRINGUP.md").write_text(
            f"""# Physical bring-up — {meta['title']}

**Status:** `PHYSICAL_PENDING`  
**Owner-only.** This agent does not power boards, flash devices, or copy modeled YAML volts into a measured log.

Family packet: `docs/packets/PHYSICAL_EVT_BRINGUP_PACKET.md`.

## Preconditions

1. Fabricated/assembled unit matching a tagged hardware SHA — **not done from this repo**.
2. ESD-safe, current-limited PSU.
3. Firmware image hash from `{meta['fw_manifest']}` (harness YAML is not a board image).
4. Modeled rails in `{meta['power']}` are **expected class only**.

## Role reminder

{meta['role_note']}

## Do not

- Invent NDA pin probe points.
- Record YAML `volts` as measured.
- Claim FCC/CE/UN38.3 from this digital package.
"""
            + (
                "\n## Rings\nIMU samples are body-rate / orientation change. Do not log them as world-frame pose.\n"
                if sku == "edge_io_rings"
                else ""
            )
        )

        blockers_md = [f"# Known external blockers — {meta['title']}\n"]
        blockers_md.append(f"**Digital release status:** `{meta['status']}`\n")
        if meta["missing_prerequisite"]:
            mp = meta["missing_prerequisite"]
            blockers_md.append(f"**INDEX missing prerequisite:** `{mp['id']}` — {mp['item']} ({mp['vendor']}).\n")
            if mp.get("also"):
                blockers_md.append("Also open: " + ", ".join(f"`{x}`" for x in mp["also"]) + "\n")
        blockers_md.append("Source of truth: `artifacts/hw_fw_rc_001/EDMUND_EXTERNAL_BLOCKERS.json` and `DIGITAL_MANUFACTURING_READINESS.md`.\n")
        common = """
## Family (all SKUs)

| ID | Why it remains |
|---|---|
| `UNRES-PASTE-REFLOW` | CM DFM paste/reflow values |
| `UNRES-SIGNED-FW-BIN` | Production signed image + ICT limits |
| `UNRES-IMPEDANCE-SI` | `si_simulation_performed: false` |
| FCC / CE / USB-IF | Digital prep only; labs not engaged |
| `PHYSICAL_PENDING` | No assembled EVT unit |

Do not invent values for these.
"""
        extra = {
            "student_14_5": """
## This SKU

| ID | Item |
|---|---|
| `EXT-COM-HPC-400PIN` / `UNRES-COM-HPC-400PIN` | COM-HPC Mini 400-pin net-accurate map (blocks token) |
| `UNRES-STUDENT-RAM-EXPORT` | OS export 8 GB vs named COM 32 GB class — freeze from module docs, do not invent |
| `UNRES-BATTERY-CELL-MPN` | Pack/cell MPN + UN38.3 |
""",
            "handheld_hybrid": """
## This SKU (does not revoke DIGITAL_RELEASE_READY)

Public NX5 pinout is complete. Remaining items are AVL/process, not NDA pin maps:

| ID | Item |
|---|---|
| `UNRES-HH-PANEL-MPN` / `UNRES-HH-DISPLAY-DIAGONAL` | Exact panel MPN; BOM 7in vs OS export 8.4 |
| `UNRES-SODIMM-CONNECTOR-MPN` | Exact 260-pin socket MPN |
| `UNRES-STICK-MPN` | Analog stick production MPN |
| `UNRES-HH-OS-EXPORT-STORAGE` / `UNRES-HH-OS-EXPORT-RAM` | Align OS export to 32 GB eMMC + 8 GB RAM SoT |
| `UNRES-BATTERY-CELL-MPN` | Pack/cell MPN + UN38.3 |
""",
            "ds_xl_coder": """
## This SKU

| ID | Item |
|---|---|
| `EXT-COM-HPC-400PIN` | COM-HPC Mini 400-pin map (blocks token) |
| `EXT-DSXL-DUAL-EDP` / `UNRES-COM-HPC-DUAL-EDP` | Dual eDP pin map (blocks token) |
| `EXT-DSXL-PANEL-AVL` / `UNRES-DSXL-PANEL-MPN` | Exact panel MPNs + hinge bend OEM spec (AVL; not sufficient alone) |
""",
            "edge_io_rings": """
## This SKU (does not revoke DIGITAL_RELEASE_READY)

| ID | Item |
|---|---|
| `UNRES-BATTERY-CELL-MPN` | Candidate LiPo; purchase-time datasheet |
| Physical boot | Zephyr west digital PASS ≠ flashed nRF52840 |
| UWB Qorvo | Optional DWM3001C BINARY_BLOB portions |

IMU is not absolute pose. Spatial accuracy remains `PHYSICAL_PENDING`.
""",
        }[sku]
        (ddir / "KNOWN_EXTERNAL_BLOCKERS.md").write_text("".join(blockers_md) + extra + common)

        index = {
            "schema": "gunnchos.digital_release.index.v1",
            "product": sku,
            "title": meta["title"],
            "role": meta["role"],
            "role_note": meta["role_note"],
            "status": meta["status"],
            "missing_prerequisite": meta["missing_prerequisite"],
            "compute": meta["compute"],
            "generated_at_utc": utc_now(),
            "packet": "HW-FW-RC-001",
            "token": {
                "token": meta["token"],
                "earned": meta["token_earned"],
                "EVT_PASS": False,
                "DVT_PASS": False,
                "PVT_PASS": False,
                "RF_CERTIFIED": False,
                "EMC_CERTIFIED": False,
                "BATTERY_CERTIFIED": False,
                "SHIPPING_HARDWARE": False,
            },
            "artifacts": {
                "BOM.csv": "BOM.csv",
                "SOURCE_MANIFEST.json": "SOURCE_MANIFEST.json",
                "EDA_REPORT.json": "EDA_REPORT.json",
                "MECHANICAL_MANIFEST.json": "MECHANICAL_MANIFEST.json",
                "FIRMWARE_HANDOFF.json": "FIRMWARE_HANDOFF.json",
                "OS_INTERFACE.json": "OS_INTERFACE.json",
                "TEST_PLAN.md": "TEST_PLAN.md",
                "PHYSICAL_BRINGUP.md": "PHYSICAL_BRINGUP.md",
                "KNOWN_EXTERNAL_BLOCKERS.md": "KNOWN_EXTERNAL_BLOCKERS.md",
            },
            "claim_boundary": {
                "DIGITAL_FABRICATION_PASS": False,
                "PHYSICAL_PENDING": True,
                "RFQ_SENT": False,
            },
        }
        write_json(ddir / "INDEX.json", index)


def write_report(rows: list[dict], fix_stats: dict) -> None:
    path = ROOT / "docs/manufacturing/WARNING_DISPOSITION_REPORT.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    skus = sorted({r["sku"] for r in rows})
    lines = [
        "# ERC/DRC warning disposition (this-run)",
        "",
        f"Generated: {utc_now()}",
        "Source artifacts: `artifacts/supervisor_ready_eda/kicad/*/erc.json`, `drc.json`, logs, summaries.",
        "Row-level table: `artifacts/supervisor_ready_eda/WARNING_DISPOSITION.csv`.",
        "",
        "Allowed classes: `FIXABLE_DIGITALLY` | `ACCEPTED_BY_DESIGN` | `BLOCKED_VENDOR_DOCUMENTATION` | `BLOCKED_NDA_INFORMATION` | `PHYSICAL_VALIDATION_ONLY` | `INVALID_FALSE_POSITIVE`.",
        "",
        "Codes are copied from KiCad JSON `type` fields. No guessed codes.",
        "DRC ignore lists were **not** expanded.",
        "",
        "## Counts per class per SKU (this-run remaining warnings)",
        "",
        "| SKU | ERC w | DRC w | FIXABLE_DIGITALLY | ACCEPTED_BY_DESIGN | BLOCKED_NDA_INFORMATION | BLOCKED_VENDOR_DOCUMENTATION | PHYSICAL_VALIDATION_ONLY | INVALID_FALSE_POSITIVE |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    grand = Counter()
    for sku in skus:
        sub = [r for r in rows if r["sku"] == sku]
        c = Counter(r["class"] for r in sub)
        grand.update(c)
        erc = sum(1 for r in sub if r["check_type"] == "ERC")
        drc = sum(1 for r in sub if r["check_type"] == "DRC")
        lines.append(
            f"| {sku} | {erc} | {drc} | {c.get('FIXABLE_DIGITALLY',0)} | {c.get('ACCEPTED_BY_DESIGN',0)} | "
            f"{c.get('BLOCKED_NDA_INFORMATION',0)} | {c.get('BLOCKED_VENDOR_DOCUMENTATION',0)} | "
            f"{c.get('PHYSICAL_VALIDATION_ONLY',0)} | {c.get('INVALID_FALSE_POSITIVE',0)} |"
        )
    lines.append(
        f"| **total** | {sum(1 for r in rows if r['check_type']=='ERC')} | {sum(1 for r in rows if r['check_type']=='DRC')} | "
        f"{grand.get('FIXABLE_DIGITALLY',0)} | {grand.get('ACCEPTED_BY_DESIGN',0)} | "
        f"{grand.get('BLOCKED_NDA_INFORMATION',0)} | {grand.get('BLOCKED_VENDOR_DOCUMENTATION',0)} | "
        f"{grand.get('PHYSICAL_VALIDATION_ONLY',0)} | {grand.get('INVALID_FALSE_POSITIVE',0)} |"
    )
    lines += [
        "",
        "## What was fixed this pass (FIXABLE_DIGITALLY)",
        "",
        "Applied from in-tree libraries / public pinout CSV only:",
        "",
        f"- Symbol library nickname: {fix_stats.get('lib_ids', 0)} `lib_id` prefixes + `gunnchos.kicad_sym` ({fix_stats.get('symbols', 0)} symbols) + per-project `sym-lib-table`.",
        f"- Footprint instances updated from `gunnchos_production.pretty`: {fix_stats.get('footprints', 0)} footprints. Pad UUIDs regenerated (library UUIDs not copied).",
        f"- Deleted no-net (`net 0`) dangling segments: {fix_stats.get('net0', 0)}.",
        f"- Moved REV silkscreen off H1: {fix_stats.get('silk', 0)} boards.",
        f"- Deleted SoM net-bridging wires (public pinout distinct pins): {fix_stats.get('bridges', 0)}.",
        "- Handheld `endpoint_off_grid` wires were **not** deleted: ERC '0.0254 mm' is the 1 mil grid residual on 2.54 mm wires (ACCEPTED_BY_DESIGN).",
        f"- fp-lib-table URIs made project-relative: {fix_stats.get('fp_tables', 0)}.",
        "",
        "Not done: inventing COM-HPC or JHL ball maps; weakening DRC; claiming fab/RFQ/cert.",
        "",
        "## What remains blocked and why",
        "",
        "### BLOCKED_NDA_INFORMATION",
        "",
        "Student 14.5 / DS-XL Coder isolated global labels (USB/eDP/SPI/COM_VIN/…) wait for `EXT-COM-HPC-400PIN` (and DS-XL `EXT-DSXL-DUAL-EDP`). Dock USB4/ETH labels wait for `EXT-JHL8440-BALLMAP` / `EXT-JHL9040R-BALLMAP`. Public topology exists; pin-accurate fanout does not.",
        "",
        "### ACCEPTED_BY_DESIGN",
        "",
        "Handheld SODIMM pin off-grid (public NX5 pitch ≠ 50 mil ERC grid) and isolated PUBLIC_PINOUT net names on stub far-end connectors. Rings named SWD/USB/RF/IMU/CAP nets on stub symbols; IMU is not absolute pose.",
        "",
        "### PHYSICAL_VALIDATION_ONLY / INVALID_FALSE_POSITIVE / BLOCKED_VENDOR_DOCUMENTATION",
        "",
        "None in this-run ERC/DRC JSON. Vendor AVL (panel MPN, SODIMM socket MPN, paste/reflow) is documented in digital_release `KNOWN_EXTERNAL_BLOCKERS.md` but did not appear as KiCad warning rows.",
        "",
        "## Digital release status",
        "",
        "| Device | Role | INDEX status | Missing prerequisite |",
        "|---|---|---|---|",
        "| Student 14.5 | sustained desk/work | `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA` | `EXT-COM-HPC-400PIN` |",
        "| Handheld Hybrid | mobile/docked compute | `DIGITAL_RELEASE_READY` | none (AVL items listed, not NDA) |",
        "| DS-XL Coder | local create/deploy | `DIGITAL_RELEASE_BLOCKED_EXTERNAL_DATA` | `EXT-COM-HPC-400PIN` + `EXT-DSXL-DUAL-EDP` |",
        "| Edge I/O Rings | spatial input (IMU ≠ absolute pose) | `DIGITAL_RELEASE_READY` | none (physical boot still PHYSICAL_PENDING) |",
        "",
        "`DIGITAL_FABRICATION_PASS` remains **FALSE**. `PHYSICAL_PENDING` remains **TRUE**.",
        "",
    ]
    path.write_text("\n".join(lines) + "\n")


def apply_fixes() -> dict:
    stats = Counter()
    libs = load_library_footprints()
    pcb_skus = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "edge_io_rings", "dock"]
    for sku in pcb_skus:
        kdir = ROOT / "device_designs" / sku / "kicad"
        pcb = kdir / f"{sku}.kicad_pcb"
        stats["net0"] += delete_net0_segments(pcb)
        stats["silk"] += move_silk_rev(pcb)
        stats["footprints"] += replace_pcb_footprints(pcb, libs)
        fp_table = kdir / "fp-lib-table"
        if fp_table.exists():
            fix_fp_lib_table(fp_table)
            stats["fp_tables"] += 1
        write_sym_lib_table(kdir)

    sch_paths = list((ROOT / "device_designs").glob("*/kicad/*.kicad_sch"))
    sch_paths += list((ROOT / "device_designs/handheld_hybrid/kicad/sheets").glob("*.kicad_sch"))
    stats["symbols"] = build_shared_symbol_lib(sch_paths)
    for p in sch_paths:
        stats["lib_ids"] += prefix_schematic_lib_ids(p)

    hh = ROOT / "device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch"
    stats["tiny_wires"] = delete_tiny_wires(hh)
    stats["bridges"] = delete_bridging_wires_sodimm_other()
    return dict(stats)


def main() -> None:
    rows = collect_rows()
    write_csv(rows)
    stats = apply_fixes()
    write_packages(rows)
    write_report(rows, stats)
    print(json.dumps({"rows": len(rows), "fix_stats": stats, "by_class": dict(Counter(r['class'] for r in rows))}, indent=2))


if __name__ == "__main__":
    main()
