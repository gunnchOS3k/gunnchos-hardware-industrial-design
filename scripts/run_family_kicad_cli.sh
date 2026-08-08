#!/usr/bin/env bash
# Family-wide KiCad CLI validation / export — soft-skip if absent.
# Each CLI step is time-bounded so skeleton boards cannot hang CI forever.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_ROOT="$ROOT/docs/full_product_family/evidence/kicad_cli"
mkdir -p "$REPORT_ROOT"

KICAD_CLI="${KICAD_CLI:-}"
if [[ -z "$KICAD_CLI" ]]; then
  for candidate in \
    "/opt/homebrew/bin/kicad-cli" \
    "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli" \
    "/Applications/KiCad 9.0.app/Contents/MacOS/kicad-cli" \
    "/Applications/KiCad 10.0.app/Contents/MacOS/kicad-cli"; do
    if [[ -x "$candidate" ]]; then KICAD_CLI="$candidate"; break; fi
  done
fi
if [[ -z "$KICAD_CLI" ]] && command -v kicad-cli >/dev/null 2>&1; then
  KICAD_CLI="$(command -v kicad-cli)"
fi

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
META="$REPORT_ROOT/family_kicad_cli_meta.json"
PRODUCTS=(handheld_hybrid dock edge_io_rings student_14_5 ds_xl_coder)
STEP_TIMEOUT="${KICAD_STEP_TIMEOUT:-90}"

run_to() {
  local name="$1"; shift
  local logfile="$1"; shift
  set +e
  if command -v timeout >/dev/null 2>&1; then
    timeout "$STEP_TIMEOUT" "$@" >"$logfile" 2>&1
  elif command -v gtimeout >/dev/null 2>&1; then
    gtimeout "$STEP_TIMEOUT" "$@" >"$logfile" 2>&1
  else
    "$@" >"$logfile" 2>&1
  fi
  local rc=$?
  set -e
  echo "${name}_rc=${rc}" >>"${logfile}.rc"
  return 0
}

if [[ -z "${KICAD_CLI}" || ! -x "${KICAD_CLI}" ]]; then
  cat >"$META" <<EOF
{
  "timestamp": "$TS",
  "status": "KICAD_CLI_ABSENT",
  "kicad_cli": null,
  "products": ["handheld_hybrid", "dock", "edge_io_rings", "student_14_5", "ds_xl_coder"],
  "note": "Resume after Edmund brew install; static validators remain mandatory.",
  "physical_claim": false
}
EOF
  echo "KICAD_CLI_ABSENT"
  exit 0
fi

VERSION="$("$KICAD_CLI" version 2>/dev/null || echo unknown)"
STATUS="BEST_EFFORT"
declare -a PRODUCT_STATUS=()

for prod in "${PRODUCTS[@]}"; do
  SCH="$ROOT/device_designs/$prod/kicad/${prod}.kicad_sch"
  PCB="$ROOT/device_designs/$prod/kicad/${prod}.kicad_pcb"
  OUT="$REPORT_ROOT/$prod"
  mkdir -p "$OUT/gerbers" "$OUT/drill" "$OUT/pos"
  : >"$OUT/steps.rc"
  if [[ -f "$SCH" ]]; then
    run_to erc "$OUT/erc.log" "$KICAD_CLI" sch erc --format json --output "$OUT/erc.json" "$SCH"
    run_to netlist "$OUT/netlist.log" "$KICAD_CLI" sch export netlist --format kicadsexpr --output "$OUT/netlist.sexp" "$SCH"
  else
    echo "missing_sch" >>"$OUT/steps.rc"
    STATUS="PARTIAL"
  fi
  if [[ -f "$PCB" ]]; then
    run_to drc "$OUT/drc.log" "$KICAD_CLI" pcb drc --format json --output "$OUT/drc.json" "$PCB"
    run_to gerber "$OUT/gerber.log" "$KICAD_CLI" pcb export gerbers --output "$OUT/gerbers" "$PCB"
    run_to drill "$OUT/drill.log" "$KICAD_CLI" pcb export drill --output "$OUT/drill" "$PCB"
    run_to pos "$OUT/pos.log" "$KICAD_CLI" pcb export pos --output "$OUT/pos/pick_place.csv" "$PCB"
    run_to step "$OUT/step.log" "$KICAD_CLI" pcb export step --output "$OUT/board.step" "$PCB"
  else
    echo "missing_pcb" >>"$OUT/steps.rc"
    STATUS="PARTIAL"
  fi
  PRODUCT_STATUS+=("$prod")
done

python3 - <<PY
import json
from pathlib import Path
root = Path("$REPORT_ROOT")
products = {}
for prod in ["handheld_hybrid", "dock", "edge_io_rings", "student_14_5", "ds_xl_coder"]:
    out = root / prod
    info = {"dir": str(out.relative_to(Path("$ROOT"))) if out.exists() else None}
    for name in ("erc.json", "drc.json", "board.step", "netlist.sexp"):
        p = out / name
        info[name] = p.exists() and p.stat().st_size > 0
    gerbers = list((out / "gerbers").glob("*")) if (out / "gerbers").exists() else []
    info["gerber_count"] = len(gerbers)
    erc = out / "erc.json"
    if erc.exists():
        try:
            data = json.loads(erc.read_text())
            # KiCad ERC JSON shapes vary; record raw keys + violation heuristic
            info["erc_keys"] = sorted(list(data.keys()))[:20]
            text = erc.read_text(encoding="utf-8", errors="ignore")
            info["erc_mentions_violations"] = ("violations" in text.lower())
        except Exception as e:
            info["erc_parse_error"] = str(e)
    products[prod] = info
meta = {
  "timestamp": "$TS",
  "status": "$STATUS",
  "kicad_cli": "$KICAD_CLI",
  "version": "$VERSION".strip(),
  "products": products,
  "physical_claim": False,
  "note": "CLI ran; Device:R skeleton boards expected to ERC-fail until vendor libs. No FULL release claim.",
}
Path("$META").write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps(meta, indent=2))
PY
echo "KICAD_CLI_FAMILY_${STATUS}"
exit 0
