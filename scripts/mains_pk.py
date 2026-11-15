"""
IBPS SO IT Officer Mains - Professional Knowledge Section (60 Questions)
"""

MAINS_PK_QUESTIONS = [
    # 1. Computer Architecture & Hardware (5 Qs)
    {
        "q": (
            "In a 5-stage instruction pipeline consisting of IF, ID, EX, MEM, and WB stages, "
            "which type of hazard occurs when an instruction depends on the result of a previous "
            "instruction that has not yet completed execution, and how is it most efficiently resolved in hardware without inserting pipeline stalls?"
        ),
        "options": [
            "Data hazard; resolved via operand forwarding (data bypassing)",
            "Structural hazard; resolved via branch prediction logic",
            "Control hazard; resolved via delayed branching",
            "Data hazard; resolved by increasing clock frequency"
        ],
        "answer": 0,
        "topic": "Computer Architecture",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "A computer system features a 2-way set-associative cache with 64 KB total capacity and 64-byte cache line size. "
            "If the main memory uses 32-bit byte addresses, how many bits are used for the Tag, Set Index, and Block Offset fields respectively?"
        ),
        "options": [
            "Tag = 17 bits, Set Index = 9 bits, Offset = 6 bits",
            "Tag = 18 bits, Set Index = 8 bits, Offset = 6 bits",
            "Tag = 16 bits, Set Index = 10 bits, Offset = 6 bits",
            "Tag = 20 bits, Set Index = 6 bits, Offset = 6 bits"
        ],
        "answer": 0,
        "topic": "Computer Architecture",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "According to Flynn's taxonomy of computer architectures, which class represents modern Graphics Processing Units (GPUs) "
            "and SIMD vector extensions where a single instruction operates concurrently across multiple data streams?"
        ),
        "options": [
            "Single Instruction, Multiple Data (SIMD)",
            "Multiple Instruction, Single Data (MISD)",
            "Single Instruction, Single Data (SISD)",
            "Multiple Instruction, Multiple Data (MIMD)"
        ],
        "answer": 0,
        "topic": "Computer Architecture",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In interrupt-driven I/O processing, what is the primary technical distinction between a vectored interrupt and a non-vectored interrupt?"
        ),
        "options": [
            "In vectored interrupts, the interrupting device directly supplies the interrupt vector address to the CPU, whereas in non-vectored interrupts, the CPU branches to a fixed address and polls devices",
            "Vectored interrupts cannot be masked by software, whereas non-vectored interrupts are always maskable",
            "Non-vectored interrupts use Direct Memory Access (DMA), while vectored interrupts require programmed I/O",
            "Vectored interrupts are generated only by software exceptions, whereas non-vectored interrupts are strictly hardware-driven"
        ],
        "answer": 0,
        "topic": "Computer Architecture",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In IEEE 754 single-precision (32-bit) floating-point representation, what are the bit allocations for Sign, Biased Exponent, and Mantissa (Fraction), and what is the bias value used for the exponent?"
        ),
        "options": [
            "Sign = 1 bit, Exponent = 8 bits, Mantissa = 23 bits, Bias = 127",
            "Sign = 1 bit, Exponent = 11 bits, Mantissa = 20 bits, Bias = 1023",
            "Sign = 1 bit, Exponent = 7 bits, Mantissa = 24 bits, Bias = 63",
            "Sign = 2 bits, Exponent = 8 bits, Mantissa = 22 bits, Bias = 128"
        ],
        "answer": 0,
        "topic": "Computer Architecture",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 2. Operating Systems (5 Qs)
    {
        "q": (
            "In the context of deadlock avoidance, Dijkstra's Banker's Algorithm determines whether granting a resource request leaves the system in a 'safe state'. "
            "A state is considered safe if and only if:"
        ),
        "options": [
            "There exists at least one safe execution sequence of processes such that every process can satisfy its maximum resource claims",
            "The total number of available resource instances exceeds the total requested resources of all running processes combined",
            "No process holds a shared resource while simultaneously requesting an exclusive lock",
            "Every resource type has exactly one instance currently unassigned in physical memory"
        ],
        "answer": 0,
        "topic": "Operating Systems",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which CPU scheduling phenomenon occurs under First-Come-First-Served (FCFS) scheduling where multiple I/O-bound processes "
            "are forced to wait for long periods behind a single long CPU-burst process, resulting in poor CPU and device utilization?"
        ),
        "options": [
            "Convoy effect",
            "Starvation anomaly",
            "Priority inversion",
            "Thrashing cascade"
        ],
        "answer": 0,
        "topic": "Operating Systems",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In virtual memory management, Belady's Anomaly describes a counter-intuitive situation where increasing the number of page frames "
            "results in an increased number of page faults. Under which page replacement algorithm is Belady's Anomaly observed?"
        ),
        "options": [
            "First-In, First-Out (FIFO)",
            "Least Recently Used (LRU)",
            "Optimal Page Replacement (OPT)",
            "Least Frequently Used (LFU)"
        ],
        "answer": 0,
        "topic": "Operating Systems",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Consider a counting semaphore S initialized to the value 7. If 12 wait() (P) operations and 8 signal() (V) operations "
            "are executed on S, what will be the resulting value of S?"
        ),
        "options": [
            "3",
            "4",
            "1",
            "2"
        ],
        "answer": 0,
        "topic": "Operating Systems",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In a Unix/Linux ext4 file system, what information is NOT stored directly inside an inode data structure?"
        ),
        "options": [
            "The filename of the file",
            "File access permissions (mode)",
            "Direct and indirect disk block pointers",
            "File size and modification timestamps"
        ],
        "answer": 0,
        "topic": "Operating Systems",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 3. DBMS & SQL (6 Qs)
    {
        "q": (
            "A relation R(A, B, C, D) has the following functional dependencies: A -> B, B -> C, and C -> D. "
            "If the primary key of relation R is A, in which normal form does relation R currently reside?"
        ),
        "options": [
            "Second Normal Form (2NF)",
            "Third Normal Form (3NF)",
            "Boyce-Codd Normal Form (BCNF)",
            "First Normal Form (1NF)"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In database transaction processing, which schedule property guarantees that if a transaction T_j reads a value written by T_i, "
            "then T_i must commit before T_j reads that value, thereby eliminating cascading rollbacks entirely?"
        ),
        "options": [
            "Cascadeless schedule",
            "Recoverable schedule",
            "Conflict serializable schedule",
            "View serializable schedule"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In a B+ Tree index of order m (where m is the maximum number of pointers in an internal node), "
            "which of the following architectural properties is TRUE?"
        ),
        "options": [
            "All data records or key-pointer pairs reside exclusively in the leaf nodes, which are linked together in a doubly linked list",
            "Internal nodes store data record pointers alongside keys to minimize tree height",
            "Leaf nodes may appear at different depths depending on insertion order",
            "A leaf node cannot have fewer than m keys under any circumstances"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Consider the SQL query:\n"
            "SELECT emp_id, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank_val FROM employees;\n\n"
            "If three employees share the highest salary of 90,000 and the next highest salary is 80,000, "
            "what rank value will be assigned to the employee earning 80,000 by DENSE_RANK() vs RANK()?"
        ),
        "options": [
            "DENSE_RANK assigns 2; RANK assigns 4",
            "DENSE_RANK assigns 4; RANK assigns 2",
            "Both DENSE_RANK and RANK assign 4",
            "DENSE_RANK assigns 2; RANK assigns 2"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Under the ANSI SQL standard isolation levels, which transaction anomaly is prevented by REPEATABLE READ "
            "that is NOT prevented by READ COMMITTED?"
        ),
        "options": [
            "Non-repeatable (Fuzzy) read",
            "Dirty read",
            "Phantom read",
            "Lost update"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In relational algebra, which fundamental operation produces a relation containing all tuples that are in relation R "
            "but NOT in relation S, provided R and S are union-compatible?"
        ),
        "options": [
            "Set Difference (R - S)",
            "Cartesian Product (R x S)",
            "Intersection (R ∩ S)",
            "Division (R ÷ S)"
        ],
        "answer": 0,
        "topic": "DBMS & SQL",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 4. Data Structures & Algorithms (6 Qs)
    {
        "q": (
            "Using the Master Theorem, what is the asymptotic time complexity of the recurrence relation: "
            "T(n) = 4T(n/2) + O(n²) ?"
        ),
        "options": [
            "Θ(n² log n)",
            "Θ(n²)",
            "Θ(n log n)",
            "Θ(n³)"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In an AVL tree, after inserting an element into the left subtree of the right child of a node, "
            "which type of rotation sequence must be performed to restore the balance factor of the violated node?"
        ),
        "options": [
            "Right-Left (RL) double rotation",
            "Left-Right (LR) double rotation",
            "Single Left (LL) rotation",
            "Single Right (RR) rotation"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Why is Bellman-Ford algorithm preferred over Dijkstra's algorithm for finding single-source shortest paths in certain weighted directed graphs?"
        ),
        "options": [
            "Bellman-Ford can correctly handle graphs with negative edge weights and detect negative-weight cycles, whereas Dijkstra's algorithm fails",
            "Bellman-Ford operates in O(V log V + E) time, which is strictly faster than Dijkstra's algorithm",
            "Bellman-Ford works exclusively on Directed Acyclic Graphs (DAGs) without using priority queues",
            "Dijkstra requires memory proportional to O(V²), making it inapplicable to sparse networks"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the theoretical lower bound for the number of key comparisons required in the worst case "
            "to sort an array of n arbitrary elements using any comparison-based sorting algorithm?"
        ),
        "options": [
            "Ω(n log₂ n)",
            "Ω(n²)",
            "Ω(n)",
            "Ω(log₂ n)"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In a hash table utilizing open addressing with linear probing, what is the primary structural drawback that causes "
            "consecutive occupied slots to form long contiguous blocks, thereby significantly degrading search performance?"
        ),
        "options": [
            "Primary clustering",
            "Secondary clustering",
            "Dynamic thrashing",
            "Chaining fragmentation"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the space complexity of the optimal Dynamic Programming tabular approach for finding the length of the "
            "Longest Common Subsequence (LCS) between two strings of lengths m and n?"
        ),
        "options": [
            "O(m × n), which can be optimized to O(min(m, n)) if only the length is required",
            "O(2^(m+n)) exponential space in all implementations",
            "O(m + n) strictly without possibility of reduction",
            "O(1) constant auxiliary space"
        ],
        "answer": 0,
        "topic": "Data Structures & Algorithms",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 5. Computer Networks (6 Qs)
    {
        "q": (
            "During the TCP connection termination handshake, which state must the active closer transition into "
            "after sending the final ACK segment, and what is the standard duration it remains in that state before completely releasing socket resources?"
        ),
        "options": [
            "TIME_WAIT state, lasting 2 × Maximum Segment Lifetime (2MSL)",
            "CLOSE_WAIT state, lasting 1 × Maximum Segment Lifetime (1MSL)",
            "FIN_WAIT_2 state, lasting indefinitely until keep-alive timer expires",
            "LAST_ACK state, lasting 30 seconds"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "An enterprise organization is assigned the IPv4 network block 192.168.10.0/24. "
            "The network engineer needs to carve out subnets to support at least 28 usable host IP addresses per subnet. "
            "What subnet mask should be assigned, and how many valid subnets can be created?"
        ),
        "options": [
            "255.255.255.224 (/27), providing 8 subnets with 30 usable hosts each",
            "255.255.255.240 (/28), providing 16 subnets with 14 usable hosts each",
            "255.255.255.192 (/26), providing 4 subnets with 62 usable hosts each",
            "255.255.255.248 (/29), providing 32 subnets with 6 usable hosts each"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In TCP congestion control (Tahoe and Reno), when a transmission timeout occurs (coarse timer expiry), "
            "how do the Slow Start Threshold (ssthresh) and Congestion Window (cwnd) adapt?"
        ),
        "options": [
            "ssthresh is set to max(FlightSize/2, 2*SMSS) and cwnd is reset to 1 SMSS (entering Slow Start)",
            "cwnd is halved and ssthresh remains unchanged (entering Fast Recovery)",
            "cwnd is set to ssthresh and increases exponentially",
            "ssthresh is doubled and cwnd is reduced to zero"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which of the following routing protocols is classified as an Exterior Gateway Protocol (EGP) based on "
            "Path Vector mechanics, operating over TCP port 179 to exchange reachability information across Autonomous Systems (AS)?"
        ),
        "options": [
            "Border Gateway Protocol (BGP)",
            "Open Shortest Path First (OSPF)",
            "Routing Information Protocol (RIP)",
            "Intermediate System to Intermediate System (IS-IS)"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the maximum sender window size in a Selective Repeat sliding window protocol if sequence numbers "
            "are represented using n bits, in order to avoid ambiguity between new frames and retransmitted duplicate frames?"
        ),
        "options": [
            "2^(n-1)",
            "2^n - 1",
            "2^n",
            "2^(n+1)"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the primary role of the Address Resolution Protocol (ARP) in the TCP/IP network protocol stack?"
        ),
        "options": [
            "To resolve a known logical IPv4 address to its corresponding physical MAC address on a local area network",
            "To map a physical MAC address to an assigned logical IPv4 address upon system boot",
            "To translate human-readable domain names into routable public IP addresses",
            "To dynamically allocate private IP addresses to newly connected DHCP clients"
        ],
        "answer": 0,
        "topic": "Computer Networks",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 6. Software Engineering & SDLC (4 Qs)
    {
        "q": (
            "In Scrum Agile methodology, which ceremony is held at the conclusion of a sprint specifically for the team "
            "to inspect its internal processes, collaboration dynamics, and engineering practices in order to plan quality and process improvements?"
        ),
        "options": [
            "Sprint Retrospective",
            "Sprint Review",
            "Daily Standup",
            "Backlog Refinement"
        ],
        "answer": 0,
        "topic": "Software Engineering",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In McCabe's Cyclomatic Complexity metric, given a control flow graph G with E edges, N nodes, and P connected components, "
            "what is the formula used to calculate the cyclomatic complexity V(G) to determine the number of independent basis paths?"
        ),
        "options": [
            "V(G) = E - N + 2P",
            "V(G) = E + N - 2P",
            "V(G) = E - N + P",
            "V(G) = 2E - N + P"
        ],
        "answer": 0,
        "topic": "Software Engineering",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In Basic COCOMO software cost estimation, which development mode corresponds to small software teams working "
            "in familiar, in-house environments with relaxed requirements and experienced developers?"
        ),
        "options": [
            "Organic mode",
            "Semidetached mode",
            "Embedded mode",
            "Agile iterative mode"
        ],
        "answer": 0,
        "topic": "Software Engineering",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which Gang of Four (GoF) design pattern defines a one-to-many dependency between objects such that when one object "
            "changes its state, all its registered dependents are notified and updated automatically?"
        ),
        "options": [
            "Observer Pattern",
            "Singleton Pattern",
            "Adapter Pattern",
            "Factory Method Pattern"
        ],
        "answer": 0,
        "topic": "Software Engineering",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 7. OOP & Programming (C/C++ & Java) (5 Qs)
    {
        "q": (
            "In Java Virtual Machine (JVM) memory architecture, where are class metadata, method bytecode, runtime constant pools, "
            "and static variables stored in Java 8 and subsequent versions?"
        ),
        "options": [
            "Metaspace (native memory)",
            "Permanent Generation (PermGen)",
            "JVM Stack frame",
            "Thread Local Storage"
        ],
        "answer": 0,
        "topic": "OOP & Programming",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In C++, how is the classic 'Diamond Problem' of multiple inheritance (where two derived classes inherit from a common base class, "
            "and a final class inherits from both derived classes) resolved to prevent duplicate base class instances?"
        ),
        "options": [
            "By declaring the common base class as 'virtual' during inheritance in the intermediate derived classes",
            "By declaring all member functions of the base class as 'static'",
            "By overloading the assignment operator in the most derived class",
            "By marking the most derived class with the 'final' specifier"
        ],
        "answer": 0,
        "topic": "OOP & Programming",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In Java, what happens during dynamic method dispatch (runtime polymorphism) when a superclass reference variable "
            "invokes an overridden method on a subclass instance?"
        ),
        "options": [
            "The JVM looks up the method implementation at runtime using the instance's virtual method table (vtable) and executes the subclass version",
            "The compiler binds the method call at compile time based strictly on the reference type",
            "The JVM throws an IllegalAccessError unless explicitly cast to the subclass type",
            "The superclass method executes first, followed automatically by the subclass method"
        ],
        "answer": 0,
        "topic": "OOP & Programming",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Since Java 8, interfaces can contain non-abstract method implementations. Which keyword must be used to declare "
            "an interface method with a default implementation that implementing classes may inherit or override?"
        ),
        "options": [
            "default",
            "virtual",
            "concrete",
            "native"
        ],
        "answer": 0,
        "topic": "OOP & Programming",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In Java exception handling, what requirement must an object meet to be declared within the parentheses of a "
            "try-with-resources statement to guarantee automatic resource deallocation?"
        ),
        "options": [
            "It must implement either java.lang.AutoCloseable or java.io.Closeable interface",
            "It must be declared with the 'transient' modifier",
            "It must extend java.lang.Throwable",
            "It must be annotated with @FunctionalInterface"
        ],
        "answer": 0,
        "topic": "OOP & Programming",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 8. Web Technologies & API (4 Qs)
    {
        "q": (
            "Which of the following is NOT an architectural constraint of the Representational State Transfer (REST) architectural style as defined by Roy Fielding?"
        ),
        "options": [
            "Stateful Session Management on Server",
            "Stateless Interactions",
            "Client-Server Separation",
            "Uniform Interface"
        ],
        "answer": 0,
        "topic": "Web Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the semantic difference between HTTP status code 401 (Unauthorized) and HTTP status code 403 (Forbidden)?"
        ),
        "options": [
            "401 indicates authentication credentials are required or have failed verification, whereas 403 indicates the client is authenticated but lacks required permissions for the resource",
            "401 applies exclusively to HTTPS connections, whereas 403 applies exclusively to plain HTTP",
            "401 indicates a server-side runtime error, whereas 403 indicates a client-side invalid payload format",
            "401 indicates temporary rate limiting, whereas 403 indicates the resource has been permanently moved"
        ],
        "answer": 0,
        "topic": "Web Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "A JSON Web Token (JWT) comprises three Base64URL-encoded segments separated by periods. What are these three segments in sequence?"
        ),
        "options": [
            "Header . Payload . Signature",
            "Metadata . Claims . Certificate",
            "Token . Body . Hash",
            "Algorithm . Ciphertext . Digest"
        ],
        "answer": 0,
        "topic": "Web Technologies",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "During Cross-Origin Resource Sharing (CORS), when a web client makes a non-simple cross-origin HTTP request (e.g., using PUT or custom headers), "
            "what preflight HTTP request method is automatically dispatched by the browser before the actual request?"
        ),
        "options": [
            "OPTIONS",
            "HEAD",
            "TRACE",
            "CONNECT"
        ],
        "answer": 0,
        "topic": "Web Technologies",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 9. Information Security & Cryptography (5 Qs)
    {
        "q": (
            "In modern symmetric cryptography, Advanced Encryption Standard (AES) operates on fixed 128-bit blocks using key lengths of:"
        ),
        "options": [
            "128, 192, or 256 bits with 10, 12, or 14 transformation rounds respectively",
            "64, 128, or 256 bits with 8, 10, or 12 transformation rounds respectively",
            "128, 256, or 512 bits with 16, 20, or 24 transformation rounds respectively",
            "256 bits exclusively with 16 transformation rounds"
        ],
        "answer": 0,
        "topic": "Cyber Security",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In public-key cryptography and digital signatures, what ensures both the integrity of the transmitted message "
            "and the non-repudiation of the sender?"
        ),
        "options": [
            "The sender encrypts the cryptographic hash of the message using their private key",
            "The sender encrypts the entire plaintext message using the recipient's public key",
            "The recipient computes a checksum and transmits their shared symmetric key back to the sender",
            "The sender prepends an unencrypted timestamp and salt to the ciphertext"
        ],
        "answer": 0,
        "topic": "Cyber Security",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which web application attack involves an attacker tricking an authenticated victim's web browser into executing "
            "an unauthorized action on a trusted web application where the victim is currently authenticated, commonly mitigated by Anti-CSRF Synchronizer Tokens?"
        ),
        "options": [
            "Cross-Site Request Forgery (CSRF)",
            "Cross-Site Scripting (XSS)",
            "Structured Query Language Injection (SQLi)",
            "Server-Side Request Forgery (SSRF)"
        ],
        "answer": 0,
        "topic": "Cyber Security",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What mathematical property must a cryptographic hash function satisfy to ensure that it is computationally infeasible "
            "to find ANY two distinct input messages m1 and m2 such that Hash(m1) = Hash(m2)?"
        ),
        "options": [
            "Collision resistance",
            "Pre-image resistance (One-way property)",
            "Second pre-image resistance (Weak collision resistance)",
            "Pseudorandom permutation property"
        ],
        "answer": 0,
        "topic": "Cyber Security",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which foundational security tenet defines the 'Zero Trust' security architecture framework mandated in modern banking infrastructure?"
        ),
        "options": [
            "'Never Trust, Always Verify' across all users, devices, applications, and data packets regardless of network location",
            "Implicit trust is granted to all traffic originating within the corporate intranet perimeter",
            "Security verification is enforced only during initial login and disabled for active sessions",
            "Air-gapped physical servers are exempt from periodic credential rotation"
        ],
        "answer": 0,
        "topic": "Cyber Security",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 10. Cloud Computing & Virtualization (4 Qs)
    {
        "q": (
            "In cloud computing, what is the core difference between a Type-1 (Bare Metal) Hypervisor and a Type-2 (Hosted) Hypervisor?"
        ),
        "options": [
            "Type-1 hypervisors run directly on the physical hardware without an underlying host OS, whereas Type-2 hypervisors execute on top of an existing host OS",
            "Type-1 hypervisors support only containerized workloads, whereas Type-2 hypervisors support full hardware virtualization",
            "Type-1 hypervisors cannot manage multicore processors, whereas Type-2 hypervisors support unlimited CPU cores",
            "Type-2 hypervisors offer significantly lower virtualization latency than Type-1 hypervisors"
        ],
        "answer": 0,
        "topic": "Cloud Computing",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Under the Cloud Shared Responsibility Model for Platform as a Service (PaaS), which layer is typically managed by the cloud service provider rather than the enterprise customer?"
        ),
        "options": [
            "Operating System patching, middleware runtime, and server hardware infrastructure",
            "Application code, custom business logic, and database user schema",
            "Customer data access control and role-based permissions",
            "Client endpoint device configuration and local network firewall"
        ],
        "answer": 0,
        "topic": "Cloud Computing",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which Linux kernel features provide resource isolation (CPU, memory, network, process tree) that enable lightweight containerization engines such as Docker to operate without full guest OS hypervisors?"
        ),
        "options": [
            "Control Groups (cgroups) and Namespaces",
            "KVM and QEMU hardware emulators",
            "SELinux policy modules and AppArmor profiles only",
            "Virtual Network Interface Cards and eBPF filters"
        ],
        "answer": 0,
        "topic": "Cloud Computing",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which cloud storage type stores data as distinct objects containing data payload, unique identifier, and customizable metadata, accessed over standard REST APIs (e.g., HTTP GET/PUT), making it ideal for unstructured big data?"
        ),
        "options": [
            "Object Storage",
            "Block Storage",
            "Network File System (NFS) Storage",
            "Storage Area Network (SAN) Raw Volume"
        ],
        "answer": 0,
        "topic": "Cloud Computing",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 11. Emerging Technologies (AI/ML, Big Data, Blockchain) (5 Qs)
    {
        "q": (
            "In supervised machine learning, how does high model variance typically manifest, and what is the standard mathematical mitigation?"
        ),
        "options": [
            "Overfitting on training data with poor test generalization; mitigated by regularization (L1/L2), cross-validation, and pruning",
            "Underfitting with high bias on training data; mitigated by simplifying the model architecture",
            "Inability to converge during gradient descent; mitigated by increasing the learning rate",
            "Complete saturation of weights; mitigated by removing hidden layers"
        ],
        "answer": 0,
        "topic": "Emerging Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Why is the Rectified Linear Unit (ReLU) activation function f(x) = max(0, x) widely preferred over the Sigmoid function "
            "in hidden layers of deep neural networks?"
        ),
        "options": [
            "It mitigates the vanishing gradient problem for positive inputs and requires significantly less computational overhead",
            "It strictly constrains output values to a symmetric range between -1 and +1",
            "It is continuously differentiable across all real numbers including zero",
            "It prevents dead neurons under all negative input conditions automatically"
        ],
        "answer": 0,
        "topic": "Emerging Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In Apache Hadoop Distributed File System (HDFS), what is the primary role of the NameNode?"
        ),
        "options": [
            "To maintain the filesystem directory tree and metadata mapping of data blocks to physical DataNodes in memory",
            "To physically store and serve file data blocks and handle disk I/O requests directly from clients",
            "To execute Map and Reduce computation tasks on cluster worker nodes",
            "To replace failed disk drives automatically using hardware RAID controller logic"
        ],
        "answer": 0,
        "topic": "Emerging Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In blockchain distributed ledger technology, which vulnerability allows an entity or mining cartel controlling "
            "more than 50% of the network hash rate to rewrite transaction history and perform double-spending attacks?"
        ),
        "options": [
            "51% Attack (Majority attack)",
            "Sybil Attack",
            "Eclipse Attack",
            "Reentrancy Attack"
        ],
        "answer": 0,
        "topic": "Emerging Technologies",
        "difficulty": "Easy",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Which lightweight, publish-subscribe network protocol designed for constrained IoT devices and low-bandwidth networks "
            "runs over TCP and utilizes a central broker to manage message topics?"
        ),
        "options": [
            "MQTT (Message Queuing Telemetry Transport)",
            "CoAP (Constrained Application Protocol)",
            "AMQP (Advanced Message Queuing Protocol)",
            "XMPP (Extensible Messaging and Presence Protocol)"
        ],
        "answer": 0,
        "topic": "Emerging Technologies",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },

    # 12. Banking Technology, Digital Payments & IT Governance (5 Qs)
    {
        "q": (
            "In India's Unified Payments Interface (UPI) ecosystem managed by NPCI, what technical entity functions as the "
            "central transaction routing switch, connecting PSP bank applications to issuing Core Banking Systems (CBS)?"
        ),
        "options": [
            "National Financial Switch (NFS) / Unified Payments Interface Switch",
            "Immediate Payment Service (IMPS) ATM Switch only",
            "Reserve Bank Information Technology (ReBIT) Gateway",
            "Clearing Corporation of India Limited (CCIL) Settlement Terminal"
        ],
        "answer": 0,
        "topic": "Banking Technology",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "What is the key settlement difference between the National Electronic Funds Transfer (NEFT) system and the "
            "Real Time Gross Settlement (RTGS) system operating under Reserve Bank of India oversight?"
        ),
        "options": [
            "NEFT settles fund transfers in half-hourly batches on a net settlement basis, whereas RTGS processes and settles each transaction continuously on an individual gross basis",
            "NEFT operates strictly for transactions exceeding Rs. 2 Lakhs, whereas RTGS has no minimum limit",
            "NEFT is available only during banking branch hours, whereas RTGS operates 24x7x365",
            "RTGS transactions can be revoked within 15 minutes of initiation, whereas NEFT is irrevocable"
        ],
        "answer": 0,
        "topic": "Banking Technology",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "In global and domestic financial interbank electronic messaging, which standard provides a rich, XML/JSON-based "
            "data dictionary to replace legacy ISO 8583 and MT format telegraphic financial messages?"
        ),
        "options": [
            "ISO 20022",
            "ISO 27001",
            "ISO 9001",
            "ISO 31000"
        ],
        "answer": 0,
        "topic": "Banking Technology",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "Under the Reserve Bank of India (RBI) Cyber Security Framework for Banks, what is the mandatory requirement "
            "regarding the reporting of critical cybersecurity incidents to the regulator?"
        ),
        "options": [
            "Banks must report all critical cybersecurity incidents to the RBI / CERT-In within 2 to 6 hours of detection",
            "Incidents must be compiled and submitted solely in the quarterly audit review",
            "Incident notification is voluntary for non-scheduled cooperative banks",
            "Reporting is required only if monetary financial loss exceeds Rs. 10 Crores"
        ],
        "answer": 0,
        "topic": "Banking Technology",
        "difficulty": "Hard",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    },
    {
        "q": (
            "According to the Payment Card Industry Data Security Standard (PCI-DSS), which of the following sensitive authentication data (SAD) "
            "must NEVER be stored by an acquiring merchant or payment gateway post-authorization under any circumstances, even if encrypted?"
        ),
        "options": [
            "Full magnetic stripe data (track 2) or Card Verification Value (CVV/CVC)",
            "Cardholder Name",
            "Primary Account Number (PAN)",
            "Card Expiration Date"
        ],
        "answer": 0,
        "topic": "Banking Technology",
        "difficulty": "Moderate",
        "sourceType": "SYLLABUS_BASED_PRACTICE"
    }
]

