# Backend Interview Revision

> Canonical category: **Backend**. Cyber and cloud modules reference this module instead of repeating it.

## REST APIs
**What is it?** A REST API exposes resources through HTTP methods and standardized status codes. **Key idea:** Use nouns for resources and HTTP verbs for operations. **Interview answer:** "REST is a resource-oriented API style. A shopping app uses GET to retrieve products, POST to create an order, PUT or PATCH to update it, and DELETE to remove it." **Real-life example:** A food-delivery app has `/restaurants`, `/orders`, and `/orders/{id}` resources. **When/why:** Use REST for widely compatible, cacheable, service-to-service or web/mobile communication. **Interview points:** Stateless, resource-oriented, JSON common, standard HTTP semantics. **Follow-ups:** REST vs RPC, pagination, versioning. **Related:** HTTP & Status Codes → API Versioning → Pagination.

## HTTP & Status Codes
**What is it?** HTTP is the application protocol for requests and responses. **Key idea:** 2xx success, 3xx redirect, 4xx client error, 5xx server failure. **Interview answer:** "I use 200 or 201 for successful reads or creations, 400 for invalid input, 401 for unauthenticated requests, 403 for insufficient permission, 404 for missing resources, and 429 for rate limits." **Example:** A payment API returns 202 for accepted processing and 503 when unavailable. **Use:** Define predictable API behavior. **Points:** GET generally safe, POST not necessarily idempotent, 401 vs 403. **Follow-ups:** Idempotency, caching, timeout handling.

## GraphQL
**What is it?** GraphQL lets a client choose the fields and relations it needs through a typed query. **Key idea:** One endpoint, explicit schema, client-defined response shape. **Interview answer:** "GraphQL reduces over-fetching and under-fetching, but it requires query limits and careful resolver security." **Example:** A profile screen requests a user and recent orders in one query. **Use:** Complex evolving client views. **Points:** Resolvers, N+1 problem, caching, introspection. **Follow-ups:** GraphQL vs REST, depth limits. **Related:** REST APIs → DataLoader → Rate Limiting.

## gRPC
**What is it?** gRPC is a high-performance RPC framework using HTTP/2 and Protocol Buffers. **Key idea:** Binary contracts between services. **Interview answer:** "I would use gRPC for tightly coupled internal microservices where typed contracts and streaming matter." **Example:** Checkout calls inventory or fraud services. **Use:** Low-latency internal communication. **Points:** Schema, streaming, HTTP/2, service discovery. **Follow-ups:** gRPC vs REST, backward-compatible schemas. **Related:** API Gateway → Microservices.

## JWT Authentication
**What is it?** JWT authentication uses a signed token containing claims to identify a caller. **Key idea:** Verify signature and claims; do not trust unverified payloads. **Interview answer:** "After login, the server issues a signed JWT with user identity and expiry; the client sends it on later requests. The server validates signature, issuer, audience, and expiry." **Example:** A mobile app sends a JWT to fetch account data. **Use:** Stateless distributed authentication. **Points:** Short access tokens, refresh rotation, secure storage, revocation. **Follow-ups:** JWT vs sessions, token theft. **Related:** Sessions & Cookies → OAuth 2.0 → JWT Security.

## OAuth 2.0
**What is it?** OAuth 2.0 delegates limited access to protected resources. **Key idea:** A client gets a scoped token without receiving the user's password. **Interview answer:** "OAuth separates authorization from authentication. A user authorizes a calendar app to access calendar data and receives scoped access through an authorization server." **Example:** Login with Google or third-party account access. **Use:** Consent-based third-party access. **Points:** Authorization Code + PKCE, scopes, redirect URI, token expiry. **Follow-ups:** OAuth vs OpenID Connect, redirect attacks. **Related:** JWT Authentication → Secure Sessions.

## Sessions & Cookies
**What is it?** Sessions associate a browser with server-side or signed state. **Key idea:** Cookies carry the session identifier, not the user's password. **Interview answer:** "After login, the server creates a session ID in an HttpOnly, Secure, SameSite cookie. Later requests retrieve server-side session state." **Example:** A logged-in banking portal. **Use:** Traditional web authentication and server control. **Points:** Session expiry, rotation, fixation, CSRF. **Follow-ups:** Sessions vs JWT, distributed session storage.

## Caching with Redis
**What is it?** Redis is an in-memory key-value store. **Key idea:** Cache frequent reads and manage fast-expiring state. **Interview answer:** "Redis can cache database results, sessions, counters, or queues. It greatly reduces latency and database load, but cached data needs expiry and invalidation." **Example:** Cache restaurant listings for a food-delivery app. **Use:** Low-latency reads and short-lived coordination. **Points:** TTL, eviction, cache stampede, persistence. **Follow-ups:** Redis vs database, cache invalidation. **Related:** Caching → Redis Data Types.

## Message Queues
**What is it?** A queue decouples producers and consumers through asynchronous messages. **Key idea:** Consumers process work later and acknowledge completion. **Interview answer:** "A checkout service publishes an order-created event; separate services send email and update analytics." **Example:** Image processing after upload. **Use:** Bursty work and asynchronous workflows. **Points:** At-least-once, duplicates, ordering, dead-letter queues. **Follow-ups:** Queue vs pub/sub, retries.

## Rate Limiting
**What is it?** Rate limiting restricts requests over a period. **Key idea:** Protect capacity and cost. **Interview answer:** "An API might allow 100 requests per minute per API key and return 429 when exceeded." **Example:** Login endpoint and public search API. **Use:** Abuse prevention and fair usage. **Points:** Token bucket, sliding window, distributed counters, 429 headers. **Follow-ups:** DDoS, per-user vs global limits. **Related:** Caching → Load Balancers.

## WebSockets
**What is it?** WebSockets provide persistent bidirectional communication. **Key idea:** Upgrade once, then send frames continuously. **Interview answer:** "I use WebSockets when the server must push updates with low latency, such as chat or live tracking." **Example:** Ride location updates. **Use:** Real-time chat, collaboration, markets. **Points:** Scaling, heartbeats, authentication, backpressure. **Follow-ups:** WebSockets vs SSE, reconnection.

## Background Jobs
**What is it?** Background jobs run work outside the request lifecycle. **Key idea:** Return quickly while workers execute later. **Interview answer:** "A document upload can return accepted while a worker generates thumbnails and extracts text." **Example:** Payment reconciliation and report generation. **Use:** Slow or retryable work. **Points:** Queue, retries, idempotency, visibility timeout. **Follow-ups:** Failure handling, duplicate execution.

## Webhooks
**What is it?** Webhooks are HTTP callbacks from a provider to an application. **Key idea:** Event-driven server-to-server notification. **Interview answer:** "A payment provider calls our HTTPS endpoint after a payment succeeds." **Example:** Stripe-like payment event, GitHub push event. **Use:** Third-party event integration. **Points:** Signing, replay protection, retries, idempotency. **Follow-ups:** Polling vs webhooks, endpoint security.

## Idempotency
**What is it?** An operation is idempotent when repeated calls have the same outcome. **Key idea:** Use keys and persist operation results. **Interview answer:** "A repeated payment request must not charge twice, so the server caches the result of each idempotency key." **Example:** Mobile payment retries. **Use:** Retries over unreliable networks. **Points:** GET, PUT, DELETE semantics, duplicate detection. **Follow-ups:** Idempotency vs exactly-once.

## File Uploads to S3
**What is it?** Objects are uploaded directly or indirectly to object storage. **Key idea:** Prefer presigned URLs and enforce limits. **Interview answer:** "The API validates metadata and returns a short-lived presigned URL; the client uploads directly, then triggers validation through an event." **Example:** Profile image and resume upload. **Use:** Large files and durable object storage. **Points:** Presigned URL, virus scan, encryption, lifecycle. **Follow-ups:** Multipart upload, CDN delivery.

## Pagination
**What is it?** Pagination divides large result sets into pages. **Key idea:** Cursor pagination is safer for changing data. **Interview answer:** "For infinite feeds, I use cursor pagination so updates do not skip or repeat records." **Example:** Social media feed. **Use:** Large lists and API stability. **Points:** Limit, offset, cursor, sort key. **Follow-ups:** Offset pagination trade-offs.

## API Versioning
**What is it?** Versioning manages incompatible API changes. **Key idea:** Additive changes should avoid unnecessary versions. **Interview answer:** "I preserve old fields and behavior or expose a new version while migrating consumers." **Example:** Mobile clients on older app versions. **Use:** Public or slow-changing clients. **Points:** URL/header negotiation, deprecation, compatibility. **Follow-ups:** Breaking vs backward-compatible changes.

## Input Validation
**What is it?** Validation rejects malformed or unsafe input at trust boundaries. **Key idea:** Validate type, range, format, and authorization. **Interview answer:** "An API validates required fields, size limits, enums, and ownership before processing." **Example:** Reject negative transfer amounts. **Use:** Security and predictable failures. **Points:** Allowlist, schemas, server-side checks. **Follow-ups:** Sanitization vs validation. **Related:** OWASP Top 10.

## Logging & Monitoring
**What is it?** Logs and metrics record system behavior. **Key idea:** Use structured telemetry and bounded retention. **Interview answer:** "I use a request ID, structured logs, latency/error metrics, and alerts based on service-level objectives." **Example:** Investigate payment failures by trace ID. **Use:** Diagnosis and capacity planning. **Points:** Metrics, logs, traces, privacy, cardinality. **Follow-ups:** Alert fatigue, sampling.

## Unit & Integration Tests
**What is it?** Unit tests isolate functions; integration tests verify connected components. **Key idea:** Test behavior and boundaries, not implementation details. **Interview answer:** "A unit test verifies pricing logic; an integration test verifies that the API stores an order and publishes a message." **Example:** Checkout regression suite. **Use:** Fast feedback and safer releases. **Points:** Test pyramid, mocks, fixtures, contracts. **Follow-ups:** E2E tests, flaky tests. **Related:** CI/CD Pipelines.
