"""
Generates:
1. data/revision/polity/polity-revision.md
2. data/revision/geography/geography-revision.md
3. data/revision/english/english-revision.md
"""
import os

os.makedirs("data/revision/polity", exist_ok=True)
os.makedirs("data/revision/geography", exist_ok=True)
os.makedirs("data/revision/english", exist_ok=True)

# 1. polity-revision.md
POLITY_MD = """# Indian Polity & Constitution Revision Notes
> **Exam-Ready Reference | Competitive Exams (UPSC, UP Police SI, CDS, CAPF, SSC, State PSC)**

---

## 1. PREAMBLE & SALIENT FEATURES
* **Adoption Date:** 26th November 1949; **Enactment Date:** 26th January 1950.
* **Borrowed Features:**
  * Parliamentary system, Rule of Law, Single Citizenship $\\to$ **UK (Britain)**
  * Fundamental Rights, Judicial Review, Preamble, Impeachment of President $\\to$ **USA**
  * Directive Principles of State Policy (DPSP), Nomination of RS members $\\to$ **Ireland**
  * Concurrent List, Joint Sitting of Parliament $\\to$ **Australia**
  * Emergency provisions (suspension of Fundamental Rights) $\\to$ **Weimar Constitution (Germany)**
  * Amendment of the Constitution $\\to$ **South Africa**
  * Fundamental Duties, Ideals of Justice in Preamble $\\to$ **USSR (Russia)**
* **42nd Amendment (1976):** Added three words to Preamble: **"SOCIALIST"**, **"SECULAR"**, and **"INTEGRITY"**.

---

## 2. FUNDAMENTAL RIGHTS (ARTICLES 12 – 35)

| Right | Articles | Key Provisos |
| :--- | :---: | :--- |
| **Right to Equality** | **14 – 18** | Art 14: Equality before law; Art 15: No discrimination; Art 16: Equal opportunity in public employment; Art 17: Abolition of Untouchability; Art 18: Abolition of Titles |
| **Right to Freedom** | **19 – 22** | Art 19: 6 Freedoms (Speech, Assembly, Association, Movement, Residence, Profession); Art 20: Protection against double jeopardy & self-incrimination; Art 21: Right to Life & Personal Liberty; Art 21A: Right to Education (6–14 yrs, 86th Amd); Art 22: Preventive detention safeguards |
| **Right against Exploitation** | **23 – 24** | Art 23: Prohibition of human trafficking & forced labor; Art 24: Prohibition of child labor in factories/mines (<14 yrs) |
| **Right to Freedom of Religion** | **25 – 28** | Art 25: Freedom of conscience & profession; Art 26: Manage religious affairs; Art 27: No taxes for religion; Art 28: Religious instruction |
| **Cultural & Educational Rights** | **29 – 30** | Art 29: Protection of minority interests; Art 30: Establish & administer educational institutions |
| **Right to Constitutional Remedies** | **32** | "Heart and Soul of the Constitution" (Dr. B.R. Ambedkar). Supreme Court issues 5 Writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto) |

> Note: Right to Property was deleted from Fundamental Rights by **44th Amendment (1978)** and made a legal right under **Article 300A**.

---

## 3. CONSTITUTIONAL BODIES COMPARISON TABLE

| Body | Constitutional Article | Appointed By | Removal Mechanism | Tenure / Retirement Age |
| :--- | :---: | :--- | :--- | :--- |
| **Election Commission** | **324** | President | Like Supreme Court Judge (Parliament address) | 6 Years or 65 Years |
| **Comptroller & Auditor General (CAG)** | **148** | President | Like Supreme Court Judge | 6 Years or 65 Years |
| **UPSC (Chairman & Members)** | **315 – 323** | President | By President on SC inquiry report | 6 Years or 65 Years |
| **Finance Commission** | **280** | President | Reconstituted every 5 years | Specified in order |
| **Attorney General of India** | **76** | President | Pleasure of the President | No fixed tenure |

---

## 4. EMERGENCY PROVISIONS

| Emergency Type | Article | Grounds for Invocation | Parliamentary Approval Needed | Max Duration |
| :--- | :---: | :--- | :--- | :--- |
| **National Emergency** | **352** | War, External aggression, Armed rebellion *(44th Amd replaced 'internal disturbance')* | Within 1 month by Special Majority | Indefinite (extended 6 months at a time) |
| **President's Rule** (State Emergency)| **356** | Failure of constitutional machinery in State (Governor report / Art 365) | Within 2 months by Simple Majority | Max 3 Years (with EC certification after 1 yr) |
| **Financial Emergency** | **360** | Financial stability or credit of India threatened | Within 2 months by Simple Majority | Indefinite (Never declared in India) |

---

## 5. SCHEDULES OF THE CONSTITUTION (1 TO 12)
* **1st Schedule:** Names of States and Union Territories.
* **2nd Schedule:** Salaries and emoluments of President, Governors, Judges, CAG.
* **3rd Schedule:** Forms of Oaths and Affirmations.
* **4th Schedule:** Allocation of seats in Rajya Sabha.
* **5th Schedule:** Administration of Scheduled Areas and Scheduled Tribes.
* **6th Schedule:** Tribal areas in Assam, Meghalaya, Tripura, Mizoram (**AMTM**).
* **7th Schedule:** Division of Powers (Union List: 100, State List: 61, Concurrent List: 52).
* **8th Schedule:** 22 Official Recognized Languages.
* **9th Schedule:** Acts immune from judicial review (added by 1st Amendment, 1951; subject to basic structure review post-1973).
* **10th Schedule:** Anti-Defection Law (added by 52nd Amendment, 1985).
* **11th Schedule:** Panchayats (29 functional items, added by 73rd Amendment, 1992).
* **12th Schedule:** Municipalities (18 functional items, added by 74th Amendment, 1992).
"""

with open("data/revision/polity/polity-revision.md", "w", encoding="utf-8") as f:
    f.write(POLITY_MD)
print("Wrote data/revision/polity/polity-revision.md")


# 2. geography-revision.md
GEOGRAPHY_MD = """# Geography – Physical & Indian Geography Revision Notes
> **Exam-Ready Reference | Competitive Exams (UPSC, UP Police SI, CDS, CAPF, SSC, State PSC)**

---

## 1. EARTH'S INTERIOR & CRUSTAL LAYERS

```text
┌──────────────────────────────────────┐  0 - 35 km   Crust (Continental: SIAL, Oceanic: SIMA)
│ CRUST (Mohorovicic Discontinuity)    │
├──────────────────────────────────────┤  35 - 2,900 km Mantle (Asthenosphere at 100-200 km)
│ MANTLE (Gutenberg Discontinuity)     │               Composed of SIMA (Olivine, Peridotite)
├──────────────────────────────────────┤  2,900 - 5,150 km Outer Core (Liquid, NIFE: Ni + Fe)
│ OUTER CORE (Lehmann Discontinuity)   │                   Generates Earth's Magnetic Field!
├──────────────────────────────────────┤  5,150 - 6,371 km Inner Core (Solid, NIFE, intense pressure)
│ INNER CORE (Center of Earth)         │
└──────────────────────────────────────┘
```

---

## 2. ATMOSPHERIC LAYERS
* **Troposphere (0–12 km):** Contains 75% of atmospheric mass. All weather phenomena (clouds, rain, storms) occur here. Temperature decreases with height (Normal lapse rate: $6.5^\\circ\\text{C}$ per km).
* **Stratosphere (12–50 km):** Temperature increases with height. Contains the **Ozone Layer** ($\text{O}_3$, absorbs harmful UV radiation). Free from clouds; ideal for flying jet aircraft.
* **Mesosphere (50–80 km):** Coldest atmospheric layer (temperatures drop to $-100^\\circ\\text{C}$). Meteors burn up here upon entering atmosphere.
* **Thermosphere / Ionosphere (80–400 km):** Temperature rises rapidly. Contains ionized particles; reflects terrestrial radio waves back to Earth. Auroras occur here.
* **Exosphere (>400 km):** Outermost fringe; merges into interplanetary space. Dominated by hydrogen and helium.

---

## 3. DRAINAGE SYSTEMS OF INDIA (RIVERS QUICK CHEAT SHEET)

### 3.1 Himalayan River Systems
| River | Origin | Major Tributaries | Outflow | Key Dam / Projects |
| :--- | :--- | :--- | :--- | :--- |
| **Indus** | Bokhar Chu Glacier (Tibet, near Mansarovar) | Jhelum, Chenab, Ravi, Beas, Satluj (Left bank); Shyok, Gilgit (Right bank) | Arabian Sea | Baglihar (Chenab), Salal (Chenab), Bhakra Nangal (Satluj) |
| **Ganga** | Gangotri Glacier (Bhagirathi + Alaknanda at Devprayag) | Yamuna, Son (Right bank); Ramganga, Gomti, Ghaghara, Gandak, Kosi (Left bank) | Bay of Bengal | Tehri Dam (Bhagirathi), Farakka Barrage |
| **Brahmaputra** | Chemayungdung Glacier (Tibet - Tsangpo) | Subansiri, Kameng, Manas, Teesta (Right); Dibang, Lohit, Dhansiri (Left) | Bay of Bengal (Jamuna) | Majuli (World's largest river island) |

### 3.2 Peninsular River Systems
| River | Origin | Direction | Tributaries | Key Dam / Feature |
| :--- | :--- | :---: | :--- | :--- |
| **Godavari** | Trimbakeshwar (Nashik, Maharashtra) | East (Bay of Bengal) | Penganga, Wainganga, Indravati, Manjira | Longest Peninsular river ("Dakshin Ganga") |
| **Krishna** | Mahabaleshwar (Maharashtra) | East (Bay of Bengal) | Tungabhadra, Koyna, Bhima, Ghataprabha | Nagarjuna Sagar, Almatti Dam |
| **Kaveri** | Brahmagiri Hills (Kodagu, Karnataka) | East (Bay of Bengal) | Hemavati, Shimsha, Arkavathi, Bhavani | Shivanasamudra Falls, Mettur Dam, Krishnarajasagara |
| **Narmada** | Amarkantak Plateau (Madhya Pradesh) | **West (Arabian Sea)** | Tawa, Hiran, Orsang | Flows in a Rift Valley; Dhuandhar Falls; Sardar Sarovar Dam |
| **Tapi (Tapti)** | Multai (Betul, Madhya Pradesh) | **West (Arabian Sea)** | Purna, Girna, Panjhra | Flows in a Rift Valley; Ukai Dam, Kakrapar |

---

## 4. MAJOR NATIONAL PARKS & BIOSPHERE RESERVES
* **Jim Corbett (Uttarakhand):** India's first National Park (1936, formerly Hailey NP).
* **Kaziranga (Assam):** Famous for the Great One-Horned Rhinoceros (UNESCO World Heritage).
* **Gir National Park (Gujarat):** Exclusive home of the Asiatic Lion.
* **Keibul Lamjao (Manipur):** World's only **floating national park** (on Loktak Lake, home of Sangai deer).
* **Sundarbans (West Bengal):** World's largest mangrove forest; home of Royal Bengal Tiger.
"""

with open("data/revision/geography/geography-revision.md", "w", encoding="utf-8") as f:
    f.write(GEOGRAPHY_MD)
print("Wrote data/revision/geography/geography-revision.md")


# 3. english-revision.md
ENGLISH_MD = """# English Language & Verbal Ability Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO, CDS, CAPF, SSC CGL, Banking)**

---

## 1. SUBJECT-VERB AGREEMENT (10 GOLDEN RULES)

1. **Rule of Along with / As well as:** When two subjects are joined by *along with, together with, as well as, in addition to, accompanied by, with, like, unlike, rather than*, the verb agrees with the **FIRST subject**.
   * *Example:* The Chief Security Officer (Singular), along with all database administrators (Plural), **was** (Singular) present.
2. **Rule of Neither... Nor / Either... Or:** The verb agrees with the **NEAREST subject**.
   * *Example:* Neither the manager nor the engineers **are** responsible. / Neither the engineers nor the manager **is** responsible.
3. **Rule of Each, Every, Either, Neither, Many a:** Always take a **SINGULAR** verb.
   * *Example:* Each of the storage disks **was** inspected. / Many a student **has** failed.
4. **Rule of Collective Nouns:** Singular when acting as a unified whole; plural when members act individually.
   * *Example:* The committee **has** submitted its report. / The jury **were** divided in their opinions.
5. **Rule of Fractional / Percentage Quantifiers:** *Percent of, Some of, All of, Half of* take verb based on the noun that follows *of*.
   * *Example:* Half of the database **was** corrupted. / Half of the servers **were** rebooted.
6. **Rule of 'The number of' vs 'A number of':**
   * **The number of** + Plural noun $\\to$ **SINGULAR** verb (*The number of cyber incidents is increasing*).
   * **A number of** + Plural noun $\\to$ **PLURAL** verb (*A number of engineers are working*).
7. **Rule of Inversion with Negative Adverbs:** When sentences start with *Hardly, Scarcely, Seldom, Rarely, Never, No sooner*, the auxiliary verb precedes the subject.
   * *Example:* Hardly **had the server crashed** when the backup system activated.
8. **No Sooner... Than vs Hardly... When:**
   * *No sooner* pairs strictly with **than** (NOT when / then).
   * *Hardly / Scarcely* pairs strictly with **when** (NOT than).
9. **Conditional Sentences (Type 3 / Past Unfulfilled):**
   * *Structure:* If + had + V3, ... would have + V3.
   * *Example:* Had the team updated the SSL certificate, the downtime **would have been** avoided.
10. **Lest... Should:** *Lest* is followed strictly by **should** (never 'may' or 'will') and never takes a negative word (it already implies negation).
    * *Example:* Verify the credentials carefully lest unauthorized users **should** gain access.

---

## 2. ACTIVE & PASSIVE VOICE CONVERSION SUMMARY

| Tense | Active Voice Form | Passive Voice Form |
| :--- | :--- | :--- |
| **Simple Present** | writes | is / am / are + written |
| **Present Continuous**| is writing | is / am / are + being + written |
| **Present Perfect** | has written | has / have + been + written |
| **Simple Past** | wrote | was / were + written |
| **Past Continuous** | was writing | was / were + being + written |
| **Past Perfect** | had written | had + been + written |
| **Simple Future** | will write | will + be + written |
| **Future Perfect** | will have written | will have + been + written |

> Note: Present Perfect Continuous, Past Perfect Continuous, Future Continuous, and Future Perfect Continuous have no standard passive voice in modern English exams.

---

## 3. HIGH-FREQUENCY IDIOMS & PHRASES
1. **Skating on thin ice:** In a precarious or risky situation.
2. **Bear the brunt:** Endure the worst part or main burden of an unpleasant event.
3. **Bite the bullet:** Force yourself to do something difficult or unpleasant.
4. **Bring to book:** Hold someone officially accountable / punish for wrongdoing.
5. **Read between the lines:** Look for hidden or implied meanings.
6. **Throw in the towel:** Admit defeat or give up.
7. **Burn the midnight oil:** Work late into the night.
8. **A blessing in disguise:** Something that seems bad at first but results in good.
9. **At the eleventh hour:** At the last possible moment.
10. **Apple of discord:** Cause of dispute or contention.

---

## 4. COMMONLY CONFUSED WORDS
* **Affect (Verb):** To influence (*The outage affected payments*).
* **Effect (Noun):** Result or outcome (*The security policy had an immediate effect*).
* **Compliment:** Polite expression of praise (*He complimented her analysis*).
* **Complement:** Completes or enhances something (*The microservice complements the API*).
* **Principal:** Head of an institution, or initial capital sum.
* **Principle:** Fundamental truth, doctrine, or rule of conduct.
"""

with open("data/revision/english/english-revision.md", "w", encoding="utf-8") as f:
    f.write(ENGLISH_MD)
print("Wrote data/revision/english/english-revision.md")

