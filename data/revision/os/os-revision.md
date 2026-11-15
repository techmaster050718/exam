# Operating Systems — Exam Revision

> **Exam Focus:** Process Management, Scheduling, Synchronization, Memory, File Systems, I/O, Disk Scheduling
> Last Updated: 2026-11-15

---

## OS command map
| Domain | Core recall points |
| :--- | :--- |
| Process model | PCB, states, context switch, transitions |
| Scheduling | FCFS, SJF, SRTF, priority, RR, MLFQ |
| Synchronization | Race conditions, critical section, mutex, semaphores, deadlock |
| Memory | Paging, segmentation, virtual memory, TLB, page replacement |
| Storage & I/O | File systems, inode, disks, DMA, buffering |
| Exam focus | Definitions, algorithm trade-offs, didactic comparisons |

---

## 1. Process Management

### What is a Process?
A **process** is a program in execution. It is an active entity, while a program is a passive entity (stored on disk).

### Process Control Block (PCB)
The OS maintains a PCB (also called Task Control Block) for every process.

```
┌─────────────────────────────┐
│        Process Control Block│
├─────────────────────────────┤
│ Process ID (PID)            │
│ Process State               │
│ Program Counter (PC)        │
│ CPU Registers               │
│ CPU Scheduling Info         │
│ Memory Management Info      │
│ Accounting Information      │
│ I/O Status Information      │
└─────────────────────────────┘
```

| PCB Field | Contents |
|---|---|
| PID | Unique process identifier |
| State | New/Ready/Running/Waiting/Terminated |
| PC | Address of next instruction |
| Registers | Accumulators, index regs, stack pointer |
| Memory limits | Base/limit registers, page tables |
| Open files | List of open file descriptors |

### Process States & Transitions

```
                    ┌──────────────────────────────────────────────┐
                    │                                              │
   new ──(admitted)──▶ READY ◀──(I/O complete / event done)── WAITING
                        │  ▲                                      ▲
              (dispatch)│  │(preemption / time slice expires)     │
                        ▼  │                                      │
                      RUNNING ──────(I/O request / event wait)───┘
                        │
                (exit/terminate)
                        ▼
                    TERMINATED
```

| Transition | From → To | Trigger |
|---|---|---|
| Admitted | New → Ready | OS accepts process |
| Dispatch | Ready → Running | Scheduler picks process |
| Timeout/Preempt | Running → Ready | Time quantum expires |
| I/O Wait | Running → Waiting | Process requests I/O |
| I/O Complete | Waiting → Ready | I/O finishes |
| Exit | Running → Terminated | Process finishes |

### Context Switch
When the OS switches the CPU from one process to another:
1. Save state of current process into its PCB
2. Load state of new process from its PCB
3. **Overhead:** Pure overhead — no useful work during switch

> **⚠️ EXAM TRAP:** A process in the **Waiting** state cannot go directly to **Running**. It must go Waiting → Ready → Running.

---

## 2. CPU Scheduling

### Goals
- **Maximize:** CPU utilization, throughput
- **Minimize:** Waiting time, turnaround time, response time

### Key Terms
- **Arrival Time (AT):** When process arrives in ready queue
- **Burst Time (BT):** CPU time needed
- **Completion Time (CT):** When process finishes
- **Turnaround Time (TAT):** CT − AT
- **Waiting Time (WT):** TAT − BT
- **Response Time:** Time from arrival to first CPU response

---

### 2.1 FCFS (First Come First Served)
**Non-preemptive.** Processes served in arrival order.

**Example:**
| Process | AT | BT |
|---|---|---|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 1 |

**Gantt Chart:**
```
|  P1  |  P2  |P3|
0      5      8  9
```
| Process | CT | TAT | WT |
|---|---|---|---|
| P1 | 5 | 5 | 0 |
| P2 | 8 | 7 | 4 |
| P3 | 9 | 7 | 6 |

**Avg WT = (0+4+6)/3 = 3.33**

**⚠️ Convoy Effect:** A long process blocks all shorter processes behind it.
**Starvation:** None (everyone eventually runs).

---

### 2.2 SJF — Non-Preemptive (Shortest Job First)
**Non-preemptive.** Once CPU is given, process runs to completion.

**Example:**
| Process | AT | BT |
|---|---|---|
| P1 | 0 | 6 |
| P2 | 1 | 2 |
| P3 | 2 | 8 |
| P4 | 3 | 3 |

**Execution order at each decision point:**
- t=0: Only P1 available → run P1
- t=6: P2(BT=2), P3(BT=8), P4(BT=3) → pick P2
- t=8: P3, P4 → pick P4
- t=11: P3 → run P3

**Gantt Chart:**
```
|   P1   | P2 | P4 |    P3    |
0        6   8   11           19
```
**⚠️ Starvation:** Long processes may never run if short jobs keep arriving.
**Fix:** Aging — increase priority of waiting processes over time.

---

### 2.3 SRTF — Preemptive SJF (Shortest Remaining Time First)
**Preemptive.** A new process with shorter remaining burst time preempts the current.

**Example:**
| Process | AT | BT |
|---|---|---|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 2 |
| P4 | 3 | 1 |

**Gantt Chart:**
```
|P1|P2|P3|P4|P3|P2|   P1   |
0  1  2  4  5  6  10       17
```

---

### 2.4 Priority Scheduling
Each process has a priority number. **Lower number = Higher priority** (convention varies).

- **Preemptive:** New high-priority process preempts current
- **Non-Preemptive:** High-priority picked at each scheduling point
- **⚠️ Starvation:** Low-priority processes may starve
- **Fix:** Aging — priority of waiting process increases with time

---

### 2.5 Round Robin (RR)
**Preemptive.** Each process gets a fixed time quantum (q). After q expires, process goes to end of ready queue.

**Example (q=2):**
| Process | AT | BT |
|---|---|---|
| P1 | 0 | 5 |
| P2 | 0 | 3 |
| P3 | 0 | 2 |

**Gantt Chart:**
```
|P1|P2|P3|P1|P2|P1|
0  2  4  6  8  9  11
```
| Process | CT | TAT | WT |
|---|---|---|---|
| P1 | 11 | 11 | 6 |
| P2 | 9 | 9 | 6 |
| P3 | 6 | 6 | 4 |

**Key Points:**
- **Higher quantum** → approaches FCFS (larger convoy effect)
- **Lower quantum** → more context switches (overhead increases)
- **Optimal quantum** = 80% of processes should finish in one quantum
- No starvation; response time is good

---

### 2.6 MLFQ (Multi-Level Feedback Queue)
Multiple queues with different priorities and time quanta. Processes move between queues based on behavior.

```
Queue 1 (Highest priority, q=8ms)  → Interactive/I/O-bound
Queue 2 (q=16ms)                   → Medium
Queue 3 (Lowest priority, FCFS)    → CPU-bound
```
- New process enters Q1
- If it doesn't finish in q, it's demoted to Q2
- **Aging:** Process promoted if waiting too long (prevents starvation)

---

### Scheduling Algorithm Comparison

| Algorithm | Preemptive | Starvation | Convoy Effect | Optimal for |
|---|---|---|---|---|
| FCFS | No | No | Yes | Simple batch |
| SJF | No | Yes | No | Minimum avg WT |
| SRTF | Yes | Yes | No | Minimum avg WT (preemptive) |
| Priority | Both | Yes | No | Prioritized tasks |
| Round Robin | Yes | No | No | Time-sharing |
| MLFQ | Yes | No (w/ aging) | No | General purpose |

> **📌 MUST REMEMBER:**
> - **SJF** gives minimum average waiting time among non-preemptive
> - **SRTF** gives minimum average waiting time among all
> - **RR** gives best average response time
> - **FCFS** is FIFO — simple but can have convoy effect

---

## 3. Synchronization

### Race Condition
When two or more processes access shared data concurrently and the final outcome depends on the order of execution.

**Example:** Two threads incrementing `counter`:
```
Thread1: LOAD counter  (reads 5)
Thread2: LOAD counter  (reads 5)
Thread1: ADD 1 → 6, STORE
Thread2: ADD 1 → 6, STORE   ← Lost update! Should be 7
```

### Critical Section Problem
A code segment where shared resources are accessed. Must satisfy:
1. **Mutual Exclusion:** Only one process in CS at a time
2. **Progress:** If no process is in CS, one of the waiting processes must enter (no deadlock outside CS)
3. **Bounded Waiting:** A process must enter CS within finite time (no starvation)

---

### 3.1 Mutex (Mutual Exclusion Lock)
Binary lock — either locked or unlocked. Only the owner can unlock.

```
lock(mutex)
  /* Critical Section */
unlock(mutex)
```

### 3.2 Semaphore
Integer variable with two atomic operations:
- **wait(S) / P(S):** S = S−1; if S < 0, block
- **signal(S) / V(S):** S = S+1; if S ≤ 0, wake a blocked process

**Types:**
- **Binary Semaphore (0/1):** Works like mutex
- **Counting Semaphore:** Controls access to N resources

**Producer-Consumer with Semaphore:**
```
Semaphores: mutex=1, empty=N, full=0

Producer:                    Consumer:
wait(empty)                  wait(full)
wait(mutex)                  wait(mutex)
  add to buffer                remove from buffer
signal(mutex)                signal(mutex)
signal(full)                 signal(empty)
```

### 3.3 Monitors
High-level synchronization construct (OOP concept). Only one process active inside monitor at a time.
- **Condition variables:** `wait()` and `signal()` on conditions
- Java's `synchronized` keyword implements monitors

---

### 3.4 Deadlock

**Definition:** A set of processes are deadlocked if each process is waiting for a resource held by another process in the set.

**Coffman's Four Necessary Conditions:**
1. **Mutual Exclusion:** Resource held in non-sharable mode
2. **Hold and Wait:** Process holds ≥1 resources and waits for more
3. **No Preemption:** Resources cannot be forcibly taken
4. **Circular Wait:** P1 waits for P2, P2 waits for P3, ..., Pn waits for P1

> ⚠️ **ALL FOUR** conditions must hold simultaneously for deadlock

**Deadlock Handling:**
| Strategy | Description |
|---|---|
| Prevention | Negate one Coffman condition |
| Avoidance | Banker's Algorithm — check safe state before granting |
| Detection | Allow deadlock, detect and recover |
| Ignorance | Ostrich algorithm (Windows/Linux — restart) |

---

### Banker's Algorithm (Deadlock Avoidance)

**Data Structures (n processes, m resource types):**
- `Available[m]` — available instances of each resource type
- `Max[n][m]` — max demand of each process
- `Allocation[n][m]` — currently allocated
- `Need[n][m]` = Max − Allocation

**Safety Algorithm:**
```
1. Work = Available; Finish[i] = false for all i
2. Find i: Finish[i]=false AND Need[i] ≤ Work
3. Work = Work + Allocation[i]; Finish[i] = true; goto 2
4. If Finish[i]=true for all i → SAFE STATE
```

**Example:**
```
         Allocation  Max    Need   Available
         A  B  C    A B C  A B C  A=3 B=3 C=2

P0       0  1  0    7 5 3  7 4 3
P1       2  0  0    3 2 2  1 2 2
P2       3  0  2    9 0 2  6 0 0
P3       2  1  1    2 2 2  0 1 1
P4       0  0  2    4 3 3  4 3 1

Safe sequence: P1→P3→P4→P0→P2 ✓
```

---

## 4. Memory Management

### Logical vs Physical Address
- **Logical (Virtual) Address:** Generated by CPU; what process sees
- **Physical Address:** Actual RAM location
- **MMU (Memory Management Unit):** Translates logical → physical

### 4.1 Paging
Memory is divided into fixed-size blocks:
- **Page:** Fixed-size block of logical memory
- **Frame:** Fixed-size block of physical memory (same size as page)
- **Page Table:** Maps page number → frame number

```
Logical Address: | Page Number (p) | Offset (d) |
                        ↓
                    Page Table
                        ↓
Physical Address: | Frame Number (f) | Offset (d) |
```

**Address Calculation:**
- If page size = 2^n bytes, offset uses n bits
- Physical address = (frame_number × page_size) + offset

**TLB (Translation Lookaside Buffer):** Cache for page table entries
- **Effective Access Time (EAT)** = α(TLB time + memory time) + (1−α)(TLB time + 2×memory time)
  - α = TLB hit ratio

### 4.2 Segmentation
Memory divided into variable-size **segments** (code, stack, data, heap).
- Segment Table: Base address + Limit
- **Advantage:** Logical view matches programmer's view
- **Disadvantage:** External fragmentation

### Internal vs External Fragmentation
| Type | Cause | Solution |
|---|---|---|
| Internal | Allocated block > needed | Smaller pages/blocks |
| External | Free space scattered in small chunks | Compaction, paging |

---

### 4.3 Virtual Memory & Demand Paging

**Virtual Memory:** Allows process to use more memory than physically available. Pages loaded on demand.

**Page Fault:** When a referenced page is not in memory.
1. OS traps page fault
2. Find free frame (or evict using replacement algorithm)
3. Load page from disk
4. Update page table
5. Restart instruction

**Thrashing:** Process spends more time paging than executing. Occurs when too many processes compete for too few frames.

---

### 4.4 Page Replacement Algorithms

**Reference String for all examples:** 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 (3 frames)

---

**FIFO (First In First Out):**
Evict the page that has been in memory the longest.
```
Ref:  7  0  1  2  0  3  0  4  2  3  0  3  2
F1:   7  7  7  2  2  2  2  4  4  4  0  0  0
F2:   -  0  0  0  0  3  3  3  2  2  2  2  2
F3:   -  -  1  1  1  1  0  0  0  3  3  3  3
Fault:✓  ✓  ✓  ✓  -  ✓  ✓  ✓  ✓  ✓  ✓  -  -
Total faults: 10
```
**⚠️ Belady's Anomaly:** With FIFO, increasing frames can INCREASE page faults!

---

**Optimal (OPT):**
Evict the page that will not be used for the longest time in future. (Theoretical — needs future knowledge)
```
Ref:  7  0  1  2  0  3  0  4  2  3  0  3  2
F1:   7  7  7  2  2  2  2  2  2  2  2  2  2
F2:   -  0  0  0  0  0  0  4  4  4  0  0  0
F3:   -  -  1  1  1  3  3  3  3  3  3  3  3
Fault:✓  ✓  ✓  ✓  -  ✓  -  ✓  -  -  ✓  -  -
Total faults: 7 (minimum possible)
```

---

**LRU (Least Recently Used):**
Evict the page not used for the longest time in the past.
```
Total faults with above string: ~8
```
- No Belady's Anomaly (stack algorithm)
- Implementation: Counter or Stack

---

**LFU (Least Frequently Used):**
Evict the page with the smallest use count. Tie-break by LRU.
- Problem: Old pages with high counts never evicted

---

**Clock (Second Chance) Algorithm:**
FIFO + use bit. If use bit=1, give second chance (set to 0, move to end). If use bit=0, evict.

```
Page frames arranged in circle:
[7,1] → [0,1] → [1,0] → ↑clock hand
On fault: scan clockwise; if use=1, set to 0, move on; if use=0, replace
```

**Algorithm Comparison:**

| Algorithm | Faults | Belady's Anomaly | Implementation |
|---|---|---|---|
| FIFO | High | YES ⚠️ | Simple queue |
| Optimal | Lowest | No | Impossible (future) |
| LRU | Near optimal | No | Counter/Stack |
| LFU | Moderate | No | Frequency counter |
| Clock | Good | No | Circular list + bit |

> **📌 MUST REMEMBER:**
> - Only **FIFO** suffers Belady's Anomaly
> - **Optimal** is best but not implementable
> - **LRU** and OPT are **stack algorithms** — no Belady's Anomaly
> - **LRU approximation** in real OS: Clock/NRU algorithm

---

## 5. File Systems

### 5.1 File Concept
File = named collection of related information. Attributes: name, type, size, location, permissions, timestamps.

**File Operations:** Create, Read, Write, Seek, Delete, Open, Close

### 5.2 inode (Index Node) — Linux/Unix
An inode stores metadata about a file (NOT the file name or data).

```
┌─────────────────────────┐
│         inode           │
├─────────────────────────┤
│ File type & permissions │
│ Owner (UID, GID)        │
│ File size               │
│ Timestamps (atime/mtime)│
│ 12 Direct block pointers│
│ 1 Single indirect ptr   │ → Block of pointers → Data blocks
│ 1 Double indirect ptr   │ → Block of ptrs → Block of ptrs → Data
│ 1 Triple indirect ptr   │
└─────────────────────────┘
```

**Max file size calculation:**
- Block size = 4KB, pointer = 4 bytes → pointers/block = 1024
- Direct blocks: 12 × 4KB = 48KB
- Single indirect: 1024 × 4KB = 4MB
- Double indirect: 1024² × 4KB = 4GB
- Triple indirect: 1024³ × 4KB = 4TB

### 5.3 FAT (File Allocation Table)
Used in DOS/Windows (FAT12, FAT16, FAT32). Table maps cluster → next cluster.
- **FAT12:** 2^12 = 4096 clusters max
- **FAT32:** Clusters addressed with 32 bits (28 usable)
- Simple; no security; file name in directory entry (not separate structure)

### 5.4 NTFS (New Technology File System)
Windows default. Uses **MFT (Master File Table)** — a table with one record per file.
- Journaling (logs changes before writing)
- ACL-based security
- Supports file compression, encryption
- MFT records: standard info, file name, data, security descriptor

### 5.5 ext4 (Linux)
- Uses **extents** (contiguous block ranges) instead of block lists
- **Journal modes:** writeback, ordered (default), journal
- Max file size: 16TB; max volume: 1EB
- Delayed allocation, dir indexing (HTree)

### Directory Structure

| Structure | Description | Advantage |
|---|---|---|
| Single-level | All files in one directory | Simple |
| Two-level | Separate directory per user | No name conflicts across users |
| Tree-structured | Hierarchical path names | Flexible |
| Acyclic graph | Shared files via links | Sharing without duplication |
| General graph | Allows cycles | Maximum flexibility (needs garbage collection) |

> **📌 MUST REMEMBER:**
> - **inode** does NOT store filename — filename is in the directory entry
> - **Hard link:** Different filename, same inode; deleting one doesn't remove file
> - **Soft (symbolic) link:** New inode pointing to path; breaks if original deleted

---

## 6. I/O Management

### I/O Techniques

| Technique | Description | CPU Involvement |
|---|---|---|
| **Polling** | CPU continuously checks device status | 100% (wasteful) |
| **Interrupt-Driven** | Device sends interrupt when ready | Only during interrupt handler |
| **DMA (Direct Memory Access)** | DMA controller handles bulk transfer | Minimal (only setup + completion interrupt) |

### Buffering
Temporary storage to smooth speed mismatch between producer and consumer.
- **Single buffer:** While processing one buffer, device fills another
- **Double buffer:** Overlap I/O and computation
- **Circular buffer:** Multiple buffers in ring

### Spooling (Simultaneous Peripheral Operations On-Line)
- Used for slow devices (printers)
- Jobs queued in disk spool; device reads from spool
- Allows multiple processes to "print" simultaneously

### Device Drivers
Software interface between OS kernel and hardware device controller.

> **📌 MUST REMEMBER:**
> - **DMA** is used for **bulk data transfer** (disk, network)
> - **Interrupt** = device tells CPU "I'm ready"; **Polling** = CPU asks "are you ready?"
> - **Spooling** = disk acts as buffer for slow devices

---

## 7. Disk Scheduling

**Goal:** Minimize seek time (head movement across disk cylinders).

**Setup for all examples:**
- Disk cylinders: 0–199
- Head currently at cylinder: **53**
- Request queue: **98, 183, 37, 122, 14, 124, 65, 67**
- Direction: toward higher cylinders (unless noted)

---

### 7.1 FCFS
Serve in order of arrival.

**Sequence:** 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
```
Head movement: |98-53|+|183-98|+|37-183|+|122-37|+|14-122|+|124-14|+|65-124|+|67-65|
             = 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 cylinders
```

### 7.2 SSTF (Shortest Seek Time First)
Always serve the closest request to current head position.

**Sequence:** 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
```
Total movement: 12+2+30+23+84+24+2+59 = 236 cylinders
```
**⚠️ Starvation:** Requests far from current head position may starve.

### 7.3 SCAN (Elevator Algorithm)
Head moves in one direction serving all requests, then reverses.

**Sequence (moving toward 199):** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 37 → 14
```
Total: (199-53) + (199-14) = 146 + 185 = 331 cylinders
```

### 7.4 C-SCAN (Circular SCAN)
Like SCAN but after reaching end, jumps to beginning (no service on return).

**Sequence:** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
```
Provides more uniform wait time than SCAN
```

### 7.5 LOOK
Like SCAN but head only goes as far as the last request (doesn't go to end of disk).

**Sequence (toward high):** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 37 → 14
```
Total: (183-53) + (183-14) = 130 + 169 = 299 cylinders
```

### 7.6 C-LOOK
Like C-SCAN but only goes to last request, then jumps to smallest request.

**Sequence:** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 14 → 37

**Algorithm Comparison:**

| Algorithm | Total Movement | Starvation | Uniform Wait |
|---|---|---|---|
| FCFS | 640 | No | No |
| SSTF | 236 | Yes | No |
| SCAN | 331 | No | Near |
| C-SCAN | ~382 | No | Yes |
| LOOK | 299 | No | Near |
| C-LOOK | ~322 | No | Yes |

> **📌 MUST REMEMBER:**
> - **SSTF** ≈ best performance but can starve
> - **SCAN/LOOK** = elevator; **C-SCAN/C-LOOK** = more uniform
> - **LOOK** is better than **SCAN** (doesn't waste movement at disk ends)
> - Modern OS uses **C-LOOK** or **N-STEP LOOK**

---

## 📌 MASTER MUST-REMEMBER BOX

| Topic | Key Fact |
|---|---|
| PCB | Contains: PID, state, PC, registers, memory info, I/O info |
| Process States | New→Ready→Running→Waiting→Terminated |
| Context Switch | Pure overhead — saves/restores PCB |
| SJF | Minimum average waiting time (non-preemptive) |
| SRTF | Minimum average waiting time (all algorithms) |
| RR | Best average response time |
| Aging | Fixes starvation in Priority and SJF |
| Coffman | ME + Hold&Wait + No Preemption + Circular Wait → Deadlock |
| Banker's | Safety algorithm — finds safe sequence |
| Belady's Anomaly | FIFO only — more frames → more faults |
| LRU/OPT | Stack algorithms — no Belady's anomaly |
| inode | Has block pointers; filename stored in directory entry |
| DMA | Handles bulk transfer; CPU freed |
| SSTF | Best disk performance but starvation risk |
| Thrashing | Too many processes → excessive page faults |

---

## ⚡ 30-SECOND REVISION

```
PROCESS STATES: New → Ready ⇄ Running → Terminated
                              ↕
                           Waiting

SCHEDULING ORDER (Best avg WT):
  SRTF > SJF > MLFQ > RR > Priority > FCFS

PAGE REPLACEMENT:
  Optimal (best, impossible) > LRU ≈ LFU > Clock > FIFO
  Belady's Anomaly: FIFO only!

DEADLOCK: All 4 Coffman conditions MUST hold
  Break any one → prevent deadlock
  Banker's: Check safe state before granting

DISK: FCFS(simple) < SSTF(best,starvation) < LOOK < C-LOOK(uniform)

MEMORY: Paging=fixed size, Segmentation=variable size
  TLB hit → 1 mem access; miss → 2 mem accesses
```

---
*End of OS Revision | ~500 lines*
