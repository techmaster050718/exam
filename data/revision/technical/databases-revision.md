# Databases Interview Revision

## SQL Basics
**What is it?** SQL defines, manipulates, and queries relational data. **Interview answer:** "I use `SELECT` for reads, `INSERT` and `UPDATE` for writes, and transactions for atomic operations." **Example:** Fetch paid orders. **Use:** Relational applications. **Points:** DDL, DML, constraints. **Follow-ups:** WHERE vs HAVING.

## Joins
**What is it?** Joins combine rows based on relationships. **Interview answer:** "An inner join keeps matches, left join keeps all left rows, and cross join creates a Cartesian product." **Example:** Orders with customers. **Use:** Normalized data. **Points:** ON vs WHERE, duplicates. **Follow-ups:** Join order.

## Normalization
**What is it?** Normalization removes update anomalies through structured relations. **Interview answer:** "I apply keys and functional dependencies while balancing access patterns." **Example:** Move customer address out of every order. **Use:** Transactional schemas. **Points:** 1NF, 2NF, 3NF. **Follow-ups:** Denormalization.

## Indexing
**What is it?** An index is an auxiliary structure that accelerates searches. **Interview answer:** "I index predicates and join keys, while measuring writes and storage." **Example:** Index email for login. **Use:** Read-heavy tables. **Points:** Selectivity, composite order. **Follow-ups:** Covering index.

## B+ Tree Indexes
**What is it?** B+ trees keep sorted keys and linked leaves. **Interview answer:** "They support range and point reads with logarithmic height and ordered leaves." **Example:** User orders by date. **Use:** Disk databases. **Points:** Height, fanout, writes. **Follow-ups:** Hash index.

## Transactions & ACID
**What is it?** A transaction groups operations that commit or roll back as a unit. **Interview answer:** "ACID means atomicity, consistency, isolation, and durability." **Example:** Debit and credit a ledger together. **Use:** Critical writes. **Points:** Commit, rollback. **Follow-ups:** Isolation trade-offs.

## Isolation Levels
**What is it?** Isolation levels control visibility of concurrent changes. **Interview answer:** "Read committed avoids dirty reads; serializable gives the strongest observable correctness." **Example:** Inventory charge. **Use:** Concurrent transactions. **Points:** Dirty, nonrepeatable, phantom. **Follow-ups:** Locking vs MVCC.

## Locks & MVCC
**What is it?** Locks serialize writes; MVCC gives readers snapshots. **Interview answer:** "MVCC reduces reader blocking, but writers still need conflict control." **Example:** Long report transaction. **Use:** Concurrent databases. **Points:** Row locks, snapshots. **Follow-ups:** Skips locked.

## Query Optimization
**What is it?** Optimization finds an efficient execution plan. **Interview answer:** "I add useful indexes, rewrite predicates, and verify cardinality with EXPLAIN." **Example:** Filter by date and tenant first. **Use:** Slow queries. **Points:** Sargability, join order. **Follow-ups:** Statistics.

## EXPLAIN Plans
**What is it?** EXPLAIN shows estimated or actual operations. **Interview answer:** "I inspect scan type, row estimates, joins, and sort or temp operations." **Example:** Discover full table scan. **Use:** SQL diagnosis. **Points:** Seq scan, index scan, actual time. **Follow-ups:** Parameter sniffing.

## Stored Procedures
**What is it?** Stored procedures are database-side named programs. **Interview answer:** "They centralize logic near data but may complicate deployment and testing." **Example:** Financial closing routine. **Use:** Controlled DB logic. **Points:** Transactions, privileges. **Follow-ups:** Procedure vs app service.

## Views & Triggers
**What is it?** Views expose reusable queries; triggers run database actions on data events. **Interview answer:** "I use views for readability and triggers sparingly because hidden side effects are hard to observe." **Example:** Audit row changes. **Use:** Specialized schemas. **Points:** Updatable view, trigger scope. **Follow-ups:** Trigger cascade.

## SQL vs NoSQL
**What is it?** SQL systems optimize relational integrity; NoSQL systems optimize flexible or distributed patterns. **Interview answer:** "I choose by access patterns and consistency, not because of a trend." **Example:** Ledger in SQL, events in document store. **Use:** Data modeling. **Points:** Schema, joins, scaling. **Follow-ups:** NewSQL.

## MongoDB
**What is it?** MongoDB is a document database storing JSON-like records. **Interview answer:** "I embed frequently together and reference independently changing entities." **Example:** Catalog with variable attributes. **Use:** Flexible documents. **Points:** Indexes, aggregation, consistency. **Follow-ups:** Embedding vs referencing.

## Redis Data Types
**What is it?** Redis provides strings, hashes, lists, sets, sorted sets, streams, and more. **Interview answer:** "I use sorted sets for rankings and streams for durable event consumption." **Example:** Leaderboard. **Use:** Specialized state. **Points:** TTL, atomic operations. **Follow-ups:** Redis persistence.

## Replication
**What is it?** Database replicas copy data for reads or failover. **Interview answer:** "I define lag and failover behavior before relying on replicas." **Example:** Read reports from replicas. **Use:** Availability. **Points:** Async, sync, quorum. **Follow-ups:** Split brain.

## Sharding
**What is it?** Sharding distributes rows by a key across database instances. **Interview answer:** "I choose a stable high-cardinality key and accept higher cross-shard complexity." **Example:** Tenant-based partition. **Use:** Very large scale. **Points:** Rebalancing, hotspots. **Follow-ups:** Auto sharding.

## Partitioning
**What is it?** Partitioning splits a table into managed ranges or categories. **Interview answer:** "A single database can prune old monthly partitions for faster queries." **Example:** Time-based logs. **Use:** Large tables. **Points:** Range/hash/list, pruning. **Follow-ups:** Partition vs shard.

## Connection Pooling
**What is it?** A pool reuses established database connections. **Interview answer:** "I keep pool size bounded because connections consume database memory." **Example:** Serverless API pool proxy. **Use:** High concurrency. **Points:** Idle timeout, pool exhaustion. **Follow-ups:** PgBouncer.

## Backups & Recovery
**What is it?** Backups create restorable copies with a tested recovery objective. **Interview answer:** "I define RPO and RTO, use point-in-time recovery, and regularly restore into a test environment." **Example:** Recover deleted records. **Use:** Business continuity. **Points:** Snapshot, WAL, encryption. **Follow-ups:** Restore test.
