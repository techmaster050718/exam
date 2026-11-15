# Computer Architecture — Revision Notes
> **Exam Focus:** Concepts, formulas, ASCII diagrams, and traps for competitive/government exams.
> Last Updated: 2026-11-15

---

## Architecture command map
| Domain | Core recall points |
| :--- | :--- |
| CPU organization | ALU, CU, registers, buses, instruction cycle |
| Memory hierarchy | Registers, cache, RAM, SSD, HDD, latency and hierarchy |
| Cache design | Direct, associative, set-associative, write policies |
| Performance | Hit time, miss penalty, AMAT, cache trade-offs |
| Exam focus | Functional block diagrams, mapping rules, memory reasoning |

---

## 1. Basic Computer Organization

### Block Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        C P U                                        │
│  ┌─────────────────────────┐   ┌────────────────────────────────┐  │
│  │   Control Unit (CU)     │   │  Arithmetic & Logic Unit (ALU) │  │
│  │  - Fetch, Decode,       │◄──►│  - ADD, SUB, MUL, DIV         │  │
│  │    Execute control      │   │  - AND, OR, NOT, XOR           │  │
│  └──────────┬──────────────┘   └──────────────┬─────────────────┘  │
│             │                                  │                    │
│  ┌──────────▼──────────────────────────────────▼─────────────────┐ │
│  │                     Registers                                  │ │
│  │   PC | IR | MAR | MDR | ACC | SP | PSW                        │ │
│  └────────────────────────────┬──────────────────────────────────┘ │
└───────────────────────────────┼─────────────────────────────────────┘
                                │  System Bus (Address + Data + Control)
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
   ┌────▼─────┐           ┌─────▼──────┐         ┌──────▼──────┐
   │  Memory  │           │   I/O Ctrl │         │  Secondary  │
   │  (RAM)   │           │  Keyboard  │         │  Storage    │
   │          │           │  Monitor   │         │  HDD/SSD    │
   └──────────┘           │  Printer   │         └─────────────┘
                          └────────────┘
```

### Component Roles

| Component | Full Name | Role |
|-----------|-----------|------|
| CPU | Central Processing Unit | Executes instructions |
| ALU | Arithmetic & Logic Unit | Performs arithmetic and logic operations |
| CU | Control Unit | Directs operation of CPU; generates control signals |
| MAR | Memory Address Register | Holds address of memory location to access |
| MDR | Memory Data Register | Holds data to be read/written from/to memory |
| PC | Program Counter | Holds address of next instruction to fetch |
| IR | Instruction Register | Holds currently executing instruction |
| ACC | Accumulator | Stores result of ALU operations |
| SP | Stack Pointer | Points to top of current stack |
| PSW | Program Status Word | Holds status/flag bits (Z, N, C, V) |

### Buses

| Bus | Carries | Direction |
|-----|---------|-----------|
| Address Bus | Memory address | CPU → Memory (unidirectional) |
| Data Bus | Actual data | Bidirectional |
| Control Bus | Signals (READ/WRITE/IRQ) | Bidirectional |

> **⚠️ Exam Trap:** Address bus width determines **addressable memory** (n-bit bus → 2ⁿ locations). Data bus width determines **word size** per transfer.

---

## 2. Instruction Cycle (Fetch–Decode–Execute–Store)

```
   ┌─────────────┐
   │   FETCH     │  PC → MAR → Memory → MDR → IR; PC = PC+1
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │   DECODE    │  CU interprets opcode in IR
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │   EXECUTE   │  ALU performs operation; result in ACC/register
   └──────┬──────┘
          ▼
   ┌─────────────┐
   │   STORE     │  Write-back result to register or memory
   └──────┬──────┘
          │
          └────────► Loop back to FETCH
```

### Detailed Steps

1. **Fetch:** PC → MAR; Memory[MAR] → MDR; MDR → IR; PC++
2. **Decode:** CU reads opcode field of IR; determines operation and operand addresses
3. **Execute:** ALU performs computation or CU initiates I/O/branch
4. **Store (Write-back):** Result stored in destination register or memory via MDR/MAR

> **⚠️ Exam Trap:** PC is incremented **during Fetch**, not after Execute. Some architectures increment by instruction size (e.g., 4 bytes for 32-bit instructions).

---

## 3. Registers — Detailed Reference

| Register | Name | Size (typical) | Purpose |
|----------|------|---------------|---------|
| PC | Program Counter | 32/64-bit | Address of next instruction |
| IR | Instruction Register | Instruction width | Currently fetched instruction |
| MAR | Memory Address Register | Address bus width | Address sent to memory |
| MDR | Memory Data Register | Data bus width | Data to/from memory |
| ACC | Accumulator | Word size | ALU result storage |
| SP | Stack Pointer | 32/64-bit | Top of stack |
| BP/FP | Base/Frame Pointer | 32/64-bit | Stack frame reference |
| PSW | Program Status Word | 8–32-bit | Flags: Z/N/C/V/I |

### PSW / FLAGS Register

```
 Bit:  7    6    5    4    3    2    1    0
      ┌────┬────┬────┬────┬────┬────┬────┬────┐
      │ S  │ Z  │ AC │  - │  - │ PF │  - │ CF │
      └────┴────┴────┴────┴────┴────┴────┴────┘
       Sign Zero Aux        Parity    Carry
```

| Flag | Meaning |
|------|---------|
| Z (Zero) | Result is zero |
| N/S (Sign) | Result is negative |
| C (Carry) | Carry out of MSB (unsigned overflow) |
| V (Overflow) | Signed arithmetic overflow |
| I (Interrupt) | Interrupt enable |

---

## 4. Memory Hierarchy

```
      Speed ▲          Cost ▲         Size ▼
            │               │              │
     ┌──────┴──┐            │              │
     │Registers│  < 1 ns    │ $$$$$        │ Bytes (< 1 KB)
     └────┬────┘            │              │
          │                 │              │
     ┌────┴────┐            │              │
     │  Cache  │  1–10 ns   │ $$$$         │ KB – MB
     │ L1/L2/L3│            │              │
     └────┬────┘            │              │
          │                 │              │
     ┌────┴────┐            │              │
     │   RAM   │  60–100 ns │ $$           │ GB
     │  (DRAM) │            │              │
     └────┬────┘            │              │
          │                 │              │
     ┌────┴────┐            │              │
     │   HDD   │  5–10 ms   │ $            │ TB
     │  /SSD   │            ▼              ▼
     └─────────┘
```

### Comparison Table

| Level | Technology | Access Time | Typical Size | Volatile? |
|-------|------------|-------------|--------------|-----------|
| Registers | Flip-flops | < 1 ns | 32–256 bytes | Yes |
| L1 Cache | SRAM | 1–4 ns | 32–64 KB | Yes |
| L2 Cache | SRAM | 4–12 ns | 256 KB – 1 MB | Yes |
| L3 Cache | SRAM | 10–40 ns | 4–64 MB | Yes |
| Main Memory (RAM) | DRAM | 60–120 ns | 4–128 GB | Yes |
| SSD | Flash | 50–150 µs | 128 GB – 4 TB | No |
| HDD | Magnetic | 5–15 ms | 500 GB – 20 TB | No |
| Optical/Tape | Optical/Mag | Seconds | Very large | No |

> **⚠️ Exam Trap:** Cache is SRAM (fast, expensive); RAM is DRAM (slower, cheap). SSD is **non-volatile** but much faster than HDD.

---

## 5. Cache Memory

### Mapping Techniques

#### Direct Mapping
- Each RAM block maps to **exactly one** cache line
- Formula: `Cache line = Block number mod (Number of cache lines)`
- **Pros:** Simple, cheap
- **Cons:** High conflict misses

```
RAM Block 0  → Cache Line 0
RAM Block 1  → Cache Line 1
RAM Block 4  → Cache Line 0  (conflict!)
RAM Block 5  → Cache Line 1  (conflict!)
```

#### Fully Associative Mapping
- Any RAM block can go to **any** cache line
- Uses tag comparison across all lines (expensive hardware)
- **Pros:** No conflict misses
- **Cons:** Complex, slow lookup, expensive

#### Set-Associative Mapping (Best of both)
- Cache divided into **sets**; each set has **k ways**
- k-way set associative: block maps to a set, can go in any of k ways
- Formula: `Set = Block number mod (Number of sets)`
- Common: 2-way, 4-way, 8-way

```
4-way Set-Associative:
Set 0: [Way 0] [Way 1] [Way 2] [Way 3]
Set 1: [Way 0] [Way 1] [Way 2] [Way 3]
```

### Write Policies

| Policy | Description | Pros | Cons |
|--------|-------------|------|------|
| Write-Through | Write to cache AND memory simultaneously | Always consistent | Slower writes, more bus traffic |
| Write-Back | Write only to cache; write to memory on eviction | Faster writes | Inconsistency risk; dirty bit needed |
| Write-Around | Write directly to memory, bypass cache | Good for non-reusable data | Cache misses on next read |

### Hit Rate & AMAT

```
Hit Rate (h) = Cache Hits / Total Accesses

AMAT = Hit Time + Miss Rate × Miss Penalty
     = h × Tc + (1-h) × Tm

Where:
  Tc = Cache access time
  Tm = Main memory access time
  h  = Hit rate
```

> **⚠️ Exam Trap:** Higher hit rate → lower AMAT. Improving hit rate from 90% to 99% has much bigger impact than 80% to 90%.

### Replacement Policies

| Policy | Description |
|--------|-------------|
| LRU | Least Recently Used — replace block unused longest |
| FIFO | First In First Out |
| LFU | Least Frequently Used |
| Random | Random eviction |

---

## 6. Pipelining

### 5-Stage RISC Pipeline

```
Stage:  IF      ID      EX      MEM     WB
        ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
Cycle 1 │I1 │   │   │   │   │   │   │   │   │
Cycle 2 │I2 │   │I1 │   │   │   │   │   │   │
Cycle 3 │I3 │   │I2 │   │I1 │   │   │   │   │
Cycle 4 │I4 │   │I3 │   │I2 │   │I1 │   │   │
Cycle 5 │I5 │   │I4 │   │I3 │   │I2 │   │I1 │  ← Full pipeline
        └───┘   └───┘   └───┘   └───┘   └───┘
```

| Stage | Name | Action |
|-------|------|--------|
| IF | Instruction Fetch | Fetch instruction from memory using PC |
| ID | Instruction Decode | Decode opcode, read registers |
| EX | Execute | ALU performs computation |
| MEM | Memory Access | Read/write data memory |
| WB | Write Back | Write result to register file |

### Speedup Formula

```
Speedup = n × k / (k + n - 1)

Where:
  n = Number of instructions
  k = Number of pipeline stages

For large n: Speedup ≈ k (ideal speedup = number of stages)
```

### Pipeline Hazards

#### Data Hazards
- **RAW (Read After Write):** Instruction reads before previous writes → most common
- **WAR (Write After Read):** Write before previous read completes (anti-dependency)
- **WAW (Write After Write):** Two writes to same register, wrong order

```
RAW Example:
  ADD R1, R2, R3    ← Writes R1
  SUB R4, R1, R5   ← Reads R1 (before ADD writes!) → STALL needed
```

**Solutions:**
- **Forwarding/Bypassing:** Route result directly from EX/MEM to EX input (avoids most stalls)
- **Stalling (bubble insertion):** Insert NOPs until hazard clears
- **Out-of-order execution:** Reorder independent instructions

#### Structural Hazards
- Two instructions need same hardware resource simultaneously
- Example: Single memory port for IF and MEM stages

**Solution:** Duplicate hardware (separate instruction/data caches)

#### Control Hazards (Branch Hazards)
- Branch target unknown until EX or later; instructions after branch are fetched speculatively

**Solutions:**
- **Branch prediction:** Static (predict not-taken) or Dynamic (branch history table)
- **Delayed branching:** Execute instruction after branch regardless (branch delay slot)
- **Flushing:** Squash wrongly fetched instructions on misprediction

> **⚠️ Exam Trap:** Forwarding/Bypassing **cannot** resolve all data hazards — load-use hazard (LOAD followed immediately by instruction using result) always requires at least 1 stall.

---

## 7. Flynn's Taxonomy

```
                  Single Data    Multiple Data
                  ──────────     ─────────────
Single Instr.  │   SISD       │    SIMD       │
               │  (Serial CPU)│  (GPU/SIMD)   │
Multiple Instr.│   MISD       │    MIMD       │
               │  (Rare/FT)   │  (Multi-core) │
```

| Class | Streams | Description | Example |
|-------|---------|-------------|---------|
| SISD | 1 instr, 1 data | Sequential, single processor | Traditional uniprocessor |
| SIMD | 1 instr, multiple data | Same operation on many data elements | GPU, Intel SSE/AVX, vector processors |
| MISD | Multiple instr, 1 data | Multiple operations on same data | Fault-tolerant systems, rare |
| MIMD | Multiple instr, multiple data | Multiple processors, independent | Multi-core CPUs, clusters, distributed |

> **⚠️ Exam Trap:** MISD is rare and mostly theoretical (some fault-tolerant pipelines). MIMD is the most common modern parallel architecture.

---

## 8. Number Systems

### Conversion Quick Reference

| Decimal | Binary | Octal | Hexadecimal |
|---------|--------|-------|-------------|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 8 | 1000 | 10 | 8 |
| 10 | 1010 | 12 | A |
| 15 | 1111 | 17 | F |
| 16 | 10000 | 20 | 10 |
| 255 | 11111111 | 377 | FF |

### Conversion Rules

```
Binary → Octal:   Group bits in 3 from right
  11010110  →  011 010 110  →  3  2  6  →  326₈

Binary → Hex:     Group bits in 4 from right
  11010110  →  1101 0110  →  D  6  →  D6₁₆

Decimal → Binary: Repeated division by 2 (read remainders bottom-up)
  13 ÷ 2 = 6 R 1
   6 ÷ 2 = 3 R 0
   3 ÷ 2 = 1 R 1
   1 ÷ 2 = 0 R 1  → 13 = 1101₂
```

### 1's and 2's Complement (for signed integers)

```
For N-bit representation of -X:

1's Complement: Flip all bits of X
  +5 = 0101  →  1's complement = 1010

2's Complement: Flip all bits, then add 1
  +5 = 0101  →  flip → 1010  → +1 → 1011 = -5

Range:
  1's complement: -(2^(n-1) - 1) to +(2^(n-1) - 1)  [two zeros!]
  2's complement: -2^(n-1) to +(2^(n-1) - 1)         [one zero, most common]
```

### IEEE 754 Floating Point

```
Single Precision (32-bit):
┌───┬────────────┬──────────────────────────────┐
│ S │  Exponent  │         Mantissa             │
│ 1 │   8 bits   │          23 bits             │
└───┴────────────┴──────────────────────────────┘

Value = (-1)^S × 1.Mantissa × 2^(Exponent - 127)
                                    ↑
                             Bias = 127 (single), 1023 (double)

Double Precision (64-bit): 1 sign + 11 exp + 52 mantissa
```

| Format | Sign | Exponent | Mantissa | Bias | Range |
|--------|------|----------|----------|------|-------|
| Single (float) | 1 | 8 | 23 | 127 | ±3.4×10³⁸ |
| Double (double) | 1 | 11 | 52 | 1023 | ±1.8×10³⁰⁸ |

> **⚠️ Exam Trap:** IEEE 754 has special values: ±0, ±Infinity, NaN. The implied leading 1 bit is **not stored** in the mantissa (normalized form).

---

## 9. Boolean Algebra

### Fundamental Laws

| Law | AND form | OR form |
|-----|----------|---------|
| Identity | A · 1 = A | A + 0 = A |
| Null | A · 0 = 0 | A + 1 = 1 |
| Idempotent | A · A = A | A + A = A |
| Complement | A · Ā = 0 | A + Ā = 1 |
| Involution | (Ā)̄ = A | — |
| Commutative | A·B = B·A | A+B = B+A |
| Associative | (A·B)·C = A·(B·C) | (A+B)+C = A+(B+C) |
| Distributive | A·(B+C) = AB+AC | A+(B·C) = (A+B)·(A+C) |
| Absorption | A·(A+B) = A | A+(A·B) = A |

### De Morgan's Theorems

```
(A · B)̄  =  Ā + B̄    "Break the bar, change the operator"
(A + B)̄  =  Ā · B̄
```

### Universal Gates

| Gate | Symbol | Why Universal? |
|------|--------|----------------|
| NAND | A↑B | NOT, AND, OR can all be built from NAND only |
| NOR | A↓B | NOT, AND, OR can all be built from NOR only |

```
Using NAND only:
  NOT A     = A NAND A
  A AND B   = NOT(A NAND B) = (A NAND B) NAND (A NAND B)
  A OR B    = (A NAND A) NAND (B NAND B)
```

### Karnaugh Map (K-Map) Method

```
2-variable K-Map:        3-variable K-Map:
       B  B̄                      BC
  A  │ AB │ AB̄│               ┌──┬──┬──┬──┐
  Ā  │ ĀB │ ĀB̄│          A  │00│01│11│10│
                           ───┼──┼──┼──┼──┤
4-variable K-Map:         0  │  │  │  │  │
         CD                   ├──┼──┼──┼──┤
    ┌────┬────┬────┬────┐  1  │  │  │  │  │
 AB │ 00 │ 01 │ 11 │ 10 │     └──┴──┴──┴──┘
────┼────┼────┼────┼────┤
 00 │    │    │    │    │
────┼────┼────┼────┼────┤
 01 │    │    │    │    │
────┼────┼────┼────┼────┤
 11 │    │    │    │    │
────┼────┼────┼────┼────┤
 10 │    │    │    │    │
    └────┴────┴────┴────┘
```

**K-Map Rules:**
1. Group 1s in powers of 2 (1, 2, 4, 8, 16...)
2. Groups must be rectangular (wrapping allowed)
3. Maximize group size, minimize number of groups
4. Each 1 must be covered by at least one group
5. SOP: Circle 1s → POS: Circle 0s

---

## 10. I/O Techniques

| Technique | How It Works | CPU Involvement | Use Case |
|-----------|-------------|-----------------|----------|
| Programmed I/O (Polling) | CPU continuously checks status register | Very high (busy-wait) | Simple/slow devices, real-time |
| Interrupt-driven I/O | Device sends interrupt signal when ready | Moderate (handle ISR) | Most general-purpose I/O |
| DMA (Direct Memory Access) | DMA controller handles transfer; interrupts CPU on completion | Low | High-speed bulk transfers (disk, network) |

### I/O Techniques — Detailed

#### Polling (Busy-Wait)
```
CPU:  Check → Check → Check → Check → Data Ready → Process
       ↑ wasteful CPU cycles
```
- CPU keeps looping until device is ready
- **Pro:** Simple, no interrupt overhead
- **Con:** Wastes CPU cycles; poor for slow devices

#### Interrupt-Driven I/O
```
CPU:  Start I/O → Continue other work →  [Interrupt!] → ISR → Resume
                                               ↑
                                         Device ready
```
- CPU initiates I/O, resumes other work, ISR called on interrupt
- **ISR (Interrupt Service Routine):** Handler executed on interrupt
- **Pro:** CPU can do useful work while waiting
- **Con:** Interrupt overhead; still needs CPU for each data word

#### DMA (Direct Memory Access)
```
CPU:  Init DMA (src, dest, count) → Other work → [Interrupt: done] → Resume
DMA:          ← transfers block of data directly to/from memory →
```
- DMA controller manages memory↔device transfers
- CPU programs DMA: source address, destination, byte count
- CPU only interrupted once at **end** of block transfer
- **Pro:** Minimal CPU involvement; best for large data transfers
- **Con:** DMA and CPU may contend for memory bus (cycle stealing)

> **⚠️ Exam Trap:** DMA still uses the system bus — it "steals" cycles from the CPU. This is called **cycle stealing**.

---

## ✅ MUST REMEMBER

```
╔══════════════════════════════════════════════════════════════════╗
║                COMPUTER ARCHITECTURE KEY FACTS                   ║
╠══════════════════════════════════════════════════════════════════╣
║  Registers → Cache → RAM → HDD  (speed ↓, size ↑, cost ↓)      ║
║  PC incremented DURING FETCH stage                               ║
║  2's complement: flip + add 1; range: -2^(n-1) to 2^(n-1)-1    ║
║  IEEE 754 single: 1+8+23 bits; bias = 127                       ║
║  NAND and NOR are universal gates                                ║
║  Pipeline speedup ≈ k (stages) for large n                      ║
║  Load-use hazard → minimum 1 stall even with forwarding          ║
║  Cache hit rate formula: hits / total accesses                   ║
║  AMAT = h·Tc + (1-h)·Tm                                         ║
║  DMA: bulk transfers, cycle stealing, one interrupt at end       ║
║  Flynn: SISD(serial), SIMD(GPU), MISD(rare), MIMD(multicore)   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## ⚡ 30-SECOND REVISION CARD

| Topic | Key Point |
|-------|-----------|
| ALU | Arithmetic + Logic ops |
| CU | Generates control signals |
| MAR | Address bus register |
| MDR | Data bus register |
| PC | Next instruction address (increments during fetch) |
| Cache Mapping | Direct < Set-Assoc < Fully Assoc (flexibility) |
| Write-Through | Slower but consistent |
| Write-Back | Faster, needs dirty bit |
| Pipeline Hazards | Data (RAW/WAR/WAW), Structural, Control |
| Forwarding | Fixes most RAW; not load-use |
| 2's Complement | Standard signed representation |
| DMA | Best for bulk I/O, one interrupt per block |
| K-Map | Group 1s in powers of 2, wrap edges |
| De Morgan's | Break bar, change operator |

---
*End of Computer Architecture Revision Notes*
