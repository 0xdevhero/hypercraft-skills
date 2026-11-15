---
name: hyper-build
description: Enforces atomic, incremental implementation one verified vertical slice at a time. Prevents catastrophic multi-file diffs and broken intermediate states. Use during code generation, feature construction, or large refactorings.
version: 1.0.0
---

# HyperBuild: Atomic Incremental Implementation

> **Core Law**: Building 500 lines of unverified code at once is a gamble. Building five 100-line verified slices is engineering.

---

## The Incremental Loop

`
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ 1. SLICE SPEC   │ ────► │ 2. WRITE & RUN  │ ────► │ 3. VERIFY GATE  │
│ 50-150 line diff│       │ Targeted change │       │ Pass tests & linter
└─────────────────┘       └─────────────────┘       └─────────────────┘
         ▲                                                   │
         └───────────── Next Slice Until Feature DONE ───────┘
`

## Principles of Atomic Execution

1. **One Vertical Slice at a Time**:
   - Never implement all database tables, all backend controllers, and all frontend views in one massive turn.
   - Pick the smallest end-to-end slice (e.g. Model schema + migration -> verify; then Service layer query -> verify; then API route -> verify; then UI component -> verify).

2. **The 150-Line Soft Ceiling**:
   - If a single code modification exceeds ~150 lines of diff, pause.
   - Decompose into two sub-steps: first create the supporting types/helpers, verify they compile, then hook them into the caller.

3. **Standing Definition of Done (DoD)**:
   A slice is NOT done until:
   - [ ] Code compiles with zero syntax errors.
   - [ ] Type-check passes cleanly (e.g. 	sc --noEmit or mypy).
   - [ ] Unit tests for this slice pass green.
   - [ ] Zero unhandled linter warnings.
   - [ ] Working tree is clean and ready for an atomic commit.

4. **Rollback Discipline**:
   - If a slice introduces unexpected architectural complications or cascaded type errors, do not keep adding band-aids.
   - Revert to the last clean green slice and re-evaluate the interface contract.