# Cyber Security Interview Revision

> Canonical category: **Cyber Security**. Authentication detail links to Backend; cloud IAM links to AWS & Cloud.

## OWASP Top 10
**What is it?** A prioritized list of common web application risks. **Key idea:** Risks are process and code defects, not a complete checklist. **Interview answer:** "I mitigate broken access control, injection, cryptographic failures, unsafe design, misconfiguration, vulnerable dependencies, and logging gaps through threat modeling and layered controls." **Example:** Require authorization checks on every object read. **Use:** Baseline security review. **Points:** Threat model, secure defaults, least privilege. **Follow-ups:** Zero Trust, secure SDLC.

## SQL Injection
**What is it?** An attacker changes SQL by injecting data into query text. **Key idea:** Parameterize queries and limit database privileges. **Interview answer:** "I never concatenate untrusted input into SQL; I use prepared statements and typed parameters." **Example:** A search box cannot change `WHERE name = ?` into a destructive query. **Use:** All database input. **Points:** Parameterization, allowlists, least privilege. **Follow-ups:** Stored procedures, error leakage.

## XSS
**What is it?** XSS executes attacker scripts in another user's browser. **Key idea:** Context-aware output encoding prevents script execution. **Interview answer:** "If a comment is rendered, I encode it for HTML and avoid unsafe DOM sinks." **Example:** `<script>` in a public review must remain text. **Use:** Any browser-rendered user content. **Points:** Stored, reflected, DOM XSS, CSP. **Follow-ups:** innerHTML, sanitization.

## CSRF
**What is it?** CSRF tricks an authenticated browser into making an unwanted request. **Key idea:** Validate origin and use anti-CSRF tokens or cookie protections. **Interview answer:** "I use SameSite cookies and server-issued CSRF tokens for state-changing requests." **Example:** A malicious page tries to transfer funds. **Use:** Cookie-authenticated applications. **Points:** Origin, token, SameSite, no sensitive actions by GET. **Follow-ups:** CSRF vs XSS.

## CORS
**What is it?** CORS controls which browser origins may read cross-origin responses. **Key idea:** CORS is browser policy, not server authentication. **Interview answer:** "I allow specific trusted origins and methods rather than wildcarding credentials." **Example:** `app.example.com` calls `api.example.com`. **Use:** Separate frontend and API origins. **Points:** Preflight, credentials, allowlists. **Follow-ups:** CORS vs CSRF.

## SSRF
**What is it?** SSRF makes a server fetch attacker-selected internal URLs. **Key idea:** Enforce destination, scheme, port, and redirect controls. **Interview answer:** "A URL preview service must reject loopback, private IP ranges, cloud metadata, and unsafe protocols." **Example:** Block `http://169.254.169.254`. **Use:** Webhooks, previews, imports. **Points:** DNS rebinding, allowlist, egress control. **Follow-ups:** Redirect handling.

## Input Validation
**What is it?** Input validation rejects data that is malformed, out of range, or unsafe before processing. **Key idea:** Validate at every trust boundary and fail clearly. **Interview answer:** "The server checks type, length, allowed values, and authorization rather than trusting client-side validation." **Example:** Reject negative transfer amounts or untrusted file types. **Use:** APIs and web forms. **Points:** Allowlists, schemas, canonicalization, server-side checks. **Follow-ups:** Validation vs sanitization. **Related:** OWASP Top 10 → SQL Injection.

## HTTPS & TLS
**What is it?** TLS encrypts and authenticates a network connection. **Key idea:** It protects confidentiality and integrity in transit. **Interview answer:** "HTTPS verifies the server certificate and encrypts application traffic." **Example:** Account login over HTTPS. **Use:** Internet APIs and browsers. **Points:** Certificates, chain validation, HSTS. **Follow-ups:** TLS handshake, certificates.

## Hashing & Encryption
**What is it?** Hashing creates a fixed digest; encryption provides reversible confidentiality. **Key idea:** Choose each primitive for the correct purpose. **Interview answer:** "I hash passwords with Argon2 and use authenticated encryption for sensitive stored fields." **Example:** Store a content digest while encrypting card data. **Use:** Integrity and confidentiality. **Points:** Salt, nonce, AEAD, no rolling custom crypto. **Follow-ups:** Symmetric vs asymmetric.

## Password Hashing
**What is it?** Passwords use a slow, salted one-way function. **Key idea:** Cost is tuned to resist guessing at scale. **Interview answer:** "I use Argon2id or bcrypt and never use plain MD5/SHA for password storage." **Example:** Login verifies a presented password against a stored hash. **Use:** Account systems. **Points:** Salt, memory cost, rehash, MFA. **Follow-ups:** Brute-force protection.

## Secure Sessions
**What is it?** Secure sessions rotate identifiers and protect server-side authentication state. **Key idea:** Invalidate old sessions after privilege changes. **Interview answer:** "I regenerate session IDs after login and clear sessions on logout or password reset." **Example:** Privilege escalation must invalidate stale sessions. **Use:** Cookie-based systems. **Points:** Rotation, expiry, HttpOnly, Secure, SameSite. **Follow-ups:** Session fixation.

## JWT Security
**What is it?** JWT security means validating every relevant claim and key lifecycle. **Key idea:** An algorithm or signature mismatch must be rejected. **Interview answer:** "I pin allowed algorithms, validate issuer and audience, use short expiry, and support key rotation." **Example:** Reject a token signed for another tenant. **Use:** Distributed authentication. **Points:** `alg=none`, key confusion, storage, revocation. **Follow-ups:** JWT vs opaque session.

## OAuth Security
**What is it?** OAuth security protects redirects, grants, and tokens. **Key idea:** PKCE and exact redirect URI matching reduce interception. **Interview answer:** "Public clients use Authorization Code with PKCE; the server validates state and exact redirects." **Example:** Native app OAuth login. **Use:** Third-party delegated access. **Points:** State, PKCE, scope, consent. **Follow-ups:** OpenID Connect.

## Secrets Management
**What is it?** Secrets management prevents credentials from leaking into code or logs. **Key idea:** Store centrally, rotate, and least-privilege access. **Interview answer:** "I inject database and API credentials from a secrets manager at runtime." **Example:** Rotate a deployed payment key without rebuilding code. **Use:** Production credentials. **Points:** Vault, environment isolation, rotation. **Follow-ups:** Secret in Git history.

## IAM & Least Privilege
**What is it?** Identity and access management maps principals to authorized actions and resources. **Key idea:** Grant only required scope and duration. **Interview answer:** "A worker may write only to one bucket prefix rather than administering storage." **Example:** Separate developer, deployer, and auditor roles. **Use:** Cloud and enterprise systems. **Points:** Roles, policies, MFA, JIT access. **Follow-ups:** RBAC vs ABAC. **Related:** AWS / Cloud — IAM.

## Security Headers & CSP
**What is it?** Browser security headers constrain scripts, framing, transport, and MIME behavior. **Key idea:** Fail closed for untrusted content. **Interview answer:** "A CSP allows only approved script origins and HSTS forces HTTPS." **Example:** Block inline scripts and framing. **Use:** Web applications. **Points:** CSP, HSTS, X-Frame-Options or frame-ancestors. **Follow-ups:** CSP nonce, report-only.

## Rate Limiting & DDoS
**What is it?** DDoS resilience combines filtering, scaling, and request limits. **Key idea:** Absorb cheap traffic and prioritize critical work. **Interview answer:** "A CDN and WAF absorb edge traffic while rate limits protect login and APIs." **Example:** Limit public search and captcha abusive login attempts. **Use:** Internet-facing services. **Points:** Edge protection, quotas, autoscaling, backpressure. **Follow-ups:** Volumetric vs application attacks.

## Dependency Scanning
**What is it?** Dependency scanning finds vulnerable or outdated third-party packages. **Key idea:** Pin, scan, and remediate dependencies in CI. **Interview answer:** "I scan lockfiles and container images, block critical findings, and verify fixes through tests." **Example:** Update a vulnerable JSON library. **Use:** Software supply chain. **Points:** SBOM, SCA, signed images. **Follow-ups:** False positives.

## Penetration Testing
**What is it?** Authorized testing attempts to discover exploitable weaknesses. **Key idea:** Test from an agreed scope and risk model. **Interview answer:** "A penetration test validates whether identified vulnerabilities can be chained into real impact." **Example:** Test object authorization and SSRF. **Use:** Before major releases or compliance audits. **Points:** Scope, rules, reporting, retest. **Follow-ups:** Vulnerability scan vs pentest.

## Prompt Injection
**What is it?** Prompt injection makes untrusted model input override instructions or access tools. **Key idea:** Treat model output as untrusted and constrain tools. **Interview answer:** "I separate instructions from retrieved text, require tool authorization, and validate final actions." **Example:** A document instructs an assistant to expose secrets. **Use:** AI assistants and agents. **Points:** Instruction hierarchy, egress control, human approval. **Follow-ups:** Indirect prompt injection.
