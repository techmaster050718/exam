# LLD / Low Level Design Revision

## OOP Pillars
**What is it?** OOP organizes code around objects combining state and behavior. **Key idea:** Encapsulation, abstraction, inheritance, and polymorphism serve different purposes. **Interview answer:** "Encapsulation hides state, abstraction exposes a focused contract, inheritance expresses is-a relationships, and polymorphism allows interchangeable behavior." **Example:** Different payment providers implement `PaymentGateway`. **Use:** Domain modeling. **Points:** Prefer composition, not inheritance by default. **Follow-ups:** Composition vs inheritance.

## SOLID
**What is it?** SOLID is a set of maintainable object-design principles. **Key idea:** Keep responsibilities focused and extensions type-safe. **Interview answer:** "A class should have one reason to change; interfaces should be narrow; new behavior should extend and not rewrite existing code." **Example:** Split notification delivery from order processing. **Use:** Refactoring and extensible design. **Points:** SRP, OCP, LSP, ISP, DIP. **Follow-ups:** DIP vs dependency injection.

## DRY
**What is it?** DRY means avoid repeated knowledge, not every repeated line. **Key idea:** Extract the same reason to change. **Interview answer:** "I duplicate a small loop if the domains differ; I centralize genuine business rules." **Example:** Shared tax calculation. **Use:** Maintainability. **Points:** Rule duplication, accidental duplication. **Follow-ups:** DRY vs KISS.

## KISS
**What is it?** KISS favors the simplest understandable solution that meets requirements. **Key idea:** Avoid speculative abstraction. **Interview answer:** "I use a direct implementation until complexity is demonstrated." **Example:** A small service does not need Kubernetes. **Use:** All design stages. **Points:** Readability, minimal parts. **Follow-ups:** When does abstraction help?

## YAGNI
**What is it?** YAGNI avoids implementing features before evidence exists. **Key idea:** Requirements should drive scope. **Interview answer:** "I would not build plugin infrastructure today only because a future plugin might appear." **Example:** Start with PostgreSQL before a generic database abstraction. **Use:** Agile delivery. **Points:** Reverse-cost of speculation. **Follow-ups:** YAGNI vs extensibility.

## Composition over Inheritance
**What is it?** Composition builds behavior by containing collaborators instead of inheriting classes. **Key idea:** It enables runtime changes and avoids deep hierarchies. **Interview answer:** "A car has an engine and can swap implementations instead of inheriting from every engine type." **Example:** Notification service delegates to email or SMS providers. **Use:** Flexible LLD. **Points:** Delegation, interfaces. **Follow-ups:** Strategy, inheritance traps.

## UML Class Diagrams
**What is it?** UML class diagrams show types and relationships. **Key idea:** Capture concepts, multiplicity, and dependencies. **Interview answer:** "I show a `User` one-to-many `Order`, and that `Order` depends on a `PaymentGateway` interface." **Example:** Parking or library design. **Use:** Communication before coding. **Points:** Association, aggregation, composition, inheritance. **Follow-ups:** Sequence diagrams.

## Singleton
**What is it?** Singleton ensures one instance within a process. **Key idea:** It introduces global state and testing risk. **Interview answer:** "I use it only for a process-wide resource when ownership is clear, usually preferring dependency injection." **Example:** Runtime configuration holder. **Use:** Rarely. **Points:** Thread safety, testability. **Follow-ups:** Singleton vs DI.

## Factory
**What is it?** A factory creates objects through an interface. **Key idea:** It hides construction choice. **Interview answer:** "A notification factory selects email or SMS from configuration." **Example:** Payment gateway creation. **Use:** Complex or variable construction. **Points:** Encapsulates selection. **Follow-ups:** Simple factory vs Factory Method.

## Abstract Factory
**What is it?** An abstract factory creates compatible families of objects. **Key idea:** Keep a set of platform-specific implementations consistent. **Interview answer:** "A UI factory creates matched Windows or Linux buttons and menus." **Example:** Cloud providers. **Use:** Product families. **Points:** More abstraction, more classes. **Follow-ups:** Factory vs Abstract Factory.

## Builder
**What is it?** Builder separates step-by-step construction from representation. **Key idea:** Useful for many optional parameters. **Interview answer:** "A query builder validates required parts while chaining filters." **Example:** HTTP request construction. **Use:** Complex immutable objects. **Points:** Readable setup, validation. **Follow-ups:** Builder vs constructor.

## Prototype
**What is it?** Prototype creates a copy of an existing configured object. **Key idea:** Cloning avoids expensive reconstruction. **Interview answer:** "A new campaign request starts from a deep-copied default template." **Example:** Document templates. **Use:** Preconfigured object variants. **Points:** Shallow vs deep copy. **Follow-ups:** Prototype vs copy constructor.

## Adapter
**What is it?** Adapter translates one interface into another. **Key idea:** Keeps a class independent of incompatible dependency. **Interview answer:** "The checkout domain expects `processPayment`; a Stripe adapter translates that call." **Example:** Legacy API integration. **Use:** Integration boundaries. **Points:** Wrapping, translation. **Follow-ups:** Adapter vs Facade.

## Decorator
**What is it?** Decorator adds behavior while preserving an interface. **Key idea:** Stack responsibilities dynamically. **Interview answer:** "A logger decorator wraps a cache decorator around a data source." **Example:** Compression or metrics around a stream. **Use:** Optional behavior. **Points:** Composition, stacking. **Follow-ups:** Decorator vs inheritance.

## Facade
**What is it?** Facade gives a simple interface over a complex subsystem. **Key idea:** Reduce caller coupling. **Interview answer:** "A travel-booking facade coordinates flights, hotels, and payments." **Example:** Payment orchestration. **Use:** Simplifying subsystem use. **Points:** Boundary, no hiding of capability. **Follow-ups:** Facade vs Adapter.

## Proxy
**What is it?** Proxy represents another object and controls access or work. **Key idea:** Preserve a compatible interface. **Interview answer:** "A remote proxy fetches data lazily or a security proxy checks authorization." **Example:** Lazy image loading. **Use:** Access, caching, remote calls. **Points:** Virtual, remote, protection. **Follow-ups:** Proxy vs Decorator.

## Observer
**What is it?** Observer notifies subscribers when state changes. **Key idea:** Publishers do not need concrete subscriber details. **Interview answer:** "An order publishes an event and inventory, notification, and analytics react independently." **Example:** UI state listener. **Use:** Event propagation. **Points:** Push/pull, memory leaks. **Follow-ups:** Observer vs message queue.

## Strategy
**What is it?** Strategy encapsulates interchangeable algorithms. **Key idea:** Change behavior by selecting an implementation. **Interview answer:** "Checkout chooses a fixed, percentage, or coupon pricing strategy." **Example:** Sorting or shipping selection. **Use:** Conditional algorithms. **Points:** Interface, runtime choice. **Follow-ups:** Strategy vs State.

## Command
**What is it?** Command encapsulates a request as an object. **Key idea:** Supports queueing, undo, and logging. **Interview answer:** "An undo system stores a cancel-payment command with execute and undo methods." **Example:** Editor actions. **Use:** Task and audit systems. **Points:** Receiver, invoker. **Follow-ups:** Command vs event.

## State
**What is it?** State lets an object alter behavior by current state. **Key idea:** Each state owns allowed transitions. **Interview answer:** "An order in `Paid` state can ship but an order in `Cancelled` state cannot." **Example:** Document workflow. **Use:** Finite-state behavior. **Points:** Avoid large conditional chains. **Follow-ups:** State vs Strategy.

## Thread Safety
**What is it?** Thread-safe code preserves correct behavior under concurrent access. **Key idea:** Protect shared mutable state or avoid sharing it. **Interview answer:** "I use immutable objects or locks for shared counters and ensure lock scope is small." **Example:** Concurrent ticket booking. **Use:** Multi-threaded applications. **Points:** Race, lock, atomic, synchronization. **Follow-ups:** Deadlocks, lock-free structures.

## Machine Coding
**What is it?** Machine coding is implementing a clear requirement under time constraints. **Key idea:** Start with models and core flows, then add tests and polish. **Interview answer:** "I clarify requirements, design classes and APIs, implement the happy path and edge cases, and verify concurrency or persistence needs." **Example:** Parking lot or splitwise. **Use:** LLD interviews. **Points:** Requirements, invariants, extensibility, time management. **Follow-ups:** What if requirements change?
