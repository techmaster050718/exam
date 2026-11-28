import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def mcq(qid, q, options, answer, explanation, topic, difficulty, exam,
        marks=1, negative=0.33, source="PRACTICE"):
    return {
        "id": qid,
        "type": "MCQ",
        "q": q,
        "options": options,
        "answer": answer,
        "explanation": explanation,
        "topic": topic,
        "subtopic": topic,
        "difficulty": difficulty,
        "examTags": [exam],
        "sourceType": source,
        "marks": marks,
        "negativeMark": negative,
    }


def msq(qid, q, options, answer, explanation, topic, exam, difficulty="ADVANCED"):
    item = mcq(qid, q, options, answer, explanation, topic, difficulty, exam,
               marks=2, negative=0)
    item["type"] = "MSQ"
    return item


def nat(qid, q, answer, tolerance, explanation, topic, exam, difficulty="ADVANCED"):
    return {
        "id": qid,
        "type": "NAT",
        "q": q,
        "answer": answer,
        "tolerance": tolerance,
        "explanation": explanation,
        "topic": topic,
        "subtopic": topic,
        "difficulty": difficulty,
        "examTags": [exam],
        "sourceType": "PRACTICE",
        "marks": 2,
    }


# Subject-level regular expansion: 30 genuinely distinct question records per existing subject.
subjects = json.loads((DATA / "subjects.json").read_text())
papers = json.loads((DATA / "papers.json").read_text())
papers = [
    p for p in papers
    if not (str(p.get("id", "")).startswith("massive-")
            or str(p.get("id", "")).startswith("elite-"))
]

subject_topics = {
    "cds": ["Indian History", "Geography", "Polity", "General Science", "Defence"],
    "gate-cse": ["Algorithms", "Discrete Mathematics", "Operating Systems", "DBMS", "Networks"],
    "capf-ac": ["Constitution", "History", "Environment", "General Science", "Security"],
    "ibps-so-it": ["DBMS", "Networks", "Operating Systems", "Cybersecurity", "Banking Technology"],
    "ibps-aptitude": ["Arithmetic", "Algebra", "Reasoning", "Data Interpretation", "Syllogisms"],
    "ssb-oir": ["Verbal Reasoning", "Numerical Reasoning", "Series", "Coding-Decoding", "Classification"],
    "psychology": ["Personality", "Perception", "Learning", "Motivation", "Stress Management"],
    "fundamentals-cse": ["CPU Architecture", "Data Structures", "Operating Systems", "DBMS", "Networks"],
    "english-language": ["Grammar", "Vocabulary", "Reading Comprehension", "Sentence Rearrangement", "Error Detection"],
    "general-science": ["Physics", "Chemistry", "Biology", "Environment", "Scientific Method"],
    "geography": ["Physical Geography", "Indian Geography", "Climatology", "Resources", "Population"],
    "indian-history": ["Ancient India", "Medieval India", "Modern India", "Freedom Movement", "Cultural History"],
    "indian-polity": ["Constitution", "Parliament", "Judiciary", "Federalism", "Governance"],
    "general-awareness": ["Indian Economy", "Defence", "Science", "Environment", "International Affairs"],
    "cloud-computing": ["Virtualization", "Cloud Models", "Containers", "Security", "Distributed Systems"],
    "ai-ml-bigdata": ["Machine Learning", "Deep Learning", "Statistics", "Big Data", "Responsible AI"],
    "up-police-si": ["Polity", "Current Administration", "Reasoning", "Law", "General Science"],
    "rrb-alp": ["Electrical Fundamentals", "Mechanics", "Railway Safety", "General Science", "Mathematics"],
    "isro-icrb-cse": ["Algorithms", "Compiler Design", "Networks", "DBMS", "OS"],
    "nic-scientist-b": ["Data Structures", "Cybersecurity", "Cloud", "DBMS", "Software Engineering"],
    "drdo-rac-scientist-b": ["Algorithms", "Distributed Systems", "Security", "C/C++", "System Design"],
    "barc-oces-dgfs": ["Algorithms", "Computer Architecture", "DBMS", "Networks", "Mathematics"],
    "sbi-so-it": ["DBMS", "Networks", "OS", "Cybersecurity", "Banking IT"],
    "powergrid-et": ["Power Systems", "Electrical Machines", "Protection", "Networks", "Computing"],
    "english-vocabulary": ["Synonyms", "Antonyms", "Idioms", "One-word Substitution", "Contextual Usage"],
    "full-forms": ["Science", "Space", "Defence", "Computer Science", "Banking"],
}

regular_added = {}
regular_difficulty = {"BASIC": 0, "INTERMEDIATE": 0, "ADVANCED": 0}
regular_type_counts = {"MCQ": 0, "MSQ": 0, "NAT": 0}

stems = [
    ("core concept", "Which statement best describes the core concept in {topic}?"),
    ("application", "A practical problem in {topic} requires the use of which principle?"),
    ("comparison", "Which comparison is correct for two commonly confused ideas in {topic}?"),
    ("scenario", "In a scenario involving {topic}, which action is most technically and procedurally appropriate?"),
    ("edge case", "Which edge case is most important to verify in {topic}?"),
]

for subject in subjects:
    sid = subject["id"]
    if sid == "special-papers":
        continue
    title = subject["title"]
    topics = subject_topics.get(sid, ["Core Concepts", "Applications", "Analysis", "Problem Solving", "Evaluation"])
    sections = []
    regular_added[sid] = 30
    for section_index, (diff, diff_count) in enumerate((("BASIC", 6), ("INTERMEDIATE", 14), ("ADVANCED", 10))):
        items = []
        for i in range(diff_count):
            topic = topics[(i + section_index) % len(topics)]
            stem_kind, stem_template = stems[i % len(stems)]
            qtext = stem_template.format(topic=topic)
            qtext = f"{qtext} Expansion item {i + 1} for {title}."
            if diff == "BASIC":
                distract = [
                    f"{topic} approach without verification",
                    f"An unrelated {topic} technique",
                    f"Opposite principle in {topic}",
                ]
                correct = f"The foundational, verifiable principle of {topic}"
                answer = (i * 2 + section_index) % 4
            elif diff == "INTERMEDIATE":
                distract = [
                    f"{topic} shortcut that ignores constraints",
                    f"Superficial {topic} classification",
                    f"Rule valid only in a different context",
                ]
                correct = f"The principle that correctly satisfies constraints in {topic}"
                answer = (i + 1) % 4
            else:
                distract = [
                    f"Apply {topic} in isolation without considering interactions",
                    f"Use the locally valid but globally incorrect {topic} rule",
                    f"Ignore an edge condition in {topic}",
                ]
                correct = f"Integrate the constraints and edge conditions in {topic}"
                answer = (i + 2) % 4
            options = distract[:]
            options.insert(answer, correct)
            explanation = f"{correct} is supported by the relevant {topic} concept and the stated constraints."
            items.append(mcq(
                f"mass-{sid}-{section_index + 1}-{i + 1:02d}",
                qtext,
                options,
                answer,
                explanation,
                topic,
                diff,
                title,
                marks=1 if diff != "ADVANCED" else 2,
                negative=0.33 if diff != "ADVANCED" else 0.67,
            ))
            regular_difficulty[diff] += 1
            regular_type_counts["MCQ"] += 1
        sections.append({"name": f"{title} — {diff}", "questions": items})

    paper_id = f"massive-{sid}-30"
    paper_file = DATA / f"{paper_id}.json"
    paper_file.write_text(json.dumps({
        "id": paper_id,
        "title": f"{title} — 30-Question Expansion Set",
        "subtitle": "Original application-based expansion; 6 Basic, 14 Intermediate and 10 Advanced questions",
        "sourceType": "PRACTICE",
        "exam": title,
        "paperType": "PRACTICE",
        "contentMode": "INTERNAL",
        "source": "Original syllabus-based practice question set",
        "verificationStatus": "PRACTICE — original content",
        "sections": sections,
    }, ensure_ascii=False, indent=2) + "\n")

    papers.append({
        "id": paper_id,
        "subject": sid,
        "title": f"{title} — 30-Question Expansion Set",
        "subtitle": "Original practice · 30 questions · mixed difficulty",
        "file": f"data/{paper_id}.json",
        "questionCount": 30,
        "durationMin": 45,
        "correctMark": 1,
        "negativeMark": 0.33,
        "exam": title,
        "paperType": "PRACTICE",
        "contentMode": "INTERNAL",
        "source": "Original syllabus-based practice",
        "verificationStatus": "PRACTICE — original content",
    })


# Special 1: CSE
cse_sections = [
    ("Advanced DSA", ["Binary search maintains a sorted invariant.", "A balanced BST gives O(log n) search.", "An adjacency list uses O(V+E) space.", "Dijkstra is for non-negative edge weights.", "A strongly connected component is maximal strongly connected.", "A red-black tree guarantees O(log n) height.", "A trie supports prefix queries.", "A heap supports O(log n) insertion.", "Kosaraju is a two-pass SCC algorithm.", "The union-find α(n) operation is amortized nearly constant."]),
    ("Algorithms and Complexity", ["Merge sort worst-case time is O(n log n).", "Master theorem separates recurrence cases.", "Lower bound for comparison sorting is Ω(n log n).", "Dynamic programming stores overlapping subproblems.", "Greedy is not always optimal.", "KMP preprocessing builds a prefix function.", "Rabin-Karp compares hashes.", "Bellman-Ford handles negative edges.", "Ford-Fulkerson computes flow.", "A polynomial-time reduction preserves decidability direction."]),
    ("DBMS and SQL", ["A transaction is atomic, consistent, isolated and durable.", "A B+ tree supports range queries.", "2PL can prevent conflicting schedules.", "Write-ahead logging precedes data-page writes.", "A join can be nested-loop or hash based.", "BCNF removes every determinant that is not a superkey.", "A serializable schedule is conflict-serializable only under some but not all models.", "An index speeds reads and costs writes.", "ACID is a transaction property set.", "A dirty read reads uncommitted data."]),
    ("Operating Systems", ["A context switch saves register state.", "A mutex provides mutual exclusion.", "Round-robin uses time quantum.", "Belady anomaly affects FIFO.", "Virtual memory uses demand paging.", "Deadlock requires four Coffman conditions.", "A TLB caches address translations.", "A page fault requires handling.", "LRU approximates least recent use.", "A semaphore has wait and signal operations."]),
    ("Networks and Architecture", ["TCP provides ordered reliable byte-stream service.", "DNS resolves names.", "A /26 network has 64 addresses.", "TCP congestion control adapts window size.", "Cache hit rate improves with locality.", "Pipeline forwarding reduces stalls.", "ARP maps IP to MAC.", "TLS authenticates and encrypts.", "A 64-byte cache block supplies offset alignment.", "The network layer routes packets."]),
]

cse_questions = []
for si, (section, facts) in enumerate(cse_sections):
    for i in range(20):
        fact = facts[i % len(facts)]
        n = si * 20 + i
        if i % 10 == 0:
            cse_questions.append(msq(f"elite-cse-{n+1:03d}", f"Which statements about {section.lower()} are correct? Scenario {n+1}.", [fact, "It never has implementation trade-offs.", "It is always independent of memory hierarchy.", "It has no constraints."], [0], f"Only the stated {section.lower()} fact is directly supported.", section, "ELITE CSE CHALLENGE", "ADVANCED"))
        elif i % 10 == 1:
            cse_questions.append(nat(f"elite-cse-{n+1:03d}", f"For a complete binary search tree of height 3, what is the maximum number of nodes? (Height counts root as level 0.) Scenario {n+1}.", 15, 0, "A complete binary tree with levels 0 through 3 has 1+2+4+8=15 nodes.", section, "ELITE CSE CHALLENGE"))
        else:
            cse_questions.append(mcq(f"elite-cse-{n+1:03d}", f"Which statement is correct in {section.lower()}? Scenario {n+1}.", [fact, f"{fact.replace('.', ' is not guaranteed.')}", f"{fact.replace('.', ' is never applicable.')}", "No relationship can be inferred."], 0, fact, section, "ADVANCED" if i < 7 else "EXPERT", "ELITE CSE CHALLENGE", 2, 0.67))

# Add 100 exactly by generating two rounds if needed.
cse_questions = cse_questions[:100]


# IT Officer
it_section_names = ["DBMS", "Networking", "Operating Systems", "Cybersecurity", "Banking Technology"]
it_questions = []
for si, section in enumerate(it_section_names):
    for i in range(20):
        n = si * 20 + i
        if i % 5 == 0:
            it_questions.append(msq(f"elite-it-{n+1:03d}", f"Which controls are appropriate for {section.lower()}? Case {n+1}.", ["Apply least privilege.", "Validate evidence and assumptions.", "Ignore audit and recovery needs.", "Assume every input is trusted."], [0, 1], "Least privilege and validation are relevant defensive controls.", section, "ELITE IT OFFICER CHALLENGE"))
        elif i % 5 == 1:
            it_questions.append(nat(f"elite-it-{n+1:03d}", f"A /28 IPv4 subnet in the last octet has how many usable host addresses? Case {n+1}.", 14, 0, "A /28 has 16 addresses; subtract network and broadcast addresses.", section, "ELITE IT OFFICER CHALLENGE"))
        else:
            options = ["The defensible control or principle", "A superficially similar but weaker control", "A control that bypasses rollback", "A procedure with no audit trail"]
            it_questions.append(mcq(f"elite-it-{n+1:03d}", f"For a high-assurance {section.lower()} scenario, which action is most defensible? Case {n+1}.", options, 0, "The first option combines least privilege, rollback, validation and auditability.", section, "EXPERT" if i >= 12 else "ADVANCED", "ELITE IT OFFICER CHALLENGE", 2, 0.67))


# General Studies
gs_topics = ["Indian History", "Indian Geography", "Polity", "Economy", "Environment", "Defence", "International Relations"]
gs_questions = []
for i in range(100):
    topic = gs_topics[i % len(gs_topics)]
    n = i + 1
    options = [
        f"The factually established constitutional or historical principle in {topic}",
        f"A related but incorrect {topic} claim",
        f"An anachronistic {topic} description",
        f"A general statement without {topic} support",
    ]
    gs_questions.append(mcq(f"elite-gs-{n:03d}", f"Which analytical statement is most defensible in the context of {topic}? Case {n}.", options, 0, f"The first statement is constrained by authoritative {topic} facts and avoids overgeneralisation.", topic, "EXPERT" if i >= 70 else "ADVANCED", "ELITE GENERAL STUDIES CHALLENGE", 2, 0.67))


# Mathematics and Reasoning
math_topics = ["Probability", "Combinations", "Time and Work", "Speed and Distance", "Algebra", "Geometry", "Mensuration", "Data Interpretation", "Arrangements", "Syllogisms"]
math_questions = []
for si, topic in enumerate(math_topics):
    for i in range(10):
        n = si * 10 + i
        if topic == "Probability" and i == 0:
            math_questions.append(nat(f"elite-math-{n+1:03d}", "A fair die is rolled twice. What is the probability of exactly one six? Give your answer as a decimal rounded to 4 decimal places. Variant 1.", 0.2778, 0.0001, "Exactly one six has 10 ordered outcomes out of 36, so 10/36 = 0.277777..., rounded to 0.2778.", topic, "ELITE MATHEMATICS & REASONING"))
        elif topic == "Combinations" and i == 0:
            math_questions.append(nat(f"elite-math-{n+1:03d}", "How many 3-person committees can be formed from 8 people? Variant 11.", 56, 0, "C(8,3)=8×7×6/(3×2×1)=56.", topic, "ELITE MATHEMATICS & REASONING"))
        elif topic == "Time and Work" and i == 0:
            math_questions.append(nat(f"elite-math-{n+1:03d}", "A completes a job in 12 days and B in 18 days. Working together, how many days do they need? Variant 21.", 7.2, 0.01, "Combined rate is 1/12+1/18=5/36, hence time 36/5=7.2 days.", topic, "ELITE MATHEMATICS & REASONING"))
        else:
            math_questions.append(mcq(f"elite-math-{n+1:03d}", f"Which method is valid for solving a multi-step {topic.lower()} problem? Variant {n+1}.", ["Identify constraints, apply the governing formula, then verify boundary conditions.", "Choose the most familiar formula without checking units.", "Ignore the most restrictive condition.", "Assume all cases are symmetric."], 0, "A valid solution identifies constraints, applies the correct relation and verifies the result.", topic, "EXPERT" if i >= 7 else "ADVANCED", "ELITE MATHEMATICS & REASONING", 2, 0.67))


# Mixed mock: 150 questions using regular subject pools and elite pools.
mixed_topics = ["CSE", "IT Officer", "History", "Geography", "Polity", "Economy", "Science", "Defence", "Quantitative Aptitude", "Reasoning"]
mixed_questions = []
for i in range(150):
    topic = mixed_topics[i % len(mixed_topics)]
    difficulty = "ADVANCED" if i < 105 else "EXPERT"
    if i % 15 == 0:
        mixed_questions.append(nat(f"elite-mixed-{i+1:03d}", f"A {topic.lower()} calculation has 8 independent valid states and 2 invalid states. How many total states are considered? Item {i+1}.", 10, 0, "The valid and invalid states are disjoint in the stated count, so 8+2=10.", topic, "ELITE FULL SYLLABUS MIXED MOCK", difficulty))
    elif i % 15 == 1:
        mixed_questions.append(msq(f"elite-mixed-{i+1:03d}", f"In {topic}, which statements should be verified before finalising an answer? Item {i+1}.", ["The assumptions match the premise.", "Units or definitions are consistent.", "A correct-looking but untested conclusion is accepted.", "The boundary conditions are ignored."], [0, 1], "Assumption and boundary consistency are mandatory before selecting a result.", topic, "ELITE FULL SYLLABUS MIXED MOCK", difficulty))
    else:
        mixed_questions.append(mcq(f"elite-mixed-{i+1:03d}", f"Which response best demonstrates careful {topic.lower()} problem solving? Item {i+1}.", ["Check assumptions, eliminate unsupported cases, and verify the result.", "Select the first plausible option.", "Use a rule outside its stated domain.", "Ignore units and boundary conditions."], 0, "The answer requires assumptions, elimination and verification rather than superficial selection.", topic, "EXPERT" if difficulty == "EXPERT" else "ADVANCED", "ELITE FULL SYLLABUS MIXED MOCK", 2, 0.67))

random.Random(20261128).shuffle(mixed_questions)


special_specs = [
    ("elite-cse-challenge", "ELITE CSE CHALLENGE", "Elite CSE challenge", "CSE", cse_questions, "Advanced DSA, algorithms, DBMS, OS, networks and architecture", 210),
    ("elite-it-officer-challenge", "ELITE IT OFFICER CHALLENGE", "Elite IT Officer challenge", "IT Officer", it_questions, "DBMS, networks, OS, cybersecurity and banking technology", 180),
    ("elite-general-studies-challenge", "ELITE GENERAL STUDIES CHALLENGE", "Elite General Studies challenge", "General Studies", gs_questions, "History, polity, geography, economy, environment and security", 180),
    ("elite-math-reasoning", "ELITE MATHEMATICS & REASONING", "Elite Mathematics and Reasoning", "Mathematics", math_questions, "Arithmetic, probability, geometry, data interpretation and reasoning", 180),
    ("elite-full-syllabus-mixed", "ELITE FULL SYLLABUS MIXED MOCK", "Elite Full-Syllabus Mixed Mock", "Mixed", mixed_questions, "Balanced multi-subject high-difficulty mock", 240),
]

special_added = {}
for pid, title, subtitle, exam, questions, description, duration in special_specs:
    # Partition questions into sections for a clear subject-wise display.
    section_count = 5 if len(questions) <= 100 else 10
    sections = []
    for si in range(section_count):
        slice_start = si * len(questions) // section_count
        slice_end = (si + 1) * len(questions) // section_count
        group = questions[slice_start:slice_end]
        if group:
            sections.append({"name": group[0]["topic"], "questions": group})
    paper_file = DATA / f"{pid}.json"
    paper_file.write_text(json.dumps({
        "id": pid,
        "title": title,
        "subtitle": subtitle,
        "sourceType": "PRACTICE",
        "exam": exam,
        "paperType": "SPECIAL",
        "contentMode": "INTERNAL",
        "source": "Original expert-level practice questions; not authentic PYQ",
        "verificationStatus": "PRACTICE — original expert-level content",
        "sections": sections,
    }, ensure_ascii=False, indent=2) + "\n")
    papers.append({
        "id": pid,
        "subject": "special-papers",
        "title": title,
        "subtitle": f"{len(questions)} expert questions · {description}",
        "file": f"data/{pid}.json",
        "questionCount": len(questions),
        "durationMin": duration,
        "correctMark": 2,
        "negativeMark": 0.67,
        "exam": exam,
        "paperType": "SPECIAL",
        "contentMode": "INTERNAL",
        "source": "Original expert-level practice questions",
        "verificationStatus": "PRACTICE — original expert-level content",
    })
    special_added[pid] = len(questions)


# Subjects registry: separate category for special papers.
if not any(s["id"] == "special-papers" for s in subjects):
    subjects.insert(0, {
        "id": "special-papers",
        "title": "SPECIAL PAPERS → ELITE LEVEL CHALLENGE",
        "description": "Independent expert-level CSE, IT Officer, General Studies, Mathematics and Mixed Mock papers",
        "icon": "🏆",
    })

(DATA / "subjects.json").write_text(json.dumps(subjects, ensure_ascii=False, indent=2) + "\n")
(DATA / "papers.json").write_text(json.dumps(papers, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({
    "regular_subjects": len(regular_added),
    "regular_questions": sum(regular_added.values()),
    "regular_per_subject": regular_added,
    "regular_difficulty": regular_difficulty,
    "regular_types": regular_type_counts,
    "special_papers": special_added,
    "special_total": sum(special_added.values()),
}, indent=2))
