import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

TARGET = {
    "Biology": 14,
    "Physics": 14,
    "Chemistry": 14,
    "Mathematics / Basic Maths": 14,
    "Polity": 14,
    "History": 14,
    "Geography": 14,
    "Economy": 14,
    "General Awareness / Static GK": 14,
    "Technology / Computer Awareness": 14,
    "B.Tech CSE Fundamentals": 14,
    "Cloud Computing": 14,
    "Fitness / Sports / Health Awareness": 14,
    "Aptitude + Reasoning + Scenario-Based": 14,
    "Mixed Revision / General Awareness": 4,
}

DIFFICULTY = ["Easy"] * 120 + ["Moderate"] * 80


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", str(text).lower())).strip()


def flat(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for sec in data.get("sections", []):
        for q in sec.get("questions", []):
            text = q["q"] if isinstance(q["q"], str) else q["q"].get("en", str(q["q"]))
            rows.append({
                "text": text,
                "options": q["options"],
                "answer": q["answer"],
                "source": sec["name"],
            })
    return rows


def classify_source(text, source, module_hint=None):
    x = (text + " " + source).lower()
    if module_hint:
        return module_hint
    if any(v in x for v in ("preamble", "president", "parliament", "fundamental rights",
                             "article", "governor", "constitution", "supreme court")):
        return "Polity"
    if any(v in x for v in ("latitude", "longitude", "monsoon", "river", "mountain",
                             "soil", "climate", "plateau", "ocean", "geography",
                             "desert", "island", "dam", "glacier")):
        return "Geography"
    if any(v in x for v in ("cloud", "iaas", "paas", "saas", "virtualization",
                             "elastic", "load balancer", "object storage")):
        return "Cloud Computing"
    if any(v in x for v in ("os", "operating system", "database", "sql", "network",
                             "tcp", "ip", "pointer", "stack", "queue", "algorithm",
                             "programming", "compiler", "data structure")):
        return "B.Tech CSE Fundamentals"
    if any(v in x for v in ("percentage", "profit", "ratio", "average", "speed",
                             "time", "number", "calculate", "area", "math",
                             "simplification", "discount")):
        return "Mathematics / Basic Maths"
    if any(v in x for v in ("syllogism", "coding", "series", "analogy",
                             "direction", "blood relation", "statement",
                             "puzzle", "arrangement")):
        return "Aptitude + Reasoning + Scenario-Based"
    if any(v in x for v in ("acid", "base", "salt", "chemical", "atom",
                             "molecule", "reaction", "periodic", "ph ",
                             "hydrogen", "oxygen", "carbon")):
        return "Chemistry"
    if any(v in x for v in ("force", "velocity", "acceleration", "energy",
                             "motion", "lens", "electric", "magnet",
                             "pressure", "work", "power", "gravity",
                             "current", "light", "heat")):
        return "Physics"
    if any(v in x for v in ("cell", "blood", "heart", "plant", "enzyme",
                             "dna", "gene", "biology", "organ", "vitamin",
                             "photosynthesis", "protein", "bone", "lung",
                             "bacteria", "virus")):
        return "Biology"
    return "General Awareness / Static GK"


CUSTOM = {
"Economy": [
("GDP measures the value of:", ["Goods and services produced within a country", "Only exports", "Only government spending", "Only bank deposits"], 0),
("Inflation means:", ["A general increase in prices", "A rise in unemployment only", "A fall in population", "An increase in rainfall"], 0),
("The central bank of India is:", ["Reserve Bank of India", "Securities and Exchange Board of India", "State Bank of India", "NITI Aayog"], 0),
("A progressive tax takes:", ["A larger proportion as income rises", "The same fixed amount from everyone", "Only from exporters", "Only from children"], 0),
("Fiscal deficit occurs when:", ["Government expenditure exceeds its total receipts excluding borrowings", "Exports exceed imports", "Tax revenue is zero", "Banks hold excess reserves"], 0),
("Which is a direct tax?", ["Income tax", "GST", "Customs duty", "Petroleum levy"], 0),
("Demand is generally said to fall when:", ["Price rises, other things remaining equal", "Income rises", "Population rises", "Advertising rises"], 0),
("Opportunity cost is:", ["The value of the next best alternative forgone", "Only the purchase price", "A fixed government tax", "The profit of a firm"], 0),
("Fiscal policy is mainly handled through:", ["Government spending and taxation", "Central bank interest rates", "Foreign exchange auctions", "Stock-market regulation"], 0),
("Monetary policy in India is principally operated by:", ["The RBI", "The Finance Commission", "The Comptroller and Auditor-General", "The Election Commission"], 0),
("An export occurs when:", ["Goods or services are sold to a foreign country", "Goods move within a State", "A bank lends locally", "A factory pays wages"], 0),
("Per capita income is:", ["National income divided by population", "Total bank savings", "Government revenue", "Exports minus imports"], 0),
("Which is a public sector organisation?", ["A government-owned enterprise", "An individual household", "An unregistered market vendor", "A foreign private firm"], 0),
("Repo rate is:", ["The rate at which RBI lends short-term funds to commercial banks", "The tax on exports", "The rate of income growth", "The minimum wage"], 0),
],
"History": [
("The Harappan civilisation is known for:", ["Planned urban settlements", "Roman aqueducts", "Medieval forts", "Steam engines"], 0),
("Ashoka is associated with:", ["Rock and pillar edicts", "The Magna Carta", "The French Revolution", "The Industrial Revolution"], 0),
("The Mauryan Empire was founded by:", ["Chandragupta Maurya", "Akbar", "Harsha", "Ashoka only"], 0),
("The Gupta period is often called:", ["The classical age in several fields of Indian culture", "The stone age", "The colonial period", "The Mughal modernisation period"], 0),
("The Battle of Plassey was fought in:", ["1757", "1857", "1947", "1526"], 0),
("The Mughal emperor who built Humayun's Tomb was:", ["It was built during Humayun's royal period", "Akbar alone", "Aurangzeb", "Bahadur Shah Zafar"], 0),
("The Revolt of 1857 began primarily with:", ["Sepoy unrest and spread to wider political grievances", "Only a student movement", "A religious crusade in Europe", "A factory workers' strike"], 0),
("The Indian National Congress was founded in:", ["1885", "1947", "1857", "1925"], 0),
("Mahatma Gandhi launched the Salt March in:", ["1930", "1947", "1919", "1922"], 0),
("The Quit India Movement was launched in:", ["1942", "1947", "1930", "1920"], 0),
("The Constituent Assembly adopted the Constitution on:", ["26 November 1949", "15 August 1947", "26 January 1950", "24 January 1950"], 0),
("India became a republic on:", ["26 January 1950", "15 August 1947", "2 October 1949", "26 November 1949"], 0),
("Buddhism was founded by:", ["Gautama Buddha", "Mahavira", "Ashoka", "Chanakya"], 0),
("The first Jain Tirthankara is traditionally:", ["Rishabhanatha", "Mahavira", "Gautama Buddha", "Ashoka"], 0),
],
"General Awareness / Static GK": [
("The President of India is also the constitutional head of:", ["The Union of India", "A State Legislative Council only", "The Reserve Bank of India", "The Supreme Court"], 0),
("The Indian Parliament consists of:", ["President, Lok Sabha and Rajya Sabha", "Lok Sabha and State Assemblies", "Only Lok Sabha", "Rajya Sabha and Governors"], 0),
("The national animal of India is:", ["Bengal tiger", "Lion", "Elephant", "Peacock"], 0),
("The national fruit of India is:", ["Mango", "Apple", "Banana", "Guava"], 0),
("The currency of Japan is:", ["Japanese yen", "Won", "Baht", "Dollar"], 0),
("The headquarters of the United Nations are in:", ["New York", "Geneva", "Paris", "London"], 0),
("The largest continent by area is:", ["Asia", "Africa", "Europe", "Australia"], 0),
("The headquarters of WHO are in:", ["Geneva", "New Delhi", "Washington", "Tokyo"], 0),
("The SI unit of temperature is:", ["Kelvin", "Celsius", "Fahrenheit", "Pascal"], 0),
("The Indian national calendar is based on:", ["Saka era", "Gregorian era", "Vikram Samvat only", "Hijri calendar"], 0),
("The Constitution of India came into effect on:", ["26 January 1950", "15 August 1947", "26 November 1949", "24 January 1950"], 0),
("The headquarters of RBI are in:", ["Mumbai", "New Delhi", "Kolkata", "Chennai"], 0),
("The State emblem of India is adapted from:", ["Lion Capital at Sarnath", "Ashoka's diamond throne", "Red Fort", "Ajanta caves"], 0),
("A leap year has:", ["366 days", "365 days", "364 days", "360 days"], 0),
],
"Technology / Computer Awareness": [
("A URL identifies:", ["A resource on the internet", "Only a Wi-Fi password", "A computer's motherboard", "A printer cable"], 0),
("The main function of a firewall is to:", ["Control network traffic according to security rules", "Convert text to speech", "Increase monitor brightness", "Store processor instructions"], 0),
("Two-factor authentication uses:", ["Two independent verification factors", "Two passwords of the same factor", "Only a username", "An email address twice"], 0),
("A malicious program that replicates itself is often called:", ["A virus", "A compiler", "A browser", "A spreadsheet"], 0),
("HTTP is primarily used for:", ["Transfer of web resources", "Cable television", "Audio equalisation", "Database backup only"], 0),
("An IP address identifies:", ["A host or network interface", "A document font", "A keyboard layout", "A hardware fan"], 0),
("The brain of a computer is:", ["CPU", "Monitor", "Keyboard", "Printer"], 0),
("An SSD is a type of:", ["Solid-state storage", "Optical tape", "Input scanner", "Cooling fan"], 0),
("Cache memory is:", ["Fast temporary memory close to the processor", "Only permanent disk storage", "Printer memory", "A network cable"], 0),
("Wi-Fi is commonly used for:", ["Wireless local network communication", "Undersea cable manufacturing", "Printing documents", "Running an engine"], 0),
("Encryption mainly provides:", ["Confidentiality of data", "Uncontrolled public access", "More screen resolution", "Faster printer movement"], 0),
("A digital signature primarily helps verify:", ["Authenticity and integrity", "Internet speed", "Monitor brightness", "Printer ink level"], 0),
("A web browser is used to:", ["Request and display web content", "Cook food", "Operate a mechanical latchet", "Measure rainfall"], 0),
("Cloud backup is used to:", ["Store recoverable copies on remote infrastructure", "Delete all old data", "Disable a network", "Upgrade a monitor"], 0),
],
"B.Tech CSE Fundamentals": [
("An algorithm is:", ["A finite sequence of well-defined steps", "A physical wire", "A database table only", "A display screen"], 0),
("Which data structure follows LIFO?", ["Stack", "Queue", "Graph", "Set"], 0),
("Which data structure follows FIFO?", ["Queue", "Stack", "Tree", "Array"], 0),
("Binary search requires:", ["Sorted input", "Random input only", "A cyclic graph", "An unordered hash table"], 0),
("A primary key is used to:", ["Uniquely identify a row", "Sort only text", "Encrypt every row", "Store all passwords"], 0),
("SQL JOIN combines:", ["Rows from related tables", "Only two file names", "Operating-system processes", "Printer commands"], 0),
("The OS is responsible for:", ["Process and resource management", "Only drawing icons", "Only internet browsing", "Only camera operation"], 0),
("A compiler converts:", ["Source code into executable or intermediate code", "Text into an image only", "A mouse into a disk", "An IP address into a power cable"], 0),
("A class in object-oriented programming represents:", ["A type or template", "A CPU clock", "A network protocol", "A database backup"], 0),
("Inheritance allows:", ["A class to reuse traits of another class", "A compiler to remove variables", "A router to stop packets", "A database to become encrypted"], 0),
("A deadlock occurs when:", ["Processes wait cyclically for resources held by each other", "A program compiles successfully", "A file is opened read-only", "A user logs out"], 0),
("Big-O notation describes:", ["Growth of resource use with input size", "The size of a hard disk", "An IP address", "A monitor's colour depth"], 0),
("The AND gate outputs 1 when:", ["All inputs are 1", "Any input is 1", "No input is 1", "Exactly one input is 0"], 0),
("TCP provides:", ["Reliable connection-oriented transport", "Only physical addressing", "Video compression", "Screen sharing"], 0),
],
"Fitness / Sports / Health Awareness": [
("Normal aerobic exercise mainly improves:", ["Cardiorespiratory fitness", "Only spelling ability", "Only eyesight", "Only memory cards"], 0),
("Vitamin C is associated with:", ["Collagen formation and antioxidant function", "Only night vision", "Only bone fluorosis", "Only iron mining"], 0),
("The organ that pumps blood is:", ["Heart", "Liver", "Stomach", "Lung"], 0),
("A balanced diet should include:", ["Appropriate combinations of nutrients", "Only sugar", "Only fried food", "Only supplements"], 0),
("Dehydration means:", ["Excessive loss or lack of body water", "Excessive oxygen", "Too much muscle fibre", "A skin allergy only"], 0),
("Cricket teams commonly have eleven players in the fielding side because:", ["It is a standard rule", "The field is always triangular", "It is a requirement of football", "Only captains may field"], 0),
("Olympic rings are:", ["Five interlocking rings", "Five separate planets", "Five mountains", "Five coloured medals"], 0),
("A cricket century means:", ["A batter scores 100 or more runs in an innings", "A 100-second over", "A 100-player team", "A 100-run penalty"], 0),
("The FIFA World Cup is associated with:", ["Football", "Cricket", "Hockey", "Badminton"], 0),
("A sprain is an injury to:", ["A ligament", "A tooth", "A nail", "A lung valve"], 0),
("Warming up before exercise helps:", ["Prepare muscles and reduce injury risk", "Guarantee immediate sleep", "Stop breathing", "Replace hydration"], 0),
("The first aid for a minor burn includes:", ["Cooling it safely with running clean water", "Applying ice directly for a long time", "Opening blisters", "Covering it in sugar"], 0),
("BMI is based on:", ["Weight and height", "Age and shoe size", "Income and education", "Pulse and hair length"], 0),
("Sleep is important for:", ["Recovery, cognition and health", "Only typing speed", "Only height measurement", "Only food storage"], 0),
],
"Mixed Revision / General Awareness": [
("Which combination is correctly matched?", ["RBI—Monetary policy", "UPSC—Village revenue only", "ISRO—Football", "WHO—Stock exchange"], 0),
("A government dashboard showing literacy, health and infrastructure indicators is mainly used for:", ["Public performance monitoring", "Secret ballot counting", "Climate change reversal only", "Creating a private bank"], 0),
("If a reported fact conflicts with an official source, a careful candidate should:", ["Verify and prefer the authoritative official source", "Choose the more surprising claim", "Ignore all evidence", "Repeat the first claim"], 0),
("Which pairing is logically valid?", ["Photosynthesis—Plants convert light energy", "Evaporation—A solid becomes a crystal", "Mitochondria—Plasma television", "GDP—A skin cell"], 0),
],
}


SOURCE_FILES = [
    DATA / "science-001.json",
    DATA / "science-002.json",
    DATA / "general-science-biology-master-001.json",
    DATA / "ibps-quant-1.json",
    DATA / "ibps-reasoning-1.json",
    DATA / "polity-001.json",
    DATA / "polity-002.json",
    DATA / "geography-001.json",
    DATA / "geography-002.json",
    DATA / "cloud-computing-001.json",
    DATA / "cloud-computing-002.json",
    DATA / "cloud-computing-003.json",
    DATA / "cloud-computing-004.json",
    DATA / "cloud-computing-005.json",
    DATA / "cse-fundamentals-100.json",
]


def load_source_rows():
    rows = []
    seen = set()
    for path in SOURCE_FILES:
        data = json.loads(path.read_text(encoding="utf-8"))
        for sec in data.get("sections", []):
            for q in sec.get("questions", []):
                text = q["q"] if isinstance(q["q"], str) else q["q"].get("en", str(q["q"]))
                key = norm(text)
                if key in seen:
                    continue
                seen.add(key)
                module_hint = None
                if "biology" in str(path).lower() or "biology" in sec["name"].lower():
                    module_hint = "Biology"
                elif "cloud" in str(path).lower():
                    module_hint = "Cloud Computing"
                elif "cse-fundamentals" in str(path).lower():
                    module_hint = "B.Tech CSE Fundamentals"
                elif "ibps-quant" in str(path).lower():
                    module_hint = "Mathematics / Basic Maths"
                elif "ibps-reasoning" in str(path).lower():
                    module_hint = "Aptitude + Reasoning + Scenario-Based"
                elif "geography" in str(path).lower():
                    module_hint = "Geography"
                elif "polity" in str(path).lower():
                    module_hint = "Polity"
                elif "science" in str(path).lower():
                    module_hint = classify_source(text, sec["name"])

                module = module_hint or classify_source(text, sec["name"])
                rows.append({
                    "module": module,
                    "text": text,
                    "options": q["options"],
                    "answer": q["answer"],
                    "topic": sec["name"],
                    "subtopic": sec["name"],
                    "pattern": "TREND_BASED",
                })
    return rows


def load_custom_rows():
    rows = []
    for module, items in CUSTOM.items():
        for text, options, answer in items:
            rows.append({
                "module": module,
                "text": text,
                "options": options,
                "answer": answer,
                "topic": module,
                "subtopic": "Static/application knowledge",
                "pattern": "CONCEPTUAL",
            })
    return rows


def select_rows():
    rng = random.Random(20261118)
    source_rows = load_source_rows()
    custom_rows = load_custom_rows()
    used = set()
    selected = []

    for module, count in TARGET.items():
        candidates = [r for r in source_rows + custom_rows if r["module"] == module]
        rng.shuffle(candidates)
        chosen = []
        for row in candidates:
            key = norm(row["text"])
            if key in used:
                continue
            used.add(key)
            chosen.append(row)
            if len(chosen) == count:
                break

        if len(chosen) < count:
            raise RuntimeError(
                f"Only {len(chosen)} unique rows available for {module}; need {count}"
            )
        selected.extend(chosen)

    if len(selected) != 200:
        raise RuntimeError(f"Expected 200 questions, got {len(selected)}")
    return selected


def build():
    rng = random.Random(20261118)
    selected = select_rows()
    rng.shuffle(selected)

    targets = [0] * 50 + [1] * 50 + [2] * 50 + [3] * 50
    rng.shuffle(targets)
    paper_sections = {name: [] for name in TARGET}
    answer_entries = []

    for i, row in enumerate(selected):
        qid = f"GA-MASTER-{i + 1:03d}"
        correct = row["options"][row["answer"]]
        distractors = [opt for j, opt in enumerate(row["options"]) if j != row["answer"]]
        answer = targets[i]
        options = distractors[:answer] + [correct] + distractors[answer:]
        difficulty = DIFFICULTY[i]
        exam_level = ["Government Exams", "Defence", "Banking", "Railway", "UP SI"]

        item = {
            "id": qid,
            "section": row["module"],
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "difficulty": difficulty,
            "exam_level": exam_level,
            "pattern": row["pattern"],
            "q": row["text"],
            "options": options,
            "marks_correct": 1,
            "marks_wrong": -0.25,
        }
        paper_sections[row["module"]].append(item)

        answer_entries.append({
            "id": qid,
            "correct_answer": chr(65 + answer),
            "correct_option": correct,
            "explanation": (
                f"{correct} is correct because it matches the basic {row['module'].lower()} concept "
                "tested by this question. The other choices are less accurate or describe a different "
                "concept. This is an easy-to-moderate screening-level question."
            ),
            "concept_tested": row["subtopic"],
            "difficulty": difficulty,
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "exam_relevance": exam_level,
            "pattern": row["pattern"],
            "why_other_options_are_wrong": [
                f"{chr(65 + j)}. {opt}: does not match the concept tested."
                for j, opt in enumerate(options) if j != answer
            ],
        })

    paper = {
        "id": "general-awareness-master-200",
        "title": "General Awareness + Mixed Knowledge Master Paper",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "Government, Defence, Banking, Railway and Technical Jobs",
        "discipline": "General Awareness",
        "source": "Mixed syllabus-based practice questions; not an official previous-year paper",
        "verificationStatus": "Practice dataset; not an official or verified previous-year paper",
        "maximum_marks": 200,
        "correct_mark": 1,
        "negative_mark": 0.25,
        "unattempted_mark": 0,
        "answerKey": "data/general-awareness-master-200-answer-key.json",
        "instructions": [
            "Correct answer: +1",
            "Incorrect answer: -0.25",
            "Unattempted: 0",
            "Choose exactly one correct answer."
        ],
        "sections": [
            {"name": name, "questions": paper_sections[name]}
            for name in TARGET
        ],
    }

    key = {
        "id": "general-awareness-master-200-answer-key",
        "paper_id": "general-awareness-master-200",
        "total_questions": 200,
        "maximum_marks": 200,
        "marking": {"correct": 1, "wrong": -0.25, "unattempted": 0},
        "answers": answer_entries,
    }

    (DATA / "general-awareness-master-200.json").write_text(
        json.dumps(paper, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (DATA / "general-awareness-master-200-answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
