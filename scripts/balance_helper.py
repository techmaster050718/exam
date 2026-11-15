"""
Helper utility to balance option answers and format questions cleanly.
"""
from collections import Counter

def make_balanced_pattern(n, counts=None):
    if counts is None:
        base = n // 4
        rem = n % 4
        counts = [base + (1 if i < rem else 0) for i in range(4)]
    else:
        counts = list(counts)

    order = []
    blocks = [ [0, 2, 1, 3], [1, 3, 0, 2], [2, 0, 3, 1], [3, 1, 2, 0] ]
    b_idx = 0
    while len(order) < n and sum(counts) > 0:
        block = blocks[b_idx % len(blocks)]
        for x in block:
            if counts[x] > 0 and len(order) < n:
                if len(order) >= 2 and order[-1] == x and order[-2] == x:
                    continue
                order.append(x)
                counts[x] -= 1
        b_idx += 1

    for x in range(4):
        while counts[x] > 0:
            inserted = False
            for i in range(len(order) + 1):
                p1 = order[i-1] if i > 0 else -1
                p2 = order[i-2] if i > 1 else -1
                n1 = order[i] if i < len(order) else -1
                n2 = order[i+1] if i + 1 < len(order) else -1
                if (p1 == x and p2 == x) or (p1 == x and n1 == x) or (n1 == x and n2 == x):
                    continue
                order.insert(i, x)
                counts[x] -= 1
                inserted = True
                break
            if not inserted:
                order.append(x)
                counts[x] -= 1
    return order


def rebalance_questions(questions, pattern=None):
    """
    Given a list of questions, reorders their options so that the correct answer
    matches the desired pattern, preserving the exact text of correct answer and distractors.
    """
    n = len(questions)
    if pattern is None:
        pattern = make_balanced_pattern(n)
    
    rebalanced = []
    for q_data, target_ans in zip(questions, pattern):
        old_opts = list(q_data["options"])
        old_ans = q_data["answer"]
        correct_val = old_opts[old_ans]
        distractors = [opt for i, opt in enumerate(old_opts) if i != old_ans]
        
        new_opts = [None] * 4
        new_opts[target_ans] = correct_val
        d_idx = 0
        for i in range(4):
            if i != target_ans:
                new_opts[i] = distractors[d_idx]
                d_idx += 1
        
        new_q = dict(q_data)
        new_q["options"] = new_opts
        new_q["answer"] = target_ans
        rebalanced.append(new_q)
    return rebalanced

