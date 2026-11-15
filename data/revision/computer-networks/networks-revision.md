# Computer Networks – Complete Exam Revision Notes
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
* Block Size (Magic Number) = $256 - \text{Octet Value of Subnet Mask}$

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
2. **OSPF (Open Shortest Path First):** Link State, Dijkstra algorithm, Metric: Cost ($10^8 / \text{bandwidth}$), Classless, uses IP protocol 89.
3. **BGP (Border Gateway Protocol):** Path Vector, Inter-Autonomous System routing, operates over TCP port 179.
4. **ARP (Address Resolution Protocol):** Resolves IP $\to$ MAC address (Broadcast request, Unicast reply).
5. **DNS (Domain Name System):** Resolves Hostname $\to$ IP address (UDP/TCP port 53).
6. **DHCP DORA Process:** **D**iscover (Broadcast) $\to$ **O**ffer (Unicast/Broadcast) $\to$ **R**equest (Broadcast) $\to$ **A**cknowledge (Unicast). Uses UDP 67/68.

---

## 6. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Sliding Window Sizes:**
   * Stop-and-Wait: Sender $W_s = 1$, Receiver $W_r = 1$.
   * Go-Back-N: $W_s = 2^n - 1$, $W_r = 1$. Discards out-of-order packets.
   * Selective Repeat: $W_s = 2^{n-1}$, $W_r = 2^{n-1}$. Buffers out-of-order packets.
2. **TCP TIME_WAIT State:** Lasts $2 \times \text{MSL}$ (Maximum Segment Lifetime) to ensure the final ACK reached the server and flush lingering network packets.
3. **HTTP Status Codes:**
   * `200 OK`, `201 Created`
   * `301 Moved Permanently`, `304 Not Modified`
   * `400 Bad Request`, `401 Unauthorized` (needs credentials), `403 Forbidden` (authenticated but denied), `404 Not Found`
   * `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout`

### COMMON TRAPS
* ⚠️ **Trap 1:** 401 Unauthorized vs 403 Forbidden. 401 means "Who are you? (Authenticate)", 403 means "I know who you are, but you cannot enter (Authorize)".
* ⚠️ **Trap 2:** Assuming Hubs reduce collision domains. Hubs share one collision domain; Switches provide a dedicated collision domain per port!
