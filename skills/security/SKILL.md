---
name: security
description: Enterprise AppSec, OWASP Top 10 API security auditing, and zero-trust hardening. Also triggered by the /security slash command. Use when reviewing authentication, testing endpoints for vulnerabilities, or hardening production systems.
---

# 🛡️ /security — HyperCraft Enterprise AppSec & Hardening Gate

The `/security` slash command enforces rigorous application security audits and zero-trust engineering standards.

## Capabilities Covered:
1. **Hyper-Security Hardening:** Blast-radius analysis, zero-trust validation, input sanitization, and secrets hygiene (`skills/hyper-security/SKILL.md`).
2. **OWASP API Security Top 10:** Systematic assessment of REST, GraphQL, and gRPC endpoints (`ecosystem/architecture-sdlc/`).
3. **Broken Object-Level Authorization (BOLA / IDOR):** Detect and patch unauthorized multi-tenant object access.
4. **JWT Vulnerability Defense:** Algorithm confusion, "none" algorithm attacks, weak HMAC secrets, and replay prevention.
5. **CORS & Origin Hardening:** Prevent cross-origin credential theft and overly permissive wildcard policies.

## Agent Execution Protocol:
- Adopt `agents/security-reviewer.md` during audits.
- Enforce: Zero hardcoded credentials, strict `.env` isolation, parameterized SQL queries, sanitized DOM inputs, and defensive timeout handling.
