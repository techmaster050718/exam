"""
Generates:
1. data/revision/algorithms/algorithms-revision.md
2. data/revision/algorithms/complexity-revision.md
3. data/revision/aptitude/number-tables.md
"""
import os

os.makedirs("data/revision/algorithms", exist_ok=True)
os.makedirs("data/revision/aptitude", exist_ok=True)

# 1. algorithms-revision.md
ALGORITHMS_MD = """# Algorithms – Searching & Sorting Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## MASTER COMPARISON TABLE: SORTING ALGORITHMS

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? | In-Place? | Key Design Method |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Yes** | **Yes** | Brute Force / Exchange |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **No** | **Yes** | Selection (min element) |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Yes** | **Yes** | Incremental Insertion |
| **Merge Sort** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n \\log n)$ | $O(n)$ | **Yes** | **No** | Divide and Conquer |
| **Quick Sort** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n^2)$ | $O(\\log n)$ | **No** | **Yes** | Divide and Conquer (Pivot) |
| **Heap Sort** | $O(n \\log n)$ | $O(n \\log n)$ | $O(n \\log n)$ | $O(1)$ | **No** | **Yes** | Heap Priority Queue |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | **Yes** | **No** | Non-comparison (Frequency) |
| **Radix Sort** | $O(d(n + k))$ | $O(d(n + k))$ | $O(d(n + k))$ | $O(n + k)$ | **Yes** | **No** | Non-comparison (Digit-by-digit) |
| **Bucket Sort** | $O(n + k)$ | $O(n)$ | $O(n^2)$ | $O(n + k)$ | **Yes** | **No** | Distribution / Scatter-Gather |

---

## 1. SEARCHING ALGORITHMS

### 1.1 Linear Search
* **Core Idea:** Sequentially scan each element from index 0 to $n-1$ until target is found or list ends.
* **Applicability:** Any collection (sorted, unsorted, linked lists, arrays).
* **Complexities:** Best: $O(1)$ (target at index 0), Average: $O(n)$, Worst: $O(n)$, Auxiliary Space: $O(1)$.
* **When to Prefer:** Small arrays ($n < 20$), unsorted lists where sorting overhead is prohibitive.

### 1.2 Binary Search
* **Core Idea:** Divide-and-conquer on **sorted** random-access array. Compare key with middle element; eliminate half the search space in each step.
```text
Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], Target = 23
Step 1: Low = 0, High = 9, Mid = 4 (val=16) -> 23 > 16 -> Low = 5
Step 2: Low = 5, High = 9, Mid = 7 (val=56) -> 23 < 56 -> High = 6
Step 3: Low = 5, High = 6, Mid = 5 (val=23) -> Found at index 5!
```
* **Recurrence:** $T(n) = T(n/2) + O(1) \\implies O(\\log n)$.
* **Complexities:** Best: $O(1)$, Average: $O(\\log n)$, Worst: $O(\\log n)$, Auxiliary Space: Iterative $O(1)$, Recursive $O(\\log n)$.
* **Trap:** Fails on singly linked lists (cannot access middle in $O(1)$ time). Integer overflow trap: use `mid = low + (high - low) / 2`.

### 1.3 Hash-Based Search
* **Core Idea:** Direct lookup using hash function $h(k)$ mapping keys to bucket indices.
* **Complexities:** Best: $O(1)$, Average: $O(1)$, Worst: $O(n)$ (all keys collide into same slot).
* **Space:** $O(n)$.

### 1.4 Breadth-First Search (BFS)
* **Core Idea:** Level-by-level graph/tree traversal using a FIFO **Queue**. Finds the shortest path in unweighted graphs.
* **Complexities:** Time: $O(V + E)$, Space: $O(V)$ (queue can hold an entire level).

### 1.5 Depth-First Search (DFS)
* **Core Idea:** Explores as deep as possible along each branch before backtracking using a **Stack** (or recursion).
* **Complexities:** Time: $O(V + E)$, Space: $O(V)$ (recursion stack equal to graph diameter).

---

## 2. SORTING ALGORITHMS (STEP-BY-STEP EXAMPLES)

### 2.1 Bubble Sort
* **Mechanism:** Repeatedly swap adjacent elements if they are out of order. Largest unsorted element bubbles to the end in each pass.
```text
Pass 1 on [5, 2, 4, 1]:
Compare (5, 2) -> swap -> [2, 5, 4, 1]
Compare (5, 4) -> swap -> [2, 4, 5, 1]
Compare (5, 1) -> swap -> [2, 4, 1, 5]  (5 is in place!)
Pass 2:
Compare (2, 4) -> ok   -> [2, 4, 1, 5]
Compare (4, 1) -> swap -> [2, 1, 4, 5]  (4 is in place!)
Pass 3:
Compare (2, 1) -> swap -> [1, 2, 4, 5]  (Sorted!)
```
* **Optimization:** If no swaps occur in a pass, break early $\\implies$ Best case $O(n)$.

### 2.2 Selection Sort
* **Mechanism:** Find the minimum element in unsorted subarray and swap it with the first unsorted position.
```text
Array: [64, 25, 12, 22, 11]
Pass 1: Min is 11 -> swap with 64 -> [11, 25, 12, 22, 64]
Pass 2: Min in [25..64] is 12 -> swap with 25 -> [11, 12, 25, 22, 64]
Pass 3: Min in [25..64] is 22 -> swap with 25 -> [11, 12, 22, 25, 64]
Pass 4: Min is 25 -> already in place -> [11, 12, 22, 25, 64]
```
* **Property:** Makes minimum number of memory writes ($O(n)$ swaps total). Ideal when writing to EEPROM/Flash memory is expensive. Unstable by default.

### 2.3 Insertion Sort
* **Mechanism:** Builds sorted array one element at a time by picking the next element and inserting it into its correct position among preceding elements.
* **Best Case:** $O(n)$ on already sorted or nearly sorted array.
* **Online Property:** Can sort a stream of numbers as they arrive. Used as the base case in hybrid algorithms (Timsort, Introsort).

### 2.4 Merge Sort
* **Mechanism:** Divide array into halves, recursively sort both, and merge the two sorted halves.
```text
        [38, 27, 43, 3, 9, 82, 10]
          /                    \\
   [38, 27, 43, 3]          [9, 82, 10]
     /        \\               /      \\
 [38, 27]   [43, 3]        [9, 82]   [10]
   Merge:
 [27, 38]   [3, 43]        [9, 82]   [10]
     \\        /               \\      /
   [3, 27, 38, 43]          [9, 10, 82]
          \\                    /
        [3, 9, 10, 27, 38, 43, 82]
```
* **Recurrence:** $T(n) = 2T(n/2) + O(n) \\implies O(n \\log n)$ in all cases.
* **Preferred For:** Linked lists ($O(1)$ extra space for merging), external sorting (huge datasets on disk).

### 2.5 Quick Sort
* **Mechanism:** Choose a pivot $P$, partition array into elements $< P$ and elements $> P$, then recurse on partitions.
* **Partition Schemes:** Lomuto (pivot at end, simpler) vs Hoare (pivots at both ends, 3x fewer swaps).
* **Worst Case ($O(n^2)$):** Occurs when pivot is consistently smallest or largest element (e.g., sorted array with first/last element as pivot).
* **Mitigation:** Randomized pivot selection or Median-of-Three pivot.

### 2.6 Heap Sort
* **Mechanism:** Build Max-Heap in $O(n)$ time. Repeatedly extract max element (root) and swap with last leaf, reduce heap size, and `heapify` root in $O(\\log n)$.
* **Advantage over Quick Sort:** Guaranteed $O(n \\log n)$ worst-case time with $O(1)$ auxiliary space. Unstable.

### 2.7 Linear (Non-Comparison) Sorting
1. **Counting Sort:** Counts occurrences of each value in range $[0..k]$. Requires $O(n + k)$ time and $O(n + k)$ space. Stable.
2. **Radix Sort:** Sorts integers digit-by-digit from least significant digit (LSD) to most significant digit (MSD) using Counting Sort as a subroutine. Time: $O(d(n + k))$.
3. **Bucket Sort:** Distributes elements into uniformly partitioned buckets, sorts each bucket individually (e.g. via Insertion Sort), and concatenates. Average time: $O(n)$.

---

## 3. COMPARISON VS NON-COMPARISON BOUNDS
* **Lower Bound of Comparison-based Sorting:** $\\Omega(n \\log_2 n)$ comparisons in worst case.
  * Proof: A comparison tree with $n!$ permutations as leaves must have height $h \\ge \\log_2(n!) = \\Theta(n \\log n)$.
* Non-comparison sorts break this lower bound because they do not rely on binary decision trees.

---

## 4. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Stability:** Preserves the relative order of duplicate elements. (Bubble, Insertion, Merge, Counting, Radix are Stable).
2. **In-place:** Uses $O(1)$ auxiliary memory beyond call stack. (Selection, Bubble, Insertion, Heap are In-place).
3. **Quick Sort Average:** $O(n \\log n)$, but worst case $O(n^2)$. Space complexity is $O(\\log n)$ due to recursion stack.
4. **Merge Sort for Linked Lists:** Preferred because nodes can be rearranged by updating pointers without extra array allocation.
5. **Selection Sort:** Minimizes write operations ($O(n)$ swaps total).

### COMMON TRAPS
* ⚠️ **Trap 1:** Assuming Heap Sort is stable. It is **unstable** due to root-to-leaf swaps.
* ⚠️ **Trap 2:** Assuming Binary Search works on singly linked lists in $O(\\log n)$. It takes $O(n)$ to locate the middle element!
* ⚠️ **Trap 3:** Confusing Quick Sort best/average time with worst case. Worst case is quadratic ($O(n^2)$).
"""

with open("data/revision/algorithms/algorithms-revision.md", "w", encoding="utf-8") as f:
    f.write(ALGORITHMS_MD)
print("Wrote data/revision/algorithms/algorithms-revision.md")


# 2. complexity-revision.md
COMPLEXITY_MD = """# Algorithmic Complexity & Asymptotic Analysis
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. COMPLEXITY GROWTH HIERARCHY
From fastest (most efficient) to slowest (intractable):

```text
O(1)        Constant Time       Hash lookup, array index access
 ↓
O(log log n) Double Logarithmic  van Emde Boas tree operations
 ↓
O(log n)    Logarithmic         Binary search, BST balanced operations
 ↓
O(√n)       Square Root         Trial division for primality
 ↓
O(n)        Linear              Linear search, single loop traversal
 ↓
O(n log n)  Linearithmic        Merge sort, Heap sort, Quick sort avg
 ↓
O(n²)       Quadratic           Bubble/Selection sort, nested loops
 ↓
O(n³)       Cubic               Matrix multiplication (naive), 3 nested loops
 ↓
O(2ⁿ)       Exponential         0/1 Knapsack recursive, Subset sum
 ↓
O(n!)       Factorial           Traveling Salesperson (brute force), Permutations
```

---

## 2. ASYMPTOTIC NOTATIONS DEFINITIONS

| Notation | Formal Definition | Graphical Meaning | Exam Meaning |
| :--- | :--- | :--- | :--- |
| **Big-O ($O$)** | $f(n) \\le c \\cdot g(n)$ for all $n \\ge n_0, c > 0$ | Asymptotic Upper Bound | "Worst-case cannot exceed this" |
| **Big-Omega ($\\Omega$)** | $f(n) \\ge c \\cdot g(n)$ for all $n \\ge n_0, c > 0$ | Asymptotic Lower Bound | "Best-case cannot be faster than this" |
| **Big-Theta ($\\Theta$)** | $c_1 g(n) \\le f(n) \\le c_2 g(n)$ for all $n \\ge n_0$ | Asymptotic Tight Bound | "Exact growth rate behavior" |
| **Little-o ($o$)** | $\\lim_{n \\to \\infty} \\frac{f(n)}{g(n)} = 0$ | Strict Upper Bound | Strictly slower growth than $g(n)$ |
| **Little-omega ($\\omega$)**| $\\lim_{n \\to \\infty} \\frac{f(n)}{g(n)} = \\infty$ | Strict Lower Bound | Strictly faster growth than $g(n)$ |

---

## 3. LOOP COMPLEXITY PATTERNS

### Pattern 1: Single Linear Loop
```c
for (int i = 0; i < n; i += c) { // O(n)
    // constant work
}
```

### Pattern 2: Multiplicative Loop
```c
for (int i = 1; i < n; i *= 2) { // O(log n)
    // runs floor(log2(n)) + 1 times
}
```

### Pattern 3: Square Root Loop
```c
for (int i = 1; i * i <= n; i++) { // O(√n)
    // runs floor(√n) times
}
```

### Pattern 4: Nested Loops with Dependent Bounds
```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        // total iterations = 1 + 2 + ... + n = n(n+1)/2 = O(n²)
    }
}
```

### Pattern 5: Harmonic Series Loop
```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j += i) {
        // total iterations = n/1 + n/2 + n/3 + ... + n/n = n * H_n = O(n log n)
    }
}
```

---

## 4. MASTER THEOREM FOR DIVIDE AND CONQUER
For recurrence: $T(n) = a T(n/b) + f(n)$ where $a \\ge 1, b > 1$:

Let critical exponent be $c = \\log_b a$:

1. **Case 1 (Leaf-heavy):** If $f(n) = O(n^{c - \\epsilon})$ for some $\\epsilon > 0$:
   $$T(n) = \\Theta(n^{\\log_b a})$$
   *Example:* $T(n) = 8T(n/2) + 1000n^2 \\implies a=8, b=2, \\log_2 8 = 3$. Since $n^2 = O(n^{3-\\epsilon})$, $T(n) = \\Theta(n^3)$.

2. **Case 2 (Balanced):** If $f(n) = \\Theta(n^c \\log^k n)$ for $k \\ge 0$:
   $$T(n) = \\Theta(n^{\\log_b a} \\log^{k+1} n)$$
   *Example (Merge Sort):* $T(n) = 2T(n/2) + O(n) \\implies \\log_2 2 = 1, k=0 \\implies T(n) = \\Theta(n \\log n)$.

3. **Case 3 (Root-heavy):** If $f(n) = \\Omega(n^{c + \\epsilon})$ and regularity condition holds ($a f(n/b) \\le d f(n)$ for $d < 1$):
   $$T(n) = \\Theta(f(n))$$
   *Example:* $T(n) = 2T(n/2) + n^2 \\implies \\log_2 2 = 1$. Since $n^2 = \\Omega(n^{1+\\epsilon})$, $T(n) = \\Theta(n^2)$.

---

## 5. COMMON RECURRENCE RELATIONS QUICK CHEAT SHEET
| Recurrence | Algorithm Example | Complexity |
| :--- | :--- | :--- |
| $T(n) = T(n-1) + O(1)$ | Sequential Search (Recursive) | $O(n)$ |
| $T(n) = T(n-1) + O(n)$ | Selection Sort, Worst QuickSort | $O(n^2)$ |
| $T(n) = 2T(n-1) + O(1)$ | Tower of Hanoi | $O(2^n)$ |
| $T(n) = T(n/2) + O(1)$ | Binary Search | $O(\\log n)$ |
| $T(n) = 2T(n/2) + O(n)$ | Merge Sort | $O(n \\log n)$ |
| $T(n) = T(n/2) + O(n)$ | Quickselect / Median-of-Medians | $O(n)$ |
| $T(n) = 2T(n/2) + O(1)$ | Tree Traversal (Binary Tree) | $O(n)$ |
| $T(n) = 7T(n/2) + O(n^2)$| Strassen's Matrix Multiplication | $O(n^{\\log_2 7}) \\approx O(n^{2.81})$|

---

## 6. 30-SECOND REVISION
* $O(1) < O(\\log n) < O(\\sqrt{n}) < O(n) < O(n \\log n) < O(n^2) < O(2^n) < O(n!)$
* If loop steps multiply or divide by constant $k$, complexity is $O(\\log_k n)$.
* Master Theorem cannot solve when $a < 1$, $b \\le 1$, or $f(n)$ is non-polynomial (e.g. $2^n$).
"""

with open("data/revision/algorithms/complexity-revision.md", "w", encoding="utf-8") as f:
    f.write(COMPLEXITY_MD)
print("Wrote data/revision/algorithms/complexity-revision.md")


# 3. number-tables.md
NUMBER_TABLES_MD = """# High-Frequency Number Tables & Speed Math Shortcuts
> **Essential Mental Arithmetic | Government Exams (IBPS, SBI, RRB, SSC, Defence)**

---

## 1. POWERS OF 2 (2⁰ to 2²⁰)
| Power | Value | Exam Relevance / Memory Hook |
| :---: | :---: | :--- |
| $2^0$ | 1 | Bit 0 |
| $2^1$ | 2 | Smallest prime |
| $2^2$ | 4 | Nibble / 2 |
| $2^3$ | 8 | 1 Byte = 8 bits |
| $2^4$ | 16 | Hexadecimal base |
| $2^5$ | 32 | IPv4 address length (32 bits) |
| $2^6$ | 64 | Standard block size (64 bytes) |
| $2^7$ | 128 | ASCII table count |
| $2^8$ | 256 | Max value of unsigned byte (0-255) |
| $2^9$ | 512 | Standard sector size (512 bytes) |
| $2^{10}$ | **1,024** | **1 Kilo (K)** in binary |
| $2^{11}$ | 2,048 | 2 K |
| $2^{12}$ | 4,096 | 4 KB standard memory page size |
| $2^{13}$ | 8,192 | 8 K |
| $2^{14}$ | 16,384 | 16 K |
| $2^{15}$ | 32,768 | Max signed 16-bit integer (32767) |
| $2^{16}$ | **65,536** | **64 KB** (Total TCP/UDP ports = 65,536) |
| $2^{17}$ | 131,072 | 128 K |
| $2^{18}$ | 262,144 | 256 K |
| $2^{19}$ | 524,288 | 512 K |
| $2^{20}$ | **1,048,576** | **1 Mega (M)** in binary (1 MB) |

---

## 2. POWERS OF 3 AND 10
| Power of 3 | Value | Power of 10 | Metric Prefix |
| :---: | :---: | :---: | :--- |
| $3^1$ | 3 | $10^1$ | Deca (da) |
| $3^2$ | 9 | $10^2$ | Hecto (h) |
| $3^3$ | 27 | $10^3$ | Kilo (k) |
| $3^4$ | 81 | $10^6$ | Mega (M) |
| $3^5$ | 243 | $10^9$ | Giga (G) |
| $3^6$ | 729 | $10^{12}$ | Tera (T) |
| $3^7$ | 2,187 | $10^{15}$ | Peta (P) |

---

## 3. SQUARES (1² to 50²)

| n | n² | n | n² | n | n² | n | n² | n | n² |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **1** | 1 | **11** | 121 | **21** | 441 | **31** | 961 | **41** | 1,681 |
| **2** | 4 | **12** | 144 | **22** | 484 | **32** | 1,024 | **42** | 1,764 |
| **3** | 9 | **13** | 169 | **23** | 529 | **33** | 1,089 | **43** | 1,849 |
| **4** | 16 | **14** | 196 | **24** | 576 | **34** | 1,156 | **44** | 1,936 |
| **5** | 25 | **15** | 225 | **25** | 625 | **35** | 1,225 | **45** | 2,025 |
| **6** | 36 | **16** | 256 | **26** | 676 | **36** | 1,296 | **46** | 2,116 |
| **7** | 49 | **17** | 289 | **27** | 729 | **37** | 1,369 | **47** | 2,209 |
| **8** | 64 | **18** | 324 | **28** | 784 | **38** | 1,444 | **48** | 2,304 |
| **9** | 81 | **19** | 361 | **29** | 841 | **39** | 1,521 | **49** | 2,401 |
| **10**| 100 | **20** | 400 | **30** | 900 | **40** | 1,600 | **50** | 2,500 |

---

## 4. CUBES (1³ to 30³)

| n | n³ | n | n³ | n | n³ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| **1** | 1 | **11** | 1,331 | **21** | 9,261 |
| **2** | 8 | **12** | 1,728 | **22** | 10,648 |
| **3** | 27 | **13** | 2,197 | **23** | 12,167 |
| **4** | 64 | **14** | 2,744 | **24** | 13,824 |
| **5** | 125 | **15** | 3,375 | **25** | 15,625 |
| **6** | 216 | **16** | 4,096 | **26** | 17,576 |
| **7** | 343 | **17** | 4,913 | **27** | 19,683 |
| **8** | 512 | **18** | 5,832 | **28** | 21,952 |
| **9** | 729 | **19** | 6,859 | **29** | 24,389 |
| **10**| 1,000 | **20** | 8,000 | **30** | 27,000 |

---

## 5. FRACTION ↔ PERCENTAGE CONVERSION TABLE

| Fraction | Decimal | Percentage | Common Multiples |
| :---: | :---: | :---: | :--- |
| **1/2** | 0.50 | 50.0% | 2/2 = 100% |
| **1/3** | 0.3333 | 33.33% (33 1/3%) | 2/3 = 66.67% (66 2/3%) |
| **1/4** | 0.25 | 25.0% | 3/4 = 75.0% |
| **1/5** | 0.20 | 20.0% | 2/5 = 40%, 3/5 = 60%, 4/5 = 80% |
| **1/6** | 0.1667 | 16.67% (16 2/3%) | 5/6 = 83.33% (83 1/3%) |
| **1/7** | 0.1428 | 14.28% (14 2/7%) | 2/7 = 28.57%, 3/7 = 42.85%, 4/7 = 57.14% |
| **1/8** | 0.125 | 12.5% (12 1/2%) | 3/8 = 37.5%, 5/8 = 62.5%, 7/8 = 87.5% |
| **1/9** | 0.1111 | 11.11% (11 1/9%) | 2/9 = 22.22%, 4/9 = 44.44%, 5/9 = 55.55% |
| **1/10** | 0.10 | 10.0% | 3/10 = 30%, 7/10 = 70%, 9/10 = 90% |
| **1/11** | 0.0909 | 9.09% (9 1/11%) | 2/11 = 18.18%, 3/11 = 27.27%, 4/11 = 36.36% |
| **1/12** | 0.0833 | 8.33% (8 1/3%) | 5/12 = 41.67%, 7/12 = 58.33% |
| **1/13** | 0.0769 | 7.69% (7 9/13%) | 2/13 = 15.38% |
| **1/14** | 0.0714 | 7.14% (7 1/7%) | Half of 1/7 |
| **1/15** | 0.0667 | 6.67% (6 2/3%) | 1/3 of 1/5 |
| **1/16** | 0.0625 | 6.25% (6 1/4%) | Half of 1/8 |
| **1/20** | 0.05 | 5.0% | 3/20 = 15%, 7/20 = 35% |
| **1/25** | 0.04 | 4.0% | 1/4 of 16% |

---

## 6. MENTAL CALCULATION SHORTCUTS

### 6.1 Multiplication by 11
* To multiply any 2-digit number by 11: Add digits and place in middle.
  * $43 \\times 11 \\implies 4 \\text{ [4+3] } 3 = 473$.
  * If sum $\\ge 10$, carry over: $78 \\times 11 \\implies 7 \\text{ [7+8=15] } 8 \\implies (7+1) 5 8 = 858$.

### 6.2 Multiplying Numbers Ending in 5 with Same Tens Digit
* Formula: For $(N5)^2 = N(N+1) \\times 100 + 25$.
  * $35^2 = 3 \\times 4 \\text{ followed by } 25 = 1225$.
  * $75^2 = 7 \\times 8 \\text{ followed by } 25 = 5625$.
  * $105^2 = 10 \\times 11 \\text{ followed by } 25 = 11025$.

### 6.3 Multiplying by 25 and 125
* Multiply by 25: Divide by 4, multiply by 100 (append 00).
  * $64 \\times 25 = (64/4) \\times 100 = 1600$.
* Multiply by 125: Divide by 8, multiply by 1000 (append 000).
  * $72 \\times 125 = (72/8) \\times 1000 = 9000$.

### 6.4 Divisibility Rules Quick Table
| Divisor | Rule |
| :---: | :--- |
| **2** | Last digit is even (0, 2, 4, 6, 8) |
| **3** | Sum of digits is divisible by 3 |
| **4** | Number formed by last 2 digits is divisible by 4 |
| **5** | Last digit is 0 or 5 |
| **6** | Divisible by both 2 and 3 |
| **7** | Double last digit and subtract from remaining number; result divisible by 7 |
| **8** | Number formed by last 3 digits is divisible by 8 |
| **9** | Sum of digits is divisible by 9 |
| **11** | Difference between sum of odd-place digits and even-place digits is 0 or multiple of 11 |
| **13** | Add 4 times the last digit to the remaining number; result divisible by 13 |
"""

with open("data/revision/aptitude/number-tables.md", "w", encoding="utf-8") as f:
    f.write(NUMBER_TABLES_MD)
print("Wrote data/revision/aptitude/number-tables.md")

