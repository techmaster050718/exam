"""
Generates:
1. data/revision/defence/defence-revision.md
2. data/revision/general-awareness/general-awareness-revision.md
3. data/revision/exam-specific/exam-specific-revision.md
"""
import os

os.makedirs("data/revision/defence", exist_ok=True)
os.makedirs("data/revision/general-awareness", exist_ok=True)
os.makedirs("data/revision/exam-specific", exist_ok=True)

# 1. defence-revision.md
DEFENCE_MD = """# Defence, Armed Forces & Security Revision Notes
> **Exam-Ready Reference | Competitive Exams (CDS, CAPF AC, SSB OIR, AFCAT, NDA)**

---

## 1. ARMED FORCES EQUIVALENT RANKS

| Hierarchy Level | Indian Army | Indian Navy | Indian Air Force |
| :---: | :--- | :--- | :--- |
| **10 (Honorary)** | Field Marshal | Admiral of the Fleet | Marshal of the Air Force |
| **9** | General (COAS) | Admiral (CNS) | Air Chief Marshal (CAS) |
| **8** | Lieutenant General | Vice Admiral | Air Marshal |
| **7** | Major General | Rear Admiral | Air Vice Marshal |
| **6** | Brigadier | Commodore | Air Commodore |
| **5** | Colonel | Captain | Group Captain |
| **4** | Lieutenant Colonel | Commander | Wing Commander |
| **3** | Major | Lieutenant Commander | Squadron Leader |
| **2** | Captain | Lieutenant | Flight Lieutenant |
| **1** | Lieutenant | Sub-Lieutenant | Flying Officer |

---

## 2. COMMAND HEADQUARTERS

### Indian Army Commands (7 Commands)
* **Northern Command:** Udhampur (J&K)
* **Western Command:** Chandimandir (Haryana)
* **Eastern Command:** Kolkata (West Bengal)
* **Southern Command:** Pune (Maharashtra)
* **Central Command:** Lucknow (Uttar Pradesh)
* **South Western Command:** Jaipur (Rajasthan)
* **Army Training Command (ARTRAC):** Shimla (Himachal Pradesh)

### Indian Navy Commands (3 Commands)
* **Western Naval Command:** Mumbai (Maharashtra)
* **Eastern Naval Command:** Visakhapatnam (Andhra Pradesh)
* **Southern Naval Command (Training):** Kochi (Kerala)

### Indian Air Force Commands (7 Commands)
* **Western Air Command:** New Delhi
* **Eastern Air Command:** Shillong (Meghalaya)
* **Central Air Command:** Prayagraj (Allahabad, UP)
* **South Western Air Command:** Gandhinagar (Gujarat)
* **Southern Air Command:** Thiruvananthapuram (Kerala)
* **Training Command:** Bengaluru (Karnataka)
* **Maintenance Command:** Nagpur (Maharashtra)

> **Tri-Services Commands:**
> 1. Andaman and Nicobar Command (ANC) – Port Blair (India's only operational theatre command)
> 2. Strategic Forces Command (SFC) – Responsible for nuclear asset command and management

---

## 3. INDIAN MISSILE SYSTEMS (DRDO IGMDP PROGRAM)
Initiated in 1983 under Dr. A.P.J. Abdul Kalam (**PATNA**):
1. **P - Prithvi:** Surface-to-Surface, Short-Range Ballistic Missile (SRBM, 150–350 km).
2. **A - Agni:** Surface-to-Surface, Medium-to-Intercontinental Ballistic Missile (ICBM).
   * Agni-I: 700–900 km
   * Agni-II: 2,000–3,000 km
   * Agni-III: 3,000–5,000 km
   * Agni-IV: 3,500–4,000 km
   * Agni-V: 5,000–8,000 km (Intercontinental Ballistic Missile, solid-fueled, road-mobile canisterized)
   * Agni-P (Prime): Next-gen canisterized SRBM
3. **T - Trishul:** Short-range Surface-to-Air Missile (SAM, 9 km).
4. **N - Nag:** 3rd Generation Fire-and-Forget Anti-Tank Guided Missile (ATGM, 4–7 km). Air-launched variant: **Helina (Dhruvastra)**.
5. **A - Akash:** Medium-range Surface-to-Air Missile (SAM, 25–30 km), multi-target handling.

* **BrahMos:** Supersonic Cruise Missile (Mach 2.8–3.0), joint venture between India (DRDO) and Russia (NPO Mashinostroyenia). Named after Brahmaputra and Moskva rivers.

---

## 4. CENTRAL ARMED POLICE FORCES (CAPF) UNDER MHA

| Force | Full Form | Established | Primary Mandate / Border Guarded | Motto |
| :--- | :--- | :---: | :--- | :--- |
| **BSF** | Border Security Force | 1965 | Guards Pakistan and Bangladesh borders | "Duty Unto Death" |
| **CRPF** | Central Reserve Police Force | 1939 | Internal security, counter-insurgency, anti-Naxal (CoBRA)| "Service and Loyalty" |
| **ITBP** | Indo-Tibetan Border Police | 1962 | Guards India-China (Tibet) border (High altitude)| "Valour, Determination, Devotion to Duty"|
| **SSB** | Sashastra Seema Bal | 1963 | Guards Nepal and Bhutan borders | "Service, Security and Brotherhood" |
| **CISF** | Central Industrial Security Force | 1969 | Protects PSUs, airports, nuclear plants, metro rails| "Protection and Security" |
| **Assam Rifles**| Assam Rifles (Oldest paramilitary) | 1835 | Guards Myanmar border & North-East counter-insurgency| "Sentinels of the North-East" |
| **NSG** | National Security Guard | 1984 | Elite counter-terrorism (Black Cats) | "Omnipresent Omnipotent Security" |
"""

with open("data/revision/defence/defence-revision.md", "w", encoding="utf-8") as f:
    f.write(DEFENCE_MD)
print("Wrote data/revision/defence/defence-revision.md")


# 2. general-awareness-revision.md
GA_MD = """# General Awareness & Static GK Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS, CDS, CAPF, UP Police SI, SSC, RRB)**

---

## 1. MAJOR INTERNATIONAL ORGANIZATIONS & HEADQUARTERS

| Organization | Abbreviation | Headquarters | Year Founded | Primary Role / Mission |
| :--- | :---: | :--- | :---: | :--- |
| **United Nations** | UN | New York City, USA | 1945 | International peace and collective security |
| **World Health Organization** | WHO | Geneva, Switzerland | 1948 | Global public health coordination |
| **International Monetary Fund**| IMF | Washington, D.C., USA | 1944 | Global monetary stability & financial bailouts |
| **World Bank Group** | WB | Washington, D.C., USA | 1944 | Developmental financing and poverty reduction |
| **World Trade Organization** | WTO | Geneva, Switzerland | 1995 | International trade rules & dispute settlement |
| **International Court of Justice**| ICJ | The Hague, Netherlands | 1945 | Principal judicial organ of the UN |
| **UNESCO** | UNESCO | Paris, France | 1945 | Education, science, culture, heritage sites |
| **International Atomic Energy Agency**| IAEA | Vienna, Austria | 1957 | Peaceful use of nuclear energy |
| **INTERPOL** | INTERPOL | Lyon, France | 1923 | Cross-border police cooperation |
| **BRICS** | BRICS | Shanghai, China (NDB) | 2009 | Emerging national economies alliance |
| **ASEAN** | ASEAN | Jakarta, Indonesia | 1967 | Southeast Asian regional economic cooperation |
| **SAARC** | SAARC | Kathmandu, Nepal | 1985 | South Asian regional cooperation |
| **Asian Development Bank** | ADB | Manila, Philippines | 1966 | Asian regional economic development |
| **AIIB** | AIIB | Beijing, China | 2016 | Asian infrastructure investment |
| **Bank for International Settlements**| BIS | Basel, Switzerland | 1930 | Central bank coordination & Basel Norms |

---

## 2. AWARDS & HONOURS SUMMARY TABLE

| Award | Category / Field | Instituted | Key Details / First Recipient |
| :--- | :--- | :---: | :--- |
| **Bharat Ratna** | Highest Civilian Award in India | 1954 | First recipients: C. Rajagopalachari, S. Radhakrishnan, C.V. Raman |
| **Param Vir Chakra** | Highest Military Wartime Gallantry Award | 1950 | First recipient: Major Somnath Sharma (1947 Indo-Pak War) |
| **Ashoka Chakra** | Highest Peacetime Gallantry Award | 1952 | First recipient: Narbahadur Thapa (1952) |
| **Jnanpith Award** | Highest Literary Award in India | 1961 | First recipient: G. Sankara Kurup (Malayalam, 1965) |
| **Dadasaheb Phalke**| Highest Cinema Award in India | 1969 | First recipient: Devika Rani (1969) |
| **Major Dhyan Chand Khel Ratna**| Highest Sports Honor in India | 1991 | First recipient: Viswanathan Anand (Chess, 1991–92) |
| **Nobel Prize** | Physics, Chem, Med, Lit, Peace, Econ | 1901 | First Indian recipient: Rabindranath Tagore (Literature, 1913) |

---

## 3. IMPORTANT NATIONAL & INTERNATIONAL DAYS

* **January:** Jan 9: Pravasi Bharatiya Divas; Jan 12: National Youth Day (Swami Vivekananda); Jan 15: Army Day; Jan 24: National Girl Child Day; Jan 25: National Voters' Day.
* **February:** Feb 2: World Wetlands Day; Feb 4: World Cancer Day; Feb 28: National Science Day (Raman Effect discovery).
* **March:** Mar 8: International Women's Day; Mar 15: World Consumer Rights Day; Mar 21: World Forestry Day; Mar 22: World Water Day; Mar 23: Shaheed Diwas (Bhagat Singh, Sukhdev, Rajguru).
* **April:** Apr 7: World Health Day; Apr 14: Ambedkar Jayanti; Apr 21: Civil Services Day; Apr 22: World Earth Day; Apr 24: National Panchayati Raj Day.
* **May:** May 1: International Labour Day; May 3: World Press Freedom Day; May 11: National Technology Day (Pokhran-II); May 21: Anti-Terrorism Day; May 31: World No Tobacco Day.
* **June:** Jun 5: World Environment Day; Jun 21: International Day of Yoga.
* **July:** Jul 1: National Doctor's Day / GST Day; Jul 11: World Population Day; Jul 26: Kargil Vijay Diwas; Jul 29: International Tiger Day.
* **August:** Aug 12: International Youth Day; Aug 15: Independence Day; Aug 29: National Sports Day (Major Dhyan Chand).
* **September:** Sep 5: Teachers' Day; Sep 8: International Literacy Day; Sep 14: Hindi Diwas; Sep 15: Engineers' Day; Sep 16: World Ozone Day.
* **October:** Oct 2: Gandhi Jayanti (International Day of Non-Violence); Oct 8: Air Force Day; Oct 24: United Nations Day; Oct 31: National Unity Day (Rashtriya Ekta Diwas, Sardar Patel).
* **November:** Nov 11: National Education Day (Maulana Azad); Nov 26: Constitution Day (Samvidhan Diwas).
* **December:** Dec 1: World AIDS Day; Dec 4: Navy Day; Dec 7: Armed Forces Flag Day; Dec 10: Human Rights Day; Dec 23: Kisan Diwas (Chaudhary Charan Singh); Dec 25: Good Governance Day (Atal Bihari Vajpayee).
"""

with open("data/revision/general-awareness/general-awareness-revision.md", "w", encoding="utf-8") as f:
    f.write(GA_MD)
print("Wrote data/revision/general-awareness/general-awareness-revision.md")


# 3. exam-specific-revision.md
EXAM_SPECIFIC_MD = """# Exam-Specific Target Revision Modules
> **Tailored High-Yield Reference Mapped to All Uploaded Question Bank Papers**

---

## 1. IBPS SO IT OFFICER (SCALE-I) — PRELIMS & MAINS

### Exam Pattern & Strategy
* **Prelims:** 150 Qs | 125 Marks | 120 Mins (English: 50Q/25M, Reasoning: 50Q/50M, Quant: 50Q/50M).
* **Mains:** 60 Qs | 60 Marks | 45 Mins (Professional Knowledge). Negative marking: 0.25 marks.

### Repeated High-Frequency Mains Topics
1. **Database & SQL:** Normalization up to BCNF, ACID properties, Cascadeless schedules, B+ Tree search order, Window ranking functions (`DENSE_RANK()`).
2. **Computer Networks:** TCP 3-way handshake & 2MSL TIME_WAIT, Subnetting CIDR masks (/27, /28), Selective Repeat window size ($2^{n-1}$), BGP Path Vector.
3. **Operating Systems:** Banker's algorithm safe sequence, Belady's anomaly in FIFO, Inode metadata structure in ext4, Counting semaphores arithmetic.
4. **Data Structures:** Master theorem cases, AVL tree RL/LR rotations, Comparison sort $\\Omega(n \\log n)$ lower bound, Linear probing primary clustering.
5. **Software Engineering:** Cyclomatic complexity $V(G) = E - N + 2P$, COCOMO organic/embedded modes, Agile Scrum ceremonies.
6. **Cybersecurity & Banking Tech:** AES 128/192/256 rounds, Digital signature hashing with private key, Zero Trust tenets, NPCI payment rails (UPI/IMPS/NEFT/RTGS), PCI-DSS prohibition on CVV storage post-authorization, RBI 2–6 hr cyber incident reporting.

---

## 2. UP POLICE SI (17 PAPERS IN BANK)

### Core Sections Tested in Question Bank
1. **General Hindi (सामान्य हिंदी):**
   * *वर्णमाला:* स्वर (11), व्यंजन (33), अयोगवाह (अं, अः), संयुक्त व्यंजन (क्ष, त्र, ज्ञ, श्र).
   * *संधि:* स्वर संधि (दीर्घ, गुण, वृद्धि, यण, अयादि), व्यंजन संधि, विसर्ग संधि.
   * *समास:* अव्ययीभाव (पहला पद प्रधान), तत्पुरुष (कारक विभक्ति), कर्मधारय (विशेषण-विशेष्य), द्विगु (संख्यावाची), द्वंद्व (दोनों पद प्रधान), बहुव्रीहि (तीसरा अर्थ).
   * *रस, छंद, अलंकार:* रस (9 स्थायी भाव; भरत मुनि के अनुसार 8), अलंकार (शब्दालंकार: अनुप्रास, यमक, श्लेष; अर्थालंकार: उपमा, रूपक, उत्प्रेक्षा).
2. **मूलविधि / संविधान / सामान्य ज्ञान (Law, Constitution & GK):**
   * *भारतीय दंड संहिता (IPC 1860):* कुल 511 धाराएं, 23 अध्याय। धारा 300 (हत्या), धारा 302 (हत्या का दंड), धारा 375/376 (बलात्कार), धारा 378/379 (चोरी), धारा 420 (धोखाधड़ी), धारा 498A (दहेज प्रताड़ना).
   * *दंड प्रक्रिया संहिता (CrPC 1973):* संज्ञेय (Cognizable - बिना वारंट गिरफ्तारी) बनाम असंज्ञेय (Non-cognizable). धारा 144 (निषेधाज्ञा), धारा 154 (FIR).
   * *संविधान:* भाग 3 (मौलिक अधिकार), भाग 4 (नीति निदेशक तत्व), राष्ट्रपति, राज्यपाल, संसद, उच्च न्यायालय।
   * *विशेष अधिनियम:* मोटर वाहन अधिनियम, सूचना प्रौद्योगिकी अधिनियम (IT Act 2000), पर्यावरण संरक्षण अधिनियम 1986, भ्रष्टाचार निवारण अधिनियम 1988, मानवाधिकार संरक्षण अधिनियम 1993, RTI Act 2005.

---

## 3. RRB ASSISTANT LOCO PILOT (ALP) — CBT-1 & CBT-2 (14 PAPERS IN BANK)

### CBT-1 High-Frequency Concepts
* **Mathematics (20 Qs):** BODMAS, Fractions, LCM/HCF, Ratio, Percentages, Mensuration, Time & Work, Speed-Time-Distance, SI & CI, Profit & Loss, Algebra, Geometry & Trigonometry.
* **General Intelligence & Reasoning (25 Qs):** Analogies, Alphabetical & Number Series, Coding-Decoding, Venn Diagrams, Syllogisms, Direction, Blood Relations.
* **General Science (20 Qs):** 10th standard Physics, Chemistry and Biology (focus on Newton's Laws, Electricity $V=IR$, Chemical Equations, Human Systems).

### CBT-2 Part A: Basic Science & Engineering (40 Qs)
1. **Units & Measurements:** Conversions, vernier calliper and micrometer screw gauge least counts.
2. **Mass, Weight & Density:** Specific gravity, Archimedes principle.
3. **Work, Power & Energy:** Mechanical efficiency, kinetic and potential energy conversions.
4. **Speed & Velocity:** Uniform acceleration equations.
5. **Heat & Temperature:** Latent heat, specific heat capacity ($Q = mc\\Delta T$), clinical vs laboratory thermometers.
6. **Basic Electricity:** Ohm's law, series/parallel combinations, electrical power and energy bills calculation.
7. **Levers & Simple Machines:** Mechanical Advantage ($MA = Load / Effort$), Velocity Ratio ($VR$), Efficiency ($\\eta = MA / VR \\times 100\\%$). Class I (Fulcrum in middle), Class II (Load in middle - wheelbarrow), Class III (Effort in middle - tweezers, human arm).
8. **Occupational Safety & Health:** Fire extinguishers (Class A: wood/paper, Class B: flammable liquids, Class C: flammable gases, Class D: metals, Electrical fires: $\\text{CO}_2$ or CTC).

---

## 4. SCIENTIFIC & TECHNICAL CSE EXAMS (ISRO, DRDO, NIC, BARC, POWERGRID)

### Repeated High-Weightage CSE Technical Topics
1. **Computer Organization & Architecture:**
   * Cache mapping formulas: Tag, Set, Offset bits calculation.
   * Pipeline speedup formula: $S = \\frac{n \\cdot k}{k + n - 1}$ for $n$ instructions on $k$ stages.
   * Flynn's taxonomy classification.
2. **Theory of Computation (TOC) & Compiler Design:**
   * Chomsky Hierarchy: Regular (Type 3, Finite Automata) $\\subset$ Context-Free (Type 2, Pushdown Automata) $\\subset$ Context-Sensitive (Type 1, Linear Bounded Automata) $\\subset$ Recursively Enumerable (Type 0, Turing Machine).
   * Pumping Lemma for Regular and Context-Free languages.
   * Decidability table (Halting problem is undecidable; emptiness of DFA is decidable).
3. **Database Systems:**
   * Conflict serializability testing using precedence graph (cycle $\\implies$ not conflict serializable).
   * View serializability (NP-complete).
   * Lossless join condition: $(R_1 \\cap R_2) \\to R_1$ or $(R_1 \\cap R_2) \\to R_2$.
4. **Computer Networks:**
   * TCP Reno vs Tahoe congestion avoidance.
   * Maximum Segment Lifetime (MSL) and TIME_WAIT state duration.
   * Distance vector routing count-to-infinity problem and split horizon fix.

---

## 5. CDS & CAPF EXAM STRATEGY

* **General Knowledge Focus:** Deep physical geography (Geomorphology, Atmospheric circulation, Indian rivers), Constitutional articles & case laws, Modern Indian History (1857 to 1947 timeline), Defence commands, missile ranges, and international summits.
* **English Focus:** Advanced error spotting, sentence improvement, active/passive voice conversions, direct/indirect reported speech, and cloze tests.
"""

with open("data/revision/exam-specific/exam-specific-revision.md", "w", encoding="utf-8") as f:
    f.write(EXAM_SPECIFIC_MD)
print("Wrote data/revision/exam-specific/exam-specific-revision.md")

