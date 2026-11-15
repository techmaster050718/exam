"""
IBPS SO IT Officer Prelims - Reasoning Ability Section (50 Questions)
"""

REASONING_QUESTIONS = [
    # Puzzle 1: Floor & Flat Puzzle (Q1 to Q5)
    {
        "q": (
            "Directions (Q1-Q5): Study the following information carefully and answer the questions that follow:\n\n"
            "Eight IT professionals — P, Q, R, S, T, U, V, and W — reside in a four-storey building where floors are numbered "
            "1 to 4 from bottom to top. Each floor has two flats: Flat A and Flat B. Flat A is to the west of Flat B. "
            "Flat A of floor 2 is immediately above Flat A of floor 1 and immediately below Flat A of floor 3, and so on. "
            "Each flat is occupied by exactly one professional.\n\n"
            "Conditions:\n"
            "1. P lives on an even-numbered floor in Flat A.\n"
            "2. There is one floor between P and W, and both live in the same flat type (Flat A).\n"
            "3. R lives immediately above W in Flat B.\n"
            "4. Q lives to the immediate east of S, but neither lives on the topmost floor.\n"
            "5. T lives on an odd-numbered floor immediately below U, but in different flat types.\n"
            "6. V does not live on floor 1, and V lives in Flat B.\n\n"
            "Question 1: Who lives on Floor 4, Flat A?"
        ),
        "options": [
            "P",
            "W",
            "U",
            "S"
        ],
        "answer": 0,
        "topic": "Floor and Flat Puzzle",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Floor & Flat arrangement (P, Q, R, S, T, U, V, W).\n\n"
            "Question 2: Who lives in Flat B on the same floor as S?"
        ),
        "options": [
            "Q",
            "R",
            "V",
            "T"
        ],
        "answer": 0,
        "topic": "Floor and Flat Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Floor & Flat arrangement (P, Q, R, S, T, U, V, W).\n\n"
            "Question 3: On which floor and in which flat does V live?"
        ),
        "options": [
            "Floor 4, Flat B",
            "Floor 3, Flat B",
            "Floor 2, Flat B",
            "Floor 1, Flat B"
        ],
        "answer": 0,
        "topic": "Floor and Flat Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Floor & Flat arrangement (P, Q, R, S, T, U, V, W).\n\n"
            "Question 4: Which of the following pairs of professionals live on Floor 1?"
        ),
        "options": [
            "T and Q",
            "T and R",
            "S and Q",
            "W and R"
        ],
        "answer": 0,
        "topic": "Floor and Flat Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Floor & Flat arrangement (P, Q, R, S, T, U, V, W).\n\n"
            "Question 5: Four of the following five are alike in a certain way based on their positions. "
            "Which one does NOT belong to that group?"
        ),
        "options": [
            "P",
            "W",
            "S",
            "R"
        ],
        "answer": 3,
        "topic": "Floor and Flat Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Seating 2: Circular Seating (In/Out Facing) (Q6 to Q10)
    {
        "q": (
            "Directions (Q6-Q10): Study the following information carefully:\n\n"
            "Eight network engineers — A, B, C, D, E, F, G, and H — are seated around a circular conference table. "
            "Four of them face towards the center and four face outwards (away from the center).\n\n"
            "Conditions:\n"
            "1. A sits third to the right of B, who faces the center.\n"
            "2. C sits second to the left of A.\n"
            "3. Immediate neighbors of C face in opposite directions (one faces in, one faces out).\n"
            "4. D sits third to the left of C and faces outward.\n"
            "5. E sits second to the right of D.\n"
            "6. F sits to the immediate left of G, who faces the center.\n"
            "7. H faces the same direction as D.\n"
            "8. Both immediate neighbors of A face the center.\n\n"
            "Question 6: Who sits to the immediate right of B?"
        ),
        "options": [
            "E",
            "D",
            "C",
            "H"
        ],
        "answer": 0,
        "topic": "Circular Seating Arrangement",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Circular Seating arrangement (A, B, C, D, E, F, G, H).\n\n"
            "Question 7: How many people sit between D and B when counted clockwise from D?"
        ),
        "options": [
            "One",
            "Two",
            "Three",
            "Four"
        ],
        "answer": 1,
        "topic": "Circular Seating Arrangement",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Circular Seating arrangement (A, B, C, D, E, F, G, H).\n\n"
            "Question 8: What is the position of F with respect to E?"
        ),
        "options": [
            "Third to the left",
            "Second to the right",
            "Immediate right",
            "Third to the right"
        ],
        "answer": 0,
        "topic": "Circular Seating Arrangement",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Circular Seating arrangement (A, B, C, D, E, F, G, H).\n\n"
            "Question 9: Which of the following four individuals all face OUTWARDS?"
        ),
        "options": [
            "D, H, C, A",
            "D, H, E, F",
            "B, G, A, C",
            "E, F, B, G"
        ],
        "answer": 0,
        "topic": "Circular Seating Arrangement",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Circular Seating arrangement (A, B, C, D, E, F, G, H).\n\n"
            "Question 10: Who sits exactly opposite to A?"
        ),
        "options": [
            "H",
            "D",
            "B",
            "E"
        ],
        "answer": 0,
        "topic": "Circular Seating Arrangement",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Puzzle 3: Box Stacking Puzzle (Q11 to Q15)
    {
        "q": (
            "Directions (Q11-Q15): Study the following information carefully:\n\n"
            "Seven backup storage drives — labelled K, L, M, N, O, P, and Q — are stacked one above another on a server rack. "
            "The bottommost shelf is position 1 and the topmost shelf is position 7.\n\n"
            "Conditions:\n"
            "1. Drive O is kept on an odd-numbered shelf but not on shelf 1.\n"
            "2. Exactly two drives are placed between drive O and drive L.\n"
            "3. Drive K is placed immediately below drive L.\n"
            "4. As many drives are placed above drive K as below drive P.\n"
            "5. Drive M is placed on a shelf immediately above drive Q.\n"
            "6. Drive N is placed on one of the shelves above drive O.\n\n"
            "Question 11: Which drive is placed on the topmost shelf (position 7)?"
        ),
        "options": [
            "N",
            "L",
            "M",
            "P"
        ],
        "answer": 0,
        "topic": "Box Stacking Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Box Stacking rack arrangement (K, L, M, N, O, P, Q).\n\n"
            "Question 12: How many drives are placed between drive M and drive P?"
        ),
        "options": [
            "None",
            "One",
            "Two",
            "Three"
        ],
        "answer": 2,
        "topic": "Box Stacking Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Box Stacking rack arrangement (K, L, M, N, O, P, Q).\n\n"
            "Question 13: What is the shelf position of drive K?"
        ),
        "options": [
            "Position 5",
            "Position 4",
            "Position 3",
            "Position 2"
        ],
        "answer": 0,
        "topic": "Box Stacking Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Box Stacking rack arrangement (K, L, M, N, O, P, Q).\n\n"
            "Question 14: Which drive is placed immediately above drive P?"
        ),
        "options": [
            "Q",
            "M",
            "O",
            "K"
        ],
        "answer": 0,
        "topic": "Box Stacking Puzzle",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Box Stacking rack arrangement (K, L, M, N, O, P, Q).\n\n"
            "Question 15: If all the drives are rearranged in alphabetical order from top (position 7) to bottom (position 1), "
            "how many drives will remain unchanged in their shelf position?"
        ),
        "options": [
            "None",
            "One",
            "Two",
            "Three"
        ],
        "answer": 1,
        "topic": "Box Stacking Puzzle",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Seating 4: Parallel Rows Seating (Q16 to Q20)
    {
        "q": (
            "Directions (Q16-Q20): Ten software architects sit in two parallel rows containing five people each.\n\n"
            "Row 1: A, B, C, D, and E are seated facing South.\n"
            "Row 2: P, Q, R, S, and T are seated facing North.\n"
            "Each person in Row 1 faces a person in Row 2.\n\n"
            "Conditions:\n"
            "1. P sits third to the right of Q.\n"
            "2. The person facing P sits second to the left of B.\n"
            "3. Only one person sits between B and E.\n"
            "4. R faces the immediate neighbor of D.\n"
            "5. D does not sit at an extreme end of the row.\n"
            "6. S sits to the immediate left of the person facing C.\n"
            "7. T faces A.\n\n"
            "Question 16: Who among the following faces D?"
        ),
        "options": [
            "Q",
            "P",
            "S",
            "R"
        ],
        "answer": 2,
        "topic": "Parallel Rows Seating",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Parallel Rows arrangement.\n\n"
            "Question 17: Who sits at the extreme left end of Row 1 (facing South)?"
        ),
        "options": [
            "B",
            "E",
            "C",
            "A"
        ],
        "answer": 0,
        "topic": "Parallel Rows Seating",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Parallel Rows arrangement.\n\n"
            "Question 18: How many people sit between T and Q in Row 2?"
        ),
        "options": [
            "None",
            "One",
            "Two",
            "Three"
        ],
        "answer": 1,
        "topic": "Parallel Rows Seating",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Parallel Rows arrangement.\n\n"
            "Question 19: Which of the following persons faces S?"
        ),
        "options": [
            "D",
            "B",
            "E",
            "C"
        ],
        "answer": 0,
        "topic": "Parallel Rows Seating",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Parallel Rows arrangement.\n\n"
            "Question 20: Four of the following five are alike in a certain way based on their positions. Which one does NOT belong?"
        ),
        "options": [
            "C",
            "B",
            "Q",
            "D"
        ],
        "answer": 3,
        "topic": "Parallel Rows Seating",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Machine Input-Output (Q21 to Q25)
    {
        "q": (
            "Directions (Q21-Q25): A word-and-number rearrangement machine, when given an input line of words and numbers, "
            "rearranges them step-by-step following a specific rule until complete.\n\n"
            "Input: secure 42 cloud 89 packet 17 token 64\n"
            "Step I: 89 secure 42 cloud packet 17 token 64\n"
            "Step II: 89 cloud secure 42 packet 17 token 64\n"
            "Step III: 89 cloud 64 secure 42 packet 17 token\n"
            "Step IV: 89 cloud 64 packet secure 42 17 token\n"
            "Step V: 89 cloud 64 packet 42 secure 17 token\n"
            "Step VI: 89 cloud 64 packet 42 token secure 17\n"
            "Step VII: 89 cloud 64 packet 42 token 17 secure\n"
            "Step VII is the final step of the arrangement.\n\n"
            "Now answer the questions for the given input:\n"
            "New Input: gateway 38 cyber 71 audit 94 route 53\n\n"
            "Question 21: Which element is third to the left of 'route' in Step IV of the given new input?"
        ),
        "options": [
            "audit",
            "71",
            "94",
            "gateway"
        ],
        "answer": 1,
        "topic": "Input Output",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Input-Output logic and the New Input:\n"
            "'gateway 38 cyber 71 audit 94 route 53'\n\n"
            "Question 22: How many steps are required to reach the final output for the new input?"
        ),
        "options": [
            "5 steps",
            "6 steps",
            "7 steps",
            "8 steps"
        ],
        "answer": 2,
        "topic": "Input Output",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Input-Output logic and the New Input:\n"
            "'gateway 38 cyber 71 audit 94 route 53'\n\n"
            "Question 23: What is the position of '38' from the right end in Step V?"
        ),
        "options": [
            "Second",
            "Third",
            "Fourth",
            "Fifth"
        ],
        "answer": 1,
        "topic": "Input Output",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Input-Output logic and the New Input:\n"
            "'gateway 38 cyber 71 audit 94 route 53'\n\n"
            "Question 24: Which element appears exactly between '71' and 'gateway' in the final step?"
        ),
        "options": [
            "cyber",
            "53",
            "audit",
            "route"
        ],
        "answer": 0,
        "topic": "Input Output",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the Input-Output logic and the New Input:\n"
            "'gateway 38 cyber 71 audit 94 route 53'\n\n"
            "Question 25: Which of the following represents Step II of the rearrangement?"
        ),
        "options": [
            "94 audit gateway 38 cyber 71 route 53",
            "94 71 audit gateway 38 cyber route 53",
            "94 audit 71 gateway 38 cyber route 53",
            "94 audit cyber gateway 38 71 route 53"
        ],
        "answer": 0,
        "topic": "Input Output",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Syllogisms (Q26 to Q30)
    {
        "q": (
            "Directions (Q26-Q30): In the question below are given three statements followed by two conclusions numbered I and II. "
            "You have to take the given statements to be true even if they seem to be at variance from commonly known facts.\n\n"
            "Statements:\n"
            "1. Only a few routers are switches.\n"
            "2. All switches are firewalls.\n"
            "3. No firewall is a hub.\n\n"
            "Conclusions:\n"
            "I. Some routers are definitely not hubs.\n"
            "II. All switches being hubs is a possibility."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Either conclusion I or II follows",
            "Neither conclusion I nor II follows"
        ],
        "answer": 0,
        "topic": "Syllogism",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements:\n"
            "1. Only a few microservices are monolithic.\n"
            "2. Some monolithic are distributed.\n"
            "3. All distributed are containerized.\n\n"
            "Conclusions:\n"
            "I. Some microservices can never be distributed.\n"
            "II. All microservices being monolithic is a possibility."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 3,
        "topic": "Syllogism",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements:\n"
            "1. All tokens are encrypted.\n"
            "2. Only a few encrypted are keys.\n"
            "3. No key is plaintext.\n\n"
            "Conclusions:\n"
            "I. Some encrypted are definitely not plaintext.\n"
            "II. All tokens can never be keys."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 0,
        "topic": "Syllogism",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements:\n"
            "1. No phishing is legitimate.\n"
            "2. A few legitimate are emails.\n"
            "3. Only a few emails are spam.\n\n"
            "Conclusions:\n"
            "I. Some emails are definitely not phishing.\n"
            "II. All spam can be legitimate."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 2,
        "topic": "Syllogism",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements:\n"
            "1. Only cloud is serverless.\n"
            "2. Some cloud is scalable.\n"
            "3. No scalable is legacy.\n\n"
            "Conclusions:\n"
            "I. Some serverless can be scalable.\n"
            "II. No serverless is legacy."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 1,
        "topic": "Syllogism",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Inequalities (Q31 to Q35)
    {
        "q": (
            "In the following question, assuming the given statements to be true, find which of the conclusion(s) is/are definitely true:\n\n"
            "Statements: M >= N > O = P; Q <= R < O; S >= R\n"
            "Conclusions:\n"
            "I. M > Q\n"
            "II. P > R"
        ),
        "options": [
            "Only conclusion I is true",
            "Only conclusion II is true",
            "Either conclusion I or II is true",
            "Both conclusions I and II are true"
        ],
        "answer": 3,
        "topic": "Inequality",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements: A < B <= C = D; E >= F > D; G <= E\n"
            "Conclusions:\n"
            "I. F > B\n"
            "II. A < E"
        ),
        "options": [
            "Only conclusion I is true",
            "Only conclusion II is true",
            "Both conclusions I and II are true",
            "Neither conclusion I nor II is true"
        ],
        "answer": 2,
        "topic": "Inequality",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements: W >= X = Y < Z; U <= V = X; T > W\n"
            "Conclusions:\n"
            "I. T > V\n"
            "II. Z > U"
        ),
        "options": [
            "Only conclusion I is true",
            "Only conclusion II is true",
            "Both conclusions I and II are true",
            "Neither conclusion I nor II is true"
        ],
        "answer": 2,
        "topic": "Inequality",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements: J <= K < L >= M; N > L <= O = P\n"
            "Conclusions:\n"
            "I. P >= J\n"
            "II. N > M"
        ),
        "options": [
            "Only conclusion I is true",
            "Only conclusion II is true",
            "Both conclusions I and II are true",
            "Neither conclusion I nor II is true"
        ],
        "answer": 1,
        "topic": "Inequality",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statements: H > I >= J = K; L <= M < J; N >= H\n"
            "Conclusions:\n"
            "I. N > M\n"
            "II. K > L"
        ),
        "options": [
            "Only conclusion I is true",
            "Only conclusion II is true",
            "Both conclusions I and II are true",
            "Neither conclusion I nor II is true"
        ],
        "answer": 2,
        "topic": "Inequality",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Blood Relations & Direction-Distance (Q36 to Q40)
    {
        "q": (
            "In a family of three generations having eight members (A, B, C, D, E, F, G, H):\n"
            "1. D is the father-in-law of B.\n"
            "2. B is the mother of F.\n"
            "3. C is the brother-in-law of B and has no siblings.\n"
            "4. A is the spouse of D.\n"
            "5. E is the paternal grandfather of G, who is the daughter of H.\n"
            "6. H is the brother of F.\n\n"
            "Question 36: How is C related to F?"
        ),
        "options": [
            "Paternal Uncle",
            "Maternal Uncle",
            "Brother",
            "Father"
        ],
        "answer": 0,
        "topic": "Blood Relations",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the family relationship details from Question 36.\n\n"
            "Question 37: How is G related to A?"
        ),
        "options": [
            "Great-granddaughter",
            "Granddaughter",
            "Daughter",
            "Niece"
        ],
        "answer": 0,
        "topic": "Blood Relations",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Study the following coded relationship symbols:\n"
            "'P @ Q' means P is the father of Q\n"
            "'P # Q' means P is the mother of Q\n"
            "'P $ Q' means P is the brother of Q\n"
            "'P % Q' means P is the sister of Q\n\n"
            "Which of the following expressions indicates that 'K is the maternal uncle of T'?"
        ),
        "options": [
            "K $ M # T",
            "K @ M % T",
            "K # M $ T",
            "K % M @ T"
        ],
        "answer": 0,
        "topic": "Blood Relations",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "A network technician starts from Data Center X and walks 12 meters North to point P. "
            "He turns right and walks 8 meters to point Q. He then turns 90 degrees clockwise and walks 18 meters to point R. "
            "From point R, he turns right and walks 16 meters to point S. "
            "Finally, he turns left and walks 6 meters to reach Data Center Y.\n\n"
            "Question 39: What is the shortest distance between Data Center X and Data Center Y?"
        ),
        "options": [
            "8√2 meters",
            "12 meters",
            "8√5 meters",
            "10 meters"
        ],
        "answer": 0,
        "topic": "Direction and Distance",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Refer to the technician's journey from Question 39 (X -> P -> Q -> R -> S -> Y).\n\n"
            "Question 40: In which direction is point P with respect to Data Center Y?"
        ),
        "options": [
            "North-East",
            "North-West",
            "South-East",
            "South-West"
        ],
        "answer": 0,
        "topic": "Direction and Distance",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Data Sufficiency (Q41 to Q45)
    {
        "q": (
            "Each of the questions below consists of a question and two statements numbered I and II given below it. "
            "You have to decide whether the data provided in the statements are sufficient to answer the question.\n\n"
            "Question: Among five systems A, B, C, D, and E having different CPU clock frequencies, which system is the fastest?\n"
            "Statement I: System C is faster than B and E, but slower than A.\n"
            "Statement II: System D is faster than C but slower than A."
        ),
        "options": [
            "The data in Statement I alone is sufficient",
            "The data in Statement II alone is sufficient",
            "The data in both Statements I and II together are sufficient",
            "The data in both Statements I and II together are not sufficient"
        ],
        "answer": 2,
        "topic": "Data Sufficiency",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Question: In which direction is terminal M located with respect to terminal R?\n"
            "Statement I: Terminal M is 10 m north of terminal P, which is 15 m west of terminal Q.\n"
            "Statement II: Terminal R is 10 m south of terminal Q."
        ),
        "options": [
            "The data in Statement I alone is sufficient",
            "The data in Statement II alone is sufficient",
            "The data in both Statements I and II together are sufficient",
            "The data in either Statement I alone or Statement II alone is sufficient"
        ],
        "answer": 2,
        "topic": "Data Sufficiency",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Question: What is the code for 'firewall' in a coded language?\n"
            "Statement I: 'secure firewall network gateway' is coded as 'kx lm np st' and 'cloud network gateway route' is coded as 'lm st fg qr'.\n"
            "Statement II: 'firewall defense token secure' is coded as 'np kx za uv' and 'firewall proxy server' is coded as 'np bc de'."
        ),
        "options": [
            "The data in Statement I alone is sufficient",
            "The data in Statement II alone is sufficient",
            "The data in both Statements I and II together are sufficient",
            "The data in either Statement I alone or Statement II alone is sufficient"
        ],
        "answer": 1,
        "topic": "Data Sufficiency",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Question: Six persons (U, V, W, X, Y, Z) are sitting around a circular table facing the center. Who sits opposite to W?\n"
            "Statement I: U sits second to the left of W. X sits to the immediate right of U.\n"
            "Statement II: Y sits opposite to U. Z is an immediate neighbor of both Y and W."
        ),
        "options": [
            "The data in Statement I alone is sufficient",
            "The data in Statement II alone is sufficient",
            "The data in both Statements I and II together are sufficient",
            "The data in either Statement I alone or Statement II alone is sufficient"
        ],
        "answer": 1,
        "topic": "Data Sufficiency",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Question: What is the total number of students in a computer certification class?\n"
            "Statement I: Rahul ranks 14th from the top and 27th from the bottom among students who passed the examination.\n"
            "Statement II: Eight students failed the examination and four students were absent on the exam day."
        ),
        "options": [
            "The data in Statement I alone is sufficient",
            "The data in Statement II alone is sufficient",
            "The data in both Statements I and II together are sufficient",
            "The data in both Statements I and II together are not sufficient"
        ],
        "answer": 2,
        "topic": "Data Sufficiency",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # Critical Reasoning (Q46 to Q50)
    {
        "q": (
            "Statement: In response to multiple ransomware incursions targeting regional rural banks, "
            "the banking ombudsman has mandated that all commercial and cooperative lenders migrate to air-gapped, "
            "immutable offline data backup repositories within sixty days.\n\n"
            "Assumptions:\n"
            "I. Immutable offline backups are technically less susceptible to network-borne ransomware encryption than continuous online cloud backups.\n"
            "II. Sixty days is a reasonable timeframe for banking institutions to procure and deploy air-gapped storage architecture."
        ),
        "options": [
            "Only assumption I is implicit",
            "Only assumption II is implicit",
            "Both assumptions I and II are implicit",
            "Neither assumption I nor II is implicit"
        ],
        "answer": 2,
        "topic": "Statement and Assumption",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statement: Despite heavy capital investment in AI-powered underwriting software, several non-banking finance "
            "companies (NBFCs) experienced a 24% surge in personal loan default rates over the past three fiscal quarters.\n\n"
            "Courses of Action:\n"
            "I. The NBFCs should immediately audit their credit assessment training datasets to check for biased or outdated historical assumptions.\n"
            "II. The NBFCs should completely terminate all digital lending operations and revert exclusively to physical branch underwriting."
        ),
        "options": [
            "Only course of action I follows",
            "Only course of action II follows",
            "Either course of action I or II follows",
            "Both courses of action I and II follow"
        ],
        "answer": 0,
        "topic": "Course of Action",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Read the two statements below and choose the correct relationship between them:\n\n"
            "Statement A: The central banking authority imposed severe business restrictions and penalties on a major payment aggregator.\n"
            "Statement B: The internal security audit of the payment aggregator revealed systemic non-compliance with customer KYC verification and data localization norms."
        ),
        "options": [
            "Statement A is the cause and Statement B is its effect",
            "Statement B is the cause and Statement A is its effect",
            "Both statements A and B are independent causes",
            "Both statements A and B are effects of independent causes"
        ],
        "answer": 1,
        "topic": "Cause and Effect",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statement: Should commercial banks mandate biometric facial recognition alongside debit card PINs for all ATM cash withdrawals?\n\n"
            "Arguments:\n"
            "I. Yes; it will virtually eliminate ATM card skimming and unauthorized PIN shoulder-surfing frauds.\n"
            "II. No; rural and elderly account holders might face transaction failures due to camera sensor glitches or age-related biometric discrepancies."
        ),
        "options": [
            "Only argument I is strong",
            "Only argument II is strong",
            "Both arguments I and II are strong",
            "Neither argument I nor II is strong"
        ],
        "answer": 2,
        "topic": "Strong and Weak Arguments",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Statement: The adoption of quantum computing threatens to render standard RSA and ECC public-key cryptographic "
            "algorithms computationally obsolete within the next decade.\n\n"
            "Conclusions:\n"
            "I. Financial regulators worldwide must initiate transition roadmaps towards post-quantum cryptography (PQC) standards.\n"
            "II. All digital banking transactions will completely cease to operate once the first commercial quantum processor is unveiled."
        ),
        "options": [
            "Only conclusion I follows",
            "Only conclusion II follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 0,
        "topic": "Statement and Conclusion",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    }
]

