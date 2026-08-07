#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 "bom/assembly_bom.csv","electrical/component_selection.yaml",
 "schematic/edge_io_ring.kicad_sch","schematic/edge_io_ring.net.json",
 "pcb/edge_io_ring.kicad_pcb","pcb/gerbers/edge_io_ring-F_Cu.gbr",
 "pcb/gerbers/edge_io_ring-Edge_Cuts.gbr","pcb/drill/edge_io_ring.drl",
 "pcb/reports/ERC_REPORT.json","pcb/reports/DRC_REPORT.json",
 "mechanical/edge_io_ring.scad","docs/STATUS.md",
]
missing=[r for r in required if not (ROOT/r).exists()]
erc=json.loads((ROOT/"pcb/reports/ERC_REPORT.json").read_text())
drc=json.loads((ROOT/"pcb/reports/DRC_REPORT.json").read_text())
if missing or erc.get("result")!="PASS" or drc.get("result")!="PASS":
    print("DIGITAL_FAB_FAIL", missing, erc.get("result"), drc.get("result")); sys.exit(1)
print("DIGITAL_FAB_PASS"); sys.exit(0)
