.PHONY: test validate validate-bom validate-cad validate-schematics \
	generate-device-reports generate-campus-kits generate-contracts \
	generate-manufacturing-package generate-hbom diagrams e2e smoke

test:
	pytest -q

validate:
	python3 scripts/hardware_validate.py

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
