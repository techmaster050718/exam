# High Level Design Revision

## Scalability
**What is it?** Scalability is the ability to handle added load through additional resources or efficiency. **Interview answer:** "I scale stateless components horizontally, split bottlenecks, and design for burst capacity." **Example:** Add API replicas for flash sales. **Use:** Growing systems. **Points:** Vertical vs horizontal, bottlenecks. **Follow-ups:** Scale limits.

## Load Balancing
**What is it?** A load balancer routes requests among healthy instances. **Interview answer:** "It reduces overload and removes failed targets through health checks." **Example:** L7 routing for `/api` and `/static`. **Use:** Availability. **Points:** Algorithms, health checks, sticky sessions. **Follow-ups:** Client-side vs server-side.

## Caching
**What is it?** Caching stores computed or frequently read data closer to consumers. **Interview answer:** "I cache immutable or slowly changing reads, set TTL, and define invalidation." **Example:** Cache popular product listings. **Use:** Latency and cost. **Points:** Cache-aside, write-through, stampede. **Follow-ups:** Redis as cache.

## CDN
**What is it?** A CDN caches content in geographically distributed edge locations. **Interview answer:** "Static assets and public responses are served from the nearest edge." **Example:** Stream video or deliver images. **Use:** Latency and origin load. **Points:** Cache key, TTL, purge. **Follow-ups:** Dynamic CDN.

## Database Sharding
**What is it?** Sharding partitions data across independent databases. **Interview answer:** "I shard only after query and growth analysis, using a stable shard key." **Example:** Partition tenants or user IDs. **Use:** Horizontal database scale. **Points:** Hot shard, resharding, cross-shard queries. **Follow-ups:** Sharding vs partitioning.

## Replication
**What is it?** Replication copies data among nodes. **Interview answer:** "A primary serves writes and replicas serve reads, but failover and lag need handling." **Example:** Read replicas for social feeds. **Use:** Availability and read scale. **Points:** Sync vs async, quorum. **Follow-ups:** Replication lag.

## Consistent Hashing
**What is it?** Consistent hashing minimizes remapping when nodes change. **Interview answer:** "Tokens map keys and nodes to a ring, so adding a node affects only nearby keys." **Example:** Cache cluster scaling. **Use:** Distributed partitions. **Points:** Virtual nodes, hotspots. **Follow-ups:** Rendezvous hashing.

## CAP Theorem
**What is it?** Under a network partition, a distributed system chooses consistency or availability for some operations. **Interview answer:** "CAP is a partition-time trade-off. A payment system may reject writes for consistency, while a feed may serve stale data for availability." **Example:** Banking ledger vs social feed. **Use:** Distributed design. **Points:** Partition, consistency, availability. **Follow-ups:** PACELC.

## PACELC
**What is it?** PACELC extends CAP by describing trade-offs even without partitions: latency vs consistency. **Interview answer:** "It asks consistency or availability during a partition and latency or consistency otherwise." **Example:** Choose synchronous or asynchronous replication. **Use:** Replication design. **Points:** Partition rule, normal trade-off. **Follow-ups:** Dynamo-style systems.

## Consistency Models
**What is it?** A consistency model defines how observed reads relate to writes. **Interview answer:** "Strong consistency shows the latest acknowledged write; eventual consistency converges and may temporarily show stale values." **Example:** Account balance vs activity feed. **Use:** Distributed state. **Points:** Linearizable, sequential, eventual. **Follow-ups:** Read-your-writes.

## Kafka & Pub/Sub
**What is it?** Kafka is a partitioned durable event log; pub/sub delivers events to subscribers. **Interview answer:** "Events are published to partitions, retained, and consumed by groups with offsets." **Example:** Order events feed inventory and analytics. **Use:** Streaming decoupling. **Points:** Partitions, offsets, replay. **Follow-ups:** Kafka vs RabbitMQ.

## Event-Driven Architecture
**What is it?** Components communicate by publishing facts and reacting to events. **Interview answer:** "An order service publishes `OrderPaid`; independent services react without direct calls." **Example:** Payment and notification workflows. **Use:** Loose coupling. **Points:** Schema, ordering, duplicate handling. **Follow-ups:** Eventual consistency.

## Microservices
**What is it?** Microservices are independently deployable domain services. **Interview answer:** "I use them only when team and scaling boundaries justify distributed overhead." **Example:** Payments and catalog services. **Use:** Large systems. **Points:** Ownership, contracts, failure. **Follow-ups:** Monolith vs microservices.

## API Gateway
**What is it?** An API gateway is a managed entry point for routing and cross-cutting policies. **Interview answer:** "It authenticates, rate limits, routes, and sometimes aggregates requests." **Example:** One public endpoint for mobile clients. **Use:** Edge service coordination. **Points:** Routing, auth, observability. **Follow-ups:** Gateway bottleneck.

## Rate Limiter Design
**What is it?** A distributed rate limiter counts allowed actions over time. **Interview answer:** "I use a token bucket in Redis or a managed edge and include retry information." **Example:** Limit login attempts. **Use:** Abuse prevention. **Points:** Atomic counters, quotas, fairness. **Follow-ups:** Sliding window.

## Bloom Filter
**What is it?** A Bloom filter is a probabilistic set test with no false negatives. **Interview answer:** "It quickly rejects keys that are definitely absent, saving cache or disk lookup." **Example:** Avoid disk reads for unknown usernames. **Use:** Memory-efficient membership. **Points:** False positives, sizing. **Follow-ups:** Bloom vs cache.

## Circuit Breaker
**What is it?** A circuit breaker stops calls to failing dependencies to give them recovery time. **Interview answer:** "After an error threshold, it opens and fails fast until a trial request succeeds." **Example:** Payment provider outage. **Use:** Cascading failure prevention. **Points:** States, thresholds, fallback. **Follow-ups:** Bulkhead.

## Saga Pattern
**What is it?** A saga coordinates long transactions through local transactions and compensations. **Interview answer:** "Each step succeeds or triggers compensating actions, because distributed ACID transactions are unsuitable." **Example:** Reserve inventory, charge card, schedule delivery. **Use:** Cross-service workflows. **Points:** Orchestration, choreography, idempotency. **Follow-ups:** 2PC vs saga.

## Blob Storage
**What is it?** Blob storage is durable object storage for large unstructured files. **Interview answer:** "I store metadata in a database and objects in S3-like storage." **Example:** Videos and invoices. **Use:** Massive files. **Points:** Objects, lifecycle, CDN. **Follow-ups:** Multipart upload.

## Back-of-the-Envelope Estimation
**What is it?** Estimation identifies rough capacity, storage, bandwidth, and cost needs. **Interview answer:** "I convert daily users to QPS and multiply average payload by traffic to estimate throughput." **Example:** 10 million uploads per day. **Use:** Early design validation. **Points:** Assumptions, peak factor, growth. **Follow-ups:** Rounding and units.
