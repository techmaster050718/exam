"""
Comprehensive validation script for IBPS SO IT Master Papers:
- data/ibps-so-it-prelims-master-001.json
- data/ibps-so-it-mains-master-001.json
"""
import json
import os
from collections import Counter

def validate_paper(filepath, expected_total, expected_sections):
    print(f"\n==========================================")
    print(f"VALIDATING: {filepath}")
    print(f"==========================================")
    
    assert os.path.exists(filepath), f"File {filepath} does not exist!"
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    paper_id = data.get("id")
    title = data.get("title")
    source_type = data.get("sourceType")
    disclaimer = data.get("disclaimer")
    sections = data.get("sections", [])
    
    print(f"Paper ID: {paper_id}")
    print(f"Title: {title}")
    print(f"Source Type: {source_type}")
    print(f"Disclaimer: {disclaimer[:60]}...")
    print(f"Section Count: {len(sections)} (Expected {len(expected_sections)})")
    
    total_q = 0
    all_q_texts = []
    answer_dist = Counter()
    difficulty_dist = Counter()
    topic_dist = Counter()
    
    invalid_option_count = 0
    duplicate_q_count = 0
    ambiguous_count = 0
    max_run = 1
    cur_run = 1
    last_ans = None
    
    for s_idx, sec in enumerate(sections):
        sec_name = sec.get("name")
        exp_sec_name, exp_sec_count = expected_sections[s_idx]
        assert sec_name == exp_sec_name, f"Section mismatch: got '{sec_name}', expected '{exp_sec_name}'"
        
        q_list = sec.get("questions", [])
        sec_q_count = len(q_list)
        print(f"  Section {s_idx + 1}: '{sec_name}' -> {sec_q_count} questions (Expected {exp_sec_count})")
        assert sec_q_count == exp_sec_count, f"Section count mismatch: {sec_q_count} vs {exp_sec_count}"
        
        for q_idx, q in enumerate(q_list):
            total_q += 1
            q_text = q.get("q", "").strip()
            options = q.get("options", [])
            ans = q.get("answer")
            diff = q.get("difficulty", "Moderate")
            topic = q.get("topic", "General")
            
            difficulty_dist[diff] += 1
            topic_dist[topic] += 1
            answer_dist[ans] += 1
            
            # Run check
            if last_ans is not None and ans == last_ans:
                cur_run += 1
                if cur_run > max_run:
                    max_run = cur_run
            else:
                cur_run = 1
            last_ans = ans
            
            # Duplication check
            if q_text in all_q_texts:
                duplicate_q_count += 1
            all_q_texts.append(q_text)
            
            # Option checks
            if len(options) != 4:
                invalid_option_count += 1
            if len(set(options)) != 4:
                invalid_option_count += 1
            for opt in options:
                opt_str = str(opt).strip().lower()
                if "all of the above" in opt_str or "none of the above" in opt_str:
                    ambiguous_count += 1
                if not opt_str:
                    invalid_option_count += 1
                    
            if not isinstance(ans, int) or ans < 0 or ans > 3:
                invalid_option_count += 1
                
    assert total_q == expected_total, f"Total question count mismatch: {total_q} vs {expected_total}"
    
    print("\n--- Summary Metrics ---")
    print(f"Total Questions: {total_q}")
    print(f"Answer Distribution: {dict(sorted(answer_dist.items()))}")
    print(f"Max Consecutive Run of Same Answer: {max_run}")
    print(f"Difficulty Breakdown: {dict(difficulty_dist)}")
    print(f"Topic Count: {len(topic_dist)} topics covered")
    print(f"Duplicate Questions: {duplicate_q_count}")
    print(f"Ambiguous / Disallowed Options ('All/None of above'): {ambiguous_count}")
    print(f"Invalid Option Count: {invalid_option_count}")
    print(f"Validation Status: {'PASS' if duplicate_q_count == 0 and ambiguous_count == 0 and invalid_option_count == 0 else 'FAIL'}")
    
    return {
        "paper_id": paper_id,
        "total": total_q,
        "answer_dist": dict(sorted(answer_dist.items())),
        "max_run": max_run,
        "difficulty": dict(difficulty_dist),
        "topics": len(topic_dist),
        "duplicates": duplicate_q_count,
        "ambiguous": ambiguous_count,
        "invalid_opts": invalid_option_count,
        "status": "PASS" if duplicate_q_count == 0 and ambiguous_count == 0 and invalid_option_count == 0 else "FAIL"
    }

if __name__ == "__main__":
    r1 = validate_paper(
        "data/ibps-so-it-prelims-master-001.json",
        150,
        [
            ("English Language", 50),
            ("Reasoning Ability", 50),
            ("Quantitative Aptitude", 50)
        ]
    )
    
    r2 = validate_paper(
        "data/ibps-so-it-mains-master-001.json",
        60,
        [
            ("Professional Knowledge", 60)
        ]
    )
    
    # Check papers.json entry
    with open("data/papers.json", "r") as f:
        papers = json.load(f)
    p_ids = [p["id"] for p in papers]
    assert "ibps-so-it-prelims-master-001" in p_ids, "Prelims paper missing in papers.json!"
    assert "ibps-so-it-mains-master-001" in p_ids, "Mains paper missing in papers.json!"
    print("\n[OK] Both papers correctly linked and registered in data/papers.json under 'ibps-so-it'.")

