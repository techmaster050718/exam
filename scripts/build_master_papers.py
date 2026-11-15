"""
Script to assemble and write:
1. data/ibps-so-it-prelims-master-001.json
2. data/ibps-so-it-mains-master-001.json
"""
import json
import os
import sys

sys.path.append(os.path.dirname(__file__))

from prelims_english import ENGLISH_QUESTIONS
from prelims_reasoning import REASONING_QUESTIONS
from prelims_quant import QUANT_QUESTIONS
from mains_pk import MAINS_PK_QUESTIONS
from balance_helper import rebalance_questions, make_balanced_pattern

def build_papers():
    # 1. Prelims Sections
    # Target counts per section to reach overall 38, 38, 37, 37:
    # Section 1 (English): 13, 13, 12, 12
    # Section 2 (Reasoning): 12, 13, 13, 12
    # Section 3 (Quant): 13, 12, 12, 13
    pat_eng = make_balanced_pattern(50, counts=[13, 13, 12, 12])
    pat_reas = make_balanced_pattern(50, counts=[12, 13, 13, 12])
    pat_quant = make_balanced_pattern(50, counts=[13, 12, 12, 13])

    rebalanced_eng = rebalance_questions(ENGLISH_QUESTIONS, pat_eng)
    rebalanced_reas = rebalance_questions(REASONING_QUESTIONS, pat_reas)
    rebalanced_quant = rebalance_questions(QUANT_QUESTIONS, pat_quant)

    prelims_paper = {
        "id": "ibps-so-it-prelims-master-001",
        "title": "IBPS SO IT Officer (Prelims) — Master Paper 1",
        "subtitle": "150 Questions | 120 Mins | English, Reasoning & Quant",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "IBPS SO IT Officer (Scale-I) Preliminary Examination",
        "disclaimer": "High-yield practice paper based on IBPS SO IT Officer syllabus and recent exam patterns; not an authentic official PYQ paper.",
        "sections": [
            {
                "name": "English Language",
                "questions": rebalanced_eng
            },
            {
                "name": "Reasoning Ability",
                "questions": rebalanced_reas
            },
            {
                "name": "Quantitative Aptitude",
                "questions": rebalanced_quant
            }
        ]
    }

    prelims_path = os.path.join("data", "ibps-so-it-prelims-master-001.json")
    with open(prelims_path, "w", encoding="utf-8") as f:
        json.dump(prelims_paper, f, indent=2, ensure_ascii=False)
    print(f"Wrote Prelims paper to {prelims_path} with {len(rebalanced_eng) + len(rebalanced_reas) + len(rebalanced_quant)} questions.")

    # 2. Mains Section
    pat_mains = make_balanced_pattern(60, counts=[15, 15, 15, 15])
    rebalanced_mains = rebalance_questions(MAINS_PK_QUESTIONS, pat_mains)

    mains_paper = {
        "id": "ibps-so-it-mains-master-001",
        "title": "IBPS SO IT Officer (Mains) — Professional Knowledge Master Paper 1",
        "subtitle": "60 Questions | 45 Mins | IT Professional Knowledge",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "IBPS SO IT Officer (Scale-I) Main Examination",
        "disclaimer": "High-yield practice paper based on IBPS SO IT Officer syllabus and recent exam patterns; not an authentic official PYQ paper.",
        "sections": [
            {
                "name": "Professional Knowledge",
                "questions": rebalanced_mains
            }
        ]
    }

    mains_path = os.path.join("data", "ibps-so-it-mains-master-001.json")
    with open(mains_path, "w", encoding="utf-8") as f:
        json.dump(mains_paper, f, indent=2, ensure_ascii=False)
    print(f"Wrote Mains paper to {mains_path} with {len(rebalanced_mains)} questions.")

if __name__ == "__main__":
    build_papers()

