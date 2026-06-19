from pathlib import Path
REQUIRED = [
    "product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md",
    "architecture/SYSTEM_BLOCK_DIAGRAM.md",
    "schematics/student_14/student_14_system_block.kicad_sch",
    "bom/student_14_bom.csv",
    "compliance/REGULATORY_MATRIX.md",
    "manufacturing/MANUFACTURING_READINESS_CHECKLIST.md",
]
def test_files_exist():
    root = Path(__file__).resolve().parents[1]
    missing = [p for p in REQUIRED if not (root / p).exists()]
    assert not missing, missing
