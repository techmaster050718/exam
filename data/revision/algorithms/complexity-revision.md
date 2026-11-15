# Algorithmic Complexity & Asymptotic Analysis
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**
> Last Updated: 2026-11-15

---

## Complexity command map
| Domain | Core recall points |
| :--- | :--- |
| Growth hierarchy | O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!) |
| Asymptotic notation | Big-O, Big-Omega, Big-Theta, little-o, little-omega |
| Recurrence analysis | Master theorem, recurrence patterns, divide-and-conquer |
| Loop analysis | Single loops, nested loops, geometric progressions |
| Exam focus | Complexity comparison and recurrence reasoning |

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
| **Big-O ($O$)** | $f(n) \le c \cdot g(n)$ for all $n \ge n_0, c > 0$ | Asymptotic Upper Bound | "Worst-case cannot exceed this" |
| **Big-Omega ($\Omega$)** | $f(n) \ge c \cdot g(n)$ for all $n \ge n_0, c > 0$ | Asymptotic Lower Bound | "Best-case cannot be faster than this" |
| **Big-Theta ($\Theta$)** | $c_1 g(n) \le f(n) \le c_2 g(n)$ for all $n \ge n_0$ | Asymptotic Tight Bound | "Exact growth rate behavior" |
| **Little-o ($o$)** | $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$ | Strict Upper Bound | Strictly slower growth than $g(n)$ |
| **Little-omega ($\omega$)**| $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$ | Strict Lower Bound | Strictly faster growth than $g(n)$ |

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
For recurrence: $T(n) = a T(n/b) + f(n)$ where $a \ge 1, b > 1$:

Let critical exponent be $c = \log_b a$:

1. **Case 1 (Leaf-heavy):** If $f(n) = O(n^{c - \epsilon})$ for some $\epsilon > 0$:
   $$T(n) = \Theta(n^{\log_b a})$$
   *Example:* $T(n) = 8T(n/2) + 1000n^2 \implies a=8, b=2, \log_2 8 = 3$. Since $n^2 = O(n^{3-\epsilon})$, $T(n) = \Theta(n^3)$.

2. **Case 2 (Balanced):** If $f(n) = \Theta(n^c \log^k n)$ for $k \ge 0$:
   $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$
   *Example (Merge Sort):* $T(n) = 2T(n/2) + O(n) \implies \log_2 2 = 1, k=0 \implies T(n) = \Theta(n \log n)$.

3. **Case 3 (Root-heavy):** If $f(n) = \Omega(n^{c + \epsilon})$ and regularity condition holds ($a f(n/b) \le d f(n)$ for $d < 1$):
   $$T(n) = \Theta(f(n))$$
   *Example:* $T(n) = 2T(n/2) + n^2 \implies \log_2 2 = 1$. Since $n^2 = \Omega(n^{1+\epsilon})$, $T(n) = \Theta(n^2)$.

---

## 5. COMMON RECURRENCE RELATIONS QUICK CHEAT SHEET
| Recurrence | Algorithm Example | Complexity |
| :--- | :--- | :--- |
| $T(n) = T(n-1) + O(1)$ | Sequential Search (Recursive) | $O(n)$ |
| $T(n) = T(n-1) + O(n)$ | Selection Sort, Worst QuickSort | $O(n^2)$ |
| $T(n) = 2T(n-1) + O(1)$ | Tower of Hanoi | $O(2^n)$ |
| $T(n) = T(n/2) + O(1)$ | Binary Search | $O(\log n)$ |
| $T(n) = 2T(n/2) + O(n)$ | Merge Sort | $O(n \log n)$ |
| $T(n) = T(n/2) + O(n)$ | Quickselect / Median-of-Medians | $O(n)$ |
| $T(n) = 2T(n/2) + O(1)$ | Tree Traversal (Binary Tree) | $O(n)$ |
| $T(n) = 7T(n/2) + O(n^2)$| Strassen's Matrix Multiplication | $O(n^{\log_2 7}) \approx O(n^{2.81})$|

---

## 6. 30-SECOND REVISION
* $O(1) < O(\log n) < O(\sqrt{n}) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$
* If loop steps multiply or divide by constant $k$, complexity is $O(\log_k n)$.
* Master Theorem cannot solve when $a < 1$, $b \le 1$, or $f(n)$ is non-polynomial (e.g. $2^n$).
