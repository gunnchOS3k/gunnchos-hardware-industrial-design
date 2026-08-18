#!/usr/bin/env bash
# Supervisor-ready DIGITAL EDA checks: KiCad ERC/DRC if kicad-cli exists;
# OpenSCAD parse if openscad exists. Never claims fab / FCC / RFQ send.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/artifacts/supervisor_ready_eda"
mkdir -p "$OUT"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
STEP_TIMEOUT="${KICAD_STEP_TIMEOUT:-120}"

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

run_to() {
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
  echo "$rc" >"${logfile}.rc"
  return 0
}

count_severity() {
  local json="$1"
  local sev="$2"
  python3 - "$json" "$sev" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
sev = sys.argv[2]
if not p.exists() or p.stat().st_size == 0:
    print("absent")
    raise SystemExit(0)
try:
    data = json.loads(p.read_text())
except Exception as e:
    print(f"parse_error:{e}")
    raise SystemExit(0)
n = 0
for sheet in data.get("sheets") or []:
    for v in sheet.get("violations") or []:
        if str(v.get("severity", "")).lower() == sev:
            n += 1
for v in data.get("violations") or []:
    if str(v.get("severity", "")).lower() == sev:
        n += 1
print(n)
PY
}

PRODUCTS=(handheld_hybrid dock edge_io_rings student_14_5 ds_xl_coder)

if [[ -z "${KICAD_CLI}" || ! -x "${KICAD_CLI}" ]]; then
  cat >"$OUT/kicad_cli_meta.json" <<EOF
{
  "timestamp": "$TS",
  "status": "KICAD_CLI_ABSENT",
  "kicad_cli": null,
  "physical_claim": false,
  "fabrication_pass": false,
  "note": "kicad-cli not found this run. Prior recorded ERC/DRC JSON under device_designs/*/manufacturing/ERC_DRC_STATUS.json remain historical digital evidence only."
}
EOF
  echo "KICAD_CLI_ABSENT"
else
  VERSION="$("$KICAD_CLI" version 2>/dev/null || echo unknown)"
  mkdir -p "$OUT/kicad"
  declare -a SUMMARY_LINES=()
  for prod in "${PRODUCTS[@]}"; do
    SCH="$ROOT/device_designs/$prod/kicad/${prod}.kicad_sch"
    PCB="$ROOT/device_designs/$prod/kicad/${prod}.kicad_pcb"
    POUT="$OUT/kicad/$prod"
    mkdir -p "$POUT"
    erc_status="missing_sch"
    drc_status="missing_pcb"
    if [[ -f "$SCH" ]]; then
      run_to "$POUT/erc.log" "$KICAD_CLI" sch erc --format json --output "$POUT/erc.json" "$SCH"
      erc_status="ran"
    fi
    if [[ -f "$PCB" ]]; then
      run_to "$POUT/drc.log" "$KICAD_CLI" pcb drc --format json --output "$POUT/drc.json" "$PCB"
      drc_status="ran"
    fi
    erc_err="$(count_severity "$POUT/erc.json" error)"
    erc_warn="$(count_severity "$POUT/erc.json" warning)"
    drc_err="$(count_severity "$POUT/drc.json" error)"
    drc_warn="$(count_severity "$POUT/drc.json" warning)"
    python3 - "$POUT/summary.json" "$prod" "$erc_status" "$drc_status" "$erc_err" "$erc_warn" "$drc_err" "$drc_warn" <<'PY'
import json, sys
from pathlib import Path
out = Path(sys.argv[1])
payload = {
  "product": sys.argv[2],
  "erc_status": sys.argv[3],
  "drc_status": sys.argv[4],
  "erc_errors": sys.argv[5],
  "erc_warnings": sys.argv[6],
  "drc_errors": sys.argv[7],
  "drc_warnings": sys.argv[8],
  "fabrication_pass": False,
  "physical_claim": False,
          "note": "Zero ERC/DRC errors is digital hygiene only. DIGITAL_FABRICATION_PASS remains false. RFQ_SENT remains false.",
}
out.write_text(json.dumps(payload, indent=2) + "\n")
PY
    SUMMARY_LINES+=("$prod")
  done
  python3 - "$OUT/kicad_cli_meta.json" "$TS" "$KICAD_CLI" "$VERSION" "$OUT" <<'PY'
import json, sys
from pathlib import Path
meta_path = Path(sys.argv[1])
root = Path(sys.argv[5])
products = {}
for prod in ["handheld_hybrid", "dock", "edge_io_rings", "student_14_5", "ds_xl_coder"]:
    p = root / "kicad" / prod / "summary.json"
    products[prod] = json.loads(p.read_text()) if p.exists() else {"status": "missing"}
meta = {
  "timestamp": sys.argv[2],
  "status": "RAN",
  "kicad_cli": sys.argv[3],
  "version": sys.argv[4].strip(),
  "products": products,
  "physical_claim": False,
  "fabrication_pass": False,
  "fcc_ce_usbif_claimed": False,
  "rfq_sent": False,
}
meta_path.write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps(meta, indent=2))
PY
fi

OPENSCAD=""
if command -v openscad >/dev/null 2>&1; then
  OPENSCAD="$(command -v openscad)"
elif [[ -x /opt/homebrew/bin/openscad ]]; then
  OPENSCAD="/opt/homebrew/bin/openscad"
elif [[ -x /Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD ]]; then
  OPENSCAD="/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
fi

SCAD_FILES=(
  "cad/openscad/student_14.scad"
  "cad/openscad/handheld_hybrid.scad"
  "cad/openscad/ds_xl_coder.scad"
  "cad/openscad/wearables_arena_set.scad"
  "cad/openscad/student_14_5/student_14_5_concept.scad"
  "cad/openscad/handheld_hybrid/handheld_hybrid_concept.scad"
  "cad/openscad/ds_xl_coder/ds_xl_coder_concept.scad"
)

mkdir -p "$OUT/openscad"
if [[ -z "$OPENSCAD" ]]; then
  cat >"$OUT/openscad_meta.json" <<EOF
{
  "timestamp": "$TS",
  "status": "OPENSCAD_ABSENT",
  "openscad": null,
  "physical_claim": false,
  "note": "OpenSCAD CLI not found this run. Placeholder STL exports and EXPORT_STATUS remain historical digital evidence only — not certified mechanical drawings."
}
EOF
  echo "OPENSCAD_ABSENT"
else
  declare -a SCAD_RESULTS=()
  for rel in "${SCAD_FILES[@]}"; do
    src="$ROOT/$rel"
    safe="$(echo "$rel" | tr '/.' '__')"
    log="$OUT/openscad/${safe}.log"
    if [[ ! -f "$src" ]]; then
      echo "missing $rel" >"$log"
      echo "1" >"${log}.rc"
      continue
    fi
    # Parse/compile check only — do not overwrite manufacturing STLs.
    run_to "$log" "$OPENSCAD" -o "$OUT/openscad/${safe}.echo" --export-format echo "$src"
  done
  python3 - "$OUT" "$TS" "$OPENSCAD" <<'PY'
import json, sys
from pathlib import Path
out = Path(sys.argv[1]) / "openscad_meta.json"
root = Path(sys.argv[1]) / "openscad"
files = {}
for log in sorted(root.glob("*.log")):
    rc_path = Path(str(log) + ".rc")
    rc = rc_path.read_text().strip() if rc_path.exists() else "unknown"
    files[log.name] = {"rc": rc, "ok": rc == "0"}
meta = {
  "timestamp": sys.argv[2],
  "status": "RAN",
  "openscad": sys.argv[3],
  "files": files,
  "all_parse_ok": all(v.get("ok") for v in files.values()) if files else False,
  "physical_claim": False,
  "note": "Parse/echo export only. Not first-article print, not certified mechanical.",
}
out.write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps(meta, indent=2))
PY
fi

python3 - "$OUT" "$TS" <<'PY'
import json, sys
from pathlib import Path
out = Path(sys.argv[1])
kicad = {}
openscad = {}
kp = out / "kicad_cli_meta.json"
op = out / "openscad_meta.json"
if kp.exists():
    kicad = json.loads(kp.read_text())
if op.exists():
    openscad = json.loads(op.read_text())
summary = {
  "timestamp": sys.argv[2],
  "kicad": {"status": kicad.get("status"), "fabrication_pass": False},
  "openscad": {"status": openscad.get("status"), "physical_claim": False},
  "DIGITAL_FABRICATION_PASS": False,
  "PHYSICAL_PENDING": True,
  "EXTERNAL_PENDING": True,
  "rfq_sent": False,
  "fcc_ce_usbif": False,
}
(out / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
PY
echo "supervisor_eda_checks_complete"
