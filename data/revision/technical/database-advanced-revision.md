# Database Advanced & Cloud Data Revision

## PostgreSQL Internals
**What is it?** PostgreSQL is an MVCC relational database with processes, WAL, B-trees, and extensible types. **Interview answer:** "I inspect plans and waits, use indexes deliberately, and tune autovacuum and checkpoints." **Example:** High-write order system. **Use:** Transactional workloads. **Points:** MVCC, WAL, vacuum, bloat. **Follow-ups:** PostgreSQL vs MySQL.

## Data Modeling / ER Design
**What is it?** ER design identifies entities, attributes, relationships, keys, and cardinality. **Interview answer:** "I model invariants and access patterns, then normalize and add constraints." **Example:** Customer, order, payment. **Use:** Schema design. **Points:** Entities, keys, 1:1/1:N/N:M. **Follow-ups:** Denormalization.

## pgvector
**What is it?** pgvector adds vector types and similarity search to PostgreSQL. **Interview answer:** "It is useful when relational metadata filtering and vector retrieval should remain in the same database." **Example:** Document retrieval with tenant filtering. **Use:** Smaller or integrated RAG systems. **Points:** Index, distance, metadata. **Follow-ups:** pgvector vs vector database.

## Vector Search
**What is it?** Vector search retrieves vectors nearest to a query vector. **Interview answer:** "It uses embeddings and ANN indexes to return semantically similar records." **Example:** Similar policy documents. **Use:** Semantic retrieval. **Points:** Recall, latency, hybrid filters. **Follow-ups:** ANN recall trade-off.

## Database Migrations
**What is it?** Migrations transform schemas across application versions. **Interview answer:** "I use expand-contract for zero-downtime additions and validate backward compatibility." **Example:** Rename a column in phases. **Use:** Continuous delivery. **Points:** Reversible, lock-aware, tested. **Follow-ups:** Large-table migration.

## CDC / Change Data Capture
**What is it?** CDC streams database row changes. **Interview answer:** "A connector reads a transaction log and publishes inserts, updates, and deletes." **Example:** Sync orders to search. **Use:** Replication and event feeds. **Points:** Ordering, backfill, schema. **Follow-ups:** Log vs trigger CDC.

## N+1 Query Problem
**What is it?** N+1 happens when one query loads a list and N additional queries load related data. **Interview answer:** "I use joins, eager loading, or batching." **Example:** Load 100 users and run 100 role queries. **Use:** ORM systems. **Points:** Detection, batching, caching. **Follow-ups:** 1+N vs joins.
