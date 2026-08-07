#!/usr/bin/env bash
# Best-effort KiCad CLI validation for Edge I/O Ring gate1 sources.
# Soft-skips when kicad-cli is absent (exit 0 with KICAD_CLI_ABSENT).
# Static ERC/DRC is mandatory separately via static_erc_drc_validator.py.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_DIR="$ROOT/validation/kicad_cli"
mkdir -p "$REPORT_DIR"

KICAD_CLI="${KICAD_CLI:-}"
if [[ -z "$KICAD_CLI" ]]; then
  for candidate in \
    "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli" \
    "/Applications/KiCad 9.0.app/Contents/MacOS/kicad-cli" \
    "/Applications/KiCad 10.0.app/Contents/MacOS/kicad-cli"; do
    if [[ -x "$candidate" ]]; then
      KICAD_CLI="$candidate"
      break
    fi
  done
fi
if [[ -z "$KICAD_CLI" ]] && command -v kicad-cli >/dev/null 2>&1; then
  KICAD_CLI="$(command -v kicad-cli)"
fi

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
META="$REPORT_DIR/kicad_cli_meta.json"

if [[ -z "${KICAD_CLI}" || ! -x "${KICAD_CLI}" ]]; then
  cat >"$META" <<EOF
{
  "timestamp": "$TS",
  "status": "KICAD_CLI_ABSENT",
  "kicad_cli": null,
  "version": null,
  "note": "kicad-cli not found; static ERC/DRC remains mandatory. No physical claim."
}
EOF
  echo "KICAD_CLI_ABSENT"
  exit 0
fi

VERSION="$("$KICAD_CLI" version 2>/dev/null || "$KICAD_CLI" --version 2>/dev/null || echo unknown)"
SCH="$ROOT/schematic/kicad/edge_io_ring_evt0.kicad_sch"
PCB="$ROOT/pcb/kicad/edge_io_ring_evt0.kicad_pcb"
[[ -f "$SCH" ]] || SCH="$ROOT/schematic/edge_io_ring.kicad_sch"
[[ -f "$PCB" ]] || PCB="$ROOT/pcb/edge_io_ring.kicad_pcb"

OUT_GERBER="$REPORT_DIR/gerbers"
OUT_DRILL="$REPORT_DIR/drill"
OUT_BOM="$REPORT_DIR/bom"
mkdir -p "$OUT_GERBER" "$OUT_DRILL" "$OUT_BOM"

STATUS="BEST_EFFORT"
NOTES_FILE="$REPORT_DIR/notes.txt"
: >"$NOTES_FILE"

run_step() {
  local name="$1"; shift
  set +e
  "$@" >"$REPORT_DIR/${name}.log" 2>&1
  local rc=$?
  set -e
  if [[ $rc -ne 0 ]]; then
    echo "${name}_rc=${rc}" >>"$NOTES_FILE"
    STATUS="PARTIAL"
  else
    echo "${name}_ok" >>"$NOTES_FILE"
  fi
}

# Generated sexp boards may not fully open in KiCad; capture failures without hard-failing.
if [[ -f "$SCH" ]]; then
  run_step erc "$KICAD_CLI" sch erc --format json --output "$REPORT_DIR/erc_cli.json" "$SCH" || true
  run_step sch_export_netlist "$KICAD_CLI" sch export netlist --format kicadsexpr --output "$REPORT_DIR/netlist_cli.sexp" "$SCH" || true
  run_step sch_export_bom "$KICAD_CLI" sch export bom --output "$OUT_BOM/bom_cli.csv" "$SCH" || true
fi

if [[ -f "$PCB" ]]; then
  run_step drc "$KICAD_CLI" pcb drc --format json --output "$REPORT_DIR/drc_cli.json" "$PCB" || true
  run_step gerber "$KICAD_CLI" pcb export gerbers --output "$OUT_GERBER" "$PCB" || true
  run_step drill "$KICAD_CLI" pcb export drill --output "$OUT_DRILL" "$PCB" || true
  run_step pos "$KICAD_CLI" pcb export pos --output "$OUT_BOM/pick_place_cli.csv" "$PCB" || true
fi

PARITY="SKIPPED"
if [[ -d "$ROOT/pcb/gerbers" ]]; then
  committed=$(find "$ROOT/pcb/gerbers" -name '*.gbr' | wc -l | tr -d ' ')
  cli_count=$(find "$OUT_GERBER" -name '*.gbr' 2>/dev/null | wc -l | tr -d ' ')
  if [[ "$cli_count" -gt 0 ]]; then
    PARITY="CLI_GERBERS=${cli_count}_COMMITTED=${committed}"
  else
    PARITY="CLI_GERBERS_UNAVAILABLE_COMMITTED=${committed}"
  fi
fi

python3 - <<PY
import json
from pathlib import Path
notes = Path("$NOTES_FILE").read_text().split()
meta = {
  "timestamp": "$TS",
  "status": "$STATUS",
  "kicad_cli": "$KICAD_CLI",
  "version": """$VERSION""".strip(),
  "schematic": "$SCH",
  "pcb": "$PCB",
  "notes": notes,
  "parity": "$PARITY",
  "physical_claim": False,
}
Path("$META").write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps(meta, indent=2))
PY

echo "KICAD_CLI_VALIDATION_${STATUS}"
exit 0
