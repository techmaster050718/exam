# Software Engineering & SDLC Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**
> Last Updated: 2026-11-15

---

## Software engineering command map
| Domain | Core recall points |
| :--- | :--- |
| SDLC & models | Waterfall, V-model, Spiral, Agile, Scrum |
| Project measurement | COCOMO, cyclomatic complexity, velocity, burn-down |
| Quality & testing | Black-box, white-box, unit, integration, system, acceptance |
| Design principles | Cohesion, coupling, modularity, maintainability |
| Exam focus | Process model selection, metrics, testing principles |

---

## 1. SDLC MODELS COMPARISON

| Model | Strengths | Weaknesses | Best Suited For |
| :--- | :--- | :--- | :--- |
| **Waterfall** | Simple, disciplined, linear stages | Inflexible to changes, working software late | Well-defined, stable requirements (e.g., defence, civil) |
| **V-Model** | Strict verification & validation paired with each stage | High rigidity, poor flexibility | Safety-critical software (medical, avionics) |
| **Spiral** | Explicit **Risk Analysis** at every iteration | Expensive, complex management | High-risk, large-scale, innovative projects |
| **Agile (Scrum)** | High adaptability, customer feedback, working software early | Scope creep potential, requires disciplined team | Dynamic, evolving product requirements |

---

## 2. AGILE & SCRUM CEREMONIES AND ARTIFACTS

```text
┌─────────────────────────┐      ┌─────────────────────────┐
│     Scrum Roles         │      │     Scrum Artifacts     │
├─────────────────────────┤      ├─────────────────────────┤
│ Product Owner (PO)      │      │ Product Backlog         │
│ Scrum Master (SM)       │      │ Sprint Backlog          │
│ Development Team        │      │ Increment (Potentially  │
│                         │      │ Shippable Product)      │
└─────────────────────────┘      └─────────────────────────┘

Sprint Ceremonies (Cycle: 1 to 4 weeks):
1. Sprint Planning   -> PO & Dev select items from Product Backlog into Sprint Backlog
2. Daily Scrum (15m) -> What did I do? What will I do? Any impediments?
3. Sprint Review     -> Live demonstration of Increment to stakeholders
4. Sprint Retrospective -> Team inspects internal processes & plans improvements
```

* **Burn-down Chart:** Shows remaining work vs time in sprint (ideal line vs actual).
* **Burn-up Chart:** Shows completed work and total scope over time.
* **Velocity:** Amount of work (story points) a team completes in a single sprint.

---

## 3. SOFTWARE METRICS & COCOMO

### 3.1 McCabe's Cyclomatic Complexity
Measures the number of linearly independent paths through program source code.
$$V(G) = E - N + 2P$$
Where:
* $E$ = Number of edges in the control flow graph
* $N$ = Number of nodes
* $P$ = Number of connected components (typically $P=1$)
* Alternatively: $V(G) = P_d + 1$ (where $P_d$ is the number of predicate/decision nodes).

### 3.2 Basic COCOMO Model
Estimates Effort ($E$ in Person-Months) and Time ($D$ in Months):
$$Effort = a \cdot (KLOC)^b \quad \text{Person-Months}$$
$$Duration = c \cdot (Effort)^d \quad \text{Months}$$

| Project Mode | Description | $a$ | $b$ |
| :--- | :--- | :---: | :---: |
| **Organic** | Small teams, familiar in-house environment, relaxed requirements | 2.4 | 1.05 |
| **Semidetached**| Medium teams, mixed experience, medium complexity | 3.0 | 1.12 |
| **Embedded** | Tight hardware/regulatory constraints, flight control, avionics | 3.6 | 1.20 |

---

## 4. SOFTWARE TESTING METHODOLOGIES

* **Black-Box Testing (Functional):** Tester has no access to internal source code.
  * *Equivalence Partitioning:* Divides input domain into valid/invalid partitions.
  * *Boundary Value Analysis (BVA):* Tests values at edges (min, min+1, nom, max-1, max).
* **White-Box Testing (Structural):** Tester has full access to internal code logic.
  * *Basis Path Testing:* Guarantees every statement and branch is executed at least once ($V(G)$ paths).
* **Testing Levels:** Unit Testing $\to$ Integration Testing $\to$ System Testing $\to$ Acceptance Testing (Alpha/Beta).

---

## 5. MUST REMEMBER & COMMON TRAPS
1. **Cohesion vs Coupling:** High Cohesion (internal strength of a module) is desirable; Low Coupling (interdependence between modules) is desirable.
2. **Alpha vs Beta Testing:** Alpha is conducted at developer's site by internal users; Beta is conducted at client's real-world environment by end users.
3. **Verification vs Validation:** Verification asks "Are we building the product right? (compliance)"; Validation asks "Are we building the right product? (user needs)".
