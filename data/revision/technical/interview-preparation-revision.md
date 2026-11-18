# Interview Preparation Action Guide

## SQL Practice
**Action:** Practice joins, group aggregation, window functions, CTEs, indexing, and transaction reasoning. **Structure:** Clarify schema, write simple SQL, optimize, test edge cases. **Example:** Find second-highest paid employee by department. **Key follow-ups:** NULL, duplicate, performance. **Interview approach:** Explain expected rows and complexity before final SQL.

## Window Functions
**What is it?** Window functions calculate across ordered or partitioned rows without collapsing them. **Interview answer:** "I use `ROW_NUMBER`, `RANK`, `LAG`, and running aggregates for per-group analytics." **Example:** Rank products within each category. **Use:** SQL interview and reporting. **Points:** Partition, order, frame. **Follow-ups:** RANK vs DENSE_RANK.

## CTEs
**What is it?** A CTE gives a readable named intermediate result. **Interview answer:** "I use CTEs to structure complex SQL and recursive CTEs for hierarchies." **Example:** Employee reporting chain. **Use:** Readability and recursion. **Points:** Inline, materialization varies. **Follow-ups:** CTE vs subquery.

## Python Coding Rounds
**Action:** State input/output, propose a brute force, improve complexity, handle edge cases, and test manually. **Example:** Longest substring. **Key points:** Types, mutability, hashing, recursion, exceptions. **Follow-ups:** Memory, overflow, test cases.

## Resume Explanation
**Action:** Use four parts: role, problem, implementation, measurable outcome. **Example:** "I owned API pagination and cut report latency from 4 seconds to 900 milliseconds." **Key care:** Claims must match actual ownership. **Follow-ups:** Why, trade-off, challenge.

## Project Explanation
**Structure:** Problem and users; constraints; architecture; your contribution; data flow; scale; failure; trade-offs; result. **Example:** Explain a payment service. **Technical follow-ups:** Database choice, consistency, retries, authentication. **Do not:** Name technologies without explaining why. **Final line:** State one measurable outcome.

## Behavioral Questions
**Action:** Prepare 6 stories: conflict, failure, leadership, ambiguity, feedback, deadline. **Example:** A failed deployment taught a rollback gate. **Key care:** Answer from your own role. **Follow-ups:** What would you change? **Do not:** Blame a teammate.

## STAR Method
**What is it?** STAR means Situation, Task, Action, Result. **Interview answer:** "I spend 15% on context, 10% on my task, 60% on actions, and 15% on a measurable result." **Example:** Resolve cross-team API delay. **Use:** Behavioral answers. **Follow-ups:** Result, learning.

## Mock Interviews
**Action:** Run timed rounds with a peer or recorder, then score correctness, communication, complexity, tests, and trade-offs. **Example:** 45-minute system design. **Key points:** Ask clarification, narrate, manage time, summarize. **Follow-ups:** Re-record and improve. **Related:** Every technical category.
