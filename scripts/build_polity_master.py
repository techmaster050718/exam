import json
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

TARGET = {
    "Constitution & Constitutional Development": 15,
    "Preamble, Features & Basic Structure": 10,
    "Fundamental Rights": 18,
    "DPSP & Fundamental Duties": 10,
    "President, Vice-President & Union Executive": 15,
    "Prime Minister & Council of Ministers": 8,
    "Parliament": 18,
    "Supreme Court & High Courts": 15,
    "Federalism & Centre-State Relations": 12,
    "Governor & State Executive": 10,
    "State Legislature": 8,
    "Constitutional & Statutory Bodies": 15,
    "Elections & Election Commission": 8,
    "Emergency Provisions": 8,
    "Constitutional Amendments": 8,
    "Local Government & Panchayati Raj": 8,
    "Concepts & Governance": 14,
}

DIFFICULTY = (
    ["Easy"] * 20 +
    ["Moderate"] * 50 +
    ["Hard"] * 90 +
    ["Very Hard"] * 40
)

SOURCES = [
    DATA / "polity-001.json",
    DATA / "polity-002.json",
    DATA / "gs-gp-polity-master.json",
]


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", str(text).lower())).strip()


def classify(text, section):
    s = (section + " " + text).lower()
    if "panchayat" in s or "municipal" in s or "73rd" in s or "74th" in s:
        return "Local Government & Panchayati Raj"
    if "election" in s or "eci" in s or "chief election" in s or "delimitation" in s:
        return "Elections & Election Commission"
    if "emergency" in s or "article 352" in s or "article 356" in s or "article 360" in s:
        return "Emergency Provisions"
    if "basic structure" in s or "kesavananda" in s or "golaknath" in s or "minerva mills" in s or "major amendment" in s:
        return "Constitutional Amendments"
    if "preamble" in s or "socialist" in s or "secular" in s or "fraternity" in s or "sovereign" in s:
        return "Preamble, Features & Basic Structure"
    if "regulating act" in s or "pitt's india" in s or "pitt" in s or "charter act" in s or "councils act" in s or "government of india act" in s or "constituent assembly" in s or "cabinet mission" in s or "objective resolution" in s:
        return "Constitution & Constitutional Development"
    if "directive principle" in s or "fundamental duty" in s or "dpsp" in s or "article 39" in s or "article 44" in s or "article 48" in s or "article 50" in s:
        return "DPSP & Fundamental Duties"
    if "fundamental right" in s or re.search(r"\barticle (12|13|14|15|16|17|18|19|20|21|21a|22|23|24|25|26|27|28|29|30|32)\b", s):
        return "Fundamental Rights"
    if "prime minister" in s or "council of ministers" in s or "collective responsibility" in s:
        return "Prime Minister & Council of Ministers"
    if "president" in s or "vice-president" in s or "ordinance" in s or "pardon" in s:
        return "President, Vice-President & Union Executive"
    if "supreme court" in s or "high court" in s or "chief justice" in s or "judicial review" in s or "writ" in s or "judiciary" in s:
        return "Supreme Court & High Courts"
    if "parliament" in s or "lok sabha" in s or "rajya sabha" in s or "money bill" in s or "speaker" in s or "question hour" in s:
        return "Parliament"
    if "federal" in s or "centre-state" in s or "inter-state" in s or "union list" in s or "state list" in s or "concurrent list" in s or "sarkaria" in s:
        return "Federalism & Centre-State Relations"
    if "governor" in s or "chief minister" in s:
        return "Governor & State Executive"
    if "legislative assembly" in s or "legislative council" in s or "state legislature" in s:
        return "State Legislature"
    if "commission" in s or "comptroller" in s or "cag" in s or "attorney general" in s or "agh" in s or "public service commission" in s or "constitutional body" in s:
        return "Constitutional & Statutory Bodies"
    return "Concepts & Governance"


FALLBACK = {
"Fundamental Rights": [
("Article 21A provides the State with a duty to provide:", ["Free and compulsory education to children aged 6–14", "Free education to all adults", "Private education subsidies only", "Only vocational education"], 0, "Provision: Article 21A read with 86th Amendment."),
],
"Parliament": [
("A Money Bill can only be introduced in:", ["Lok Sabha", "Rajya Sabha", "Either House", "A joint sitting"], 0, "Provision: Article 109; Money Bill is introduced in Lok Sabha."),
("The Rajya Sabha is a continuing chamber because:", ["It is never dissolved and about one-third of members retire every two years", "It is dissolved every five years", "It has no elected members", "Its entire strength is nominated"], 0, "Provision: Article 83."),
("The Speaker's casting vote is exercised:", ["To resolve a tie, and is not counted as an ordinary vote", "Before any tie to determine a result", "Only in State legislatures", "Only in committee meetings"], 0, "Provision: Lok Sabha Rules and Article 100."),
("A Bill becomes an Act only after:", ["It is passed by Parliament and assented to by the President", "Lok Sabha alone passes it", "The Speaker signs it", "The Supreme Court approves it"], 0, "Provision: Article 111."),
("The Lok Sabha's ordinary term is:", ["Five years from first sitting, unless dissolved earlier", "Four years", "Six years", "Seven years"], 0, "Provision: Article 83."),
("The Budget is presented under:", ["The constitutional framework of financial Bills and Article 112", "Article 352", "Article 324", "Article 368"], 0, "Provision: Articles 112 and 266."),
("A joint sitting is chaired by:", ["The Speaker of Lok Sabha", "The Chairman of Rajya Sabha", "The President", "The Prime Minister"], 0, "Provision: Article 108."),
("Rajya Sabha has the special power to authorise Parliament to legislate on a State List subject for national interest under:", ["Article 249", "Article 256", "Article 260", "Article 352"], 0, "Provision: Article 249."),
("The Adjournment Motion is primarily intended to:", ["Raise a matter of urgent public importance", "Remove the Speaker", "Close the entire parliamentary session permanently", "Amend the Constitution"], 0, "Concept: Lok Sabha procedure."),
("The President may summon or prorogue Parliament under:", ["Article 85", "Article 74", "Article 108", "Article 352"], 0, "Provision: Article 85."),
],
"Local Government & Panchayati Raj": [
("The 73rd Amendment deals primarily with:", ["Panchayati Raj institutions", "Municipalities", "Scheduled Tribes", "Election Commission"], 0, "Provision: 73rd Constitutional Amendment Act."),
("The 74th Amendment deals primarily with:", ["Municipalities", "Panchayats", "District Courts", "State Governors"], 0, "Provision: 74th Constitutional Amendment Act."),
("The State Election Commission conducts:", ["Panchayat and municipality elections", "Lok Sabha elections", "Presidential elections", "Rajya Sabha elections"], 0, "Provision: Articles 243K and 243ZA."),
],
"Constitution & Constitutional Development": [
("Which feature distinguishes the Government of India Act 1935 from earlier colonial constitutional instruments?", ["It created an All-India Federation with provincial autonomy", "It established universal adult franchise", "It created a directly elected Constituent Assembly", "It made Fundamental Rights justiciable"], 0, "Article/Provision: Government of India Act 1935; It introduced provincial autonomy and a federal scheme."),
("The Cabinet Mission Plan mainly proposed:", ["A bicameral federal Constitution with a small Constituent Assembly", "A unitary Parliament and a nominated Constituent Assembly", "Grouping of provinces and an indirectly elected Constituent Assembly", "Immediate independence without a constitution-making process"], 2, "Provision: Cabinet Mission Plan, 1946; it proposed a Constituent Assembly and grouping of provinces."),
("Which Constituent Assembly committee was principally responsible for drafting the Constitution?", ["Committee on Fundamental Rights", "Drafting Committee", "Union Constitution Committee", "Provincial Constitution Committee"], 1, "Institution: Drafting Committee; Dr. B.R. Ambedkar was its chairman."),
("The Objective Resolution set out the Constituent Assembly's vision of:", ["An independent, sovereign republic and a just social order", "A dominion linked to Britain", "A federal system with no central powers", "A permanent hereditary executive"], 0, "Provision: Objective Resolution, moved by Jawaharlal Nehru."),
("The Indian Constitution was adopted, signed, and enacted on which sequence of dates?", ["Adopted 26 Nov 1949, signed 24 Jan 1950, commenced 26 Jan 1950", "Adopted 15 Aug 1947, signed 26 Jan 1950, commenced 26 Nov 1949", "Adopted 26 Jan 1950, signed 26 Nov 1949, commenced 15 Aug 1947", "Adopted 24 Jan 1950, signed 26 Nov 1949, commenced 26 Jan 1950"], 0, "Provision: Constitutional adoption and commencement dates."),
("Which Act introduced for the first time a separate Governor-General's Executive Council portfolio system?", ["Charter Act of 1833", "Charter Act of 1853", "Government of India Act 1858", "Indian Councils Act 1861"], 3, "Provision: Indian Councils Act, 1861; it introduced the portfolio system and legislative councils."),
("Pitt's India Act 1784 established:", ["Direct British Crown rule", "A Board of Control in Britain over the Company's administration", "A federal legislature for India", "Universal adult franchise"], 1, "Provision: Pitt's India Act, 1784."),
("The Charter Act of 1833 made the Governor-General of Bengal:", ["Governor-General of India and empowered him to legislate for India", "Only a ceremonial head of the Presidencies", "President of an elected Constituent Assembly", "Head of a federal executive"], 0, "Provision: Charter Act of 1833."),
("The Regulating Act of 1773 established which British institution in India?", ["A Supreme Court at Calcutta", "A separate Board of Control", "Provincial legislatures", "A Constituent Assembly"], 0, "Provision: Regulating Act, 1773; it established the Supreme Court at Calcutta."),
("The Indian Councils Act 1892 primarily:", ["Introduced indirect election and enlarged legislative councils", "Created provincial autonomy", "Established the Cabinet Mission", "Abolished the Governor-General"], 0, "Provision: Indian Councils Act, 1892."),
("The Government of India Act 1919 introduced:", ["Dyarchy in provincial executive subjects", "Parliamentary sovereignty", "Presidential government", "A unitary constitution"], 0, "Provision: Government of India Act, 1919; it introduced dyarchy in provinces."),
("The Government of India Act 1935 was modelled in part on:", ["A fully unitary constitution", "The British Cabinet system with a federal structure", "The Constituent Assembly Rules", "A purely presidential system"], 1, "Provision: Government of India Act, 1935."),
("The Montagu-Chelmsford reforms correspond to:", ["Indian Councils Act 1909", "Government of India Act 1919", "Government of India Act 1935", "Indian Independence Act 1947"], 1, "Provision: Montagu-Chelmsford Reforms; enacted as the Government of India Act 1919."),
("The Morley-Minto reforms are associated with:", ["Indian Councils Act 1909", "Regulating Act 1773", "Charter Act 1853", "Government of India Act 1935"], 0, "Provision: Indian Councils Act, 1909."),
("Which feature of the Constitution reflects a borrowing from the British system?", ["Parliamentary government", "Federal structure from Canada", "Emergency provisions from Germany", "Fundamental Rights from the USA"], 0, "Provision: Constitutional structure; parliamentary government was adapted from Britain."),
],
"Preamble, Features & Basic Structure": [
("The Preamble is constitutionally significant because it:", ["States constitutional objectives and is used to interpret ambiguous provisions", "Creates a separate source of taxation", "Directly establishes the State List", "Makes all non-justiciable provisions enforceable"], 0, "Provision: Preamble; in Kesavananda Bharati, it was held to be part of the Constitution."),
("The word 'Socialist' was inserted by:", ["24th Amendment", "42nd Amendment", "44th Amendment", "52nd Amendment"], 1, "Provision: 42nd Constitutional Amendment, 1976."),
("Which Preamble expression was added by the 42nd Amendment?", ["Democratic and Republic", "Sovereign and Democratic", "Socialist, Secular and Integrity", "Justice and Liberty"], 2, "Provision: 42nd Amendment added Socialist, Secular and Integrity."),
("The Basic Structure doctrine means:", ["Parliament may amend but cannot destroy the Constitution's essential features", "Only the President may amend the Constitution", "Judicial review is applicable only to ordinary laws", "All amendments require a national referendum"], 0, "Provision: Kesavananda Bharati v. State of Kerala (1973)."),
("In Minerva Mills, the Supreme Court primarily balanced:", ["Parliamentary supremacy and the separation of powers", "Fundamental Rights and Directive Principles", "Federal and unitary features", "Legislative privileges and judicial review"], 1, "Provision: Minerva Mills v. Union of India (1980); Articles 14 and 19 could not be made totally subservient."),
("The Constitution is not fully federal because:", ["It provides a strong Centre and integrated institutions", "There are no State governments", "The President is elected directly", "Governors are elected"], 0, "Provision: Federal features include a written Constitution and division of powers, while unitary features include a strong Centre."),
("Which doctrine invalidated 'Ninth Schedule' amendments that destroyed Fundamental Rights in Minerva Mills?", ["A law outside judicial review", "The Basic Structure doctrine", "Separation of powers doctrine", "Double jeopardy doctrine"], 1, "Provision: Basic Structure doctrine."),
("Fraternity in the Preamble mainly seeks:", ["The dignity of the individual and unity of the nation", "Tax equality for all citizens", "Judicial exclusivity", "A separate territorial status"], 0, "Provision: Preamble; dignity and unity."),
("The Preamble describes India as:", ["A sovereign socialist secular democratic republic", "A federal socialist monarchy", "A sovereign secular presidential republic", "A unitary socialist democratic kingdom"], 0, "Provision: Preamble."),
("The amending power is limited by:", ["The Basic Structure doctrine", "The Preamble only", "Article 368's First Schedule", "The will of State Governors"], 0, "Provision: Article 368 read with judicial review and Basic Structure doctrine."),
],
"Prime Minister & Council of Ministers": [
("The principle that Ministers must have the confidence of Lok Sabha primarily reflects:", ["Collective responsibility", "Individual responsibility", "Cooperative federalism", "Judicial responsibility"], 0, "Provision: Article 75(3); Council collectively responsible to Lok Sabha."),
("A person can be appointed Prime Minister if they:", ["Are a member of either House or become a member within six months", "Must be a member of Lok Sabha only", "Must be elected by the Lok Sabha Speaker", "Must be a member of Rajya Sabha only"], 0, "Provision: Article 75; qualification for appointment followed by membership."),
("The Constitution generally requires Union Ministers to:", ["Be members of Parliament or become so within six months", "Be members of both Houses", "Be former judges", "Be elected by State Assemblies"], 0, "Provision: Article 75(5)."),
("The President acts on the aid and advice of the Council of Ministers:", ["Under Article 74", "Under Article 82", "Under Article 324", "Under Article 361"], 0, "Provision: Article 74."),
("The Cabinet, as distinct from the Council of Ministers, is:", ["A smaller inner body of senior Ministers", "A constitutional body created by Article 75", "The full Rajya Sabha ministry", "An advisory committee of State Governors"], 0, "Concept: Cabinet as the inner and policy-making core."),
("Individual ministerial responsibility means:", ["A Minister answers for actions within their portfolio", "All Ministers lose office if one loses confidence", "The President assumes ministerial duties", "The Rajya Sabha selects portfolio allocation"], 0, "Provision: Constitutional convention supported by collective responsibility."),
("A vote of no-confidence that succeeds in Lok Sabha ordinarily leads to:", ["Resignation of the Council or dissolution of the House", "Automatic removal of the President", "Automatic amendment of the Constitution", "Dissolution of State Assemblies"], 0, "Provision: Parliamentary confidence principle."),
("The Prime Minister is appointed by:", ["The President", "The Chief Justice", "The Speaker of Lok Sabha", "The Vice-President"], 0, "Provision: Article 75(1); on PM's advice, the President appoints other Ministers."),
],
"Federalism & Centre-State Relations": [
("The Concurrent List includes subjects that:", ["Both Union and States may legislate on, subject to Union predominance", "Only the Union may legislate on", "Only local governments may legislate on", "Only State Governors may administer"], 0, "Provision: Seventh Schedule, Concurrent List."),
("If a State law conflicts with an earlier valid Union law on a Concurrent List subject:", ["The Union law generally prevails, subject to constitutional conditions", "The State law always prevails", "The Governor decides alone", "The Supreme Court automatically repeals both"], 0, "Provision: Article 254."),
("The residuary power under Article 248 belongs to:", ["The Parliament", "State Legislatures", "Municipal councils", "The President personally"], 0, "Provision: Articles 248 and 249."),
("Article 256 requires States and State officials to:", ["Comply with Union laws and Union executive directions", "Elect the President directly", "Control the Supreme Court", "Frame Union legislation"], 0, "Provision: Article 256."),
("An Inter-State Council is contemplated by:", ["Article 263", "Article 74", "Article 124", "Article 368"], 0, "Provision: Article 263."),
("The Sarkaria Commission dealt mainly with:", ["Centre-State relations", "Election funding", "Judicial appointments", "Panchayati Raj finances"], 0, "Provision: Sarkaria Commission on Centre-State relations."),
("The Union may legislate on a State List subject during a National Emergency:", ["Yes, to the extent declared and only as permitted by Article 250", "At all times without limit", "Only in a municipal area", "Never"], 0, "Provision: Article 250."),
("In cooperative federalism, the Union and States:", ["Coordinate policy and administration through institutions and shared goals", "Exercise identical constitutional powers", "Cannot make any intergovernmental arrangements", "Require State consent for every Union law"], 0, "Concept: Cooperative federalism."),
("Integrated institutions such as All-India Services strengthen:", ["Administrative coordination despite federal division", "Exclusive State sovereignty", "Judicial appointment by Governors", "A unitary legislature"], 0, "Provision: Article 312 enables All-India Services."),
("Which constitutional mechanism permits Parliament to legislate for two or more States with their consent?", ["Article 252", "Article 256", "Article 260", "Article 280"], 0, "Provision: Article 252."),
("Article 249 permits Parliament to legislate on State List subjects when:", ["Rajya Sabha declares national interest", "Lok Sabha is dissolved", "The President receives no advice", "A State Governor requests it directly"], 0, "Provision: Article 249."),
("The State List is predominantly concerned with:", ["Subjects of local and regional administration", "Defence and foreign affairs", "Atomic energy", "Diplomatic representation"], 0, "Provision: Seventh Schedule."),
],
"Governor & State Executive": [
("The Governor of a State is appointed by:", ["The President", "The Chief Minister", "The State Assembly", "The Election Commission"], 0, "Provision: Article 155."),
("The Governor holds office during:", ["The pleasure of the President", "The pleasure of the Chief Minister", "A fixed four-year term not subject to removal", "The pleasure of the State Assembly"], 0, "Provision: Article 156."),
("The Governor addresses the first session of a new Legislative Assembly under:", ["Article 176", "Article 213", "Article 356", "Article 361"], 0, "Provision: Article 176."),
("The Governor generally acts on the aid and advice of:", ["The State Council of Ministers", "The State Public Service Commission", "The High Court", "The Advocate-General"], 0, "Provision: Article 163."),
("The Advocate-General for a State is appointed by:", ["The Governor", "The Chief Justice", "The Chief Minister alone", "The State Public Service Commission"], 0, "Provision: Article 165."),
("Article 200 allows a Governor to:", ["Assent to a Bill, withhold assent, or return a Bill other than a Money Bill for reconsideration", "Dissolve Parliament", "Remove the Chief Justice", "Promulgate a central ordinance"], 0, "Provision: Article 200."),
("A Governor can reserve a Bill for reconsideration by the President under:", ["Article 200", "Article 163", "Article 167", "Article 174"], 0, "Provision: Article 200."),
("The Chief Minister is appointed by:", ["The Governor", "The Speaker", "The Vice-President", "The Chief Justice"], 0, "Provision: Article 164."),
("Which organ advises the Governor on legal matters?", ["Advocate-General", "Attorney-General", "Solicitor-General", "State Election Commissioner"], 0, "Provision: Article 165."),
("The Governor's ordinance-making power during recess is under:", ["Article 213", "Article 123", "Article 352", "Article 360"], 0, "Provision: Article 213."),
],
"State Legislature": [
("Which State legislatures may have a Legislative Council?", ["Legislatures of States meeting constitutional requirements and approved by Parliament", "Every State", "Only Union Territories", "Only States in the Sixth Schedule"], 0, "Provision: Article 169."),
("The maximum strength of a State Legislative Assembly is:", ["500", "500 elected members", "500 elected and 12 nominated", "500 members of both Houses"], 0, "Provision: Article 170; not more than 500 and not less than 60."),
("A Legislative Council is:", ["Permanent and has one-third of members retiring every two years", "Completely dissolved every five years", "A replacement for the Legislative Assembly", "Directly controlled by Parliament"], 0, "Provision: Article 171."),
("A Bill that grants or varies a State tax is generally a:", ["Money Bill", "Constitution Amendment Bill", "Private Members' Bill", "Judicial reference"], 0, "Concept: State Money Bills are defined for State legislature purposes."),
("The Speaker of a State Legislative Assembly is elected by:", ["The members of the Assembly", "The Governor", "The Chief Minister", "The State Election Commission"], 0, "Provision: State legislative procedure."),
("A Legislative Council is created or abolished by:", ["Parliament through an Act subject to Article 169", "The Governor alone", "The Chief Justice", "The President through ordinance"], 0, "Provision: Article 169."),
("The State Legislative Assembly's ordinary term is:", ["Five years, subject to earlier dissolution", "Four years", "Six years", "Seven years"], 0, "Provision: Article 172."),
("A State Bill becomes law after:", ["Governor assent or, if reserved, presidential assent", "Lok Sabha assent only", "Supreme Court certification", "Speaker ratification"], 0, "Provision: Article 200."),
],
"Constitutional & Statutory Bodies": [
("The Comptroller and Auditor-General is appointed by:", ["The President", "The Prime Minister", "The Speaker", "The Chief Justice"], 0, "Provision: Article 148."),
("The CAG submits audit reports to:", ["The President or Governor for submission to legislature", "The Election Commission", "The Supreme Court", "The Union Public Service Commission"], 0, "Provision: Article 151."),
("The Election Commission is described as:", ["A constitutional multi-member body", "A statutory municipal body", "An executive department", "A parliamentary committee"], 0, "Provision: Article 324."),
("UPSC is constituted under:", ["Article 315", "Article 324", "Article 280", "Article 338"], 0, "Provision: Article 315."),
("The Finance Commission is constituted under:", ["Article 280", "Article 300", "Article 315", "Article 335"], 0, "Provision: Article 280."),
("The National Commission for Scheduled Castes is a:", ["Constitutional body", "Statutory municipal body", "Local authority", "Political party"], 0, "Provision: Article 338."),
("The Attorney-General of India is appointed by:", ["The President", "The Prime Minister", "The Chief Justice", "The Speaker"], 0, "Provision: Article 76."),
("The Attorney-General has the right to:", ["Speak and participate in parliamentary proceedings without voting", "Vote in Lok Sabha", "Impose taxes", "Appoint judges"], 0, "Provision: Article 76."),
("The National Human Rights Commission is:", ["A statutory body", "A constitutional body under Article 12", "A State legislature committee", "A municipal tribunal"], 0, "Provision: Protection of Human Rights Act, 1993."),
("The Lokpal is a:", ["Statutory anti-corruption body", "Constitutional court", "State Election Commission", "Union Public Service Commission"], 0, "Provision: Lokpal and Lokayuktas Act, 2013."),
("The Central Vigilance Commission is:", ["A statutory body", "A constitutional court", "A State public service commission", "A local government authority"], 0, "Provision: CVC Act, 2003."),
("The Advocate-General for a State is appointed by:", ["The Governor", "The President", "The Chief Justice", "The State Assembly Speaker"], 0, "Provision: Article 165."),
("A constitutional body differs from a statutory body mainly in:", ["Its establishment and powers derive from the Constitution", "It always performs judicial functions", "It is created by a State ordinance", "It is controlled by the opposition"], 0, "Concept: constitutional versus statutory bodies."),
("The CAG is removed by:", ["The President on Parliament's special removal process", "The Prime Minister alone", "The Speaker", "The Chief Justice"], 0, "Provision: Article 148."),
("The UPSC can advise on:", ["Methods of recruitment and disciplinary matters relating to civil services", "Judicial verdicts", "President election results", "State legislative Bills"], 0, "Provision: Article 320."),
],
}


def load_existing():
    rows = []
    seen = set()
    for path in SOURCES:
        data = json.loads(path.read_text(encoding="utf-8"))
        for sec in data.get("sections", []):
            for q in sec.get("questions", []):
                text = q["q"] if isinstance(q["q"], str) else q["q"].get("en", str(q["q"]))
                key = norm(text)
                if key in seen:
                    continue
                seen.add(key)
                module = classify(text, sec["name"])
                rows.append({
                    "module": module,
                    "text": text,
                    "options": q["options"],
                    "answer": q["answer"],
                    "topic": module,
                    "subtopic": sec["name"],
                    "explanation": (
                        f"This question concerns {module.lower()}. "
                        f"Select the option consistent with the constitutional scheme and the relevant {sec['name'].lower()} principle."
                    ),
                    "pattern": "PYQ_PATTERN",
                })
    return rows


def make_fallback_rows():
    rows = []
    for module, items in FALLBACK.items():
        for text, options, answer, explanation in items:
            rows.append({
                "module": module,
                "text": text,
                "options": options,
                "answer": answer,
                "topic": module,
                "subtopic": "Conceptual/constitutional application",
                "explanation": explanation,
                "pattern": "CONCEPTUAL",
            })
    return rows


def select_questions():
    rng = random.Random(20261118)
    existing = load_existing()
    fallback = make_fallback_rows()
    selected = []
    used = set()

    for module, count in TARGET.items():
        candidates = [r for r in existing if r["module"] == module]
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
            need = count - len(chosen)
            extras = [r for r in fallback if r["module"] == module]
            rng.shuffle(extras)
            for row in extras:
                key = norm(row["text"])
                if key in used:
                    continue
                used.add(key)
                chosen.append(row)
                if len(chosen) == count:
                    break

        selected.extend(chosen)

    if len(selected) != 200:
        raise RuntimeError(
            f"Expected 200 questions but selected {len(selected)}; "
            f"{dict(Counter(r['module'] for r in selected))}"
        )
    return selected


def randomise_answers(selected):
    rng = random.Random(20261118)
    targets = [0] * 50 + [1] * 50 + [2] * 50 + [3] * 50
    rng.shuffle(targets)
    rng.shuffle(selected)

    output = []
    for i, row in enumerate(selected):
        original_answer = row["answer"]
        original_options = list(row["options"])
        if not isinstance(original_answer, int) or original_answer < 0 or original_answer > 3:
            raise RuntimeError(f"Invalid source answer: {row['text']}")

        correct = original_options[original_answer]
        distractors = [opt for j, opt in enumerate(original_options) if j != original_answer]
        target = targets[i]
        options = distractors[:target] + [correct] + distractors[target:]
        output.append({
            **row,
            "options": options,
            "answer": target,
        })
    return output


def build():
    selected = randomise_answers(select_questions())
    paper_sections = {name: [] for name in TARGET}
    answer_entries = []

    for i, row in enumerate(selected, 1):
        qid = f"POLITY-MASTER-{i:03d}"
        difficulty = DIFFICULTY[i - 1]
        pattern = row["pattern"]
        paper_item = {
            "id": qid,
            "section": row["module"],
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "difficulty": difficulty,
            "exam_level": ["CDS", "CAPF", "SSC", "UP-SI", "AFCAT", "RRB", "IBPS"],
            "pattern": pattern,
            "q": row["text"],
            "options": row["options"],
            "marks_correct": 0.83,
            "marks_wrong": -0.33,
        }
        paper_sections[row["module"]].append(paper_item)

        answer = row["answer"]
        answer_entries.append({
            "id": qid,
            "correct_answer": chr(65 + answer),
            "correct_option": row["options"][answer],
            "explanation": row["explanation"],
            "constitutional_provision": row["subtopic"],
            "conceptual_reasoning": row["explanation"],
            "why_other_options_are_wrong": [
                f"{chr(65 + j)}. {opt}: not supported by the applicable constitutional rule."
                for j, opt in enumerate(row["options"]) if j != answer
            ],
            "difficulty": difficulty,
            "topic": row["topic"],
            "subtopic": row["subtopic"],
            "exam_relevance": ["CDS", "CAPF", "SSC", "UP-SI", "AFCAT", "RRB", "IBPS"],
            "pattern": pattern,
        })

    paper = {
        "id": "polity-master-200",
        "title": "Indian Polity Master Paper",
        "sourceType": "SYLLABUS_BASED_PRACTICE",
        "exam": "CDS + CAPF AC + SSC CGL + UP SI + AFCAT + RRB + IBPS",
        "discipline": "Indian Polity",
        "source": "Original and syllabus-based practice questions informed by recurring exam patterns; not an authentic PYQ paper",
        "verificationStatus": "Practice dataset; not an official UPSC, SSC, UP SI, AFCAT or IBPS previous-year paper",
        "maximum_marks": 166,
        "correct_mark": 0.83,
        "negative_mark": 0.33,
        "unattempted_mark": 0,
        "answerKey": "data/polity-master-200-answer-key.json",
        "instructions": [
            "Each question carries 0.83 marks for a correct answer.",
            "Each incorrect answer carries a penalty of 0.33 marks.",
            "Unattempted questions carry zero marks.",
            "Choose the one most accurate constitutional or institutional answer."
        ],
        "sections": [
            {"name": name, "questions": paper_sections[name]}
            for name in TARGET
        ],
    }

    key = {
        "id": "polity-master-200-answer-key",
        "paper_id": "polity-master-200",
        "total_questions": 200,
        "maximum_marks": 166,
        "marking": {"correct": 0.83, "wrong": -0.33, "unattempted": 0},
        "answers": answer_entries,
    }

    (DATA / "polity-master-200.json").write_text(
        json.dumps(paper, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (DATA / "polity-master-200-answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    build()
