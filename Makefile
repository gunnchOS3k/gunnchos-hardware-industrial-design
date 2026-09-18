.PHONY: test validate validate-bom validate-cad validate-schematics \
	generate-device-reports generate-campus-kits generate-contracts \
	generate-manufacturing-package generate-hbom diagrams e2e smoke gate6-dry-run \
	validate-digital-mfg supervisor-eda-checks

test:
	pytest -q

validate:
	python3 scripts/hardware_validate.py
	python3 scripts/validate_digital_manufacturing.py

validate-digital-mfg:
	python3 scripts/validate_digital_manufacturing.py

supervisor-eda-checks:
	bash scripts/run_supervisor_eda_checks.sh

validate-bom:
	python3 scripts/validate_bom_schema.py

validate-cad:
	python3 scripts/validate_cad_tree.py

validate-schematics:
	python3 scripts/validate_schematics.py

generate-device-reports:
	python3 scripts/generate_device_reports.py

generate-campus-kits:
	python3 scripts/generate_campus_device_kits.py

generate-contracts:
	python3 scripts/generate_contracts.py
	python3 scripts/generate_hbom.py

generate-manufacturing-package:
	python3 scripts/generate_manufacturing_package.py

diagrams:
	@echo "Diagrams in docs/diagrams/ (Mermaid)"

e2e:
	@mkdir -p results/e2e
	$(MAKE) validate
	$(MAKE) validate-bom validate-cad validate-schematics
	$(MAKE) generate-device-reports generate-campus-kits generate-contracts generate-manufacturing-package
	pytest -q 2>&1 | tee results/e2e/e2e_terminal_output.txt || true
	python3 scripts/generate_device_spec_tables.py
	bash scripts/render_openscad.sh >> results/e2e/e2e_terminal_output.txt 2>&1 || echo "OpenSCAD optional"
	python3 scripts/make_e2e_report.py
	python3 scripts/run_all_tool_exports.py 2>> results/e2e/e2e_terminal_output.txt || true
	$(MAKE) e2e-tooling 2>> results/e2e/e2e_terminal_output.txt || true
	python3 scripts/e2e_check_required_artifacts.py

smoke: e2e

e2e-tooling:
	@mkdir -p results/tool_exports
	python3 scripts/run_all_tool_exports.py 2>/dev/null || python3 scripts/check_optional_backends.py || true

e2e-sionna e2e-deepmimo e2e-aerial e2e-oran:
	@echo "Optional target $@ — requires external install; not run in default CI"

# Gate 6 harness only — synthetic/emulated; DESIGN_ONLY / HARDWARE_PROTOTYPE_PENDING
gate6-dry-run:
	python3 scripts/gate6_dry_run.py

# Continuation VI — EDA closure / KiCad resume
.PHONY: continuation-vi validate-continuation-vi kicad-validate-family placeholder-scan-vi
.PHONY: continuation-vii validate-continuation-vii

continuation-vi:
	$(PYTHON) scripts/continuation_vi_eda_closure.py

validate-continuation-vi:
	$(PYTHON) scripts/validate_continuation_vi.py

continuation-vii:
	$(PYTHON) scripts/continuation_vii_eda_release_clean.py

validate-continuation-vii:
	$(PYTHON) scripts/validate_continuation_vii.py

kicad-validate-family:
	bash scripts/run_family_kicad_cli.sh

placeholder-scan-vi:
	$(PYTHON) scripts/continuation_vi_eda_closure.py

.PHONY: continuation-viii validate-continuation-viii
continuation-viii:
	$(PYTHON) scripts/continuation_viii_manufacturer_release.py
validate-continuation-viii:
	$(PYTHON) scripts/validate_continuation_viii.py

.PHONY: continuation-ix validate-continuation-ix release
continuation-ix:
	$(PYTHON) scripts/continuation_ix_pre_evt_hardware_lock.py
validate-continuation-ix:
	$(PYTHON) scripts/validate_continuation_ix.py
release: continuation-ix
	@echo Cont IX release artifacts in artifacts/continuation_ix_pre_evt/

# Hardware v1.0 mainline campaign (digital architecture / EVT prep — not physical pass)
PYTHON ?= python3
.PHONY: hardware-v1-generate hardware-v1-validate hardware-v1-gates hardware-v1-report hardware-v1-all
hardware-v1-generate:
	$(PYTHON) scripts/generate_hardware_v1_campaign.py

hardware-v1-validate:
	$(PYTHON) scripts/validate_hardware_v1.py

hardware-v1-gates:
	@test -f hardware_v1/GATES.json
	@$(PYTHON) -c "import json; g=json.load(open('hardware_v1/GATES.json')); keys=['HARDWARE_V1_READY_FOR_EVT_BUILD','HARDWARE_V1_DIGITAL_ARCHITECTURE_COMPLETE','REFERENCE_PLATFORM_0_READY_FOR_FAB','RP0_A_COTS_PROCUREMENT_PACKET_READY','RP0_A_READY_TO_ORDER','RP0_A_PHYSICAL_BUILD_PENDING','RP0_A_BRINGUP_PENDING','RP0_B_CUSTOM_READY_FOR_FAB','PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING','UNRES_NRF54L15_FOOTPRINT_CLOSED','UNRES_FN990B40_AVL_CLOSED','EXT_DSXL_DUAL_EDP_CLOSED','EXT_COM_HPC_400PIN_RP0_A_BLOCKING','EXT_COM_HPC_400PIN_RP0_B_BLOCKING','EXT_JHL8440_BALLMAP_RP0_A_BLOCKING','EXT_JHL8440_BALLMAP_RP0_B_BLOCKING','EXT_JHL9040R_BALLMAP_RP0_A_BLOCKING','EXT_JHL9040R_BALLMAP_RP0_B_BLOCKING','EVT_PENDING','DVT_PENDING','PVT_PENDING','PHYSICAL_HARDWARE_VALIDATED','CERTIFICATION_COMPLETE','MANUFACTURING_VALIDATED','RFQ_SENT','NEXT_OWNER_ACTION','NEXT_GATE'];\
[print(k+'='+str(g.get(k)).lower() if isinstance(g.get(k), bool) else k+'='+str(g.get(k))) for k in keys]"

hardware-v1-report:
	@test -f hardware_v1/REPORT_SECTION_33_A_TO_Z.md
	@echo "Report: hardware_v1/REPORT_SECTION_33_A_TO_Z.md"

hardware-v1-all: hardware-v1-generate hardware-v1-validate hardware-v1-gates hardware-v1-report
