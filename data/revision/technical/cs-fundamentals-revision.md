# CS Fundamentals Interview Revision

## Processes & Threads
**What is it?** A process owns resources and an address space; threads share it within the process. **Interview answer:** "Processes isolate faults and memory; threads are lighter but require synchronization." **Example:** A web server uses worker threads or processes. **Use:** Concurrency. **Points:** Context cost, isolation, shared memory. **Follow-ups:** Thread pool.

## Context Switching
**What is it?** Context switching saves and restores CPU execution state. **Interview answer:** "The kernel saves registers and scheduling state before restoring another task." **Example:** A blocked disk task yields CPU. **Use:** Multitasking. **Points:** Direct vs indirect cost, cache impact. **Follow-ups:** Process vs thread switch.

## CPU Scheduling
**What is it?** Scheduling decides which runnable process or thread uses CPU. **Interview answer:** "FCFS is simple, Round Robin gives fairness, and priority or shortest-job methods optimize goals." **Example:** Interactive and batch jobs. **Use:** OS resource allocation. **Points:** Turnaround, waiting, throughput. **Follow-ups:** Starvation.

## Concurrency & Locks
**What is it?** Concurrency interleaves tasks; locks serialize shared-state access. **Interview answer:** "I reduce shared mutation and protect critical sections by lock scope." **Example:** Bank balance update. **Use:** Parallel programs. **Points:** Mutex, semaphore, atomic. **Follow-ups:** Lock granularity.

## Deadlocks
**What is it?** Deadlock occurs when tasks hold resources while waiting for one another. **Interview answer:** "The four conditions are mutual exclusion, hold and wait, no preemption, and circular wait." **Example:** Two transactions lock opposite rows. **Use:** Resource concurrency. **Points:** Prevention, detection, timeout. **Follow-ups:** Livelock.

## Memory Management
**What is it?** Memory management allocates and protects address space. **Interview answer:** "The OS maps virtual addresses to physical frames and manages heap and stack." **Example:** Prevent one app from corrupting another. **Use:** Processes. **Points:** Allocation, fragmentation. **Follow-ups:** Paging.

## Virtual Memory & Paging
**What is it?** Virtual memory gives processes isolated address spaces and may store inactive pages on disk. **Interview answer:** "Page tables map virtual pages to frames; page faults load missing pages." **Example:** Running more applications than RAM. **Use:** Memory isolation. **Points:** TLB, demand paging, thrashing. **Follow-ups:** Segmentation.

## File Systems
**What is it?** File systems organize persistent data into files and directories. **Interview answer:** "They manage metadata, allocation, caching, journaling, and crash recovery." **Example:** fsync an append-only log. **Use:** Persistent storage. **Points:** Inode, journal, permissions. **Follow-ups:** Ext4 vs XFS.

## System Calls
**What is it?** System calls are controlled transitions from user mode to kernel services. **Interview answer:** "An application calls `open`, `read`, or `write` instead of directly manipulating hardware." **Example:** Read a configuration file. **Use:** OS access. **Points:** Mode switch, ABI. **Follow-ups:** Interrupts.

## OSI Model
**What is it?** OSI is a seven-layer conceptual network model. **Interview answer:** "Physical and data-link move frames; network routes packets; transport provides TCP or UDP; session, presentation, and application define higher behavior." **Example:** Trace an HTTPS request. **Use:** Troubleshooting. **Points:** Layers, encapsulation. **Follow-ups:** TCP/IP mapping.

## TCP vs UDP
**What is it?** TCP provides reliable ordered streams; UDP provides best-effort datagrams. **Interview answer:** "I use TCP for APIs and UDP for latency-tolerant or real-time traffic." **Example:** Video calls and file download. **Use:** Transport choice. **Points:** Retransmission, ordering, overhead. **Follow-ups:** QUIC.

## TCP Handshake
**What is it?** TCP establishes a connection with SYN, SYN-ACK, and ACK. **Interview answer:** "The handshake initializes sequence numbers and then data can flow." **Example:** Browser connects to HTTPS server. **Use:** Reliable sessions. **Points:** Three-way handshake, teardown. **Follow-ups:** SYN flood.

## IP & Subnets
**What is it?** IP addresses identify network locations; subnets divide address ranges. **Interview answer:** "CIDR notation defines the network prefix and available host range." **Example:** Allocate `10.0.1.0/24`. **Use:** Routing and segmentation. **Points:** Public/private, NAT. **Follow-ups:** IPv4 exhaustion.

## DNS
**What is it?** DNS maps names to records such as IP addresses. **Interview answer:** "A resolver caches an address returned by authoritative DNS and a client connects to it." **Example:** Resolve `api.example.com`. **Use:** Service discovery. **Points:** TTL, A/AAAA, CNAME. **Follow-ups:** DNS cache poisoning.

## HTTP/1.1 vs HTTP/2
**What is it?** HTTP/2 multiplexes binary frames over one connection. **Interview answer:** "HTTP/1.1 has connection and head-of-line constraints; HTTP/2 improves multiplexing and header compression." **Example:** Load many assets. **Use:** Web performance. **Points:** Multiplexing, server push. **Follow-ups:** HTTP/3.

## TLS Handshake
**What is it?** TLS establishes a secure authenticated session. **Interview answer:** "The client validates certificates and both sides derive shared session keys." **Example:** HTTPS login. **Use:** Secure transport. **Points:** Certificate, key exchange, forward secrecy. **Follow-ups:** Resumption.

## Sockets
**What is it?** Sockets expose network endpoints to applications. **Interview answer:** "An endpoint combines IP address and port; listen, accept, connect, send, and receive perform communication." **Example:** Chat server. **Use:** Network APIs. **Points:** TCP vs UDP socket, blocking. **Follow-ups:** Epoll.

## Compilers vs Interpreters
**What is it?** Compilers translate before execution; interpreters execute source or bytecode dynamically. **Interview answer:** "Compiled languages catch more static issues earlier, while interpreted runtimes offer flexibility." **Example:** Java compiles source to bytecode and the JVM interprets or JITs it. **Use:** Language implementation. **Points:** Lexing, parsing, optimization. **Follow-ups:** JIT.

## Garbage Collection
**What is it?** Garbage collection reclaims unreachable heap objects. **Interview answer:** "Tracing GC marks reachable objects and collects unreachable regions; pauses depend on algorithm." **Example:** Java service heap. **Use:** Managed runtimes. **Points:** Reference counting, tracing, generations. **Follow-ups:** GC pauses.

## Character Encoding
**What is it?** Encoding maps characters to bytes and decoding reverses it. **Interview answer:** "I use UTF-8 and state encoding at boundaries." **Example:** Store Hindi and emoji text. **Use:** Text storage and APIs. **Points:** Unicode, surrogate, normalization. **Follow-ups:** UTF-8 vs UTF-16.
