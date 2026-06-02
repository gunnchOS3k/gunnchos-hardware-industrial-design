.PHONY: test e2e

test:
	pytest -q

e2e:
	@mkdir -p results/e2e
	pytest -q 2>&1 | tee results/e2e/e2e_terminal_output.txt || true
	python3 scripts/validate_bom_schema.py
	python3 scripts/validate_cad_tree.py
	python3 scripts/generate_device_spec_tables.py
	bash scripts/render_openscad.sh >> results/e2e/e2e_terminal_output.txt 2>&1 || echo "OpenSCAD optional"
	python3 scripts/make_e2e_report.py
	python3 scripts/generate_campus_device_kits.py >> results/e2e/e2e_terminal_output.txt
	python3 scripts/e2e_check_required_artifacts.py


# Smoke test only — not evidence of readiness
smoke: e2e
