import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

CATEGORIES = {
    "Memory & Recall": [
        ("A short sequence is 7, 2, 9, 4, 1. Which number appeared immediately before 4?",
         ["9", "2", "7", "1"], 0,
         "In the displayed sequence, 9 is immediately before 4."),
        ("Remember the words: river, candle, garden, silver. Which was the third word?",
         ["Candle", "Silver", "Garden", "River"], 2,
         "The third item in the sequence is garden."),
        ("A code is 5-8-3-6. Which digit is at the second position from the left?",
         ["6", "8", "3", "5"], 1,
         "Reading left to right, the second digit is 8."),
        ("A list contains red, blue, green, yellow. Which colour came directly after blue?",
         ["Yellow", "Red", "Blue", "Green"], 3,
         "Green directly follows blue."),
        ("A person hears the room number 4-1-7 and then the floor number 2. What was the room number?",
         ["4-1-7", "4-2-7", "1-7-2", "2-4-1"], 0,
         "The room number given before the floor number was 4-1-7."),
    ],
    "Attention & Concentration": [
        ("Which option exactly matches the target string 40918?",
         ["40981", "49018", "40918", "40917"], 2,
         "Only 40918 preserves every digit in the same position as the target."),
        ("Which word contains the letter 'p' exactly twice?",
         ["paperclip", "pepper", "pupil", "planet"], 2,
         "Pupil contains two p letters; paperclip and pepper contain three, while planet contains one."),
        ("Which pair is identical?",
         ["M7Q2 / M7O2", "B4D9 / B4D9", "K3P8 / K8P3", "T6R1 / T6R7"], 1,
         "Both strings in the second pair are exactly B4D9."),
        ("In the word CONCENTRATION, which letter appears most often?",
         ["C", "N", "O", "T"], 1,
         "N appears three times; each of the other listed letters appears fewer times."),
        ("Which number is not in increasing order?",
         ["2, 5, 8, 11", "1, 4, 7, 10", "3, 6, 9, 12", "4, 7, 6, 10"], 3,
         "In the last sequence, 6 follows 7, so the sequence does not increase throughout."),
    ],
    "Pattern Recognition": [
        ("What comes next: 2, 6, 12, 20, 30, __?",
         ["40", "42", "38", "44"], 1,
         "The terms are n × (n+1): 1×2, 2×3, …, 6×7 = 42."),
        ("What letter comes next: A, C, F, J, O, __?",
         ["T", "U", "V", "S"], 1,
         "The alphabet-position increments are +2, +3, +4, +5; the next is +6, giving U."),
        ("Find the missing number: 5, 10, 20, 40, __.",
         ["60", "75", "80", "100"], 2,
         "Each term doubles, so 40 × 2 = 80."),
        ("Which shape completes the sequence: circle, square, circle, square, __?",
         ["Triangle", "Circle", "Square", "Rectangle"], 1,
         "The two shapes alternate, so the next is a circle."),
        ("What comes next: 1, 4, 9, 16, __?",
         ["20", "24", "25", "36"], 2,
         "These are consecutive squares: 1², 2², 3², 4², then 5² = 25."),
    ],
    "Observation": [
        ("Which option exactly matches the target: R8K-31Q?",
         ["R8K-31O", "R8K-13Q", "R8K-31Q", "R8X-31Q"], 2,
         "Only the third option preserves every character and its position."),
        ("A meeting begins at 14:25 and ends at 15:10. How long does it last?",
         ["35 minutes", "40 minutes", "45 minutes", "55 minutes"], 2,
         "From 14:25 to 15:00 is 35 minutes, then 10 more minutes: 45."),
        ("A shelf has a blue book between a red book and a green book. The red book is left of blue. What is the order from left to right?",
         ["Green, blue, red", "Red, blue, green", "Blue, red, green", "Red, green, blue"], 1,
         "The stated relationships give red, then blue, then green."),
        ("A receipt lists 2 notebooks at $3 each and 1 pen at $2. What is the total?",
         ["$5", "$6", "$8", "$9"], 2,
         "Two notebooks cost $6 and the pen costs $2, for a total of $8."),
        ("Which item is missing from this set of labels: A1, A2, A3, A5?",
         ["A0", "A4", "A6", "B4"], 1,
         "A4 is the only missing label in the consecutive A-number sequence."),
    ],
    "Logical Reasoning": [
        ("All sparrows are birds. All birds are animals. Which conclusion must follow?",
         ["All animals are sparrows", "All sparrows are animals", "No birds are animals", "Some animals are not birds"], 1,
         "Membership in sparrows implies membership in birds and therefore animals."),
        ("Mira is taller than Dev. Dev is taller than Lee. Who is the shortest?",
         ["Mira", "Dev", "Lee", "Cannot be determined"], 2,
         "The height order is Mira > Dev > Lee."),
        ("Glove is to hand as sock is to:",
         ["Head", "Foot", "Arm", "Shoulder"], 1,
         "A glove is worn on a hand; a sock is worn on a foot."),
        ("A bus leaves every 20 minutes. One leaves at 10:00. When is the next one?",
         ["10:10", "10:15", "10:20", "10:30"], 2,
         "Twenty minutes after 10:00 is 10:20."),
        ("Some artists are teachers. All teachers are readers. Which conclusion is valid?",
         ["Some artists are readers", "All artists are teachers", "No readers are artists", "All readers are artists"], 0,
         "The artists who are teachers must also be readers."),
    ],
    "Working Memory": [
        ("Reverse the digits 3-8-1. Which sequence results?",
         ["1-8-3", "8-1-3", "3-1-8", "1-3-8"], 0,
         "Reversing the order gives 1-8-3."),
        ("Start with 4, add 3, then double the result. What do you get?",
         ["11", "14", "10", "12"], 1,
         "4 + 3 = 7, and 7 × 2 = 14."),
        ("Remember the positions: red=1, blue=2, yellow=3. What colour is at position 2?",
         ["Red", "Yellow", "Blue", "Green"], 2,
         "Blue was assigned position 2."),
        ("Reorder these letters alphabetically: D, A, C, B.",
         ["A, B, C, D", "D, C, B, A", "B, A, D, C", "A, C, B, D"], 0,
         "Alphabetical order is A, B, C, D."),
        ("Take 9, subtract 2, then add 5. What is the result?",
         ["10", "11", "12", "13"], 2,
         "9 − 2 = 7; 7 + 5 = 12."),
    ],
    "Cognitive Flexibility": [
        ("Use this rule: if a number is even, add 1; if odd, subtract 1. What is the result for 8?",
         ["7", "8", "9", "10"], 2,
         "Eight is even, so add 1 to get 9."),
        ("A sorting rule changes from 'alphabetical order' to 'shortest word first'. Which word should be first: pear, fig, banana?",
         ["Pear", "Fig", "Banana", "Cannot be determined"], 1,
         "Under the new rule, the three-letter word fig comes first."),
        ("If LEFT now means move right and RIGHT means move left, what does the instruction 'LEFT, then RIGHT' become?",
         ["Left, then left", "Right, then right", "Right, then left", "Left, then right"], 2,
         "Apply the reversed mapping to each word: LEFT becomes right, RIGHT becomes left."),
        ("A pattern rule was 'add 2'. It changes to 'multiply by 2'. Starting from 3, what is the next term under the new rule?",
         ["5", "6", "8", "9"], 1,
         "Apply the new rule to 3: 3 × 2 = 6."),
        ("You usually solve a problem by drawing a table, but the table gives no progress. What is the most flexible next step?",
         ["Repeat the same table without checking it", "Change representation, such as testing a small example", "Stop considering the problem", "Assume the problem has no solution"], 1,
         "Changing representation or testing a small case can reveal a route when the current method stalls."),
    ],
    "Decision-Making": [
        ("Your phone battery is low and you need directions to a new campus building. What is the most practical choice?",
         ["Keep watching videos until it shuts down", "Check the route, save key directions, and conserve battery", "Ignore the destination", "Delete the map app"], 1,
         "Secure the needed information first, then conserve the remaining battery."),
        ("A teammate misses a deadline and the group presentation is tomorrow. What is a useful first response?",
         ["Clarify what is incomplete and redistribute remaining tasks", "Publicly blame the teammate", "Cancel without checking options", "Do nothing and hope it is finished"], 0,
         "Clarifying the gap and coordinating a realistic recovery plan addresses the immediate need."),
        ("You are considering buying a fitness device with money set aside for transport. What should you do first?",
         ["Buy it because it is on sale", "Check essential costs and whether the purchase fits the budget", "Borrow without planning repayment", "Assume the transport cost will disappear"], 1,
         "Compare the purchase with essential expenses and the available budget before deciding."),
        ("A friend sends an alarming but unverified health claim. What is the soundest response?",
         ["Forward it immediately", "Check a reliable health source before acting or sharing", "Treat the number of forwards as proof", "Stop all medical care"], 1,
         "Verification from a reliable source reduces the risk of spreading misinformation."),
        ("You feel unusually dizzy during exercise. What is the safest immediate decision?",
         ["Increase intensity to finish sooner", "Stop, move to a safe place, and seek appropriate help if symptoms persist or are severe", "Ignore it every time", "Compete with a friend"], 1,
         "Stop the activity and prioritize safety; persistent or severe symptoms warrant appropriate help."),
    ],
    "Cognitive Biases": [
        ("A person searches only for evidence supporting a belief and dismisses contrary evidence. This is:",
         ["Confirmation bias", "Anchoring", "Hindsight bias", "Availability heuristic"], 0,
         "Confirmation bias is the tendency to favour information that supports an existing belief."),
        ("After seeing an expensive first price, a buyer judges a lower price as cheap even without checking value. This illustrates:",
         ["Availability heuristic", "Anchoring", "Sunk-cost fallacy", "Survivorship bias"], 1,
         "The initial price acts as an anchor for later judgments."),
        ("Someone estimates danger mainly from a dramatic event they recently saw in the news. This is most like:",
         ["Hindsight bias", "Availability heuristic", "Confirmation bias", "Sunk-cost fallacy"], 1,
         "The ease of recalling a vivid event influences the estimate of how common or likely it is."),
        ("A person keeps funding a failing project only because they have already spent a lot on it. This is:",
         ["Sunk-cost fallacy", "Anchoring", "Framing effect", "Representativeness"], 0,
         "Past unrecoverable costs should not determine whether to continue investing."),
        ("A report studies only successful companies and concludes that their habits guarantee success, ignoring failed companies. This overlooks:",
         ["Survivorship bias", "Hindsight bias", "Primacy effect", "Loss aversion"], 0,
         "Survivorship bias ignores cases that did not survive and can distort conclusions."),
    ],
    "Emotional Intelligence": [
        ("A colleague criticizes your idea in a meeting. What response best supports constructive discussion?",
         ["Ask which part concerns them and listen before replying", "Interrupt and raise your voice", "Assume the criticism is a personal attack", "End the meeting immediately"], 0,
         "Curiosity and listening help separate feedback about an idea from a personal judgment."),
        ("You notice you are becoming angry during a disagreement. What is a useful first step?",
         ["Pause and take a few calm breaths before responding", "Send the first message that comes to mind", "Bring up unrelated past conflicts", "Pretend no feeling is present"], 0,
         "A brief pause can reduce impulsive reactions and allow a more deliberate response."),
        ("A teammate seems unusually quiet after receiving bad news. What is an empathetic response?",
         ["Ask privately if they would like support", "Demand that they explain in public", "Tell them to stop being sensitive", "Assume they want no contact"], 0,
         "A private, non-pressuring check-in offers support while respecting their choice."),
        ("Two group members disagree about task ownership. What is a constructive approach?",
         ["Clarify responsibilities and agree on a fair division", "Let the conflict grow", "Choose a side without hearing both", "Remove both from the group"], 0,
         "Clarifying expectations and agreeing on responsibilities addresses the source of conflict."),
        ("You made a mistake that inconvenienced a friend. What is the best response?",
         ["Acknowledge it, apologize specifically, and discuss how to repair it", "Blame the friend", "Avoid them until it is forgotten", "Insist that impact does not matter"], 0,
         "Taking responsibility and offering repair supports trust and effective communication."),
    ],
    "Mental Calculation": [
        ("What is 15% of 200?",
         ["20", "25", "30", "35"], 2,
         "10% of 200 is 20 and 5% is 10, so 15% is 30."),
        ("What is three-quarters of  forty?",
         ["25", "30", "35", "20"], 1,
         "One-quarter of 40 is 10, so three-quarters is 30."),
        ("A cyclist travels 12 km in 30 minutes at a steady speed. How far in 90 minutes?",
         ["24 km", "30 km", "36 km", "42 km"], 2,
         "Ninety minutes is three times 30 minutes, so the distance is 12 × 3 = 36 km."),
        ("A meal costs $80 and a 10% tip is added. What is the total?",
         ["$84", "$86", "$88", "$90"], 2,
         "Ten percent of $80 is $8; total is $88."),
        ("A ratio is 2:3 and the total is 25. What is the smaller share?",
         ["10", "12", "15", "8"], 0,
         "There are five ratio parts; each is 25 ÷ 5 = 5, so the smaller share is 2 × 5 = 10."),
    ],
    "Spatial Reasoning": [
        ("You face north, turn right, then turn right again. Which direction do you face?",
         ["East", "South", "West", "North"], 1,
         "Two right turns from north lead east, then south."),
        ("A square is rotated 90 degrees clockwise. What happens to its shape?",
         ["It becomes a circle", "It remains a square", "It becomes a triangle", "It becomes a rectangle of double width"], 1,
         "Rotation changes orientation, not the shape of a square."),
        ("A person walks 3 blocks east and then 3 blocks west along the same route. Where are they relative to the starting point?",
         ["3 blocks east", "3 blocks west", "At the starting point", "3 blocks north"], 2,
         "The equal opposite movements cancel, returning to the starting point."),
        ("On a standard map with north at the top, which direction is to the left of east?",
         ["North", "South", "West", "Northeast"], 0,
         "Facing east, the left-hand direction is north."),
        ("A cube has a red face on top. The cube is turned upside down. Where is the red face?",
         ["On top", "On the bottom", "On the left", "On the right"], 1,
         "Turning the cube upside down moves the top face to the bottom."),
    ],
    "Verbal Reasoning": [
        ("Book is to reading as fork is to:",
         ["Cooking", "Eating", "Writing", "Cutting"], 1,
         "A book is used for reading; a fork is commonly used for eating."),
        ("Choose the word closest in meaning to 'brief'.",
         ["Short", "Noisy", "Careful", "Late"], 0,
         "Brief means short in duration or length."),
        ("Which word does not belong?",
         ["Oak", "Pine", "Maple", "Copper"], 3,
         "Oak, pine, and maple are trees; copper is a metal."),
        ("All lab assistants wear badges. Nila is a lab assistant. What follows?",
         ["Nila wears a badge", "Everyone wearing a badge is a lab assistant", "Nila is a doctor", "No lab assistants wear badges"], 0,
         "The general statement applies to Nila because she is a lab assistant."),
        ("Choose the sentence that best completes: 'The roads were flooded; ___, the event was postponed.'",
         ["therefore", "meanwhile", "for example", "similarly"], 0,
         "Therefore expresses the result of the flooded roads."),
    ],
    "Reaction & Response": [
        ("Reaction time is generally the interval between:",
         ["A stimulus and a response", "Two unrelated memories", "A meal and sleep", "Two body measurements"], 0,
         "Reaction time describes the delay between a stimulus and a response."),
        ("A reflex action is typically:",
         ["A rapid, automatic response to a stimulus", "A carefully written plan", "A long-term memory", "A voluntary calculation"], 0,
         "Many reflexes are rapid and automatic protective responses."),
        ("Why should a multiple-choice exercise not be treated as a direct measurement of reaction time?",
         ["It does not record response latency under controlled conditions", "It contains written words", "It has four options", "It asks about attention"], 0,
         "A reaction-time measure requires timed stimulus and response recording under controlled conditions."),
        ("When startled by a loud sound, pausing to check the source before acting is an example of:",
         ["Response inhibition and assessment", "A guaranteed reflex", "Long-term recall", "Anchoring"], 0,
         "Pausing helps inhibit an impulsive response while evaluating the situation."),
        ("Which factor can slow a person's response on a task?",
         ["Distraction or divided attention", "Clear instructions", "Adequate practice", "A well-rested state"], 0,
         "Distraction competes for attention and can delay responding."),
    ],
    "Critical Thinking": [
        ("A product is called 'the best' because everyone in one person's friend group uses it. What is the main weakness?",
         ["A small, unrepresentative sample is treated as decisive evidence", "The product has too many users", "The claim uses a measurement", "The conclusion is based on a controlled trial"], 0,
         "One social group may not represent the broader population or establish product quality."),
        ("A headline claims a study proves a food prevents illness, but the study only found an association. What information is most important?",
         ["Whether the study establishes causation and controls alternatives", "The headline's font size", "How many comments the headline received", "Whether the food is colourful"], 0,
         "Association alone does not establish causation; study design and confounders matter."),
        ("A school changes its timetable and attendance rises. What is the strongest conclusion from this information alone?",
         ["Attendance rose after the change, but the change may not be the only cause", "The timetable definitely caused the rise", "The school has no other influences", "Attendance will continue rising forever"], 0,
         "A before-and-after observation alone cannot rule out other explanations."),
        ("Which is the strongest evidence that a phone battery lasts longer after a software update?",
         ["Repeated controlled tests under similar usage conditions", "One user's memory of a single day", "A colourful advertisement", "A comment that the phone feels faster"], 0,
         "Repeated comparable tests provide stronger evidence than anecdote or promotion."),
        ("A survey asks only people who visited a gym whether exercise is useful. What key information is missing?",
         ["How the sample was selected and whether non-gym users were represented", "The survey's paper colour", "The gym's opening music", "The number of exercise machines"], 0,
         "The sampling method and representation affect whether the result generalizes."),
    ],
    "Brain Teasers": [
        ("A farmer has 3 baskets with 2 apples in each. How many apples are there altogether?",
         ["5", "6", "8", "9"], 1,
         "Three baskets × two apples each = six apples."),
        ("A clock shows 3:00. What is the smaller angle between the hour and minute hands?",
         ["45°", "90°", "120°", "180°"], 1,
         "At 3:00 the minute hand is at 12 and the hour hand at 3, a right angle."),
        ("A bag has 3 red balls and 1 blue ball. Without looking, which colour is more likely to be drawn?",
         ["Red", "Blue", "Both equally likely", "Neither can be drawn"], 0,
         "Three of the four balls are red, so red is more likely."),
        ("A number is greater than 10, less than 15, and even. Which could it be?",
         ["11", "12", "13", "15"], 1,
         "12 is even and lies strictly between 10 and 15."),
        ("Two people each shake hands once with the other. How many handshakes occur?",
         ["1", "2", "3", "4"], 0,
         "A handshake between the same two people is one event, not two."),
    ],
}


def build():
    questions = []
    for category, items in CATEGORIES.items():
        if len(items) != 5:
            raise RuntimeError(f"{category} must have exactly five questions")
        for text, options, answer, explanation in items:
            questions.append({
                "category": category,
                "q": text,
                "options": list(options),
                "answer": answer,
                "explanation": explanation,
            })

    if len(questions) != 80:
        raise RuntimeError(f"Expected 80 questions, got {len(questions)}")

    rng = random.Random(20261118)
    desired_answers = [0] * 20 + [1] * 20 + [2] * 20 + [3] * 20
    rng.shuffle(desired_answers)
    shuffled = list(enumerate(questions))
    rng.shuffle(shuffled)

    paper_sections = {category: [] for category in CATEGORIES}
    answer_entries = []
    for idx, (source_index, item) in enumerate(shuffled):
        answer = desired_answers[idx]
        correct_option = item["options"][item["answer"]]
        distractors = [v for i, v in enumerate(item["options"]) if i != item["answer"]]
        options = distractors[:answer] + [correct_option] + distractors[answer:]
        difficulty = "Easy" if idx < 56 else "Moderate"
        qid = f"BRAIN-SHARP-{idx + 1:03d}"
        category = item["category"]

        paper_sections[category].append({
            "id": qid,
            "q": item["q"],
            "options": options,
            "topic": category,
            "subtopic": category,
            "difficulty": difficulty,
            "exam_level": ["Cognitive skills practice"],
            "question_type": "Cognitive skills MCQ",
            "marks_correct": 1,
            "marks_wrong": -0.25,
        })
        answer_entries.append({
            "id": qid,
            "correct_answer": chr(65 + answer),
            "correct_option": correct_option,
            "explanation": item["explanation"],
            "cognitive_skill": category,
            "difficulty": difficulty,
            "why_other_options_are_wrong": [
                f"{chr(65 + i)}. {opt}: does not fit the item or rule in the question."
                for i, opt in enumerate(options) if i != answer
            ],
        })

    paper = {
        "id": "brain-sharpness-80",
        "title": "Brain Sharpness & Cognitive Skills Practice",
        "sourceType": "SKILLS_PRACTICE",
        "exam": "General cognitive-skills practice",
        "discipline": "Cognitive Skills",
        "source": "Original practice questions for specific cognitive tasks; not an IQ or clinical assessment",
        "verificationStatus": "Practice module; performance is limited to the tasks included and does not establish IQ or overall intelligence",
        "maximum_marks": 80,
        "correct_mark": 1,
        "negative_mark": 0.25,
        "unattempted_mark": 0,
        "answerKey": "data/brain-sharpness-80-answer-key.json",
        "instructions": [
            "Correct answer: +1; incorrect answer: -0.25; unattempted: 0.",
            "This practice module measures performance only on the presented tasks.",
            "The reaction section tests concepts and response choices; it does not measure actual reaction time."
        ],
        "sections": [
            {"name": category, "questions": paper_sections[category]}
            for category in CATEGORIES
        ],
    }

    key = {
        "id": "brain-sharpness-80-answer-key",
        "paper_id": "brain-sharpness-80",
        "total_questions": 80,
        "maximum_marks": 80,
        "marking": {"correct": 1, "wrong": -0.25, "unattempted": 0},
        "answers": answer_entries,
    }
    (DATA / "brain-sharpness-80.json").write_text(
        json.dumps(paper, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (DATA / "brain-sharpness-80-answer-key.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    build()
