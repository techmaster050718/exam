# Object-Oriented Programming (OOP) & Language Fundamentals
> **Exam-Ready Reference | Competitive Exams (IBPS SO IT, GATE, ISRO, NIC, RRB)**

---

## 1. CORE OOP PILLARS

```text
┌─────────────────┬─────────────────────────────────────────────────────────┐
│ Pillar          │ Core Mechanism & Real-World Purpose                     │
├─────────────────┼─────────────────────────────────────────────────────────┤
│ Encapsulation   │ Bundling data & methods; data hiding via private access │
│ Abstraction     │ Hiding complex implementation; showing essential APIs   │
│ Inheritance     │ Code reuse; 'is-a' hierarchy (Single, Multilevel, etc.) │
│ Polymorphism    │ Many forms: Compile-time (Overload) vs Runtime (Override)│
└─────────────────┴─────────────────────────────────────────────────────────┘
```

### Dynamic Method Dispatch (Runtime Polymorphism)
```java
class SuperClass {
    void display() { System.out.println("SuperClass"); }
}
class SubClass extends SuperClass {
    @Override
    void display() { System.out.println("SubClass"); }
}
// In Main:
SuperClass obj = new SubClass();
obj.display(); // Prints "SubClass" at runtime via Virtual Method Table (vtable)
```

---

## 2. SOLID PRINCIPLES QUICK REFERENCE
* **S - Single Responsibility Principle:** A class should have one, and only one, reason to change.
* **O - Open/Closed Principle:** Open for extension, closed for modification.
* **L - Liskov Substitution Principle:** Derived classes must be substitutable for their base classes without altering program correctness.
* **I - Interface Segregation Principle:** Many client-specific interfaces are better than one general-purpose interface.
* **D - Dependency Inversion Principle:** Depend on abstractions, not concretions.

---

## 3. JAVA INTERNALS & MEMORY ARCHITECTURE

### JVM Memory Organization
```text
┌────────────────────────────────────────────────────────┐
│ JVM Memory                                             │
│ ┌───────────────────────────┬────────────────────────┐ │
│ │ Heap Space (All Threads)  │ Non-Heap / Native      │ │
│ │ - Young Gen (Eden, S0, S1)│ - Metaspace (Java 8+)  │ │
│ │ - Old (Tenured) Gen       │   (Class metadata)     │ │
│ └───────────────────────────┴────────────────────────┘ │
│ ┌───────────────────────────┬────────────────────────┐ │
│ │ Thread Stacks (Per-Thread)│ PC Registers & Native   │ │
│ │ - Method Frames           │ Method Stacks          │ │
│ │ - Local Variables         │                        │ │
│ └───────────────────────────┴────────────────────────┘ │
└────────────────────────────────────────────────────────┘
```
* **Java 8 Change:** `PermGen` was completely removed and replaced by `Metaspace`, which grows dynamically in native OS memory.
* **Garbage Collection (GC):** Tracks reachable objects via Root references; sweeps unreachable objects. Common collectors: G1, ZGC, ParallelGC.

---

## 4. C++ SPECIFICS & DIAMOND PROBLEM

### Diamond Problem Resolution via Virtual Base Class
```text
      Class A (Base)
       /         \
 Class B          Class C
 (virtual A)      (virtual A)
       \         /
      Class D (Derived)
```
```cpp
class A { public: int val; };
class B : virtual public A { };
class C : virtual public A { };
class D : public B, public C { }; // Only ONE copy of A::val exists in D!
```

---

## 5. DESIGN PATTERNS QUICK CLASSIFICATION

| Category | Pattern | Purpose |
| :--- | :--- | :--- |
| **Creational** | **Singleton** | Ensures exactly one instance exists with a global access point |
| | **Factory Method** | Defines interface for creating objects; subclasses decide which class to instantiate |
| | **Builder** | Constructs complex objects step-by-step |
| **Structural** | **Adapter** | Allows incompatible interfaces to work together |
| | **Decorator** | Dynamically attaches additional responsibilities to an object |
| | **Proxy** | Provides a surrogate/placeholder for another object to control access |
| **Behavioral** | **Observer** | One-to-many dependency; notifies dependents automatically upon state change |
| | **Strategy** | Encapsulates a family of algorithms and makes them interchangeable |
| | **Command** | Encapsulates a request as an object |

---

## 6. MUST REMEMBER & COMMON TRAPS

### MUST REMEMBER
1. **Abstract Class vs Interface (Java 8+):**
   * Abstract classes can have state (instance fields) and constructors.
   * Interfaces can have `default` and `static` methods, but fields are always `public static final`.
2. **`final` Keyword in Java:**
   * Final variable: Constant (cannot reassign).
   * Final method: Cannot be overridden.
   * Final class: Cannot be inherited.
3. **C++ Pointers vs References:** A reference must be initialized upon declaration and cannot be null; a pointer can be null and reassigned.

### COMMON TRAPS
* ⚠️ **Trap 1:** Overloading vs Overriding. Overloading happens at **compile-time** within the same class (same name, different parameters); Overriding happens at **runtime** between parent/child classes (same name and exact same signature).
* ⚠️ **Trap 2:** Thinking `finally` block in Java never executes. It executes almost always, except if `System.exit(0)` is called or JVM crashes.
