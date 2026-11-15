# Database Management Systems (DBMS) & SQL Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**
> Last Updated: 2026-11-15

---

## DBMS command map
| Domain | Core recall points |
| :--- | :--- |
| Data model | ER model, cardinality, participation, keys |
| Relational design | Normal forms, dependency rules, key hierarchy |
| SQL | DDL/DML, joins, aggregations, window functions |
| Transactions | ACID, isolation levels, locking, concurrency |
| Exam focus | Schema design, query reasoning, normalization, transaction anomalies |

---

## 1. ENTITY-RELATIONSHIP (ER) MODEL

### 1.1 ER Components & Notations
```text
┌──────────────┐     ◇ (Diamond)     ( Ellipse )      ╔══════════════╗
│    Entity    │     Relationship     Attribute       ║ Weak Entity  ║
└──────────────┘                                      ╚══════════════╝
(Double Ellipse)    (Dashed Ellipse)   (Underlined)     (Double Diamond)
Multivalued Attr      Derived Attr      Primary Key     Identifying Rel
```

* **Cardinality Ratios:** 1:1 (One-to-One), 1:N (One-to-Many), M:N (Many-to-Many).
* **Participation:** Total (Double line - every entity must participate), Partial (Single line).

---

## 2. RELATIONAL KEYS HIERARCHY
```text
Super Key (Any set of attributes uniquely identifying a tuple)
  ↓ [Minimal Super Key]
Candidate Key (Super key with no redundant attributes)
  ↓ [Designated by DBA]
Primary Key (Candidate key chosen as main identifier, NOT NULL & UNIQUE)
```
* **Alternate Key:** Candidate keys not selected as the primary key.
* **Foreign Key:** Attribute in relation $R_1$ that references the primary key of relation $R_2$. Enforces **Referential Integrity**.

---

## 3. NORMALIZATION SUMMARY TABLE

| Normal Form | Violated By | Condition for Compliance | Lossless & FD Preserving? |
| :--- | :--- | :--- | :---: |
| **1NF** | Composite / Multivalued attributes | All attribute domains must contain only atomic values | Always achievable |
| **2NF** | Partial Dependency ($A \to B$ where $A$ is proper subset of Candidate Key and $B$ is non-prime) | 1NF + No non-prime attribute is partially dependent on any candidate key | Always achievable |
| **3NF** | Transitive Dependency ($X \to Y \to Z$) | 2NF + For every FD $X \to Y$: Either $X$ is a Super Key OR $Y$ is a Prime Attribute | Always achievable (Lossless + Dependency Preserving) |
| **BCNF** | Key dependency violation | For every non-trivial FD $X \to Y$, $X$ must be a **Super Key** | Always Lossless, but may NOT preserve dependencies |
| **4NF** | Multivalued Dependency ($X \twoheadrightarrow Y$) | BCNF + For every non-trivial MVD $X \twoheadrightarrow Y$, $X$ is a Super Key | Lossless decomposition |

### Normalization Cheat Rule:
* In $X \to Y$:
  * **3NF:** $X$ is Super Key OR $Y$ is Prime.
  * **BCNF:** $X$ MUST be Super Key (no exceptions!).

---

## 4. SQL WINDOW FUNCTIONS & COMMON TABLES

### 4.1 Ranking Functions Comparison
```sql
SELECT emp_id, dept, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,
       RANK()       OVER (ORDER BY salary DESC) as rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rnk
FROM employees;
```
For Salaries: `[90000, 90000, 80000, 70000]`:
* `ROW_NUMBER()`: 1, 2, 3, 4 (always sequential, never ties)
* `RANK()`: 1, 1, **3**, 4 (skips rank after ties)
* `DENSE_RANK()`: 1, 1, **2**, 3 (never skips rank after ties)

### 4.2 SQL Joins Summary
```text
Table A (Left)               Table B (Right)
┌──────┬──────┐              ┌──────┬──────┐
│  ID  │ ValA │              │  ID  │ ValB │
├──────┼──────┤              ├──────┼──────┤
│  1   │  A1  │              │  1   │  B1  │
│  2   │  A2  │              │  3   │  B3  │
└──────┴──────┘              └──────┴──────┘

INNER JOIN:  (1, A1, B1)
LEFT JOIN:   (1, A1, B1), (2, A2, NULL)
RIGHT JOIN:  (1, A1, B1), (3, NULL, B3)
FULL JOIN:   (1, A1, B1), (2, A2, NULL), (3, NULL, B3)
CROSS JOIN:  Cartesian product (A x B) -> 2 x 2 = 4 rows
```

---

## 5. TRANSACTIONS & ACID PROPERTIES
* **Atomicity:** "All or Nothing". Ensured by Recovery Manager (Undo logs / WAL).
* **Consistency:** Database moves from one valid state to another. Preserved by application & constraints.
* **Isolation:** Concurrently executing transactions do not interfere. Ensured by Concurrency Control (Locking / Timestamping).
* **Durability:** Committed changes persist even across system crashes. Ensured by Redo logs / Checkpoints.

### ANSI SQL Isolation Levels vs Anomalies
| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | Occurs | Occurs | Occurs |
| **Read Committed** | **Prevented** | Occurs | Occurs |
| **Repeatable Read** | **Prevented** | **Prevented** | Occurs |
| **Serializable** | **Prevented** | **Prevented** | **Prevented** |

---

## 6. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **BCNF vs 3NF:** 3NF always allows dependency preservation; BCNF does not guarantee it.
2. **Cascadeless Schedules:** If $T_j$ reads data written by $T_i$, then $T_i$ must commit before $T_j$ reads it.
3. **B+ Tree:** Leaf nodes contain all actual data pointers and are connected in a doubly linked list for efficient range queries.
4. **Natural Join:** Equi-join on all common attributes, removing duplicate join columns.

### COMMON TRAPS
* ⚠️ **Trap 1:** Believing BCNF is always preferable to 3NF. In practice, losing functional dependencies makes update verification costly.
* ⚠️ **Trap 2:** Confusing `COUNT(*)` with `COUNT(column)`. `COUNT(*)` counts all rows including NULLs; `COUNT(column)` ignores NULL values!
* ⚠️ **Trap 3:** Thinking `WHERE` can filter aggregate results. Aggregate results must be filtered using `HAVING`!
