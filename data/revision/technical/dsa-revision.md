# DSA Interview Revision

## Arrays & Strings
**What is it?** Arrays store indexed contiguous-like elements; strings are character sequences. **Interview answer:** "I first identify indexing, mutation, and subarray requirements, then choose prefix or two-pointer techniques." **Example:** Find a longest repeating substring. **Use:** Most coding rounds. **Points:** In-place, prefix, immutability. **Follow-ups:** Complexity and overflow.

## Hashing
**What is it?** Hashing maps keys to buckets for average constant-time lookup. **Interview answer:** "I use a hash map to trade memory for faster membership or pair lookup." **Example:** Two-sum. **Use:** Frequency, deduplication, caches. **Points:** Collision, expected O(1), worst-case. **Follow-ups:** Hash collision.

## Two Pointers
**What is it?** Two pointers traverse from positions or ends toward a result. **Interview answer:** "For sorted pairs or partitions, I move pointers by comparing a sum or boundary." **Example:** Remove duplicates. **Use:** Sorted arrays and strings. **Points:** O(n), pointer invariant. **Follow-ups:** Sliding window distinction.

## Sliding Window
**What is it?** A sliding window maintains a moving contiguous range. **Interview answer:** "I add entering elements and remove leaving elements while updating the answer." **Example:** Minimum window containing target characters. **Use:** Subarray and substring constraints. **Points:** Fixed vs variable. **Follow-ups:** Sliding window vs prefix.

## Prefix Sum
**What is it?** Prefix sum stores cumulative totals for fast range queries. **Interview answer:** "Precompute prefix values so a range sum becomes O(1)." **Example:** Aggregate sales between dates. **Use:** Range sums and counts. **Points:** Build once, query many. **Follow-ups:** 2D prefix.

## Binary Search
**What is it?** Binary search halves a monotonic search space. **Interview answer:** "I search a predicate or sorted value and preserve a proven lower or upper boundary." **Example:** Find first bad deployment. **Use:** Sorted arrays and answer optimization. **Points:** Mid overflow, invariant. **Follow-ups:** Search on answer.

## Stack & Queue
**What is it?** Stack is LIFO; queue is FIFO. **Interview answer:** "I use stack for nested or reverse-order work and queue for level or arrival order." **Example:** Valid brackets and task scheduling. **Use:** Parsing and traversal. **Points:** LIFO/FIFO. **Follow-ups:** Deque.

## Monotonic Stack
**What is it?** A monotonic stack keeps elements in increasing or decreasing order. **Interview answer:** "I pop elements while their next greater or smaller boundary is known." **Example:** Daily temperatures. **Use:** Next-greater, histogram, span problems. **Points:** O(n), invariant. **Follow-ups:** Monotonic queue.

## Linked List
**What is it?** Linked nodes reference adjacent nodes. **Interview answer:** "I use slow and fast pointers or a dummy head to handle traversal and missing boundaries." **Example:** Cycle detection. **Use:** Dynamic insertion and pointer problems. **Points:** Reversal, cycle, dummy node. **Follow-ups:** List vs array.

## Recursion
**What is it?** Recursion solves a problem through smaller instances. **Interview answer:** "I define the base case and state transition, then reason about call depth." **Example:** Factorial or tree traversal. **Use:** Divide-and-conquer. **Points:** Stack cost, memoization. **Follow-ups:** Tail recursion.

## Backtracking
**What is it?** Backtracking explores candidates and reverses choices after failure. **Interview answer:** "I choose, recurse, and unchoose; pruning removes impossible branches." **Example:** N-Queens. **Use:** Combinatorial search. **Points:** State copy, pruning. **Follow-ups:** Complexity.

## Trees & BST
**What is it?** Trees are hierarchical nodes; BST keeps ordered child subtrees. **Interview answer:** "I choose traversal or divide around the root and prove recursive bounds." **Example:** Directory hierarchy. **Use:** Search and hierarchy. **Points:** Traversals, depth, balance. **Follow-ups:** Rotations.

## Heap / Priority Queue
**What is it?** A heap retrieves minimum or maximum priority quickly. **Interview answer:** "I maintain the top K or merge streams with a heap." **Example:** Median of a stream. **Use:** Scheduling and top-K. **Points:** O(log n) update. **Follow-ups:** Heap sort.

## Tries
**What is it?** A trie stores strings along character edges. **Interview answer:** "A trie supports prefix lookup and autocomplete efficiently." **Example:** Dictionary search. **Use:** Prefix-heavy text. **Points:** Memory, compressed trie. **Follow-ups:** Hash alternative.

## Graphs BFS/DFS
**What is it?** BFS explores breadth; DFS explores depth. **Interview answer:** "BFS finds shortest unweighted paths, while DFS is suited to connectivity and cycle tasks." **Example:** Maze and social network traversal. **Use:** Relations and grids. **Points:** Visited, queue/stack. **Follow-ups:** Directed cycles.

## Topological Sort
**What is it?** Topological sort orders directed acyclic graph nodes. **Interview answer:** "An indegree Kahn's algorithm returns tasks only after prerequisites complete." **Example:** Build dependencies. **Use:** Scheduling. **Points:** Cycle detection. **Follow-ups:** Lexicographic order.

## Dijkstra
**What is it?** Dijkstra finds shortest paths with non-negative weights. **Interview answer:** "A priority queue expands the minimum tentative distance." **Example:** Navigation routes. **Use:** Weighted graph. **Points:** Greedy proof, no negative edges. **Follow-ups:** Bellman-Ford.

## Union Find
**What is it?** Union Find tracks disjoint sets and connectivity. **Interview answer:** "I merge components and test whether two nodes share a root." **Example:** Network islands. **Use:** Dynamic connectivity. **Points:** Path compression, rank. **Follow-ups:** Kruskal.

## Greedy
**What is it?** Greedy makes locally optimal choices toward a global solution. **Interview answer:** "I prove or counterexample the exchange property before using it." **Example:** Activity selection. **Use:** Interval and scheduling. **Points:** Proof, sorting. **Follow-ups:** Greedy vs DP.

## Dynamic Programming
**What is it?** DP solves overlapping subproblems with optimal substructure. **Interview answer:** "I define state, recurrence, base case, and traversal, then optimize memory." **Example:** Minimum coin count or longest subsequence. **Use:** Optimization and counting. **Points:** 1D/2D, memoization. **Follow-ups:** Backtracking alternatives.
