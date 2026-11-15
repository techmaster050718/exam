"""
Generates:
1. data/revision/dbms/dbms-revision.md
2. data/revision/computer-networks/networks-revision.md
3. data/revision/programming/programming-revision.md
"""
import os

os.makedirs("data/revision/dbms", exist_ok=True)
os.makedirs("data/revision/computer-networks", exist_ok=True)
os.makedirs("data/revision/programming", exist_ok=True)

# 1. dbms-revision.md
DBMS_MD = """# Database Management Systems (DBMS) & SQL Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

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
| **2NF** | Partial Dependency ($A \\to B$ where $A$ is proper subset of Candidate Key and $B$ is non-prime) | 1NF + No non-prime attribute is partially dependent on any candidate key | Always achievable |
| **3NF** | Transitive Dependency ($X \\to Y \\to Z$) | 2NF + For every FD $X \\to Y$: Either $X$ is a Super Key OR $Y$ is a Prime Attribute | Always achievable (Lossless + Dependency Preserving) |
| **BCNF** | Key dependency violation | For every non-trivial FD $X \\to Y$, $X$ must be a **Super Key** | Always Lossless, but may NOT preserve dependencies |
| **4NF** | Multivalued Dependency ($X \\twoheadrightarrow Y$) | BCNF + For every non-trivial MVD $X \\twoheadrightarrow Y$, $X$ is a Super Key | Lossless decomposition |

### Normalization Cheat Rule:
* In $X \\to Y$:
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
"""

with open("data/revision/dbms/dbms-revision.md", "w", encoding="utf-8") as f:
    f.write(DBMS_MD)
print("Wrote data/revision/dbms/dbms-revision.md")


# 2. networks-revision.md
NETWORKS_MD = """# Computer Networks – Complete Exam Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. OSI VS TCP/IP PROTOCOL SUITE

```text
OSI 7 LAYERS                       TCP/IP 4 LAYERS     DATA UNIT (PDU)    PROTOCOLS / HARDWARE
┌────────────────────────┐
│ 7. Application Layer   │──┐
├────────────────────────┤  │── Application Layer      Data / Message     HTTP, HTTPS, DNS, SMTP, FTP, SSH
│ 6. Presentation Layer  │──┤
├────────────────────────┤  │
│ 5. Session Layer       │──┘
├────────────────────────┤
│ 4. Transport Layer     │───── Transport Layer        Segment / Datagram TCP, UDP (Ports)
├────────────────────────┤
│ 3. Network Layer       │───── Internet Layer         Packet             IPv4, IPv6, ICMP, ARP, OSPF, BGP (Routers)
├────────────────────────┤
│ 2. Data Link Layer     │──┐
├────────────────────────┤  │── Network Access Layer   Frame / Bit        Ethernet, Wi-Fi, MAC, PPP (Switches, Bridges)
│ 1. Physical Layer      │──┘                          Bits               Cables, Hubs, Repeaters
└────────────────────────┘
```

---

## 2. IP ADDRESSING & SUBNETTING CHEAT SHEET

### 2.1 IPv4 Default Classes
| Class | 1st Octet Range | Leading Bits | Default Subnet Mask | Network / Host Bits | Usable Hosts / Network |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 1 – 126 | `0` | 255.0.0.0 (/8) | 8 Net / 24 Host | $2^{24} - 2 = 16,777,214$ |
| **B** | 128 – 191 | `10` | 255.255.0.0 (/16) | 16 Net / 16 Host | $2^{16} - 2 = 65,534$ |
| **C** | 192 – 223 | `110` | 255.255.255.0 (/24)| 24 Net / 8 Host | $2^8 - 2 = 254$ |
| **D** | 224 – 239 | `1110`| Multicast (No mask) | N/A | Multicast Groups |
| **E** | 240 – 255 | `1111`| Experimental | N/A | Reserved |

> Note: 127.0.0.0/8 is reserved for Loopback (localhost: 127.0.0.1).

### 2.2 Subnetting Formulas
* Number of subnets created with $b$ borrowed host bits = $2^b$
* Number of usable hosts per subnet with $h$ remaining host bits = $2^h - 2$
  *(Subtract 2 for Network ID and Directed Broadcast Address)*
* Block Size (Magic Number) = $256 - \\text{Octet Value of Subnet Mask}$

---

## 3. TCP VS UDP COMPARISON

| Feature | Transmission Control Protocol (TCP) | User Datagram Protocol (UDP) |
| :--- | :--- | :--- |
| **Connection** | Connection-Oriented (3-way handshake) | Connectionless |
| **Reliability** | Guaranteed delivery (ACK + Retransmission) | Best-effort (No retransmission) |
| **Ordering** | In-order delivery guaranteed (Seq numbers) | No ordering (packets can arrive out of order) |
| **Header Size** | 20 to 60 bytes | Fixed 8 bytes |
| **Speed** | Slower (protocol overhead) | Extremely fast (low latency) |
| **Flow Control** | Yes (Sliding Window) | No |
| **Congestion Control**| Yes (Slow start, Congestion avoidance) | No |
| **Broadcasting** | Unicast only | Unicast, Multicast, Broadcast |
| **Protocols** | HTTP/S, FTP, SSH, SMTP, BGP | DNS, DHCP, TFTP, SNMP, VoIP, Video Streaming |

---

## 4. TCP HANDSHAKE & TEARDOWN

### 3-Way Connection Handshake
```text
Client                                  Server
  │                 SYN (Seq=x)            │
  │───────────────────────────────────────>│  Server enters SYN_RCVD
  │                                        │
  │           SYN-ACK (Seq=y, Ack=x+1)     │
  │<───────────────────────────────────────│  Client enters ESTABLISHED
  │                                        │
  │                 ACK (Ack=y+1)          │
  │───────────────────────────────────────>│  Server enters ESTABLISHED
```

### 4-Way Connection Teardown
```text
Client (Active Closer)                  Server (Passive Closer)
  │                 FIN (Seq=u)            │
  │───────────────────────────────────────>│  Server sends ACK, enters CLOSE_WAIT
  │                 ACK (Ack=u+1)          │
  │<───────────────────────────────────────│  Client enters FIN_WAIT_2
  │                                        │  Server finishes sending data...
  │                 FIN (Seq=v)            │
  │<───────────────────────────────────────│  Server enters LAST_ACK
  │                 ACK (Ack=v+1)          │
  │───────────────────────────────────────>│  Client enters TIME_WAIT (2MSL timer)
```

---

## 5. ROUTING & CORE PROTOCOLS

1. **RIP (Routing Information Protocol):** Distance Vector, Bellman-Ford, Metric: Hop count (Max 15 hops, 16 = unreachable), updates every 30 sec via UDP 520.
2. **OSPF (Open Shortest Path First):** Link State, Dijkstra algorithm, Metric: Cost ($10^8 / \\text{bandwidth}$), Classless, uses IP protocol 89.
3. **BGP (Border Gateway Protocol):** Path Vector, Inter-Autonomous System routing, operates over TCP port 179.
4. **ARP (Address Resolution Protocol):** Resolves IP $\\to$ MAC address (Broadcast request, Unicast reply).
5. **DNS (Domain Name System):** Resolves Hostname $\\to$ IP address (UDP/TCP port 53).
6. **DHCP DORA Process:** **D**iscover (Broadcast) $\\to$ **O**ffer (Unicast/Broadcast) $\\to$ **R**equest (Broadcast) $\\to$ **A**cknowledge (Unicast). Uses UDP 67/68.

---

## 6. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Sliding Window Sizes:**
   * Stop-and-Wait: Sender $W_s = 1$, Receiver $W_r = 1$.
   * Go-Back-N: $W_s = 2^n - 1$, $W_r = 1$. Discards out-of-order packets.
   * Selective Repeat: $W_s = 2^{n-1}$, $W_r = 2^{n-1}$. Buffers out-of-order packets.
2. **TCP TIME_WAIT State:** Lasts $2 \\times \\text{MSL}$ (Maximum Segment Lifetime) to ensure the final ACK reached the server and flush lingering network packets.
3. **HTTP Status Codes:**
   * `200 OK`, `201 Created`
   * `301 Moved Permanently`, `304 Not Modified`
   * `400 Bad Request`, `401 Unauthorized` (needs credentials), `403 Forbidden` (authenticated but denied), `404 Not Found`
   * `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout`

### COMMON TRAPS
* ⚠️ **Trap 1:** 401 Unauthorized vs 403 Forbidden. 401 means "Who are you? (Authenticate)", 403 means "I know who you are, but you cannot enter (Authorize)".
* ⚠️ **Trap 2:** Assuming Hubs reduce collision domains. Hubs share one collision domain; Switches provide a dedicated collision domain per port!
"""

with open("data/revision/computer-networks/networks-revision.md", "w", encoding="utf-8") as f:
    f.write(NETWORKS_MD)
print("Wrote data/revision/computer-networks/networks-revision.md")


# 3. programming-revision.md
PROGRAMMING_MD = """# Object-Oriented Programming (OOP) & Language Fundamentals
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. CORE OOP PILLARS

```text
┌─────────────────┬─────────────────────────────────────────────────────────┐
│ Pillar          │ Core Mechanism & Real-World Purpose                     │
├─────────────────┼─────────────────────────────────────────────────────────┤
│ Encapsulation   │ Bundling data & methods; data hiding via private access │
│ Abstraction     │ Hiding complex implementation; showing essential APIs   │
│ Inheritance     │ Code reuse; 'is-a' hierarchy (Single, Multilevel, etc.) │
│ Polymorphism    │ Many forms: Compile-time (Overload) vs Runtime (Override)│
└─────────────────┴─────────────────────────────────────────────────────────┘
```

### Dynamic Method Dispatch (Runtime Polymorphism)
```java
class SuperClass {
    void display() { System.out.println("SuperClass"); }
}
class SubClass extends SuperClass {
    @Override
    void display() { System.out.println("SubClass"); }
}
// In Main:
SuperClass obj = new SubClass();
obj.display(); // Prints "SubClass" at runtime via Virtual Method Table (vtable)
```

---

## 2. SOLID PRINCIPLES QUICK REFERENCE
* **S - Single Responsibility Principle:** A class should have one, and only one, reason to change.
* **O - Open/Closed Principle:** Open for extension, closed for modification.
* **L - Liskov Substitution Principle:** Derived classes must be substitutable for their base classes without altering program correctness.
* **I - Interface Segregation Principle:** Many client-specific interfaces are better than one general-purpose interface.
* **D - Dependency Inversion Principle:** Depend on abstractions, not concretions.

---

## 3. JAVA INTERNALS & MEMORY ARCHITECTURE

### JVM Memory Organization
```text
┌────────────────────────────────────────────────────────┐
│ JVM Memory                                             │
│ ┌───────────────────────────┬────────────────────────┐ │
│ │ Heap Space (All Threads)  │ Non-Heap / Native      │ │
│ │ - Young Gen (Eden, S0, S1)│ - Metaspace (Java 8+)  │ │
│ │ - Old (Tenured) Gen       │   (Class metadata)     │ │
│ └───────────────────────────┴────────────────────────┘ │
│ ┌───────────────────────────┬────────────────────────┐ │
│ │ Thread Stacks (Per-Thread)│ PC Registers & Native   │ │
│ │ - Method Frames           │ Method Stacks          │ │
│ │ - Local Variables         │                        │ │
│ └───────────────────────────┴────────────────────────┘ │
└────────────────────────────────────────────────────────┘
```
* **Java 8 Change:** `PermGen` was completely removed and replaced by `Metaspace`, which grows dynamically in native OS memory.
* **Garbage Collection (GC):** Tracks reachable objects via Root references; sweeps unreachable objects. Common collectors: G1, ZGC, ParallelGC.

---

## 4. C++ SPECIFICS & DIAMOND PROBLEM

### Diamond Problem Resolution via Virtual Base Class
```text
      Class A (Base)
       /         \\
 Class B          Class C
 (virtual A)      (virtual A)
       \\         /
      Class D (Derived)
```
```cpp
class A { public: int val; };
class B : virtual public A { };
class C : virtual public A { };
class D : public B, public C { }; // Only ONE copy of A::val exists in D!
```

---

## 5. DESIGN PATTERNS QUICK CLASSIFICATION

| Category | Pattern | Purpose |
| :--- | :--- | :--- |
| **Creational** | **Singleton** | Ensures exactly one instance exists with a global access point |
| | **Factory Method** | Defines interface for creating objects; subclasses decide which class to instantiate |
| | **Builder** | Constructs complex objects step-by-step |
| **Structural** | **Adapter** | Allows incompatible interfaces to work together |
| | **Decorator** | Dynamically attaches additional responsibilities to an object |
| | **Proxy** | Provides a surrogate/placeholder for another object to control access |
| **Behavioral** | **Observer** | One-to-many dependency; notifies dependents automatically upon state change |
| | **Strategy** | Encapsulates a family of algorithms and makes them interchangeable |
| | **Command** | Encapsulates a request as an object |

---

## 6. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Abstract Class vs Interface (Java 8+):**
   * Abstract classes can have state (instance fields) and constructors.
   * Interfaces can have `default` and `static` methods, but fields are always `public static final`.
2. **`final` Keyword in Java:**
   * Final variable: Constant (cannot reassign).
   * Final method: Cannot be overridden.
   * Final class: Cannot be inherited.
3. **C++ Pointers vs References:** A reference must be initialized upon declaration and cannot be null; a pointer can be null and reassigned.

### COMMON TRAPS
* ⚠️ **Trap 1:** Overloading vs Overriding. Overloading happens at **compile-time** within the same class (same name, different parameters); Overriding happens at **runtime** between parent/child classes (same name and exact same signature).
* ⚠️ **Trap 2:** Thinking `finally` block in Java never executes. It executes almost always, except if `System.exit(0)` is called or JVM crashes.
"""

with open("data/revision/programming/programming-revision.md", "w", encoding="utf-8") as f:
    f.write(PROGRAMMING_MD)
print("Wrote data/revision/programming/programming-revision.md")

