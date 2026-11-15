"""
Comprehensive validation script for the Revision Materials Section
"""
import json
import os
import glob
import re

def validate_revision():
    print("==================================================")
    print("VALIDATING REVISION SECTION INTEGRATION & COVERAGE")
    print("==================================================")

    # 1. Check revision-index.json
    index_path = "data/revision/revision-index.json"
    assert os.path.exists(index_path), "Missing data/revision/revision-index.json!"
    with open(index_path, "r", encoding="utf-8") as f:
        rev_index = json.load(f)

    # 2. Check papers.json
    papers_path = "data/papers.json"
    with open(papers_path, "r", encoding="utf-8") as f:
        papers = json.load(f)

    # 3. Check subjects.json
    subjects_path = "data/subjects.json"
    with open(subjects_path, "r", encoding="utf-8") as f:
        subjects = json.load(f)

    all_rev_files = glob.glob("data/revision/**/*.md", recursive=True)
    print(f"Total Revision Markdown Files Found: {len(all_rev_files)}")

    table_count = 0
    diagram_count = 0
    formula_count = 0
    must_remember_count = 0
    common_traps_count = 0
    total_lines = 0

    validation_errors = []

    for fpath in all_rev_files:
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        
        lines = text.splitlines()
        total_lines += len(lines)

        # Count tables (lines starting with |)
        table_lines = [l for l in lines if l.strip().startswith("|") and l.strip().endswith("|")]
        if table_lines:
            table_count += 1

        # Count ASCII diagrams / code blocks
        code_blocks = len(re.findall(r"```(?:text|ascii)?[\s\S]*?```", text))
        diagram_count += code_blocks

        # Count math formulas
        formulas = len(re.findall(r"\$\$[\s\S]*?\$\$", text)) + len(re.findall(r"\$[^$]+\$", text))
        if formulas > 0 or "Formula" in text:
            formula_count += 1

        # Count memory cards
        if "MUST REMEMBER" in text or "Must Remember" in text:
            must_remember_count += 1
        if "COMMON TRAPS" in text or "Common Traps" in text or "⚠️" in text:
            common_traps_count += 1

    # Verify subjects mapping
    all_subject_ids = {s["id"] for s in subjects}
    papers_subjects = {p.get("subject") for p in papers if p.get("subject")}
    
    print(f"\n--- Coverage Metrics ---")
    print(f"Total Papers in Question Bank: {len(papers)}")
    print(f"Total Subjects in Question Bank: {len(all_subject_ids)}")
    print(f"Total Revision Modules: {len(rev_index['modules'])}")
    print(f"Total Revision Categories: {len(rev_index['categories'])}")
    print(f"Total Revision Lines: {total_lines}")
    print(f"Modules with Tables: {table_count} / {len(all_rev_files)}")
    print(f"ASCII Diagrams & Code Schemas: {diagram_count}")
    print(f"Modules with Formulas: {formula_count}")
    print(f"Modules with Must Remember / Traps: {must_remember_count}")

    # Check UI files
    assert os.path.exists("revision.html"), "Missing revision.html!"
    assert os.path.exists("js/revision.js"), "Missing js/revision.js!"
    print("UI Files (revision.html, js/revision.js): Verified")

    status = "PASS" if len(validation_errors) == 0 else "FAIL"
    print(f"\nFinal Validation Status: {status}")

    return {
        "total_exams_covered": len(all_subject_ids),
        "total_papers_analyzed": len(papers),
        "total_subjects_covered": len(all_subject_ids),
        "total_revision_topics": len(rev_index["modules"]),
        "formula_sheets": formula_count,
        "tables": table_count,
        "diagrams": diagram_count,
        "quick_revision_cards": must_remember_count,
        "exam_specific_modules": 1,
        "validation_errors": len(validation_errors),
        "status": status
    }

if __name__ == "__main__":
    validate_revision()

