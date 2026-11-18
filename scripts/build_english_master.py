import json
import re
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SOURCE_FILES = [
    DATA / "english-ibps-cds-003.json",
    DATA / "english-ibps-cds-004.json",
    DATA / "english-ibps-cds-002.json",
    DATA / "english-ibps-cds-001.json",
    DATA / "cds-capf-english-practice-02.json",
]

TARGET_COUNTS = {
    "Grammar": 45,
    "Vocabulary": 35,
    "Error Detection": 25,
    "Fillers & Cloze": 20,
    "Sentence Arrangement": 15,
    "Reading Comprehension": 25,
    "Sentence-Based English": 20,
    "Advanced / Descriptive Language": 15,
}


def classify_section(name):
    n = name.lower()
    if "reading comprehension" in n or "difficult reading" in n:
        return "Reading Comprehension"
    if "error" in n or "spot" in n:
        return "Error Detection"
    if "cloze" in n or "fill" in n or "blank" in n:
        return "Fillers & Cloze"
    if "jumbl" in n or "order" in n or "p/q/r/s" in n or "para" in n or "s1-s6" in n:
        return "Sentence Arrangement"
    if "sentence" in n or "connector" in n or "improvement" in n or "phrase replacement" in n:
        return "Sentence-Based English"
    if any(x in n for x in (
        "synonym", "antonym", "vocab", "idiom", "word substitution",
        "spelling", "foreign", "phrasal", "paired", "one word",
    )) and "sentence" not in n:
        return "Vocabulary"
    if "parts of speech" in n or "grammar" in n:
        return "Grammar"
    if "usage" in n or "word" in n:
        return "Vocabulary"
    return "Grammar"


def normalise(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", text.lower())).strip()


def flatten_sources():
    rows = []
    seen = set()
    for path in SOURCE_FILES:
        data = json.loads(path.read_text(encoding="utf-8"))
        for sec in data["sections"]:
            module = classify_section(sec["name"])
            for q in sec["questions"]:
                text = q["q"] if isinstance(q["q"], str) else q["q"].get("en", str(q["q"]))
                key = normalise(text)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "module": module,
                    "source_section": sec["name"],
                    "q": q,
                    "text": text,
                })
    return rows


ADVANCED_QUESTIONS = [
    ("Choose the most appropriate opening for an essay on responsible artificial intelligence.",
     ["AI promises progress, but its benefits must be secured through accountable governance.",
      "AI is a popular topic that many people discuss in modern times.",
      "This essay discusses several things about AI and its uses.",
      "Artificial intelligence has become better and faster in every year."], 0,
     "The first option establishes a specific evaluative theme and anticipates a balanced discussion."),
    ("Which sentence would provide the strongest concluding sentence for an essay about climate resilience?",
     ["Climate resilience therefore requires adaptation, mitigation, and cooperation across institutions and communities.",
      "Climate has always been changing in human history.",
      "Many people can speak about climate at school.",
      "The problem was discussed in detail in the previous paragraph."], 0,
     "It synthesises the issue and offers a clear, forward-looking conclusion."),
    ("Select the most effective précis of: 'Experts agree that cities should expand public transport, but expansion will succeed only if fares are affordable, routes are dependable, and authorities coordinate land-use policy.'",
     ["Affordable, reliable public transport needs integrated planning and coordination.",
      "Experts enjoy travelling around modern cities.",
      "Public transport expansion is always expensive and should be avoided.",
      "Land-use policy has no relationship with transport."], 0,
     "It preserves the key conditions and compresses the argument without adding unsupported claims."),
    ("Which sentence is the most concise while preserving the intended meaning?",
     ["Due to the heavy rain, the match was postponed.",
      "On account of the fact that heavy rain occurred, the match was postponed.",
      "The match was postponed because of the occurrence of heavy rainfall.",
      "The heavy rain being what it was, this was why the match was postponed."], 0,
     "'Due to the heavy rain' directly expresses the cause and avoids redundant nominal constructions."),
    ("Which opening best maintains formal official tone in a report about a failed relief operation?",
     ["The operation encountered delays that require institutional review and corrective measures.",
      "The whole operation was a mess and should never have happened.",
      "Honestly, nobody did the right thing during the relief work.",
      "One may feel quite sad because the operation did not succeed."], 0,
     "The option is factual, impersonal, and appropriately formal for an official report."),
    ("Choose the sentence that maintains the strongest logical continuity after: 'The expedition was adequately funded and scientifically prepared.'",
     ["Yet poor coordination between the teams delayed the first field survey.",
      "Funding and preparation are also possible in ordinary situations.",
      "The teams later bought some new maps.",
      "Science is a useful and interesting subject."], 0,
     "The contrast signalled by 'Yet' follows naturally from the implication that preparation should have prevented delays."),
    ("Which sentence presents the strongest counter-argument to: 'All public services should be fully automated to eliminate human error.'",
     ["Automation can improve consistency, but vulnerable users may need human judgment and an appeal process.",
      "Automation is expensive because computers require electricity.",
      "Public services should never use any kind of technology.",
      "Human beings make mistakes and therefore must be removed from every process."], 0,
     "It accepts a limited benefit while exposing why the absolute proposal is inadequate."),
    ("Which sentence best preserves logical coherence in a paragraph on journalistic ethics?",
     ["Accuracy, independence, and correction of demonstrable errors are essential to public trust.",
      "A newspaper uses many pages and several printing machines.",
      "Journalism is one among several forms of entertainment.",
      "Headlines are usually written in a large and attractive size."], 0,
     "The option addresses ethical principles relevant to the stated topic and maintains conceptual continuity."),
    ("Choose the most appropriate formal expression for declining a request.",
     ["We are unable to approve the request under the present guidelines.",
      "Sorry, we cannot do it because the rules say no.",
      "You should have known before asking us.",
      "The request is rejected and that ends the matter."], 0,
     "It states the decision politely, impersonally, and without unnecessary hostility."),
    ("Which sentence would be the best topic sentence for a paragraph on institutional accountability?",
     ["Public institutions earn legitimacy by explaining decisions and accepting review.",
      "Institutions are found in every city and village.",
      "A building may contain several offices and meeting rooms.",
      "People often work for many years before retirement."], 0,
     "It directly defines accountability and gives the paragraph a clear controlling idea."),
    ("Select the best summary of: 'A research finding is persuasive only when its evidence is reproducible, its assumptions are explicit, and its limitations are honestly acknowledged.'",
     ["Credible research combines reproducibility, transparent assumptions, and honest limits.",
      "All research is persuasive regardless of its evidence.",
      "Scientific findings should never mention limitations.",
      "Reproducibility makes every assumption unnecessary."], 0,
     "The summary captures all three conditions as jointly necessary for credibility."),
    ("Which closing is most suitable for a formal email requesting a meeting?",
     ["I would appreciate the opportunity to meet and discuss this matter at a convenient time.",
      "Come for a meeting whenever you feel like it.",
      "If you do not reply, I will understand that you are wrong.",
      "Please attend because this is very important for me."], 0,
     "It makes a courteous request while leaving the time and recipient's convenience unresolved."),
    ("Which sentence has the most appropriate tone for an official précis?",
     ["The report recommends a phased implementation supported by measurable review indicators.",
      "The report wants people to try the plan and see what happens.",
      "The report has some ideas that sound quite exciting.",
      "The report tells everyone to hurry up and finish everything."], 0,
     "It is neutral, precise, and suitable for condensed official language."),
    ("Choose the sentence that most clearly distinguishes evidence from opinion.",
     ["The audit records show a 12% increase, whereas the committee believes the increase is desirable.",
      "The audit seems to show a lot of growth, and growth is always good.",
      "A 12% increase is popular, so it must be desirable.",
      "The committee believes everything in the audit is correct."], 0,
     "It separates the factual measure ('audit records show') from the evaluative belief ('committee believes')."),
    ("Which conclusion follows logically from the facts: 'The census found that literacy rose; it did not measure whether graduates found work.'",
     ["Literacy improved, but employment outcomes remain unknown.",
      "Literacy rose and therefore unemployment disappeared.",
      "No conclusion can be drawn about literacy.",
      "Employment rates must have fallen after the census."], 0,
     "It states what the census established and refrains from inferring an unmeasured employment outcome."),
]


GRAMMAR_QUESTIONS = [
    ("No sooner had the committee concluded the hearing ___ the chairman requested a written revision.",
     ["than", "then", "when", "as"], 0,
     "No sooner is followed by than in this correlative construction."),
    ("The captain, together with two newly appointed officers, ___ the post at dawn.",
     ["inspects", "inspect", "are inspecting", "have inspect"], 0,
     "The head noun 'captain' is singular; the intervening phrase does not change subject-verb agreement."),
    ("Had I known that the route would be closed, I ___ an alternative before departure.",
     ["would have arranged", "will arrange", "would arrange", "had arranged"], 0,
     "In an inverted unreal past conditional, the main clause uses would have plus the past participle."),
    ("The minister was determined ___ neither an official reprimand nor public criticism ___ her resolve.",
     ["that; weaken", "for; to weaken", "to; would weaken", "that; would weaken"], 2,
     "The construction requires the infinitive 'to weaken', with 'neither…nor' linking the prepositional objects."),
    ("The board is reluctant to endorse a policy unless it ___ objectively verifiable safeguards.",
     ["includes", "shall include", "has included", "including"], 0,
     "After the singular subject 'it', the present tense 'includes' is appropriate in an unless clause."),
    ("The fewer restrictions there are on legitimate research, ___ the likelihood of a transparent conclusion.",
     ["the greater", "greater", "the greatest", "greatly"], 0,
     "The correlative comparative 'the fewer… the greater' is required."),
    ("Scarcely ___ the briefing begun when the signal failed.",
     ["had", "has", "did", "was"], 0,
     "Scarcely requires inversion: 'had' precedes the subject 'the briefing'."),
    ("Choose the sentence that uses a participial phrase correctly:",
     ["Having exhausted the supply, the officer revised the ration schedule.",
      "Having exhausted the supply, the ration schedule was revised by the officer.",
      "Having exhausted, the ration schedule was revised.",
      "The ration schedule, having exhausted the supply, was revised."], 0,
     "The subject 'officer' logically performed both the action of exhausting and the later revision."),
    ("The order applies to ___ personnel posted beyond the perimeter.",
     ["all", "every", "each", "each of"], 0,
     "'All' is the determiner appropriate before a plural noun referring collectively to personnel."),
    ("Neither the pilots nor the flight commander ___ authority to cancel the exercise.",
     ["has", "have", "is having", "are"], 0,
     "With neither/nor, the verb agrees with the nearer subject 'flight commander', which is singular."),
    ("Not until the reports were cross-checked ___ the incident.",
     ["was the cause established", "the cause was established", "did established the cause", "the cause established"], 0,
     "Negative adverbial 'Not until…' triggers subject-auxiliary inversion in the following clause."),
    ("The evidence is too inconclusive ___ any definite charge.",
     ["to sustain", "for sustaining", "that sustain", "of sustaining"], 0,
     "'Too inconclusive to sustain' is the standard too…to construction."),
    ("A competent analyst should distinguish mere correlation ___ demonstrable causation.",
     ["from", "with", "by", "against"], 0,
     "'Distinguish…from' is the standard dependent preposition pairing."),
    ("The proposal, which has been revised twice, ___ to the cabinet next week.",
     ["is to be submitted", "was submitted", "submits", "has submit"], 0,
     "The present progressive passive construction 'is to be submitted' can express a future plan."),
    ("Each of the new manuals ___ an appendix explaining the emergency procedure.",
     ["contains", "contain", "are containing", "have contained"], 0,
     "The distributive determiner 'Each' takes a singular verb, 'contains'."),
]


def make_advanced():
    output = []
    for i, (text, options, answer, explanation) in enumerate(ADVANCED_QUESTIONS, 1):
        output.append({
            "module": "Advanced / Descriptive Language",
            "source_section": "MCQ-based advanced language skills",
            "text": text,
            "q": {
                "q": text,
                "options": options,
                "answer": answer,
                "topic": "Advanced Language",
                "subtopic": "Formal and coherent expression",
                "explanation": explanation,
            },
        })
    return output


def make_grammar():
    output = []
    for text, options, answer, explanation in GRAMMAR_QUESTIONS:
        output.append({
            "module": "Grammar",
            "source_section": "Original grammar application",
            "text": text,
            "q": {
                "q": text,
                "options": options,
                "answer": answer,
                "topic": "Grammar",
                "subtopic": "Advanced application",
                "explanation": explanation,
            },
        })
    return output


def select_questions():
    available = flatten_sources()
    selected = []
    used_keys = set()

    for module, count in TARGET_COUNTS.items():
        if module == "Advanced / Descriptive Language":
            continue
        candidates = [r for r in available if r["module"] == module and normalise(r["text"]) not in used_keys]
        for row in candidates[:count]:
            selected.append(row)
            used_keys.add(normalise(row["text"]))

    selected.extend(make_grammar())
    selected.extend(make_advanced())
    return selected


def difficulty_for_index(index):
    if index < 20:
        return "Easy"
    if index < 80:
        return "Moderate"
    if index < 170:
        return "Hard"
    return "Very Hard"


def topic_for(row):
    q = row["q"]
    if q.get("topic"):
        return q["topic"]
    source = row["source_section"]
    return source


def subtopic_for(row):
    q = row["q"]
    if q.get("subtopic"):
        return q["subtopic"]
    return row["source_section"]


def build():
    selected = select_questions()
    if len(selected) != 200:
        missing = Counter(r["module"] for r in selected)
        raise RuntimeError(f"Expected 200 questions, got {len(selected)}. Counts: {dict(missing)}")

    paper_questions = []
    answer_key = []
    sections = {}
    target_answers = [0] * 50 + [1] * 50 + [2] * 50 + [3] * 50
    random.Random(20261118).shuffle(target_answers)

    for i, row in enumerate(selected, 1):
        q = row["q"]
        text = row["text"]
        original_options = list(q["options"])
        original_answer = q["answer"]
        answer = target_answers[i - 1]
        remaining = [opt for j, opt in enumerate(original_options) if j != original_answer]
        options = remaining[:answer] + [original_options[original_answer]] + remaining[answer:]
        difficulty = difficulty_for_index(i - 1)
        topic = topic_for(row)
        subtopic = subtopic_for(row)
        pattern = "PYQ_PATTERN" if i <= 135 else ("TREND_BASED" if i <= 175 else "HIGH_DIFFICULTY")

        qid = f"ENG-MASTER-{i:03d}"
        item = {
            "id": qid,
            "section": row["module"],
            "topic": topic,
            "subtopic": subtopic,
            "difficulty": difficulty,
            "exam_level": ["CDS", "CAPF", "IBPS", "AFCAT", "SSC"],
            "pattern": pattern,
            "q": text,
            "options": options,
            "answer": answer,
            "marks_correct": 0.83,
            "marks_wrong": -0.33,
            "explanation": q.get("explanation") or (
                f"Option {chr(65 + answer)} is correct in the context of {topic.lower()}. "
                f"It is the choice that is grammatically and semantically consistent with the question."
            ),
        }
        paper_questions.append(item)

        explanation = item["explanation"]
        answer_key.append({
            "id": qid,
            "correct_answer": chr(65 + answer),
            "correct_option": options[answer],
            "explanation": explanation,
            "topic": topic,
            "subtopic": subtopic,
            "difficulty": difficulty,
            "exam_pattern": pattern,
            "why_other_options_are_wrong": [
                f"{chr(65 + j)}. {opt}: not the correct choice for this question."
                for j, opt in enumerate(options) if j != answer
            ],
        })

        sections.setdefault(row["module"], []).append(item)

    paper = {
        "id": "english-master-200",
        "title": "English Master Paper",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "CDS + CAPF AC + IBPS/SO + AFCAT/SSC",
        "discipline": "English",
        "source": "Original and syllabus-based practice questions informed by competitive-exam patterns; not an authentic PYQ paper",
        "verificationStatus": "Practice dataset; not an official UPSC or IBPS previous-year paper",
        "maximum_marks": 166,
        "correct_mark": 0.83,
        "negative_mark": 0.33,
        "unattempted_mark": 0,
        "sections": [
            {"name": name, "questions": sections.get(name, [])}
            for name in TARGET_COUNTS
        ],
    }

    (DATA / "english-master-200.json").write_text(
        json.dumps(paper, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    key = {
        "id": "english-master-200-answer-key",
        "paper_id": "english-master-200",
        "total_questions": 200,
        "maximum_marks": 166,
        "marking": {"correct": 0.83, "wrong": -0.33, "unattempted": 0},
        "answers": answer_key,
    }
    (DATA / "english-master-200-answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    build()
