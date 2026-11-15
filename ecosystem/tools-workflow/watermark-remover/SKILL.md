---
name: watermark-remover
description: Scans codebases, agent skills, documentation, and configs to detect and scrub third-party developer watermarks, upstream attribution leaks, personal handles, and promotional links. Use when sanitizing imported repositories or preparing clean distributions.
metadata:
  version: "1.0.0"
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Watermark Remover & Upstream Brand Sanitizer

When importing or consolidating open-source packages, agent skills, or third-party templates, repositories often contain residual developer watermarks: personal GitHub/Twitter handles, donation links, personal blog URLs, promotional surveys, and hardcoded author tags.

This skill provides a systematic auditing and cleansing protocol to scrub all third-party branding while preserving 100% of functional code and logic.

## What Constitutes a Developer Watermark?

1. **Personal Handles & Profile Links:**
   - GitHub profile URLs (`github.com/developer-username`)
   - Twitter / X handles (`@developer`, `twitter.com/...`)
   - LinkedIn, Substack, Medium, or personal portfolio URLs.
2. **Promotional & Financial Links:**
   - Buy Me a Coffee, Ko-fi, Patreon, or personal crypto donation addresses.
   - Feedback surveys, Typeforms, or newsletter signup links.
3. **Upstream Metadata in Headers:**
   - YAML frontmatter tags like `origin: <upstream-fork-name>` or `author: <individual>`.
   - Top-level doc comments claiming sole authorship of standard logic.
4. **Brand Inconsistencies:**
   - Mentions of previous parent suites or old project codenames in prose, docs, or comments.

---

## 4-Phase Sanitization Protocol

### Phase 1: Forensic Discovery
Scan the target directory for all personal handles, URLs, and authorship strings:
```bash
python scripts/scrub-watermarks.py <target-directory> --dry-run
```

### Phase 2: Metadata & Frontmatter Normalization
- Update YAML frontmatter:
  - `author: <Your Unified Brand>`
  - `origin: <Your Core Distribution>`
  - `license: Apache-2.0` (or target project license)
- Ensure no broken YAML delimiters or encoding artifacts (strip UTF-8 BOM).

### Phase 3: Text & Code Sanitization
- Replace hardcoded author names in prose and docstrings with the target team/brand name.
- Remove tracking queries, personal referral tags, and promotional survey links.
- Preserve all functional imports, library namespace references, and package dependencies.

### Phase 4: Cleanliness Verification Gate
Re-scan the codebase to assert that zero third-party handles or unapproved domains remain.

---

## Autonomous CLI Usage

Run the built-in sanitization script directly:
```bash
# Scan and report without modifying
python scripts/scrub-watermarks.py path/to/repo --dry-run

# Clean all files and rebrand to target brand
python scripts/scrub-watermarks.py path/to/repo --brand "HyperCraft Core Team"
```
