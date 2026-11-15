---
name: hyper-plan
description: Defines structured engineering specifications, capability maps, and atomic task Directed Acyclic Graphs (DAGs) before writing code. Enforces context boundary isolation and stops agents from guessing on ambiguous requirements. Use when starting a new project, feature, refactor, or complex task.
version: 1.0.0
---

# HyperPlan: Spec & Task Architecture

> **Core Law**: Code without an approved specification is guessing. Guessing in production is technical debt.

## Overview
HyperPlan is the architecture phase of the HyperCraft suite. It converts loose conversational prompts or high-level product requirements into an authoritative, reviewable technical specification and an atomic implementation DAG before a single line of production code is touched.

---

## The Gated Workflow

`
SPECIFY ────────► CAPABILITY MAP ────────► ATOMIC TASKS ────────► IMPLEMENT
   │                     │                       │                     │
   ▼                     ▼                       ▼                     ▼
Verified              Verified                Verified              Verified
Requirements          Boundaries              Checklist             Execution
`

### Phase 1: Ambiguity & Intent Interrogation
When an ask lacks clarity on user persona, success metrics, technical constraints, or edge-case handling:
1. Formulate a single concise hypothesis of the user's intent with a confidence score (0–100%).
2. Ask targeted, multiple-choice questions one at a time to lock down intent.
3. Stop interrogation the moment confidence exceeds 90%.

### Phase 2: Capability Decomposition (Phase 0 Scope Check)
If the feature spans multiple distinct domains (e.g. Authentication, Billing, Real-Time Ingestion, Reporting):
* Construct a **Capability Map** before writing individual module specs:
  | Module ID | Responsibility | Depends On | Verifiable Milestone |
  |---|---|---|---|
  | uth-core | Session & JWT issuance | None | Unit & integration tests green |
  | data-feed | WebSocket streaming | uth-core | Mock feed stream parsing validated |

### Phase 3: Technical Specification
Draft a concise Markdown specification containing:
1. **User Story & Objectives**: Who it is for and why it matters.
2. **Interface Contracts**: Exact API endpoints, function signatures, database schema changes, and typed DTOs.
3. **Invariants & Non-Goals**: Explicitly declare what this change will *never* do.
4. **Failure Modes & Error Handling**: What happens on network disconnects, invalid payloads, or rate limits.

### Phase 4: Atomic Task Breakdown (DAG)
Decompose the spec into sequential, testable task slices:
* Target: Each task represents a single logical unit of work (ideally 50–150 lines of diff).
* Each task MUST state:
  - **Prerequisites**: What must be done before this starts.
  - **Files Touched**: Exact file paths.
  - **Verification Gate**: Exact automated test command or proof needed to declare the task DONE.

---

## Anti-Patterns to Reject
- Starting code implementation while requirements remain ambiguous.
- Creating monolithic tasks that bundle database migrations, backend logic, and frontend UI into one step.
- Expanding context arbitrarily: isolate reasoning to the current capability slice.