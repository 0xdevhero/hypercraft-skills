# ⚡ HyperCraft: Autonomous Engineering & Quant Trading Suite

> **The unified, batteries-included engineering distribution for AI coding agents.**  
> Combines architectural planning, editorial visuals, design intelligence, anti-slop UI craft, strict TDD, algorithmic quant trading, and production API hardening under one cohesive standard.

[![CI](https://github.com/Hero-Coco/hypercraft-skills/actions/workflows/verify.yml/badge.svg)](https://github.com/Hero-Coco/hypercraft-skills/actions)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 400+ Enterprise](https://img.shields.io/badge/Skills-400+_Enterprise_Packs-brightgreen.svg)](#the-architecture)
[![Trading: Quant & SMC](https://img.shields.io/badge/Trading-Quant_%26_SMC_Suite-gold.svg)](#trading--quant-suite)
[![Agents: 4 Personas](https://img.shields.io/badge/Agents-4_Specialists-orange.svg)](#specialized-agents)
[![Compatibility](https://img.shields.io/badge/Platforms-Antigravity%20%7C%20Claude%20Code%20%7C%20Cursor%20%7C%20Codex-blueviolet.svg)](#installation)

---

## 📖 Operational Architecture & Guide

For a full technical walkthrough explaining how the Core 10, Trading Suite, and On-Disk Search engine work together:
👉 **[Read the Complete How It Works Guide (docs/HOW_IT_WORKS.md)](docs/HOW_IT_WORKS.md)**

---

## 🏛️ The Architecture: Ultimate Hybrid Structure

Loading 400+ skills simultaneously in an AI agent typically triggers **token exhaustion** (consuming 25,000+ tokens per prompt) and **attention dilution** (where agents hallucinate or choose incorrect tools).

**HyperCraft solves this with a two-tier hybrid architecture:**

1. **⚡ Core 10 Master Packs (`skills/core/`):**  
   Universally applicable across all stacks. Lean footprint (< 500 tokens). Always active by default to guide end-to-end SDLC without cognitive friction.
2. **🌐 Categorized Ecosystem Packs (`skills/ecosystem/`):**  
   Over 400 deep-domain skills spanning Algorithmic Trading, Languages, Frameworks, Cloud/DevOps, Security, and 3D Web.
3. **🔍 Instant On-Disk Skill Search (`scripts/search-skills.py`):**  
   Zero token overhead in the system prompt. The agent queries deep-domain rules on disk in milliseconds:
   ```bash
   python scripts/search-skills.py "quant indicators"
   python scripts/search-skills.py "flutter routing"
   ```

---

## ⚡ The 10 Core Master Skills

| Master Skill | Capabilities & Value |
|---|---|
| **`hyper-plan`** | RFC-style task planning, acceptance criteria, milestone mapping, and scope bounding. |
| **`hyper-diagram`** | Stripe & Linear publication-grade architectural diagrams (C4, Entity-Relationship, Sequence, Flowchart). |
| **`hyper-ui-intelligence`** | Local BM25 design search: 192 domain palettes, 59 typography pairings, and 99 UI recipes. |
| **`hyper-ui-craft`** | Modern editorial web aesthetics: anti-slop CSS, fluid typography, dark-mode glassmorphism, and micro-interactions. |
| **`hyper-tdd`** | Strict Red-Green-Refactor loop. Writes reproducible tests first, proves failure, then implements to green. |
| **`hyper-build`** | Atomic incremental compiler & build resolver. Minimal diffs; zero intermediate breakage. |
| **`hyper-verify`** | Independent verification gate. Audits boundary contracts, silent exceptions, and test coverage before commit. |
| **`hyper-simplify`** | Behavior-preserving refactoring. Eliminates dead code, collapses cyclomatic complexity, and flattens nesting. |
| **`hyper-security`** | OWASP Top 10 hardening, BOLA defenses, JWT validation, strict CORS policies, and rate-limiting. |
| **`hyper-ship`** | Semantic releases, Conventional Commits, changelog generation, and pre-push verification. |

---

## 📈 Trading & Quant Suite (`skills/ecosystem/trading/`)

A production-grade algorithmic and quantitative trading suite for AI agents:

| Skill | Description |
|---|---|
| **`trading-quant-indicators`** | Vectorized oscillators (RSI, MACD, Bollinger Bands, ATR, EMA, VWAP) and Smart Money Concepts (Fair Value Gaps, Order Blocks, Liquidity Sweeps). |
| **`trading-backtesting-engine`** | Quantitative backtesting pipeline with fee and dynamic slippage modeling, Sharpe/Sortino ratios, and Max Drawdown calculations. |
| **`trading-exchange-connectors`** | Unified execution via CCXT for 100+ crypto exchanges (Binance, Bybit, OKX) and Alpaca API for US equities. Bracket & OCO orders. |
| **`trading-risk-management`** | Capital preservation framework: Kelly Criterion, 1% fixed fractional risk, portfolio heat caps, and automated emergency kill switch. |
| **`trading-sentiment-intelligence`** | Real-time Crypto Fear & Greed index integration, perpetual funding rate squeeze detection, and high-impact macro calendar gating (FOMC/CPI). |
| **`trading-agent-security`** | Financial prompt injection defense, spend limits, pre-send transaction simulations, and wallet isolation. |
| **`trading-defi-amm-security`** | On-chain DEX protection, MEV sandwich defense, and slippage guards. |
| **`trading-evm-token-decimals`** | High-precision floating point math protection for EVM token calculations. |
| **`trading-prediction-market-risk`** | Risk management for event-driven contracts (Polymarket, Kalshi). |
| **`trading-prediction-oracle-research`** | Oracle resolution analysis and cross-venue probability arbitrage. |

---

## 🌐 Ecosystem Domains (`skills/ecosystem/`)

HyperCraft categorizes specialized skills across 12 engineering disciplines:

- **`languages/`**: Python, Go, Rust, Dart/Flutter, Swift, Kotlin, C++, C#, Modern Perl.
- **`frameworks/`**: React 19, Next.js App Router, Vue 3, Nuxt 4, Laravel, Django, Spring Boot, NestJS, Ktor.
- **`databases/`**: PostgreSQL, MySQL, Redis, ClickHouse, BigQuery, JPA/Hibernate.
- **`devops-cloud/`**: Docker, Kubernetes, CI/CD pipelines, Uncloud, Cisco IOS, Homelab.
- **`security/`**: Deep Auth, BOLA, JWT, CORS, Rate-Limiting, HIPAA compliance.
- **`multimedia-3d/`**: Three.js WebGL, GSAP, Framer Motion, Spline 3D, Remotion, Manim.
- **`agentic-ai/`**: Autonomous loops, DevFleet, DMUX multi-agent worktrees, agent harnesses.
- **`science-bio/`**: PubChem, ChEMBL, AlphaFold, ClinVar, GTEx, NCBI sequence pipelines.
- **`testing-qa/`**: Playwright E2E, Windows native desktop UI automation, CodeScene Code Health.
- **`architecture-sdlc/`**: Clean Architecture, Hexagonal patterns, API contracts, ADRs.
- **`frontend-ui/`**: Accessible components, Tailwindcss-motion, React Bits dynamic canvases.
- **`tools-workflow/`**: Git workflows, Jira integration, conventional commits, cost tracking.

---

## 🤖 Specialized Personas (`agents/`)

| Persona | Role | Focus |
|---|---|---|
| **`hyper-architect`** | Principal Systems Architect | System decomposition, capability maps, contracts, and RFC plans. |
| **`hyper-designer`** | Staff Product Designer | Modern editorial aesthetics, color harmony, typography pairings, and zero-slop UI. |
| **`hyper-security-auditor`** | Lead AppSec Engineer | OWASP Top 10, financial prompt injection, threat modeling, and cryptographic integrity. |
| **`hyper-reviewer`** | Principal Code Reviewer | Cyclomatic reduction, memory leak detection, immutability, and zero regression. |

---

## 🚀 Installation & Usage

### 1. Google Antigravity
Clone directly into your configuration directory:
```bash
git clone https://github.com/Hero-Coco/hypercraft-skills.git ~/.gemini/config/plugins/hypercraft-skills
```

### 2. Claude Code
Install as a workspace plugin:
```bash
claude plugin add https://github.com/Hero-Coco/hypercraft-skills
```

### 3. Cursor & Windsurf
Add to your project root or workspace rules:
```bash
git submodule add https://github.com/Hero-Coco/hypercraft-skills.git .agents/hypercraft
```

---

## 🔍 On-Disk Skill Search Engine

AI agents or operators can query the entire 400+ skill catalog on demand without prompt bloat:
```bash
# Search by keyword
python scripts/search-skills.py "quant indicators"

# Filter by category
python scripts/search-skills.py "bracket order" --category trading

# Query framework patterns
python scripts/search-skills.py "declarative routing" --category languages
```

---

## 🤝 Community & Contributing

We welcome community improvements and new domain packs! Please review:
- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

---

## 📄 License

Distributed under the **Apache 2.0 License**. See [LICENSE](LICENSE) for details.  
Built with precision by the **HyperCraft Core Team** ([Hero-Coco](https://github.com/Hero-Coco)).
