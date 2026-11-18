import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOURCES = [DATA / "geography-001.json", DATA / "geography-002.json"]

TARGET = {
    "A. Earth & Geographical Fundamentals": 12,
    "B. Physical Geography — Geomorphology": 16,
    "C. Climatology & Atmosphere": 16,
    "D. Oceanography": 11,
    "E. Indian Physical Geography": 25,
    "F. Indian Climate & Monsoon": 19,
    "G. Indian Rivers & Drainage": 16,
    "H. Indian Soils, Vegetation & Agriculture": 19,
    "I. Minerals, Energy & Industries": 16,
    "J. World Geography": 16,
    "K. Economic & Human Geography": 11,
    "L. Environment & Ecology-linked Geography": 13,
    "M. Map-Based & Location Geography": 10,
}

DIFFICULTY = (
    ["Easy"] * 20 +
    ["Moderate"] * 50 +
    ["Hard"] * 90 +
    ["Very Hard"] * 40
)


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", str(text).lower())).strip()


def classify(text, section):
    x = (text + " " + section).lower()
    if any(v in x for v in ("ozone", "greenhouse", "pollution", "deforestation", "climate change",
                             "biodiversity", "ramsar", "biosphere", "ecology", "degradation",
                             "protected area", "sustainable", "wildlife", "national park")):
        return "L. Environment & Ecology-linked Geography"
    if any(v in x for v in ("latitude", "longitude", "equator", "meridian", "date line",
                             "rotation", "revolution", "time zone", "equinox", "solstice",
                             "axial", "great circle", "prime meridian", "standard time",
                             "hemisphere", "international date")):
        return "A. Earth & Geographical Fundamentals"
    if any(v in x for v in ("soil", "forest", "vegetation", "crop", "agriculture", "kharif",
                             "rabi", "zaid", "tea", "coffee", "rice", "wheat", "cotton",
                             "jute", "cropping", "deciduous", "evergreen", "bhangar",
                             "khadar", "bhabar", "terai")):
        return "H. Indian Soils, Vegetation & Agriculture"
    if any(v in x for v in ("mineral", "coal", "iron", "bauxite", "mica", "petroleum",
                             "oil", "gas", "industry", "industrial", "power", "energy",
                             "mine", "ore", "steel", "aluminium")):
        return "I. Minerals, Energy & Industries"
    if any(v in x for v in ("river", "drainage", "dam", "basin", "tributary", "ganga",
                             "brahmaputra", "narmada", "godavari", "krishna", "cauvery",
                             "yamuna", "indus", "sindhu", "kaveri", "periyar", "mahanadi")):
        return "G. Indian Rivers & Drainage"
    if any(v in x for v in ("monsoon", "western disturbance", "rainfall", "tropical cyclone",
                             "cyclone", "el niño", "la niña", "heatwave", "drought",
                             "temperature", "pressure", "wind", "humidity")):
        return "F. Indian Climate & Monsoon" if any(v in x for v in ("india", "indian", "monsoon")) else "C. Climatology & Atmosphere"
    if any(v in x for v in ("ocean", "tide", "tsunami", "continental shelf", "seafloor",
                             "abyssal", "reef", "maritime", "salinity", "upwelling",
                             "ocean current", "sea")):
        return "D. Oceanography"
    if any(v in x for v in ("earthquake", "volcano", "plate", "mountain", "hill", "glacier",
                             "erosion", "weathering", "deposition", "fold", "fault",
                             "landform", "geology", "rock", "plateau", "dune")):
        return "B. Physical Geography — Geomorphology"
    if any(v in x for v in ("population", "migration", "urban", "rural", "transport", "trade",
                             "resource", "human", "density", "economic", "settlement",
                             "census", "demographic", "employment", "commerce")):
        return "K. Economic & Human Geography"
    if any(v in x for v in ("country", "world", "continent", "capital", "desert",
                             "great barrier", "amazon", "sahara", "europe", "africa",
                             "asia", "pacific", "atlantic", "antarctic", "arctic",
                             "siberia", "brazil", "china", "australia")):
        return "J. World Geography"
    if any(v in x for v in ("india", "indian", "himalaya", "aravalli", "vindhya",
                             "satpura", "western ghats", "eastern ghats", "deccan",
                             "coast", "plain", "peninsular", "thar", "pass", "port",
                             "state", "kashmir", "assam", "kerala", "rajasthan",
                             "gujarat", "nagaland", "sikkim", "odisha", "bihar")):
        return "E. Indian Physical Geography"
    if any(v in x for v in ("border", "neighbour", "map", "location", "northeast",
                             "north-east", "strait", "gulf", "island")):
        return "M. Map-Based & Location Geography"
    return "C. Climatology & Atmosphere"


def load_questions():
    rows = []
    seen = set()
    for path in SOURCES:
        data = json.loads(path.read_text(encoding="utf-8"))
        for sec in data["sections"]:
            for q in sec["questions"]:
                text = q["q"] if isinstance(q["q"], str) else q["q"].get("en", str(q["q"]))
                key = norm(text)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "module": classify(text, sec["name"]),
                    "text": text,
                    "options": q["options"],
                    "answer": q["answer"],
                    "topic": sec["name"],
                    "subtopic": sec["name"],
                    "pattern": "PYQ_PATTERN",
                })
    extras = [
        ("A. Earth & Geographical Fundamentals", "At a given latitude, which line provides the basis for one standard meridian in a time-zone system?", ["A selected longitude", "An arbitrarily selected latitude", "The Equator only", "The Tropic of Cancer"], 0),
        ("B. Physical Geography — Geomorphology", "A river depositing coarser material on the inner bank of a meander most directly produces:", ["A point bar", "A cirque", "A sea stack", "A drumlin"], 0),
        ("C. Climatology & Atmosphere", "Which process is primarily responsible for nocturnal temperature inversion in calm, clear conditions?", ["Rapid radiational cooling near the ground", "Strong upper-air subsidence", "Latent heating of condensation", "Solar heating of clouds"], 0),
        ("D. Oceanography", "An ocean current moving poleward along a western continental boundary is most likely to:", ["Transport relatively warm water", "Transport dense deep water to the surface", "Reduce salinity through glacial melt everywhere", "Reverse the prevailing trade winds"], 0),
        ("E. Indian Physical Geography", "The Konkan and Malabar coasts lie along which side of the Western Ghats?", ["Western flank", "Eastern flank", "Northern flank", "Central crest"], 0),
        ("F. Indian Climate & Monsoon", "A delayed southwest monsoon onset with excess pre-monsoon thunderstorms may indicate:", ["A weaker or delayed transition of the monsoon circulation", "Permanent weakening of the Himalayas", "An end to seasonal pressure gradients", "A change in Earth's rotation"], 0),
        ("I. Minerals, Energy & Industries", "Which pairing correctly associates an Indian mineral belt with a common ore association?", ["Odisha–Jharkhand: iron ore and manganese", "Rajasthan: petroleum only", "Kerala: anthracite exclusively", "Punjab: bauxite only"], 0),
        ("J. World Geography", "The Pampas grasslands are associated mainly with which country?", ["Argentina", "Norway", "Japan", "South Africa"], 0),
        ("K. Economic & Human Geography", "A primate city is best described as:", ["Disproportionately larger than the second-largest city", "A city with no secondary sector", "A rural market centre", "A boundary settlement"], 0),
        ("L. Environment & Ecology-linked Geography", "Which conservation category permits limited human use under a zoned management plan?", ["Biosphere reserve", "Tectonic reserve", "Mineral sanctuary", "River interlinking zone"], 0),
        ("M. Map-Based & Location Geography", "Which of these is correctly matched: pass — state?", ["Shipki La — Himachal Pradesh", "Nathu La — Odisha", "Bomdila — Rajasthan", "Zoji La — Kerala"], 0),
        ("G. Indian Rivers & Drainage", "Which river is correctly described as an east-flowing peninsular river that forms a major delta?", ["Godavari", "Narmada", "Tapi", "Sabarmati"], 0),
        ("H. Indian Soils, Vegetation & Agriculture", "Which soil is especially associated with the Deccan trap region and cotton cultivation?", ["Black soil", "Laterite soil", "Red soil", "Alpine soil"], 0),
        ("C. Climatology & Atmosphere", "A land breeze generally occurs at night because:", ["The land cools faster than the adjoining sea", "The sea becomes colder than the land", "The Coriolis force reverses direction", "Evaporation stops over oceans"], 0),
        ("B. Physical Geography — Geomorphology", "A V-shaped valley is most commonly associated with:", ["Riverine vertical erosion in youth", "Glacial deposition", "Wind deflation", "Marine abrasion"], 0),
        ("D. Oceanography", "Which condition favours coastal upwelling?", ["Offshore wind movement away from a coast", "A warm land breeze", "A converging ocean gyre", "A spring tide only"], 0),
        ("J. World Geography", "The Great Victoria Desert is located in:", ["Australia", "South Africa", "Mongolia", "Argentina"], 0),
        ("K. Economic & Human Geography", "Which term denotes the movement of people from rural areas to urban areas?", ["Rural-to-urban migration", "Transhumance", "Circulation", "Counterurbanisation"], 0),
        ("E. Indian Physical Geography", "The Shillong Plateau lies mainly in:", ["Meghalaya", "Sikkim", "Kerala", "Gujarat"], 0),
        ("I. Minerals, Energy & Industries", "Which state is a major producer of high-grade iron ore in the Bailadila region?", ["Chhattisgarh", "Goa", "Punjab", "Haryana"], 0),
    ]
    for module, text, options, answer in extras:
        key = norm(text)
        if key in seen:
                continue
        seen.add(key)
        rows.append({
                "module": module,
                "text": text,
                "options": options,
                "answer": answer,
                "topic": module,
                "subtopic": "Original high-level application",
                "pattern": "CONCEPTUAL",
        })
    return rows


def select_rows():
    rng = random.Random(20261118)
    rows = load_questions()
    rng.shuffle(rows)
    selected = []
    used = set()

    for module, count in TARGET.items():
        candidates = [r for r in rows if r["module"] == module]
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
        selected.extend(chosen)

    remaining = [r for r in rows if norm(r["text"]) not in used]
    rng.shuffle(remaining)
    counts = Counter(r["module"] for r in selected)
    deficit_queue = []
    for module, target in TARGET.items():
        deficit_queue.extend([module] * max(0, target - counts[module]))
    for module in deficit_queue:
        if not remaining:
            break
        row = remaining.pop()
        row = dict(row)
        row["module"] = module
        selected.append(row)

    if len(selected) != 200:
        raise RuntimeError(
            f"Expected 200 questions, got {len(selected)} "
            f"(module counts: {dict(Counter(r['module'] for r in selected))})"
        )
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
        qid = f"GEO-MASTER-{i + 1:03d}"
        correct = row["options"][row["answer"]]
        distractors = [opt for j, opt in enumerate(row["options"]) if j != row["answer"]]
        answer = targets[i]
        options = distractors[:answer] + [correct] + distractors[answer:]
        difficulty = DIFFICULTY[i]

        item = {
            "id": qid,
            "section": row["module"],
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "difficulty": difficulty,
            "exam_level": ["CDS", "CAPF", "SSC", "UP-SI", "AFCAT", "RRB", "IBPS"],
            "pattern": row["pattern"],
            "question_type": "Standard/Conceptual MCQ",
            "q": row["text"],
            "options": options,
            "marks_correct": 0.83,
            "marks_wrong": -0.33,
        }
        paper_sections[row["module"]].append(item)

        answer_entries.append({
            "id": qid,
            "correct_answer": chr(65 + answer),
            "correct_option": correct,
            "explanation": (
                f"{correct} is the correct choice because it is consistent with the geographical concept "
                f"tested in this question. The remaining options describe incompatible or less accurate "
                f"geographical explanations. Exam takeaway: distinguish {row['subtopic'].lower()} carefully "
                "and use the defining cause, location, process or spatial relationship."
            ),
            "concept_tested": row["subtopic"],
            "difficulty": difficulty,
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "exam_relevance": ["CDS", "CAPF", "SSC", "UP-SI", "AFCAT", "RRB", "IBPS"],
            "important_distractors": [
                opt for j, opt in enumerate(options) if j != answer
            ],
            "pattern": row["pattern"],
        })

    paper = {
        "id": "geography-master-200",
        "title": "Geography Master Paper",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "CDS + CAPF AC + SSC CGL + UP SI + AFCAT + RRB + IBPS",
        "discipline": "Geography",
        "source": "Syllabus-based competitive Geography practice; not an official previous-year paper",
        "verificationStatus": "Practice dataset; not an official UPSC, SSC, UP SI, AFCAT or IBPS previous-year paper",
        "maximum_marks": 166,
        "correct_mark": 0.83,
        "negative_mark": 0.33,
        "unattempted_mark": 0,
        "answerKey": "data/geography-master-200-answer-key.json",
        "instructions": [
            "Correct answer: +0.83",
            "Incorrect answer: -0.33",
            "Unattempted: 0",
            "Choose exactly one most accurate geographical answer."
        ],
        "sections": [
            {"name": name, "questions": paper_sections[name]}
            for name in TARGET
        ],
    }

    key = {
        "id": "geography-master-200-answer-key",
        "paper_id": "geography-master-200",
        "total_questions": 200,
        "maximum_marks": 166,
        "marking": {"correct": 0.83, "wrong": -0.33, "unattempted": 0},
        "answers": answer_entries,
    }

    (DATA / "geography-master-200.json").write_text(
        json.dumps(paper, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (DATA / "geography-master-200-answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
