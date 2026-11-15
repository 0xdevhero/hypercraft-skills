# Contributing to HyperCraft

First off, thank you for considering contributing to **HyperCraft**! It is community contributions, stress-testing, and real-world feedback that make this autonomous engineering suite the gold standard for AI agents.

---

## Code of Conduct

This project adheres to the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## How Can I Contribute?

### 1. Reporting Bugs
- Check existing issues to see if the bug has already been reported.
- Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.yml) and include:
  - The AI agent or host client you used (Antigravity, Claude Code, Cursor, Codex).
  - The exact skill triggered (e.g. `hyper-ui-craft`, `hyper-security`).
  - Steps to reproduce and unexpected behavior.

### 2. Proposing a New Skill
- We welcome additions that address real practitioner gaps across the SDLC.
- Open a [New Skill Proposal](.github/ISSUE_TEMPLATE/new_skill.yml) before drafting extensive files.
- Guidelines for skills:
  - Must adhere to the `agentskills.io` standard (`SKILL.md` with structured YAML frontmatter).
  - Must follow the **Zero-AI-Slop** philosophy (opinionated, actionable, and verified).
  - Must avoid personal promotional links, tracking URLs, or single-vendor lock-in.

### 3. Improving Existing Skills
- Refinements to make instructions more concise, reduce token cost, or add language recipes (e.g. adding Elixir/Kotlin to `hyper-tdd`) are enthusiastically welcomed.

---

## Development Workflow

1. Fork the repo and create your branch from `main`:
   ```bash
   git checkout -b feature/my-new-skill
   ```
2. Verify that all markdown frontmatters are valid and JSON files pass syntax validation.
3. Test python scripts locally:
   ```bash
   python skills/hyper-ui-intelligence/scripts/search.py "test query" --domain color
   ```
4. Follow [Conventional Commits](skills/hyper-ship/SKILL.md) for all commit messages:
   ```bash
   git commit -m "feat(security): add CSRF token rotation defense to hyper-security"
   ```
5. Push to your fork and submit a Pull Request!