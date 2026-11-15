---
name: hyper-ship
description: Enforces pre-launch release quality gates, Conventional Commits formatting, secret leak detection, and deployment readiness checklists. Use before committing code, creating pull requests, or deploying to production.
version: 1.0.0
---

# HyperShip: Release Quality & Conventional Git

> **Core Law**: Never commit broken tests, never push hardcoded secrets, and never write vague commit messages like "fix stuff". Every release is a production artifact.

---

## The Pre-Ship Gate (The Standing Bar)

Before executing `git commit` or deploying:
- [ ] **Tests Green**: 100% of the automated test suite passes.
- [ ] **Types Clean**: Zero type errors (`tsc --noEmit`, `mypy`, `go vet`, `cargo check`).
- [ ] **Linter Clean**: Zero lint errors (`eslint`, `ruff`, `golangci-lint`).
- [ ] **Secrets Check**: Zero hardcoded API keys, tokens, or private `.env` files in git staging.
- [ ] **Build Check**: Production build succeeds (`npm run build`, `go build`, `cargo build --release`).

---

## Conventional Commits Protocol

Format all git commit messages according to the Conventional Commits specification:

```
<type>(<optional scope>): <short description in present tense>

[optional body explaining WHY this change was made]

[optional footer(s) like Closes #123]
```

### Allowed Types
* `feat`: A new user-facing capability or API feature.
* `fix`: A bug fix or defect correction.
* `refactor`: Code change that neither fixes a bug nor adds a feature.
* `test`: Adding or correcting tests.
* `docs`: Documentation updates only.
* `perf`: Performance optimization.
* `chore`: Maintenance tasks, dependency bumps, or build configurations.

### Examples
* `feat(auth): implement token-bucket rate limiting for login route`
* `fix(trading): correct trailing stop calculation on partial fills`
* `refactor(ui): extract reusable KPI card component into design tokens`