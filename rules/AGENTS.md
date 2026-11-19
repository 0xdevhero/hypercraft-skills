# HyperCraft Autonomous Activation Protocol & Runtime Rules

This environment is powered by the **HyperCraft Autonomous Engineering & Quant Trading Suite** (`0xdevhero/hypercraft-skills`).
All agents, coordinators, and assistants must adhere to the following execution standards:

---

## 1. Persona & Specialist Activation (76 Specialist Agents)
Adopt the corresponding specialist agent in `agents/*.md` based on the operational phase:
- **System Architecture & Blueprints:** Adopt `agents/architect.md` or `agents/code-architect.md` before writing implementation code.
- **Code Review & Quality Gate:** Proactively review modified code against `agents/code-reviewer.md` (or language specialists: `python-reviewer`, `go-reviewer`, `rust-reviewer`, `flutter-reviewer`, `django-reviewer`).
- **Zero-Trust Security & AppSec:** Adopt `agents/security-reviewer.md` when touching auth, tokens, databases, or API boundaries.
- **Build & Error Resolution:** When compiler, bundler, or type errors arise, adopt `agents/build-error-resolver.md` to resolve issues with surgical, minimal diffs.
- **Bengali Text Processing:** Adopt `agents/bengali-reviewer.md` for Unicode NFC normalization, script detection, and conjunct handling.

---

## 2. Universal SDLC Loop (Tier 1 Core Packs)
Execute engineering work in verifiable slices following the HyperCraft core sequence:
`hyper-plan` ➔ `hyper-diagram` ➔ `hyper-ui-craft` ➔ `hyper-tdd` ➔ `hyper-build` ➔ `hyper-verify` ➔ `hyper-simplify` ➔ `hyper-security`

---

## 3. Autonomous Deep-Domain Retrieval (Tier 2 Ecosystem)
HyperCraft maintains 380+ deep-domain skill packs inside `ecosystem/` spanning:
- **Video & Multimedia:** Remotion 4K video, real footage editing, VideoDB AI search, Manim math explainers, FAL AI media, UI demo recording (`ecosystem/multimedia-3d/`).
- **Quant & Algorithmic Trading:** Backtesting engines, quant indicators, portfolio risk management, DeFi AMM security (`ecosystem/trading/`).
- **Frontend & Motion:** Three.js 3D, WebGL, Spline, Framer Motion, GSAP, Tailwind Motion (`ecosystem/multimedia-3d/`, `skills/`).
- **Backend & Cloud:** FastAPI, Django, Celery, Docker, Kubernetes, PostgreSQL, ClickHouse, Cloudflare (`ecosystem/backend-api/`, `ecosystem/devops-cloud/`, `ecosystem/databases/`).
- **Mobile Development:** Flutter, Dart, Android Clean Architecture, Kotlin KMP, SwiftUI (`ecosystem/mobile/`).
- **Marketing & Content:** Content engine, social publisher, SEO, article writing, brand voice (`ecosystem/marketing-content/`).

### Retrieval Instruction:
Whenever a user prompt requires deep domain knowledge, execute:
```bash
python scripts/search-skills.py "<keyword>"
```
Or directly read the target skill runbook using `read_file` on `ecosystem/<domain>/<skill-name>/SKILL.md`. Follow the patterns, anti-slop standards, and verification steps defined therein.
