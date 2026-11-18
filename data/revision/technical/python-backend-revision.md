# Python / Backend Advanced Revision

## Async/Await & asyncio
**What is it?** Async Python yields control while I/O waits. **Interview answer:** "I use `await` for network or async database operations and avoid blocking calls on the event loop." **Example:** Concurrent API calls. **Use:** I/O-bound services. **Points:** Event loop, tasks, coroutines. **Follow-ups:** Async vs threads.

## GIL
**What is it?** The CPython GIL prevents multiple threads executing Python bytecode simultaneously. **Interview answer:** "It limits CPU-bound Python threads, while async and native I/O can overlap waiting." **Example:** Use processes for CPU work. **Use:** Runtime performance. **Points:** GIL, process pool. **Follow-ups:** C extensions.

## Decorators & Generators
**What is it?** Decorators wrap callables; generators yield values lazily. **Interview answer:** "Decorators add cross-cutting behavior, and generators stream sequences without full memory." **Example:** Timing decorator and CSV generator. **Use:** Reuse and memory. **Points:** `functools.wraps`, yield. **Follow-ups:** Contextmanager.

## Dependency Injection
**What is it?** Dependencies are supplied by a caller rather than constructed inside a component. **Interview answer:** "I inject repositories or clients to improve testing and switch implementations." **Example:** Inject a fake payment gateway. **Use:** Modular Python. **Points:** Constructor, container, interface. **Follow-ups:** Service locator.

## FastAPI Dependency Injection
**What is it?** FastAPI resolves dependencies for requests. **Interview answer:** "I declare database session, auth, and configuration dependencies and FastAPI handles lifespan and cleanup." **Example:** Return current user. **Use:** API services. **Points:** `Depends`, overrides, teardown. **Follow-ups:** Sync vs async.

## Middleware
**What is it?** Middleware wraps requests and responses. **Interview answer:** "I place tracing, authentication, compression, and security headers in middleware." **Example:** Add request ID. **Use:** Cross-cutting HTTP concerns. **Points:** Order, exception handling. **Follow-ups:** Middleware vs dependency.

## ORM & Migrations
**What is it?** An ORM maps objects to tables; migrations version schema. **Interview answer:** "I use ORM for common data access and SQL or migrations for complex queries." **Example:** SQLAlchemy model and Alembic migration. **Use:** Python persistence. **Points:** Session, lazy load, migration. **Follow-ups:** N+1.

## SQLAlchemy
**What is it?** SQLAlchemy provides ORM and SQL expression APIs. **Interview answer:** "I manage sessions explicitly and eager-load relations needed by a query." **Example:** User and orders. **Use:** Database Python. **Points:** Session, relationship, transaction. **Follow-ups:** Async SQLAlchemy.

## Alembic
**What is it?** Alembic manages SQLAlchemy schema migrations. **Interview answer:** "A migration upgrades and downgrades database state alongside application releases." **Example:** Add a status column. **Use:** Schema evolution. **Points:** Revision graph, lock, rollback. **Follow-ups:** Expand-contract.

## Celery
**What is it?** Celery executes asynchronous Python tasks through a broker. **Interview answer:** "A web request queues an email task, while workers retry it." **Example:** PDF generation. **Use:** Background work. **Points:** Broker, result, retry, visibility. **Follow-ups:** Duplicate tasks.

## Pydantic
**What is it?** Pydantic validates Python data against typed models. **Interview answer:** "I reject malformed API input before it reaches business logic." **Example:** Validate payment currency and amount. **Use:** FastAPI and configuration. **Points:** Coercion, validators, serialization. **Follow-ups:** Strictness.

## Server-Sent Events
**What is it?** SSE streams one-way server updates over HTTP. **Interview answer:** "I use SSE for simple server-to-client updates and WebSockets when the client must send continuously." **Example:** LLM streaming response. **Use:** Live progress. **Points:** Reconnect, event ID. **Follow-ups:** SSE vs WebSocket.

## Django ORM Internals
**What is it?** Django ORM translates QuerySets into SQL lazily. **Interview answer:** "I add `select_related` and `prefetch_related` to control N+1 queries." **Example:** Product list with categories. **Use:** Django applications. **Points:** QuerySet, lazy eval, transactions. **Follow-ups:** `annotate` vs `extra`.
