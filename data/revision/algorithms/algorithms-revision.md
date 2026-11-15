# Algorithms – Searching & Sorting Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## MASTER COMPARISON TABLE: SORTING ALGORITHMS

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? | In-Place? | Key Design Method |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Yes** | **Yes** | Brute Force / Exchange |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **No** | **Yes** | Selection (min element) |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Yes** | **Yes** | Incremental Insertion |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **Yes** | **No** | Divide and Conquer |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | **No** | **Yes** | Divide and Conquer (Pivot) |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | **No** | **Yes** | Heap Priority Queue |
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
* **Recurrence:** $T(n) = T(n/2) + O(1) \implies O(\log n)$.
* **Complexities:** Best: $O(1)$, Average: $O(\log n)$, Worst: $O(\log n)$, Auxiliary Space: Iterative $O(1)$, Recursive $O(\log n)$.
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
* **Optimization:** If no swaps occur in a pass, break early $\implies$ Best case $O(n)$.

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
          /                    \
   [38, 27, 43, 3]          [9, 82, 10]
     /        \               /      \
 [38, 27]   [43, 3]        [9, 82]   [10]
   Merge:
 [27, 38]   [3, 43]        [9, 82]   [10]
     \        /               \      /
   [3, 27, 38, 43]          [9, 10, 82]
          \                    /
        [3, 9, 10, 27, 38, 43, 82]
```
* **Recurrence:** $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$ in all cases.
* **Preferred For:** Linked lists ($O(1)$ extra space for merging), external sorting (huge datasets on disk).

### 2.5 Quick Sort
* **Mechanism:** Choose a pivot $P$, partition array into elements $< P$ and elements $> P$, then recurse on partitions.
* **Partition Schemes:** Lomuto (pivot at end, simpler) vs Hoare (pivots at both ends, 3x fewer swaps).
* **Worst Case ($O(n^2)$):** Occurs when pivot is consistently smallest or largest element (e.g., sorted array with first/last element as pivot).
* **Mitigation:** Randomized pivot selection or Median-of-Three pivot.

### 2.6 Heap Sort
* **Mechanism:** Build Max-Heap in $O(n)$ time. Repeatedly extract max element (root) and swap with last leaf, reduce heap size, and `heapify` root in $O(\log n)$.
* **Advantage over Quick Sort:** Guaranteed $O(n \log n)$ worst-case time with $O(1)$ auxiliary space. Unstable.

### 2.7 Linear (Non-Comparison) Sorting
1. **Counting Sort:** Counts occurrences of each value in range $[0..k]$. Requires $O(n + k)$ time and $O(n + k)$ space. Stable.
2. **Radix Sort:** Sorts integers digit-by-digit from least significant digit (LSD) to most significant digit (MSD) using Counting Sort as a subroutine. Time: $O(d(n + k))$.
3. **Bucket Sort:** Distributes elements into uniformly partitioned buckets, sorts each bucket individually (e.g. via Insertion Sort), and concatenates. Average time: $O(n)$.

---

## 3. COMPARISON VS NON-COMPARISON BOUNDS
* **Lower Bound of Comparison-based Sorting:** $\Omega(n \log_2 n)$ comparisons in worst case.
  * Proof: A comparison tree with $n!$ permutations as leaves must have height $h \ge \log_2(n!) = \Theta(n \log n)$.
* Non-comparison sorts break this lower bound because they do not rely on binary decision trees.

---

## 4. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Stability:** Preserves the relative order of duplicate elements. (Bubble, Insertion, Merge, Counting, Radix are Stable).
2. **In-place:** Uses $O(1)$ auxiliary memory beyond call stack. (Selection, Bubble, Insertion, Heap are In-place).
3. **Quick Sort Average:** $O(n \log n)$, but worst case $O(n^2)$. Space complexity is $O(\log n)$ due to recursion stack.
4. **Merge Sort for Linked Lists:** Preferred because nodes can be rearranged by updating pointers without extra array allocation.
5. **Selection Sort:** Minimizes write operations ($O(n)$ swaps total).

### COMMON TRAPS
* ⚠️ **Trap 1:** Assuming Heap Sort is stable. It is **unstable** due to root-to-leaf swaps.
* ⚠️ **Trap 2:** Assuming Binary Search works on singly linked lists in $O(\log n)$. It takes $O(n)$ to locate the middle element!
* ⚠️ **Trap 3:** Confusing Quick Sort best/average time with worst case. Worst case is quadratic ($O(n^2)$).
