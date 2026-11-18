# Advanced System Design Revision

## Distributed Locks
**What is it?** A distributed lock ensures exclusive access across processes or hosts. **Interview answer:** "I use a lease with fencing tokens and a bounded TTL, because crashes can otherwise leave work running after lock loss." **Example:** One job processes a tenant. **Use:** Coordination. **Points:** TTL, fencing, split brain. **Follow-ups:** Database vs Redis lock.

## Leader Election
**What is it?** Leader election chooses one coordinator from replicas. **Interview answer:** "A quorum or consensus service grants a lease and steps down on lost majority." **Example:** Single batch scheduler. **Use:** Coordinator workflows. **Points:** Term, quorum, fencing. **Follow-ups:** Split brain.

## Service Discovery
**What is it?** Service discovery resolves logical service names to healthy network locations. **Interview answer:** "Registration and health checks update a registry, while clients or proxies consume it." **Example:** Kubernetes Service. **Use:** Dynamic instances. **Points:** Client vs server side, TTL. **Follow-ups:** DNS discovery.

## Outbox Pattern
**What is it?** Outbox stores domain changes and events in one transaction, then relays them. **Interview answer:** "The database write adds an outbox row atomically, and a worker publishes it exactly as reliably as delivery permits." **Example:** Order and event commit. **Use:** Reliable event publishing. **Points:** At-least-once, dedupe. **Follow-ups:** Inbox pattern.

## CQRS
**What is it?** CQRS separates command and query models. **Interview answer:** "Writes optimize invariants and reads use projections, even if initially backed by the same database." **Example:** Analytics leaderboard. **Use:** Different read/write needs. **Points:** Projection lag, complexity. **Follow-ups:** CQRS vs CQS.

## Event Sourcing
**What is it?** Event sourcing stores state changes as an append-only event history. **Interview answer:** "A projection rebuilds current state from events, preserving auditability." **Example:** Account ledger. **Use:** Audit and temporal models. **Points:** Replay, schema, snapshots. **Follow-ups:** Event sourcing vs CRUD.

## Two-Phase Commit
**What is it?** 2PC coordinates one transaction outcome across participants. **Interview answer:** "A coordinator asks all participants to prepare, then decides commit or abort." **Example:** Coordinated database resources. **Use:** Strong atomicity. **Points:** Blocking, coordinator failure. **Follow-ups:** Saga.

## URL Shortener Design
**Requirements:** Short unique links, redirect, analytics, expiry. **Components:** API, key generator, redirect cache, object or relational store, analytics stream. **Data flow:** Create assigns code and stores mapping; redirect normalizes code and fetches mapping. **Scale:** Cache reads, partition mappings, CDN and base62 capacity. **Failure:** Duplicate generation retry, cache miss fallback, expired links. **Trade-offs:** Short code collision handling, custom aliases, analytics loss. **Interview follow-ups:** 301 vs 302, hot links.

## Chat System Design
**Requirements:** Delivery, ordering, presence, history, media. **Components:** Gateway, chat service, WebSocket cluster, message store, queue, push service. **Data flow:** Send validates and stores message, publishes, pushes to online/offline users. **Scale:** Partition by conversation, fanout, read replicas. **Failure:** Duplicates and reconnect sequence. **Trade-offs:** Strong order, offline storage, fanout on write vs read. **Follow-ups:** Typing indicators, encryption.

## Notification System Design
**Requirements:** Multi-channel, templates, preferences, retry, dedupe. **Components:** API, scheduler, preference store, template service, channel workers. **Data flow:** Event creates notification records; workers render and send; provider callbacks update status. **Scale:** Partition queues and batch providers. **Failure:** DLQ, retry with backoff, idempotency. **Trade-offs:** Priority, latency, provider cost. **Follow-ups:** Alerting storms.
