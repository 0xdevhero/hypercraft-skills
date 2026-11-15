---
name: hyper-tdd
description: Enforces strict Test-Driven Development (TDD) using the Red-Green-Refactor cycle. Mandates writing failing automated tests as mathematical proof of requirements before implementing production code. Covers Python, TypeScript, Go, Rust, and Java. Use when creating new features, fixing bugs, or refactoring logic.
version: 1.0.0
---

# HyperTDD: Test-Driven Engineering

> **Core Law**: If there is no automated test that failed first, you have not proven that your implementation actually works. Tests are executable proof.

---

## The Red-Green-Refactor Protocol

`
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   1. RED    │ ────► │  2. GREEN   │ ────► │ 3. REFACTOR │
│ Write test  │       │ Minimum code│       │ Clean code  │
│ Verify fail │       │ Make it pass│       │ Keep green  │
└─────────────┘       └─────────────┘       └─────────────┘
       ▲                                           │
       └───────────────────────────────────────────┘
`

### Phase 1: RED (Proof of the Requirement)
1. Write a minimal unit or integration test describing the expected behavior.
2. Run the test runner command.
3. **Verify it FAILS for the right reason**:
   - The failure MUST be an assertion failure or missing function, not an import syntax error.
   - If the test passes without implementing the code, the test is invalid.

### Phase 2: GREEN (Minimum Working Implementation)
1. Write the absolute minimum production code required to make the failing test pass.
2. Do not prematurely optimize or write speculative edge-case logic yet.
3. Run the test suite: verify that the test turns GREEN.

### Phase 3: REFACTOR (Architectural Polish)
1. With all tests passing green, clean up the implementation:
   - Remove duplicate code and magic numbers.
   - Improve variable naming and extract helper functions.
2. Re-run tests to confirm 100% green status. No behavior changes allowed during refactor.

---

## Multi-Language Quick Reference

### Python (pytest)
`ash
pytest tests/test_module.py -v --tb=short
`
* Pattern: Use @pytest.fixture for dependency injection and @pytest.mark.parametrize for boundary matrix testing.

### TypeScript / JavaScript (vitest / jest)
`ash
npx vitest run tests/feature.test.ts
`
* Pattern: Keep tests isolated; mock I/O boundaries (fetch, DB, disk) using i.spyOn or i.fn().

### Go
`ash
go test -v -run TestFeature ./...
`
* Pattern: Table-driven tests with 	t := []struct{ name string; input ...; expected ... }.

### Rust
`ash
cargo test --test feature_tests
`
* Pattern: Unit tests in #[cfg(test)] mod tests, integration tests in 	ests/.

---

## Defect Resolution Protocol (Bug Fixing)
When a bug is reported:
1. **Never edit the source code first.**
2. Write a regression test that reproduces the exact bug and fails (RED).
3. Apply the surgical fix in the source code until the test passes (GREEN).
4. Run the full test suite to guarantee zero regression across adjacent features.