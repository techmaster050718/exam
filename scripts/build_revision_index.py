"""
Scans data/revision and creates data/revision/revision-index.json
"""
import json
import os
import glob

def build_index():
    revision_files = sorted(glob.glob("data/revision/**/*.md", recursive=True))
    
    categories = [
        {
            "id": "computer-science",
            "name": "Computer Science & IT (Mains / Specialist)",
            "icon": "💻",
            "description": "DSA, Algorithms, Complexity, OS, DBMS, Networks, Architecture, OOP, SE, Security, Cloud, AI/ML, Banking Tech",
            "files": [
                "data/revision/data-structures/data-structures-revision.md",
                "data/revision/algorithms/algorithms-revision.md",
                "data/revision/algorithms/complexity-revision.md",
                "data/revision/os/os-revision.md",
                "data/revision/dbms/dbms-revision.md",
                "data/revision/computer-networks/networks-revision.md",
                "data/revision/computer-architecture/architecture-revision.md",
                "data/revision/programming/programming-revision.md",
                "data/revision/software-engineering/se-revision.md",
                "data/revision/cybersecurity/security-revision.md",
                "data/revision/cloud-computing/cloud-revision.md",
                "data/revision/ai-ml/ai-ml-revision.md",
                "data/revision/banking-technology/banking-tech-revision.md"
            ]
        },
        {
            "id": "aptitude-reasoning",
            "name": "Quantitative Aptitude & Reasoning Ability",
            "icon": "🧮",
            "description": "Arithmetic, Algebra, Geometry, Speed Math Tables, Verbal & Non-Verbal Reasoning, Puzzles",
            "files": [
                "data/revision/aptitude/aptitude-revision.md",
                "data/revision/aptitude/number-tables.md",
                "data/revision/reasoning/reasoning-revision.md"
            ]
        },
        {
            "id": "english-verbal",
            "name": "English Language & Verbal Ability",
            "icon": "📚",
            "description": "Grammar Rules, Subject-Verb Agreement, Voice/Speech, Vocabulary, Idioms, Error Spotting",
            "files": [
                "data/revision/english/english-revision.md"
            ]
        },
        {
            "id": "general-science",
            "name": "General Science (Physics, Chemistry, Biology)",
            "icon": "🔬",
            "description": "Physics Formulas & Laws, Chemistry Reactions & Compounds, Biology Human Systems & Cell",
            "files": [
                "data/revision/physics/physics-revision.md",
                "data/revision/chemistry/chemistry-revision.md",
                "data/revision/biology/biology-revision.md"
            ]
        },
        {
            "id": "general-studies",
            "name": "General Studies & Humanities",
            "icon": "🏛️",
            "description": "Indian Polity & Constitution, Indian & Physical Geography, Indian History Timeline",
            "files": [
                "data/revision/polity/polity-revision.md",
                "data/revision/geography/geography-revision.md",
                "data/revision/history/history-revision.md"
            ]
        },
        {
            "id": "defence-gk-exam",
            "name": "Defence, Static GK & Target Exam Modules",
            "icon": "🎖️",
            "description": "Armed Forces, Commands, Missiles, International Orgs, Exam-Specific Strategy (IBPS SO, UP SI, ALP, ISRO)",
            "files": [
                "data/revision/defence/defence-revision.md",
                "data/revision/general-awareness/general-awareness-revision.md",
                "data/revision/exam-specific/exam-specific-revision.md"
            ]
        }
    ]

    modules_list = []
    total_lines = 0
    total_words = 0

    for file_path in revision_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        line_count = len(lines)
        word_count = len(content.split())
        total_lines += line_count
        total_words += word_count

        # Extract title from first heading
        title = ""
        subtopics = []
        for line in lines:
            if line.startswith("# ") and not title:
                title = line[2:].strip()
            elif line.startswith("## "):
                subtopics.append(line[3:].strip())

        module_id = os.path.basename(file_path).replace(".md", "")
        category_match = "general"
        for cat in categories:
            if file_path in cat["files"]:
                category_match = cat["id"]
                break

        modules_list.append({
            "id": module_id,
            "title": title or module_id.title(),
            "file": file_path,
            "category": category_match,
            "lineCount": line_count,
            "wordCount": word_count,
            "estimatedReadMin": max(3, round(word_count / 150)),
            "subtopicsCount": len(subtopics),
            "subtopics": subtopics[:15]
        })

    index_data = {
        "title": "Lakshya Question Bank — Master Revision Encyclopedia",
        "description": "High-density exam revision materials covering all 79 papers and 21 exam subjects present in the question bank.",
        "version": "1.0",
        "lastUpdated": "2026-11-15",
        "totalModules": len(modules_list),
        "totalLines": total_lines,
        "totalWords": total_words,
        "categories": categories,
        "modules": modules_list
    }

    with open("data/revision/revision-index.json", "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"Built revision-index.json successfully!")
    print(f"Total modules: {len(modules_list)}")
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")

if __name__ == "__main__":
    build_index()

