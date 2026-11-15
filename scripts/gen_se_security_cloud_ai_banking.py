"""
Generates:
1. data/revision/software-engineering/se-revision.md
2. data/revision/cybersecurity/security-revision.md
3. data/revision/ai-ml/ai-ml-revision.md
4. data/revision/banking-technology/banking-tech-revision.md
"""
import os

os.makedirs("data/revision/software-engineering", exist_ok=True)
os.makedirs("data/revision/cybersecurity", exist_ok=True)
os.makedirs("data/revision/ai-ml", exist_ok=True)
os.makedirs("data/revision/banking-technology", exist_ok=True)

# 1. se-revision.md
SE_MD = """# Software Engineering & SDLC Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

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
$$Effort = a \\cdot (KLOC)^b \\quad \\text{Person-Months}$$
$$Duration = c \\cdot (Effort)^d \\quad \\text{Months}$$

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
* **Testing Levels:** Unit Testing $\\to$ Integration Testing $\\to$ System Testing $\\to$ Acceptance Testing (Alpha/Beta).

---

## 5. MUST REMEMBER & COMMON TRAPS
1. **Cohesion vs Coupling:** High Cohesion (internal strength of a module) is desirable; Low Coupling (interdependence between modules) is desirable.
2. **Alpha vs Beta Testing:** Alpha is conducted at developer's site by internal users; Beta is conducted at client's real-world environment by end users.
3. **Verification vs Validation:** Verification asks "Are we building the product right? (compliance)"; Validation asks "Are we building the right product? (user needs)".
"""

with open("data/revision/software-engineering/se-revision.md", "w", encoding="utf-8") as f:
    f.write(SE_MD)
print("Wrote data/revision/software-engineering/se-revision.md")


# 2. security-revision.md
SECURITY_MD = """# Information Security & Cryptography Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. CRYPTOGRAPHIC ALGORITHMS OVERVIEW

| Algorithm | Category | Key Length | Block Size | Underlying Math Problem | Use Case |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **DES** | Symmetric Feistel | 56 bits | 64 bits | Substitution-Permutation | Legacy (Insecure) |
| **3DES** | Symmetric Feistel | 112 / 168 bits | 64 bits | Encrypt-Decrypt-Encrypt | Legacy banking |
| **AES** | Symmetric SPN | 128, 192, 256 bits | 128 bits | Galois Field arithmetic | Global standard (E-commerce, Wi-Fi) |
| **RSA** | Asymmetric | 2048 to 4096 bits | Variable | Prime Factorization of large $n=pq$ | Key exchange, Digital Signatures |
| **ECC** | Asymmetric | 256 to 384 bits | Variable | Discrete Logarithm on Elliptic Curves | High security with smaller keys (TLS 1.3) |
| **SHA-256** | Hash Function | 256-bit digest | 512-bit block | Merkle-Damgård construction | Integrity, Blockchain, Certificates |

### AES Transformation Rounds
* AES-128: 10 rounds
* AES-192: 12 rounds
* AES-256: 14 rounds
* *Round operations:* SubBytes, ShiftRows, MixColumns (omitted in final round), AddRoundKey.

---

## 2. DIGITAL SIGNATURES & PKI

```text
Sender Alice:
Message M ──> Hash Function ──> Digest D ──> Encrypt with Alice's PRIVATE Key ──> Digital Signature S
                                                                                       │
Receiver Bob receives (M, S):                                                          ▼
Signature S ──> Decrypt with Alice's PUBLIC Key ──> Decrypted Digest D1
Message M   ──> Hash Function ─────────────────────> Calculated Digest D2
              If D1 == D2 -> Message is Authentic, Unaltered, and Non-Repudiated!
```
* **Guarantees:** Integrity, Authentication, and Non-Repudiation (Alice cannot deny having sent it).

---

## 3. WEB APPLICATION SECURITY (OWASP TOP 10)

```text
┌──────────────────┬─────────────────────────────────────┬─────────────────────────────────────┐
│ Attack Vector    │ Mechanism                           │ Defenses                            │
├──────────────────┼─────────────────────────────────────┼─────────────────────────────────────┤
│ SQL Injection    │ Malicious SQL appended to input     │ Prepared Statements, Param Queries  │
│ Stored XSS       │ Malicious JS stored in server DB    │ Context-aware output encoding, CSP  │
│ Reflected XSS    │ Malicious JS in URL query parameter │ Input sanitization, CSP             │
│ CSRF             │ Forges unauthorized victim request   │ Anti-CSRF Synchronizer Tokens, SameSite│
│ SSRF             │ Server tricked into fetching internal│ URL allowlists, restrict loopback   │
└──────────────────┴─────────────────────────────────────┴─────────────────────────────────────┘
```

---

## 4. ZERO TRUST ARCHITECTURE & BANKING GOVERNANCE
* **Zero Trust Tenet:** "Never Trust, Always Verify". Perimeter defenses are inadequate; assume breach.
* **Core Controls:** Identity & Access Management (IAM), Multi-Factor Authentication (MFA), Micro-segmentation, Least Privilege Principle.
* **PCI-DSS:** Mandates that Sensitive Authentication Data (SAD) — specifically **CVV/CVC and Full Magnetic Stripe data** — must NEVER be stored post-authorization, even if encrypted.
* **RBI Mandate:** Banks must report critical cybersecurity breaches to RBI / CERT-In within **2 to 6 hours** of detection.
"""

with open("data/revision/cybersecurity/security-revision.md", "w", encoding="utf-8") as f:
    f.write(SECURITY_MD)
print("Wrote data/revision/cybersecurity/security-revision.md")


# 3. ai-ml-revision.md
AI_ML_MD = """# Artificial Intelligence, Machine Learning & Big Data Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. MACHINE LEARNING PARADIGMS

| Paradigm | Description | Feedback / Signal | Typical Algorithms |
| :--- | :--- | :--- | :--- |
| **Supervised** | Model trains on labeled input-output pairs $(X, y)$ | Direct target error | Linear Regression, Logistic Regression, Decision Trees, SVM |
| **Unsupervised** | Discovers hidden patterns in unlabeled data $X$ | No external labels | K-Means, Hierarchical Clustering, PCA, Autoencoders |
| **Reinforcement** | Agent interacts with environment to maximize cumulative reward | Reward / Penalty signal | Q-Learning, Policy Gradients, SARSA |

---

## 2. MODEL EVALUATION & CONFUSION MATRIX

```text
                    Actual Positive          Actual Negative
Predicted Positive   True Positive (TP)       False Positive (FP) [Type I Error]
Predicted Negative   False Negative (FN) [Type II] True Negative (TN)
```

### Key Metrics Formulas:
$$\\text{Accuracy} = \\frac{TP + TN}{TP + TN + FP + FN}$$
$$\\text{Precision} = \\frac{TP}{TP + FP} \\quad (\\text{Quality of positive predictions})$$
$$\\text{Recall (Sensitivity)} = \\frac{TP}{TP + FN} \\quad (\\text{Ability to find all positives})$$
$$F_1\\text{-Score} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2TP}{2TP + FP + FN}$$

---

## 3. BIAS-VARIANCE TRADEOFF & REGULARIZATION
* **High Bias (Underfitting):** Model is too simplistic; misses key trends. High error on both training and test data.
* **High Variance (Overfitting):** Model memorizes training noise; poor generalization on unseen data.
* **Regularization Techniques:**
  * **L1 Regularization (Lasso):** Adds penalty $\\lambda \\sum |w_i|$. Induces **sparsity** (sets non-informative weights to 0 for feature selection).
  * **L2 Regularization (Ridge):** Adds penalty $\\lambda \\sum w_i^2$. Shrinks weights close to zero; preserves all features.
  * **Dropout:** Randomly deactivates neurons during training in deep neural networks.

---

## 4. DEEP LEARNING ACTIVATION FUNCTIONS
* **Sigmoid:** $\\sigma(x) = \\frac{1}{1 + e^{-x}}$, outputs in range $(0, 1)$. Vanishing gradient problem for extreme values.
* **Tanh:** $\\tanh(x) = \\frac{e^x - e^{-x}}{e^x + e^{-x}}$, outputs in range $(-1, 1)$, zero-centered.
* **ReLU (Rectified Linear Unit):** $f(x) = \\max(0, x)$. Computationally trivial; prevents vanishing gradient for positive activations. Can suffer from "Dying ReLU".
* **Softmax:** Converts a vector of $K$ real values into a categorical probability distribution summing to 1.

---

## 5. APACHE HADOOP & BIG DATA ARCHITECTURE
* **HDFS (Storage):** Master-Slave Architecture.
  * **NameNode (Master):** Stores filesystem namespace directory tree and block metadata in RAM.
  * **DataNode (Slave):** Stores physical data blocks on local disks (default block size: 128 MB, default replication: 3).
* **MapReduce (Compute):** Splits computation into Map phase (key-value pairs) and Reduce phase (aggregation).
* **Apache Spark:** In-memory distributed computation framework using Resilient Distributed Datasets (RDDs); up to 100x faster than MapReduce.
"""

with open("data/revision/ai-ml/ai-ml-revision.md", "w", encoding="utf-8") as f:
    f.write(AI_ML_MD)
print("Wrote data/revision/ai-ml/ai-ml-revision.md")


# 4. banking-tech-revision.md
BANKING_TECH_MD = """# Banking Technology, Digital Payments & IT Governance Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, SBI SO, FinTech)**

---

## 1. PAYMENT SYSTEMS IN INDIA COMPARISON

| Feature | UPI | IMPS | NEFT | RTGS |
| :--- | :--- | :--- | :--- | :--- |
| **Operated By** | NPCI | NPCI | RBI | RBI |
| **Settlement** | Real-Time Immediate | Real-Time Immediate | Batch-wise (Half-hourly) | Real-Time Gross Settlement |
| **Operating Hours** | 24x7x365 | 24x7x365 | 24x7x365 | 24x7x365 |
| **Minimum Limit** | ₹1 | ₹1 | ₹1 | **₹2,00,000** |
| **Maximum Limit** | ₹1 Lakh to ₹5 Lakh (varies) | ₹5 Lakh | No upper ceiling | No upper ceiling |
| **Identifier** | Virtual Payment Address (VPA) / Mobile | Mobile No. + MMID / Acc+IFSC | Account Number + IFSC | Account Number + IFSC |

---

## 2. CORE BANKING SOLUTION (CBS)
* **Definition:** Centralized software system that allows customers to operate their accounts from any branch of the bank ("Anywhere, Anytime Banking").
* **Leading Platforms:**
  * **Finacle:** Developed by Infosys (used by SBI, PNB, Canara Bank).
  * **BaNCS:** Developed by TCS.
  * **Flexcube:** Developed by Oracle.
* **Key Architecture Components:** Central Database cluster, High-Availability Hot Standby Disaster Recovery site (RPO $\\approx 0$, RTO $< 30$ mins), Integration Middleware (MQ / ESB).

---

## 3. FINANCIAL MESSAGING STANDARDS
* **ISO 8583:** Legacy point-of-sale and ATM transaction interchange messaging format (bitmap-driven).
* **ISO 20022:** Modern XML/JSON financial industry messaging standard replacing SWIFT MT format. Supports rich, structured metadata to combat AML/CFT fraud.
* **SWIFT (Society for Worldwide Interbank Financial Telecommunication):** Global messaging network for international financial wire transfers.

---

## 4. MUST REMEMBER & REGULATORY COMPLIANCE
1. **IFSC (Indian Financial System Code):** 11 characters alphanumeric. First 4 characters = Bank code, 5th character = Reserved `0`, Last 6 characters = Branch code.
2. **MICR Code:** 9 digits numerical for cheque clearing. First 3 = City, Next 3 = Bank, Last 3 = Branch.
3. **CTS (Cheque Truncation System):** Electronic image of cheque sent to clearing house instead of physical movement.
4. **NPCI Payment Rails:** RuPay, UPI, IMPS, NACH, AePS (Aadhaar-enabled Payment System), BBPS (Bharat Bill Payment System).
"""

with open("data/revision/banking-technology/banking-tech-revision.md", "w", encoding="utf-8") as f:
    f.write(BANKING_TECH_MD)
print("Wrote data/revision/banking-technology/banking-tech-revision.md")

