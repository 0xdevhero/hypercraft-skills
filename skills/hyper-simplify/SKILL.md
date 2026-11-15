---
name: hyper-simplify
description: Simplifies working code for clarity, readability, and maintainability without altering runtime behavior. Ruthlessly removes dead code, deeply nested conditionals, premature abstractions, and bloated wrappers. Use after getting tests green, during code review, or when cleaning up complex legacy files.
version: 1.0.0
---

# HyperSimplify: Ruthless Clean Code & Anti-Bloat

> **Core Law**: The goal is not fewer lines of code—it is code that a new engineer can understand, debug, and modify in minutes. Every simplification must pass the test: "Does this make the logic easier to reason about?"

---

## The 5 Simplification Principles

### 1. Preserve Behavior 100% Exactly
Never alter what the code accomplishes—only how cleanly it expresses it.
* Every input must yield the identical output.
* All error types, side effects, ordering, and return signatures must remain intact.
* All automated unit tests MUST pass before and after the simplification with zero modifications to the tests themselves.

### 2. Flatten Deep Nesting (Early Returns)
Convert deeply nested if/else ladders into guard clauses that exit early:
`	ypescript
// AVOID: Deep arrow-anti-pattern
function processOrder(order) {
  if (order) {
    if (order.isValid) {
      if (order.hasFunds) {
        return execute(order);
      }
    }
  }
  return null;
}

// PREFER: Flat guard clauses
function processOrder(order) {
  if (!order || !order.isValid || !order.hasFunds) return null;
  return execute(order);
}
`

### 3. Kill Premature Abstractions
* Delete single-use helper functions that add mental indirection without reuse.
* Inline trivial wrapper classes that merely forward calls to standard library methods.
* Replace custom utility helpers with modern language primitives (e.g. Array.prototype.flatMap, Optional Chaining ?., Nullish Coalescing ??).

### 4. Eliminate Dead Code & Zombie Comments
* Delete commented-out code blocks immediately. Version control (Git) remembers history.
* Remove unused variables, dead imports, and obsolete configuration flags.
* Replace verbose explanatory comments with clear, self-documenting function and variable names.

### 5. Single Responsibility per Function
* If a function performs validation, database fetching, data transformation, AND notification sending—break it down into small, cohesive, pure functions.