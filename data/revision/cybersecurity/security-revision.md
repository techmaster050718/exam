# Information Security & Cryptography Revision Notes
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. CRYPTOGRAPHIC ALGORITHMS OVERVIEW

| Algorithm | Category | Key Length | Block Size | Underlying Math Problem | Use Case |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **DES** | Symmetric Feistel | 56 bits | 64 bits | Substitution-Permutation | Legacy (Insecure) |
| **3DES** | Symmetric Feistel | 112 / 168 bits | 64 bits | Encrypt-Decrypt-Encrypt | Legacy banking |
| **AES** | Symmetric SPN | 128, 192, 256 bits | 128 bits | Galois Field arithmetic | Global standard (E-commerce, Wi-Fi) |
| **RSA** | Asymmetric | 2048 to 4096 bits | Variable | Prime Factorization of large $n=pq$ | Key exchange, Digital Signatures |
| **ECC** | Asymmetric | 256 to 384 bits | Variable | Discrete Logarithm on Elliptic Curves | High security with smaller keys (TLS 1.3) |
| **SHA-256** | Hash Function | 256-bit digest | 512-bit block | Merkle-Damgård construction | Integrity, Blockchain, Certificates |

### AES Transformation Rounds
* AES-128: 10 rounds
* AES-192: 12 rounds
* AES-256: 14 rounds
* *Round operations:* SubBytes, ShiftRows, MixColumns (omitted in final round), AddRoundKey.

---

## 2. DIGITAL SIGNATURES & PKI

```text
Sender Alice:
Message M ──> Hash Function ──> Digest D ──> Encrypt with Alice's PRIVATE Key ──> Digital Signature S
                                                                                       │
Receiver Bob receives (M, S):                                                          ▼
Signature S ──> Decrypt with Alice's PUBLIC Key ──> Decrypted Digest D1
Message M   ──> Hash Function ─────────────────────> Calculated Digest D2
              If D1 == D2 -> Message is Authentic, Unaltered, and Non-Repudiated!
```
* **Guarantees:** Integrity, Authentication, and Non-Repudiation (Alice cannot deny having sent it).

---

## 3. WEB APPLICATION SECURITY (OWASP TOP 10)

```text
┌──────────────────┬─────────────────────────────────────┬─────────────────────────────────────┐
│ Attack Vector    │ Mechanism                           │ Defenses                            │
├──────────────────┼─────────────────────────────────────┼─────────────────────────────────────┤
│ SQL Injection    │ Malicious SQL appended to input     │ Prepared Statements, Param Queries  │
│ Stored XSS       │ Malicious JS stored in server DB    │ Context-aware output encoding, CSP  │
│ Reflected XSS    │ Malicious JS in URL query parameter │ Input sanitization, CSP             │
│ CSRF             │ Forges unauthorized victim request   │ Anti-CSRF Synchronizer Tokens, SameSite│
│ SSRF             │ Server tricked into fetching internal│ URL allowlists, restrict loopback   │
└──────────────────┴─────────────────────────────────────┴─────────────────────────────────────┘
```

---

## 4. ZERO TRUST ARCHITECTURE & BANKING GOVERNANCE
* **Zero Trust Tenet:** "Never Trust, Always Verify". Perimeter defenses are inadequate; assume breach.
* **Core Controls:** Identity & Access Management (IAM), Multi-Factor Authentication (MFA), Micro-segmentation, Least Privilege Principle.
* **PCI-DSS:** Mandates that Sensitive Authentication Data (SAD) — specifically **CVV/CVC and Full Magnetic Stripe data** — must NEVER be stored post-authorization, even if encrypted.
* **RBI Mandate:** Banks must report critical cybersecurity breaches to RBI / CERT-In within **2 to 6 hours** of detection.
