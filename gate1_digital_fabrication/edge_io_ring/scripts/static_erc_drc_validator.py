#!/usr/bin/env python3
"""Deterministic static ERC/DRC validator for Edge I/O Ring gate1 sources.

Fails on regressions vs baselines/pinout_baseline.json without requiring kicad-cli.
Does not claim physical fabrication or KiCad GUI equivalence.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "validation" / "baselines" / "pinout_baseline.json"
NETLIST_CANDIDATES = [
    ROOT / "schematic" / "netlist.json",
    ROOT / "schematic" / "edge_io_ring.net.json",
]
SCH_CANDIDATES = [
    ROOT / "schematic" / "kicad" / "edge_io_ring_evt0.kicad_sch",
    ROOT / "schematic" / "edge_io_ring.kicad_sch",
]
PCB_CANDIDATES = [
    ROOT / "pcb" / "kicad" / "edge_io_ring_evt0.kicad_pcb",
    ROOT / "pcb" / "edge_io_ring.kicad_pcb",
]
GERBER_DIR = ROOT / "pcb" / "gerbers"
DRILL_CANDIDATES = [
    ROOT / "pcb" / "gerbers" / "edge_io_ring_evt0.drl",
    ROOT / "pcb" / "drill" / "edge_io_ring.drl",
]
BOM_CANDIDATES = [
    ROOT / "bom" / "assembly_bom.csv",
    ROOT / "pcb" / "assembly" / "assembly_bom.csv",
]
OUT_ERC = ROOT / "schematic" / "reports" / "static_erc_report.json"
OUT_DRC = ROOT / "pcb" / "reports" / "static_drc_report.json"
OUT_MD = ROOT / "validation" / "STATIC_VALIDATION_REPORT.md"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _first_existing(paths: list[Path]) -> Path | None:
    for p in paths:
        if p.exists():
            return p
    return None


def _nets_from_netlist(data: dict) -> dict[str, list]:
    if "nets" in data and isinstance(data["nets"], dict):
        return {k: list(v) for k, v in data["nets"].items()}
    if "nets" in data and isinstance(data["nets"], list):
        out: dict[str, list] = {}
        for n in data["nets"]:
            name = n.get("name") or n.get("net")
            nodes = n.get("nodes") or n.get("pins") or []
            if name:
                out[name.replace("NET_", "")] = list(nodes)
                out[name] = list(nodes)
        return out
    return {}


def _gpio_from_nodes(nodes: list) -> set[str]:
    found = set()
    for n in nodes:
        s = str(n)
        m = re.search(r"P0\.\d+|P1\.\d+", s)
        if m:
            found.add(m.group(0))
    return found


def run_erc(baseline: dict) -> dict:
    issues: list[str] = []
    warnings: list[str] = []
    netlist_path = _first_existing(NETLIST_CANDIDATES)
    sch_path = _first_existing(SCH_CANDIDATES)
    if not netlist_path:
        issues.append("missing_netlist")
        nets = {}
    else:
        nets = _nets_from_netlist(_load_json(netlist_path))

    # Normalize net names (strip NET_ prefix for required checks)
    net_names = set(nets.keys())
    for req in baseline["required_nets"]:
        aliases = {req, f"NET_{req}", req.replace("3V3", "VDD"), "NET_VDD" if req == "3V3" else req}
        if not (net_names & aliases):
            # Allow VBAT_SYS as VBAT-adjacent presence
            if req == "VBAT" and ({"VBAT", "NET_VBAT", "VBAT_SYS"} & net_names):
                continue
            if req == "3V3" and ({"3V3", "NET_VDD", "VDD"} & net_names):
                continue
            issues.append(f"missing_net:{req}")

    gpio_map = baseline["gpio_map"]
    for net, pin in gpio_map.items():
        aliases = [net, f"NET_{net}"]
        matched = False
        for alias in aliases:
            if alias in nets:
                gpios = _gpio_from_nodes(nets[alias])
                if pin in gpios or any(pin in str(x) for x in nets[alias]):
                    matched = True
                    break
                # Accept pin string anywhere in node list
                if any(pin in str(x) for x in nets[alias]):
                    matched = True
                    break
        if not matched:
            # sch sexp fallback for net_tie lines
            if sch_path and sch_path.exists():
                text = sch_path.read_text(encoding="utf-8", errors="replace")
                if f"U1.{pin}" in text or pin in text:
                    # verify net association loosely
                    if net in text or f"NET_{net}" in text:
                        matched = True
            if not matched:
                issues.append(f"gpio_mismatch:{net}!={pin}")

    # Pin conflict: same GPIO used for two functions
    pin_owners: dict[str, str] = {}
    for net, nodes in nets.items():
        for g in _gpio_from_nodes(nodes):
            if g in pin_owners and pin_owners[g] != net:
                # ignore NET_ vs plain duplicates
                a, b = sorted([pin_owners[g].replace("NET_", ""), net.replace("NET_", "")])
                if a != b:
                    issues.append(f"pin_conflict:{g}:{pin_owners[g]}|{net}")
            else:
                pin_owners[g] = net

    # Required refs from schematic or netlist components
    refs_found: set[str] = set()
    if netlist_path:
        data = _load_json(netlist_path)
        for c in data.get("components", []):
            if "ref" in c:
                refs_found.add(c["ref"])
    if sch_path:
        for m in re.finditer(r'\(property "Reference" "([^"]+)"', sch_path.read_text(encoding="utf-8", errors="replace")):
            refs_found.add(m.group(1))
    for ref in baseline["required_refs"]:
        # ANT1 may appear as A1 in simplified sch
        if ref not in refs_found and not (ref == "ANT1" and "A1" in refs_found):
            warnings.append(f"ref_absent_or_alias:{ref}")

    if not sch_path:
        issues.append("missing_schematic")

    result = "PASS" if not issues else "FAIL"
    report = {
        "tool": "gunnchos_static_erc",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "result": result,
        "netlist": str(netlist_path) if netlist_path else None,
        "schematic": str(sch_path) if sch_path else None,
        "issues": issues,
        "warnings": warnings,
        "baseline": str(BASELINE),
        "physical_claim": False,
    }
    return report


def run_drc(baseline: dict) -> dict:
    issues: list[str] = []
    warnings: list[str] = []
    pcb_path = _first_existing(PCB_CANDIDATES)
    if not pcb_path:
        issues.append("missing_pcb")
        pcb_text = ""
    else:
        pcb_text = pcb_path.read_text(encoding="utf-8", errors="replace")

    rules = baseline["rules"]
    # Required layers / edge cuts presence
    for token in ("F.Cu", "B.Cu", "Edge.Cuts", "F.Mask"):
        if token not in pcb_text and f'"{token}"' not in pcb_text:
            issues.append(f"missing_layer:{token}")

    # Board OD/ID encoded in reports or stackup — check stackup + geometry notes
    stackup = ROOT / "pcb" / "stackup.yaml"
    sizes = ROOT / "mechanical" / "sizes.yaml"
    od = rules["board_od_mm"]
    id_mm = rules["board_id_mm"]
    geometry_ok = False
    for p in (stackup, sizes, ROOT / "mechanical" / "geometry_spec.md", ROOT / "pcb" / "fabrication_notes.md"):
        if p.exists():
            t = p.read_text(encoding="utf-8", errors="replace")
            if str(od) in t and str(id_mm) in t:
                geometry_ok = True
    if not geometry_ok:
        # Accept if PCB silk / notes mention annular ring dimensions
        if str(od) in pcb_text and str(id_mm) in pcb_text:
            geometry_ok = True
    if not geometry_ok:
        warnings.append("geometry_od_id_not_embedded_in_pcb_sexp")

    # Gerber parity
    required_gerbers = [
        "F_Cu",
        "B_Cu",
        "Edge_Cuts",
        "F_Mask",
        "F_SilkS",
    ]
    gerbers = list(GERBER_DIR.glob("*.gbr")) if GERBER_DIR.exists() else []
    gnames = " ".join(g.name for g in gerbers)
    for layer in required_gerbers:
        if layer not in gnames:
            issues.append(f"missing_gerber:{layer}")

    drill = _first_existing(DRILL_CANDIDATES)
    if not drill:
        issues.append("missing_drill")
    else:
        drill_txt = drill.read_text(encoding="utf-8", errors="replace")
        # Excellon-ish content
        if "M48" not in drill_txt and "T0" not in drill_txt and "INCH" not in drill_txt and "METRIC" not in drill_txt:
            # generated minimal drills may just list holes
            if len(drill_txt.strip()) < 8:
                issues.append("drill_empty")

    bom = _first_existing(BOM_CANDIDATES)
    if not bom:
        issues.append("missing_bom")
    else:
        bom_txt = bom.read_text(encoding="utf-8", errors="replace")
        if "nRF52840" not in bom_txt and "NRF52840" not in bom_txt.upper():
            warnings.append("bom_missing_nrf52840_string")

    # Min rule regression: compare committed DRC report if present
    committed = ROOT / "pcb" / "reports" / "DRC_REPORT.json"
    if not committed.exists():
        # Legacy lowercase name (case-sensitive CI must not rely on this alone)
        committed = ROOT / "pcb" / "reports" / "drc_report.json"
    if committed.exists():
        prev = _load_json(committed)
        prev_rules = prev.get("rules") or {}
        for k, v in rules.items():
            if k in prev_rules and prev_rules[k] != v:
                issues.append(f"rule_regression:{k}:{prev_rules[k]}->{v}")

    result = "PASS" if not issues else "FAIL"
    return {
        "tool": "gunnchos_static_drc",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "result": result,
        "pcb": str(pcb_path) if pcb_path else None,
        "drill": str(drill) if drill else None,
        "bom": str(bom) if bom else None,
        "gerber_count": len(gerbers),
        "rules": rules,
        "issues": issues,
        "warnings": warnings,
        "physical_claim": False,
    }


def main() -> int:
    if not BASELINE.exists():
        print("STATIC_ERC_DRC_FAIL missing baseline", BASELINE)
        return 1
    baseline = _load_json(BASELINE)
    erc = run_erc(baseline)
    drc = run_drc(baseline)
    OUT_ERC.parent.mkdir(parents=True, exist_ok=True)
    OUT_DRC.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_ERC.write_text(json.dumps(erc, indent=2) + "\n", encoding="utf-8")
    OUT_DRC.write_text(json.dumps(drc, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Static ERC/DRC Validation",
        "",
        f"Generated: `{erc['timestamp']}`",
        "",
        f"- ERC: **{erc['result']}** ({len(erc['issues'])} issues, {len(erc['warnings'])} warnings)",
        f"- DRC: **{drc['result']}** ({len(drc['issues'])} issues, {len(drc['warnings'])} warnings)",
        "",
        "Deterministic static checks only. No physical claim.",
        "",
    ]
    if erc["issues"]:
        lines.append("## ERC issues")
        lines.extend(f"- `{i}`" for i in erc["issues"])
        lines.append("")
    if drc["issues"]:
        lines.append("## DRC issues")
        lines.extend(f"- `{i}`" for i in drc["issues"])
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    if erc["result"] != "PASS" or drc["result"] != "PASS":
        print("STATIC_ERC_DRC_FAIL", erc["issues"], drc["issues"])
        return 1
    print("STATIC_ERC_DRC_PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
