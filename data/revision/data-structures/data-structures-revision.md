# Data Structures – Complete Revision Notes
> **Exam-Ready | Government Competitive Exams (GATE, SSC, Banking, NIC, ISRO)**

---

## TABLE OF CONTENTS
1. [Array](#1-array)
2. [Linked List – Singly](#2-singly-linked-list)
3. [Linked List – Doubly](#3-doubly-linked-list)
4. [Linked List – Circular](#4-circular-linked-list)
5. [Stack](#5-stack)
6. [Queue](#6-queue)
7. [Circular Queue](#7-circular-queue)
8. [Deque (Double-Ended Queue)](#8-deque)
9. [Priority Queue](#9-priority-queue)
10. [Hash Table](#10-hash-table)
11. [Tree – General](#11-tree)
12. [Binary Tree](#12-binary-tree)
13. [Binary Search Tree (BST)](#13-binary-search-tree-bst)
14. [AVL Tree](#14-avl-tree)
15. [Heap – Min & Max](#15-heap)
16. [B-Tree & B+ Tree](#16-b-tree--b-tree)
17. [Trie](#17-trie)
18. [Graph](#18-graph)

---

## 1. ARRAY

**Definition:** A contiguous block of memory storing elements of the same type, accessed via integer index.

### Diagram
```
Index →  0     1     2     3     4
        ┌─────┬─────┬─────┬─────┬─────┐
        │  10 │  20 │  30 │  40 │  50 │
        └─────┴─────┴─────┴─────┴─────┘
         ↑                             ↑
       Base                        Base + 4×size
```
Address of element at index i = Base + i × sizeof(element)

### Operations Complexity
| Operation       | Best     | Average  | Worst    |
|-----------------|----------|----------|----------|
| Access by index | O(1)     | O(1)     | O(1)     |
| Search (linear) | O(1)     | O(n)     | O(n)     |
| Search (binary) | O(1)     | O(log n) | O(log n) |
| Insert at end   | O(1)     | O(1)     | O(1)*    |
| Insert at start | O(n)     | O(n)     | O(n)     |
| Insert at mid   | O(n)     | O(n)     | O(n)     |
| Delete at end   | O(1)     | O(1)     | O(1)     |
| Delete at start | O(n)     | O(n)     | O(n)     |

> *Amortized O(1) for dynamic arrays (doubling strategy)

**Space Complexity:** O(n)

### Types of Arrays
| Type | Description |
|------|-------------|
| 1D Array | Simple linear array |
| 2D Array | Matrix form – row-major or column-major storage |
| Jagged Array | Array of arrays of different lengths |
| Dynamic Array | Resizes automatically (e.g., ArrayList, Python list) |

### Row-Major vs Column-Major
```
Matrix:  A[0][0]  A[0][1]  A[0][2]
         A[1][0]  A[1][1]  A[1][2]

Row-Major storage:    A[0][0] A[0][1] A[0][2] A[1][0] A[1][1] A[1][2]
Column-Major storage: A[0][0] A[1][0] A[0][1] A[1][1] A[0][2] A[1][2]

Row-Major formula:    Base + (i × cols + j) × size
Column-Major formula: Base + (j × rows + i) × size
```

**When to Use:**
- Random access is needed (O(1) access).
- Data size is known in advance.
- Cache-friendly sequential traversal.

### ⚠️ Common Exam Traps
- **Array index starts at 0** in most languages; memory address formula uses 0-based index.
- Binary search only works on a **sorted** array.
- Inserting at the beginning requires shifting **all** n elements → O(n).

> ### 📌 MUST REMEMBER
> - Access: **O(1)** | Search: **O(n)** linear, **O(log n)** binary
> - Insert/Delete at middle: **O(n)** due to shifting
> - 2D Row-major address: **Base + (i × C + j) × w**

---

## 2. SINGLY LINKED LIST

**Definition:** A sequence of nodes where each node stores data and a pointer to the next node. Last node points to NULL.

### Diagram
```
HEAD
  ↓
[10 | ●]──→[20 | ●]──→[30 | ●]──→[40 | ●]──→NULL
  Node1       Node2       Node3       Node4

Each Node:  ┌──────┬──────┐
            │ Data │ Next │
            └──────┴──────┘
```

### Operations Complexity
| Operation         | Best | Average | Worst |
|-------------------|------|---------|-------|
| Insert at head    | O(1) | O(1)    | O(1)  |
| Insert at tail    | O(n) | O(n)    | O(n)* |
| Insert at middle  | O(1) | O(n)    | O(n)  |
| Delete at head    | O(1) | O(1)    | O(1)  |
| Delete at tail    | O(n) | O(n)    | O(n)  |
| Delete (by value) | O(1) | O(n)    | O(n)  |
| Search            | O(1) | O(n)    | O(n)  |
| Access by index   | O(1) | O(n)    | O(n)  |

> *O(1) if tail pointer is maintained

**Space Complexity:** O(n) — extra space for pointers

### When to Use
- Frequent insertions/deletions at the beginning.
- Size of data is unknown or varies dynamically.
- No need for random access.

### ⚠️ Common Exam Traps
- **No backward traversal** — to delete a node you need the previous node.
- Tail insertion is O(n) unless a tail pointer is kept.
- Reversing a singly linked list requires 3 pointers (prev, curr, next).

> ### 📌 MUST REMEMBER
> - Insert at head: **O(1)** | Insert at tail: **O(n)**
> - No random access — must traverse from HEAD
> - To detect a loop: **Floyd's Cycle Detection** (slow & fast pointer)

---

## 3. DOUBLY LINKED LIST

**Definition:** Each node has pointers to both the next and previous nodes, allowing bidirectional traversal.

### Diagram
```
NULL←[●|10|●]⟷[●|20|●]⟷[●|30|●]⟷[●|40|●]→NULL
      ↑                                   ↑
     HEAD                               TAIL

Each Node:  ┌──────┬──────┬──────┐
            │ Prev │ Data │ Next │
            └──────┴──────┴──────┘
```

### Operations Complexity
| Operation         | Best | Average | Worst |
|-------------------|------|---------|-------|
| Insert at head    | O(1) | O(1)    | O(1)  |
| Insert at tail    | O(1) | O(1)    | O(1)  |
| Insert at middle  | O(1) | O(n)    | O(n)  |
| Delete (by node)  | O(1) | O(1)    | O(1)  |
| Delete (by value) | O(1) | O(n)    | O(n)  |
| Search            | O(1) | O(n)    | O(n)  |

**Space Complexity:** O(n) — 2 pointers per node (extra overhead vs singly)

### When to Use
- Need to traverse both forward and backward (e.g., browser history).
- Frequent deletion given the node reference.
- LRU Cache implementation.

### ⚠️ Common Exam Traps
- Uses **more memory** than singly linked list (2 pointers per node).
- Deletion is O(1) **only if you have the node reference** (not O(1) by value).
- Requires updating 4 pointer links on insert/delete.

> ### 📌 MUST REMEMBER
> - Bidirectional traversal | Tail insert: **O(1)**
> - Delete given node pointer: **O(1)**
> - Extra memory: **2 pointers per node**

---

## 4. CIRCULAR LINKED LIST

**Definition:** A linked list where the last node points back to the first node (head), forming a circle.

### Diagram
```
Singly Circular:
    ┌──────────────────────────────┐
    ↓                             │
  [10|●]──→[20|●]──→[30|●]──→[40|●]
  HEAD

Doubly Circular:
    ┌────────────────────────────────────────────┐
    │  ┌─────────────────────────────────────┐  │
    ↓  ↑                                     ↓  ↑
  [●|10|●]⟷[●|20|●]⟷[●|30|●]⟷[●|40|●]
```

### Operations Complexity
| Operation      | Best | Average | Worst |
|----------------|------|---------|-------|
| Insert at head | O(1) | O(1)    | O(1)  |
| Insert at tail | O(1) | O(1)    | O(1)* |
| Search         | O(1) | O(n)    | O(n)  |
| Delete at head | O(1) | O(1)    | O(1)  |

> *O(1) if tail pointer is maintained

**Space Complexity:** O(n)

### When to Use
- Round-robin scheduling (CPU scheduling).
- Circular buffer / ring buffer.
- Applications where traversal must loop (Josephus problem).

### ⚠️ Common Exam Traps
- No NULL at end — traversal loop termination uses HEAD comparison.
- Must be careful to avoid infinite loops when traversing.
- Insertion at tail doesn't require traversal if tail pointer is kept.

> ### 📌 MUST REMEMBER
> - Last node points to **HEAD** (not NULL)
> - Used in **Round-Robin CPU Scheduling**
> - Traversal: stop when you reach HEAD again

---

## 5. STACK

**Definition:** A Last-In, First-Out (LIFO) linear data structure. Elements are inserted and removed from the same end (top).

### Diagram
```
         PUSH →        POP ←
              ↓        ↑
         ┌────────┐
   TOP → │  40   │  ← most recently pushed
         ├────────┤
         │  30   │
         ├────────┤
         │  20   │
         ├────────┤
   BOT → │  10   │  ← first pushed
         └────────┘
```

### Operations Complexity
| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Push      | O(1) | O(1)    | O(1)  |
| Pop       | O(1) | O(1)    | O(1)  |
| Peek/Top  | O(1) | O(1)    | O(1)  |
| Search    | O(n) | O(n)    | O(n)  |
| isEmpty   | O(1) | O(1)    | O(1)  |

**Space Complexity:** O(n)

### Implementation Options
| Approach        | Insert | Delete | Limitation              |
|-----------------|--------|--------|-------------------------|
| Array-based     | O(1)   | O(1)   | Fixed size (stack overflow) |
| Linked List     | O(1)   | O(1)   | Extra pointer memory    |

### Applications
| Use Case                    | Why Stack? |
|-----------------------------|------------|
| Function call management    | Call stack uses LIFO |
| Undo/Redo operations        | Last action undone first |
| Expression evaluation       | Infix → Postfix conversion |
| Parenthesis matching        | Push open, pop on close |
| DFS (iterative)             | Stack simulates recursion |
| Browser back button         | Last page popped first |

### Infix → Postfix Conversion (Key Exam Topic)
```
Precedence: ^ > * / > + -
Associativity: ^ is right-to-left; rest are left-to-right

Example: A + B * C - D
Step 1: A     → output: A
Step 2: +     → stack: [+]
Step 3: B     → output: A B
Step 4: *     → stack: [+ *] (* > +, so push)
Step 5: C     → output: A B C
Step 6: -     → pop *, pop + → output: A B C * + ; stack: [-]
Step 7: D     → output: A B C * + D
Step 8: end   → pop - → output: A B C * + D -
Result: A B C * + D -
```

### ⚠️ Common Exam Traps
- Stack **overflow**: pushing onto a full stack; **underflow**: popping from empty stack.
- In **postfix evaluation**, operands pushed, operator pops two operands.
- Right-associative operators (^) go on stack without popping same-precedence operator.

> ### 📌 MUST REMEMBER
> - LIFO | All operations: **O(1)**
> - **Postfix/Prefix evaluation** uses stack
> - **Infix→Postfix**: higher or equal precedence operators popped (except ^)

---

## 6. QUEUE

**Definition:** A First-In, First-Out (FIFO) linear data structure. Elements inserted at REAR, removed from FRONT.

### Diagram
```
Enqueue →                    ← Dequeue
          ┌────┬────┬────┬────┐
REAR →    │ 40 │ 30 │ 20 │ 10 │  ← FRONT
          └────┴────┴────┴────┘
     Enqueue adds here    Dequeue removes here
```

### Operations Complexity
| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Enqueue   | O(1) | O(1)    | O(1)  |
| Dequeue   | O(1) | O(1)    | O(1)  |
| Front/Peek| O(1) | O(1)    | O(1)  |
| Search    | O(n) | O(n)    | O(n)  |
| isEmpty   | O(1) | O(1)    | O(1)  |

**Space Complexity:** O(n)

### Applications
| Use Case                 | Why Queue? |
|--------------------------|------------|
| CPU Process Scheduling   | FCFS scheduling |
| BFS traversal            | Level-order traversal |
| Print spooler            | First job printed first |
| IO Buffer                | Sequential data transfer |
| Keyboard buffer          | Characters processed in order |

### ⚠️ Common Exam Traps
- Simple array queue wastes space — after n dequeues, front shifts right leaving empty slots at beginning.
- **Solution**: Use Circular Queue to reuse empty slots.
- Queue implemented with two stacks: Enqueue O(1), Dequeue O(n) amortized O(1).

> ### 📌 MUST REMEMBER
> - FIFO | All operations: **O(1)**
> - **BFS uses Queue** | **DFS uses Stack**
> - Array queue problem: front pointer drift → use **Circular Queue**

---

## 7. CIRCULAR QUEUE

**Definition:** A queue where the last position is connected to the first, forming a ring. Solves array queue's space wastage problem.

### Diagram
```
Circular Queue (size=5):
         ┌───┐
      ┌──┤ 0 ├──┐
      │  └───┘  │
   ┌──┤4│     │1├──┐
   │  └─┘     └─┘  │
   │  ┌─┐     ┌─┐  │
   └──┤3│     │2├──┘
      └─┘     └─┘

FRONT=1, REAR=3  → elements at positions 1,2,3

Enqueue: REAR = (REAR + 1) % SIZE
Dequeue: FRONT = (FRONT + 1) % SIZE
Full:    (REAR + 1) % SIZE == FRONT
Empty:   FRONT == REAR
```

### Operations Complexity
| Operation | Complexity |
|-----------|------------|
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Peek      | O(1)       |
| isFull    | O(1)       |
| isEmpty   | O(1)       |

**Space Complexity:** O(n) — no wasted slots

### ⚠️ Common Exam Traps
- Max elements storable = SIZE - 1 (one slot reserved to distinguish full vs empty).
- Full condition: `(rear+1) % size == front` — NOT `rear == size-1`.
- Modulo arithmetic is key: always `(index + 1) % size`.

> ### 📌 MUST REMEMBER
> - Fixes **wasted space** in linear queue
> - Capacity = **SIZE - 1** (not SIZE)
> - Full: `(rear+1)%size == front` | Empty: `front == rear`

---

## 8. DEQUE

**Definition:** Double-Ended Queue. Allows insertion and deletion at both FRONT and REAR ends.

### Diagram
```
Insert/Delete         Insert/Delete
at Front ←→          at Rear ←→
           ┌────┬────┬────┬────┐
FRONT  →   │ 10 │ 20 │ 30 │ 40 │  ← REAR
           └────┴────┴────┴────┘
```

### Types
| Type            | Restriction                                  |
|-----------------|----------------------------------------------|
| Input-Restricted | Insert only at REAR; delete at both ends    |
| Output-Restricted | Delete only at FRONT; insert at both ends  |

### Operations Complexity
| Operation         | Complexity |
|-------------------|------------|
| InsertFront       | O(1)       |
| InsertRear        | O(1)       |
| DeleteFront       | O(1)       |
| DeleteRear        | O(1)       |
| PeekFront         | O(1)       |
| PeekRear          | O(1)       |

**Space Complexity:** O(n)

### ⚠️ Common Exam Traps
- Deque is **more general** than both Stack and Queue (subsumes both).
- Stack = Output-Restricted Deque with insert/delete at same end.
- Queue = Input-Restricted Deque with insert at REAR, delete at FRONT.

> ### 📌 MUST REMEMBER
> - Deque generalizes Stack + Queue
> - **Sliding Window Maximum** problem uses Deque — O(n) solution
> - All 4 operations: **O(1)**

---

## 9. PRIORITY QUEUE

**Definition:** A queue where each element has a priority. The element with the highest (or lowest) priority is served first, regardless of insertion order.

### Diagram
```
Priority Queue (Max-Priority):

Inserted: (task1, p=3), (task2, p=5), (task3, p=1)

Internal (Max-Heap):       Dequeue order:
       [task2, 5]           1st: task2 (p=5)
      /           \         2nd: task1 (p=3)
  [task1, 3]  [task3, 1]   3rd: task3 (p=1)
```

### Implementations & Complexities
| Implementation  | Insert    | Delete-Max | Peek-Max |
|-----------------|-----------|------------|----------|
| Unsorted Array  | O(1)      | O(n)       | O(n)     |
| Sorted Array    | O(n)      | O(1)       | O(1)     |
| Binary Heap     | O(log n)  | O(log n)   | O(1)     |
| Fibonacci Heap  | O(1)*     | O(log n)*  | O(1)     |

> *Amortized

**Space Complexity:** O(n)

**Best Implementation:** Binary Heap (most common in practice)

### ⚠️ Common Exam Traps
- Priority Queue ≠ Sorted Queue — it only guarantees the top element.
- **Dijkstra's algorithm** uses a Min-Priority Queue.
- **Huffman Coding** uses a Min-Priority Queue.

> ### 📌 MUST REMEMBER
> - Best implementation: **Binary Heap**
> - Insert & Delete: **O(log n)** | Peek: **O(1)**
> - Used in: **Dijkstra, Huffman, Prim's algorithm**

---

## 10. HASH TABLE

**Definition:** A data structure that maps keys to values using a hash function, enabling average O(1) insert, delete, and lookup.

### Diagram
```
Keys: "apple"=1, "banana"=2, "cherry"=3  (table size=7)

hash("apple")  = 1  → slot 1
hash("banana") = 2  → slot 2
hash("cherry") = 6  → slot 6

Slots:  0    1       2        3    4    5       6
       ┌───┬──────┬────────┬────┬────┬────┬────────┐
       │   │apple │banana  │    │    │    │cherry  │
       └───┴──────┴────────┴────┴────┴────┴────────┘

Collision at slot 3 (chaining):
       ┌───┐
  3 → │●  │ → ["mango"|●] → ["grape"|●] → NULL
       └───┘
```

### Hash Functions
| Method          | Formula                                | Notes                    |
|-----------------|----------------------------------------|--------------------------|
| Division        | h(k) = k mod m                        | m should be prime        |
| Multiplication  | h(k) = floor(m × (k × A mod 1))      | A ≈ 0.618 (golden ratio) |
| Universal       | h(k) = ((ak+b) mod p) mod m           | Randomized               |

### Collision Resolution
| Method             | Diagram                              | Pros                | Cons                    |
|--------------------|--------------------------------------|---------------------|-------------------------|
| Chaining           | Each slot → linked list              | Simple, unlimited   | Extra memory            |
| Open Addressing    | Probe sequence within table          | Cache-friendly      | Clustering, limited size|
| Linear Probing     | h(k,i) = (h(k)+i) mod m             | Simple              | Primary clustering      |
| Quadratic Probing  | h(k,i) = (h(k)+i²) mod m           | Less clustering     | Secondary clustering    |
| Double Hashing     | h(k,i) = (h1(k)+i×h2(k)) mod m     | Minimal clustering  | Complex                 |

### Operations Complexity
| Operation | Average | Worst    |
|-----------|---------|----------|
| Insert    | O(1)    | O(n)     |
| Delete    | O(1)    | O(n)     |
| Search    | O(1)    | O(n)     |

> Worst case occurs when all keys hash to the same slot (all chained).

**Space Complexity:** O(n)

**Load Factor (α):** α = n/m (n = elements, m = slots)
- Chaining: performance degrades at α > 0.7
- Open Addressing: must keep α < 0.5

### ⚠️ Common Exam Traps
- Worst-case search is **O(n)** (all keys in one chain), NOT O(1).
- Table size should be **prime** for division method.
- **Deleted slots** in open addressing must be marked as "DELETED" (not empty) to avoid breaking probe chains.
- Load factor threshold for rehashing varies by implementation.

> ### 📌 MUST REMEMBER
> - Average: **O(1)** | Worst: **O(n)**
> - Load factor α = n/m; rehash when α too high
> - **Chaining**: unlimited; **Open addressing**: table size limits
> - Best hash table size: **prime number**

---

## 11. TREE

**Definition:** A hierarchical, non-linear data structure with a root node and subtrees of children, with no cycles.

### Diagram
```
           [A]           ← Root (Level 0)
          / | \
        [B][C][D]        ← Level 1 (children of A)
       / \    |
     [E] [F] [G]         ← Level 2 (leaves: E, F, G, D... wait D has G)
```

### Key Terminology
| Term         | Definition                                              |
|--------------|---------------------------------------------------------|
| Root         | Top-most node with no parent                            |
| Leaf         | Node with no children                                   |
| Edge         | Link between parent and child                           |
| Height       | Longest path from node to a leaf (bottom-up)            |
| Depth        | Distance from root to node (top-down)                   |
| Degree       | Number of children of a node                            |
| Level        | Depth + 1 (root is level 1 in some definitions)        |
| Subtree      | A node and all its descendants                          |
| Ancestor     | Any node on path from root to given node                |
| Descendant   | Any node in a node's subtree                            |

### Important Formulas
```
For a tree with n nodes:
  - Number of edges = n - 1
  - For binary tree: max nodes at level i = 2^i (root at level 0)
  - For binary tree with height h: max total nodes = 2^(h+1) - 1
  - Min height of binary tree with n nodes = ⌊log₂ n⌋
```

### ⚠️ Common Exam Traps
- Height of a single node (root only) = 0 (some books say 1 — check convention).
- Number of edges in a tree with n nodes = **n - 1** (always).
- A tree with n nodes and n-1 edges is **always connected and acyclic**.

> ### 📌 MUST REMEMBER
> - Edges = **n - 1**
> - Max nodes at level i = **2^i**
> - Height of leaf = 0, Height of tree = max depth of any leaf

---

## 12. BINARY TREE

**Definition:** A tree where each node has at most 2 children: left and right.

### Diagram
```
         50
        /  \
       30   70
      / \   / \
    20  40 60  80
```

### Types of Binary Trees
| Type               | Property                                                     |
|--------------------|--------------------------------------------------------------|
| Full Binary Tree   | Every node has 0 or 2 children (never 1)                    |
| Complete Binary Tree | All levels full except last; last level filled left-to-right |
| Perfect Binary Tree | All internal nodes have 2 children; all leaves at same level |
| Balanced Binary Tree | Height difference of left/right subtrees ≤ 1 for all nodes |
| Degenerate (Skewed) | Each node has only 1 child — degenerates to a linked list   |

### Properties Table
| Type      | Height    | Nodes (n)         | Note                      |
|-----------|-----------|-------------------|---------------------------|
| Perfect   | log₂(n+1)-1 | 2^(h+1) - 1    | All levels completely full |
| Complete  | ⌊log₂ n⌋ | Between 2^h and 2^(h+1)-1 | Heap uses this |
| Skewed    | n-1       | n                 | Worst case for BST        |

### Tree Traversals
```
Tree:        1
            / \
           2   3
          / \
         4   5

Inorder   (L → Root → R): 4 2 5 1 3
Preorder  (Root → L → R): 1 2 4 5 3
Postorder (L → R → Root): 4 5 2 3 1
Level-order (BFS):        1 2 3 4 5
```

### Traversal Use Cases
| Traversal   | Use Case                                      |
|-------------|-----------------------------------------------|
| Inorder     | BST → sorted output                           |
| Preorder    | Copy a tree; Serialization                    |
| Postorder   | Delete a tree; Expression evaluation          |
| Level-order | Level-by-level processing; Shortest path      |

### ⚠️ Common Exam Traps
- **Inorder of BST gives sorted order** — a frequent exam question.
- A full binary tree with n internal nodes has **n+1 leaf nodes**.
- Preorder + Inorder (or Postorder + Inorder) uniquely reconstructs a binary tree. Preorder + Postorder does NOT uniquely reconstruct (unless full).

> ### 📌 MUST REMEMBER
> - Inorder traversal of BST = **sorted sequence**
> - Full BT: leaves = internal nodes + 1
> - Complete BT stored in array: parent at i, children at **2i+1** and **2i+2** (0-indexed)

---

## 13. BINARY SEARCH TREE (BST)

**Definition:** A binary tree where for every node, all values in the left subtree are less, and all values in the right subtree are greater.

### Diagram
```
Insert sequence: 50, 30, 70, 20, 40, 60, 80

           50
          /  \
         30   70
        / \  / \
       20 40 60 80

Property: Left < Node < Right (at every node)

Inorder: 20 30 40 50 60 70 80 ✓ (sorted!)
```

### Operations Complexity
| Operation | Best    | Average  | Worst |
|-----------|---------|----------|-------|
| Insert    | O(log n)| O(log n) | O(n)  |
| Delete    | O(log n)| O(log n) | O(n)  |
| Search    | O(1)    | O(log n) | O(n)  |

> Worst case O(n) when tree is skewed (sorted input → degenerate BST)

**Space Complexity:** O(n)

### BST Deletion Cases
```
Case 1: Delete leaf node (40 → no children)
         50                50
        / \               / \
       30  70    →       30  70
      / \               /
     20  40            20

Case 2: Delete node with ONE child (30 → left child only)
         50                50
        / \               / \
       30  70    →       20  70
      /
     20

Case 3: Delete node with TWO children (50 → has left and right)
   Replace with INORDER SUCCESSOR (smallest in right subtree)
   or INORDER PREDECESSOR (largest in left subtree)
         50                60
        / \               / \
       30  70    →       30  70
          / \               \
         60  80              80
```

### ⚠️ Common Exam Traps
- Inserting already-sorted data creates a **skewed tree** → O(n) operations.
- Inorder successor = **leftmost node of right subtree**.
- Inorder predecessor = **rightmost node of left subtree**.
- BST does **not** self-balance — use AVL/Red-Black for guaranteed O(log n).

> ### 📌 MUST REMEMBER
> - Average: **O(log n)** | Worst (skewed): **O(n)**
> - Delete with 2 children → replace with **inorder successor**
> - Sorted input → skewed BST (worst case)

---

## 14. AVL TREE

**Definition:** A self-balancing BST where the height difference (Balance Factor) between left and right subtrees of any node is at most 1.

### Balance Factor
```
Balance Factor (BF) = Height(Left subtree) - Height(Right subtree)

Valid BF values: -1, 0, +1
If BF < -1 or BF > +1 → ROTATION NEEDED
```

### Diagram & Rotations
```
Right Rotation (LL Case):
     z                y
    /      →         / \
   y                x   z
  /
 x

Left Rotation (RR Case):
 z                    y
  \          →       / \
   y                z   x
    \
     x

Left-Right Rotation (LR Case): Left rotate y, then Right rotate z
Right-Left Rotation (RL Case): Right rotate y, then Left rotate z
```

### When Which Rotation?
```
Imbalance at node z:
  LL (Left-Left):   New node in LEFT subtree of LEFT child   → Single Right Rotation
  RR (Right-Right): New node in RIGHT subtree of RIGHT child → Single Left Rotation
  LR (Left-Right):  New node in RIGHT subtree of LEFT child  → Left then Right Rotation
  RL (Right-Left):  New node in LEFT subtree of RIGHT child  → Right then Left Rotation
```

### Operations Complexity
| Operation | Best     | Average  | Worst    |
|-----------|----------|----------|----------|
| Insert    | O(log n) | O(log n) | O(log n) |
| Delete    | O(log n) | O(log n) | O(log n) |
| Search    | O(log n) | O(log n) | O(log n) |

**Space Complexity:** O(n)

### ⚠️ Common Exam Traps
- After insertion, **only one rotation** (single or double) needed to restore balance.
- After deletion, **multiple rotations** may be needed up the tree.
- Height of AVL tree with n nodes ≈ **1.44 log₂(n)**.
- Minimum nodes in AVL tree of height h: N(h) = N(h-1) + N(h-2) + 1 (Fibonacci-like).

> ### 📌 MUST REMEMBER
> - All ops: **O(log n)** guaranteed
> - BF ∈ {-1, 0, +1} | 4 rotation types
> - Min nodes: **N(h) = N(h-1) + N(h-2) + 1**
> - After insert: **at most 1** rotation; After delete: **multiple** possible

---

## 15. HEAP

**Definition:** A complete binary tree satisfying the heap property: Max-Heap (parent ≥ children) or Min-Heap (parent ≤ children).

### Diagram
```
Max-Heap:              Min-Heap:
       100                   1
      /    \               /    \
    50      80            10     5
   / \    /   \          / \   /  \
  30  20  70   60       15  12 8    7

Stored as Array (0-indexed):
Max: [100, 50, 80, 30, 20, 70, 60]
Min: [1, 10, 5, 15, 12, 8, 7]

Index relations (0-indexed):
  Parent of i:       (i-1) / 2
  Left child of i:   2i + 1
  Right child of i:  2i + 2
```

### Operations Complexity
| Operation    | Best     | Average  | Worst    |
|--------------|----------|----------|----------|
| Insert       | O(1)     | O(log n) | O(log n) |
| Delete-Max   | O(1)     | O(log n) | O(log n) |
| Peek-Max     | O(1)     | O(1)     | O(1)     |
| Heapify      | O(n)     | O(n)     | O(n)     |
| Heap Sort    | O(n log n)| O(n log n) | O(n log n) |

**Space Complexity:** O(n) — stored as array (no pointer overhead)

### Heapify Process
```
Build Max-Heap from [4, 10, 3, 5, 1]:

Array: [4, 10, 3, 5, 1]   → start from last non-leaf (index n/2 - 1 = 1)

Index 1 (value 10): children are 5 and 1 → 10 > 5,1 → no swap
Index 0 (value 4):  children are 10 and 3 → swap 4 and 10

Result: [10, 5, 3, 4, 1]
         ↓
        10
       /  \
      5    3
     / \
    4   1
```

### ⚠️ Common Exam Traps
- Heapify (build heap) is **O(n)** — NOT O(n log n) (counterintuitive!).
- Heap sort is **NOT stable**.
- Deleting the root: replace with last element, then sift-down → O(log n).
- Min-Heap root = **minimum** element; Max-Heap root = **maximum**.

> ### 📌 MUST REMEMBER
> - Peek: **O(1)** | Insert/Delete: **O(log n)** | Build Heap: **O(n)**
> - Stored as **array** (no pointers needed)
> - Heap Sort: **O(n log n), NOT stable, in-place**
> - Root always = **min** (min-heap) or **max** (max-heap)

---

## 16. B-TREE & B+ TREE

**Definition:** Self-balancing multi-way search trees designed for disk-based storage, minimizing disk I/O operations.

### B-Tree of order m (Diagram)
```
B-Tree of order 3 (each node: 1–2 keys, 2–3 children):

             [30 | 70]
            /    |    \
        [10|20] [40|60] [80|90]

Properties of B-Tree order m:
- Root has 2 to m children (or 1 to m-1 keys)
- Each non-root node has ⌈m/2⌉ to m children
- All leaves at the same level
- A node with k keys has k+1 children
```

### B+ Tree Diagram
```
B+ Tree (all data at leaves, internal nodes are index only):

Internal:    [30 | 70]
            /    |    \
         [10|20] [40|60] [80|90]
Leaves:  [10,20]→[40,60]→[80,90]  ← Linked List of leaves

Key differences from B-Tree:
- All actual data is at LEAF nodes
- Internal nodes store only keys (routing keys)
- Leaf nodes are linked (supports range queries)
```

### B-Tree vs B+ Tree
| Feature           | B-Tree                  | B+ Tree                        |
|-------------------|-------------------------|--------------------------------|
| Data location     | Internal + Leaf nodes   | Leaf nodes only                |
| Leaf linking      | No                      | Yes (linked list)              |
| Range queries     | Poor                    | Excellent                      |
| Space efficiency  | Less (data everywhere)  | More (index + data separated)  |
| Search            | May stop at internal    | Always reaches leaf            |
| Used in           | General purpose         | Databases, file systems        |

### Operations Complexity (Order m, n keys)
| Operation | Complexity           |
|-----------|----------------------|
| Search    | O(log_m n) = O(log n)|
| Insert    | O(log n)             |
| Delete    | O(log n)             |

### ⚠️ Common Exam Traps
- B-Tree order m means max **m children** (not m keys).
- B+ Tree: **internal nodes do NOT store data records**, only keys.
- All leaves of B-Tree (and B+ Tree) are at the **same level** — always balanced.
- B+ Tree is preferred for **databases** (range queries via leaf linked list).

> ### 📌 MUST REMEMBER
> - All leaves at same level → **always balanced**
> - B+ Tree leaf nodes → **linked list** (enables range queries)
> - Used in **databases and file systems** (MySQL InnoDB uses B+ Tree)
> - Min children per non-root node: **⌈m/2⌉**

---

## 17. TRIE

**Definition:** A tree-like data structure for storing strings where each node represents a character. All strings with a common prefix share the same path from root.

### Diagram
```
Inserting: "cat", "car", "card", "care", "bat"

              [root]
             /      \
           [c]      [b]
           |          |
          [a]        [a]
         /   \         \
       [t]*  [r]       [t]*
              |
             [d]*  or  [e]*
                  (*=end of word marker)

Traversal to find "car": root → c → a → r  ✓
"ca" is NOT a word (no end marker at 'a')
```

### Operations Complexity
| Operation | Time        | Notes                           |
|-----------|-------------|----------------------------------|
| Insert    | O(m)        | m = length of string             |
| Search    | O(m)        | m = length of string             |
| Delete    | O(m)        | m = length of string             |
| Prefix search | O(m)   | m = prefix length                |
| All words with prefix | O(m + k) | k = number of results    |

**Space Complexity:** O(ALPHABET_SIZE × m × n) — can be large

### Trie vs Hash Table (String Storage)
| Aspect            | Trie            | Hash Table                       |
|-------------------|-----------------|----------------------------------|
| Prefix search     | O(m) ✓          | O(n) (must scan all keys) ✗      |
| Space             | More (tree)     | Less                             |
| Sorted output     | Yes (DFS) ✓     | No ✗                             |
| Exact match       | O(m)            | O(1) average                     |

### Applications
- Autocomplete / type-ahead search
- Spell checker
- IP routing (Longest Prefix Matching)
- Dictionary implementation
- Phone directory

### ⚠️ Common Exam Traps
- Trie search is O(m) where m = string length, **independent of number of strings**.
- Each node has up to 26 children (for lowercase letters) → high space usage.
- End-of-word marker is essential — "car" vs "card" differ only at end marker.

> ### 📌 MUST REMEMBER
> - All ops: **O(m)** where m = string length (independent of n)
> - Best for **prefix matching and autocomplete**
> - Space-efficient alternative: **Compressed Trie (Patricia/Radix Trie)**

---

## 18. GRAPH

**Definition:** A set of vertices (V) and edges (E) connecting pairs of vertices. Can be directed or undirected, weighted or unweighted.

### Diagram
```
Undirected Graph:        Directed Graph (Digraph):
   A ─── B                  A ──→ B
   │     │                  │     │
   │     │                  ↓     ↓
   C ─── D                  C ──→ D

Weighted Graph:
   A ──5── B
   │       │
   3       2
   │       │
   C ──4── D
```

### Graph Representations
```
Graph: A-B, A-C, B-D (undirected)

Adjacency Matrix (V×V):
     A  B  C  D
  A [0, 1, 1, 0]
  B [1, 0, 0, 1]
  C [1, 0, 0, 0]
  D [0, 1, 0, 0]

Adjacency List:
  A → [B, C]
  B → [A, D]
  C → [A]
  D → [B]

Incidence Matrix (V×E): rows=vertices, cols=edges; 1 if vertex is endpoint of edge
```

### Representation Comparison
| Aspect             | Adjacency Matrix | Adjacency List |
|--------------------|------------------|----------------|
| Space              | O(V²)            | O(V + E)       |
| Check edge (u,v)   | O(1)             | O(degree(u))   |
| Find all neighbors | O(V)             | O(degree(u))   |
| Best for           | Dense graphs     | Sparse graphs  |
| Add edge           | O(1)             | O(1)           |

### Graph Terminology
| Term               | Definition                                                    |
|--------------------|---------------------------------------------------------------|
| Degree             | Number of edges incident to a vertex (undirected)             |
| In-degree          | Number of edges coming INTO a vertex (directed)               |
| Out-degree         | Number of edges going OUT of a vertex (directed)              |
| Path               | Sequence of vertices connected by edges                       |
| Cycle              | Path that starts and ends at the same vertex                  |
| Connected Graph    | Every vertex reachable from every other vertex                |
| Strongly Connected | Directed: every vertex reachable from every other (both ways) |
| DAG                | Directed Acyclic Graph — no cycles                            |
| Spanning Tree      | Subgraph containing all vertices with V-1 edges, no cycles    |

### Graph Algorithms Quick Reference
| Algorithm              | Use Case                     | Complexity       |
|------------------------|------------------------------|------------------|
| BFS                    | Shortest path (unweighted)   | O(V + E)         |
| DFS                    | Cycle detection, topology    | O(V + E)         |
| Dijkstra               | Shortest path (weighted, +ve)| O((V+E) log V)   |
| Bellman-Ford           | Shortest path (negative wts) | O(VE)            |
| Floyd-Warshall         | All-pairs shortest path      | O(V³)            |
| Prim's                 | Minimum Spanning Tree        | O(E log V)       |
| Kruskal's              | Minimum Spanning Tree        | O(E log E)       |
| Topological Sort       | DAG ordering                 | O(V + E)         |

### ⚠️ Common Exam Traps
- Handshaking Lemma: **Sum of all degrees = 2 × |E|** (each edge counted twice).
- In a **complete graph Kₙ**: edges = n(n-1)/2.
- BFS finds **shortest path** in unweighted graphs; **not** in weighted graphs.
- Dijkstra fails with **negative weight edges** — use Bellman-Ford instead.
- Topological sort only possible in **DAGs** (no cycles, directed).

> ### 📌 MUST REMEMBER
> - Sum of degrees = **2|E|** (Handshaking Lemma)
> - Kₙ edges = **n(n-1)/2**
> - BFS → shortest path (unweighted) | Dijkstra → shortest path (weighted, positive)
> - Adj Matrix: **O(V²)** space | Adj List: **O(V+E)** space

---

## QUICK REFERENCE — ALL DATA STRUCTURES

| Data Structure  | Access    | Search   | Insert   | Delete   | Space  |
|-----------------|-----------|----------|----------|----------|--------|
| Array           | O(1)      | O(n)     | O(n)     | O(n)     | O(n)   |
| Dynamic Array   | O(1)      | O(n)     | O(1)*    | O(n)     | O(n)   |
| Singly LL       | O(n)      | O(n)     | O(1)**   | O(n)     | O(n)   |
| Doubly LL       | O(n)      | O(n)     | O(1)**   | O(1)***  | O(n)   |
| Stack           | O(n)      | O(n)     | O(1)     | O(1)     | O(n)   |
| Queue           | O(n)      | O(n)     | O(1)     | O(1)     | O(n)   |
| Hash Table      | N/A       | O(1)avg  | O(1)avg  | O(1)avg  | O(n)   |
| BST (balanced)  | N/A       | O(log n) | O(log n) | O(log n) | O(n)   |
| BST (skewed)    | N/A       | O(n)     | O(n)     | O(n)     | O(n)   |
| AVL Tree        | N/A       | O(log n) | O(log n) | O(log n) | O(n)   |
| Heap            | O(1)top   | O(n)     | O(log n) | O(log n) | O(n)   |
| Trie            | N/A       | O(m)     | O(m)     | O(m)     | O(nm)  |
| Graph (Adj Mat) | O(1)      | O(1)     | O(1)     | O(V²)    | O(V²)  |
| Graph (Adj Lst) | O(deg)    | O(deg)   | O(1)     | O(deg)   | O(V+E) |

> \* Amortized | \*\* At head | \*\*\* Given node reference

---

## FINAL EXAM CHEAT SHEET

```
┌─────────────────────────────────────────────────────────────────┐
│                    DS EXAM CHEAT SHEET                          │
├────────────────┬────────────────────────────────────────────────┤
│ BFS            │ Queue, O(V+E), shortest path (unweighted)      │
│ DFS            │ Stack/Recursion, O(V+E), cycle detection       │
│ Dijkstra       │ Min-PQ, O((V+E)logV), no negative edges        │
│ Prim's         │ Min-PQ, O(E log V), MST for dense graphs       │
│ Kruskal's      │ Union-Find, O(E log E), MST for sparse graphs  │
│ Heap Build     │ O(n) — NOT O(n log n)                          │
│ Heap Sort      │ O(n log n), NOT stable, IN-PLACE               │
│ AVL rotations  │ LL→R, RR→L, LR→LR, RL→RL                      │
│ BST inorder    │ Always gives sorted output                     │
│ Hash worst     │ O(n) — all keys collide                        │
│ B+ Tree        │ Leaves linked, used in databases               │
│ Trie ops       │ O(m) — m=string length, not n                  │
│ Handshaking    │ Σdegrees = 2|E|                                │
└────────────────┴────────────────────────────────────────────────┘
```
