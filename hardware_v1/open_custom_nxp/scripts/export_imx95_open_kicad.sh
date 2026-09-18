#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
KICAD="${ROOT}/hardware_v1/open_custom_nxp/kicad"
OUT="${ROOT}/artifacts/digital_engineering_exhaustion/stream_e/nxp_kicad_cli"
mkdir -p "$OUT"
CLI="${KICAD_CLI:-/opt/homebrew/bin/kicad-cli}"
if [[ ! -x "$CLI" ]]; then echo "KICAD_CLI_ABSENT"; exit 0; fi
"$CLI" sch erc --format json --output "$OUT/erc.json" "$KICAD/imx95_open_custom.kicad_sch" || true
"$CLI" pcb drc --format json --output "$OUT/drc.json" "$KICAD/imx95_open_custom.kicad_pcb" || true
"$CLI" pcb export gerbers --output "$OUT/gerbers" "$KICAD/imx95_open_custom.kicad_pcb" || true
"$CLI" pcb export drill --output "$OUT/drill" "$KICAD/imx95_open_custom.kicad_pcb" || true
echo "wrote $OUT"
