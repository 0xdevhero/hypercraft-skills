---
name: hyper-security
description: Hardens backend APIs and web applications against the OWASP API Security Top 10. Enforces Broken Object Level Authorization (BOLA/IDOR) isolation, sliding-window/token-bucket rate limiting, JWT token hardening, and strict CORS locking. Use when building or auditing API endpoints, authentication flows, or web server configurations.
version: 1.0.0
---

# HyperSecurity: API Armor & Web Hardening

> **Core Law**: Never trust client-supplied input, never trust client-supplied IDs, and never expose an API endpoint without rate-limiting and authorization armor.

---

## The 5 Pillars of Web & API Hardening

`
┌────────────────────────────────────────────────────────────────────────┐
│                        HYPERSECURITY API GATE                          │
├─────────────┬─────────────┬──────────────┬──────────────┬──────────────┤
│ 1. BOLA/IDOR│ 2. RATE     │ 3. JWT       │ 4. CORS &    │ 5. INPUT     │
│ Protection  │ Limiting    │ Hardening    │ Headers      │ Sanitization │
└─────────────┴─────────────┴──────────────┴──────────────┴──────────────┘
`

### Pillar 1: BOLA / IDOR Defense (OWASP API1)
* **The Vulnerability**: Attacker alters /api/orders/101 to /api/orders/102 to view another user's private data.
* **The Defense**:
  - Never query records by ID alone: SELECT * FROM orders WHERE id = :id.
  - Always enforce tenant/ownership scoping: SELECT * FROM orders WHERE id = :id AND user_id = :current_user_id.
  - Prefer non-sequential IDs (UUIDv4 or CUID2) over auto-incrementing integers to prevent enumeration.

### Pillar 2: API Rate Limiting & Abuse Prevention (OWASP API4)
* **The Vulnerability**: Automated scripts brute-force login endpoints, scrape pricing, or exhaust server memory.
* **The Defense**:
  - Implement **Token Bucket** or **Sliding Window** rate limiting backed by Redis or in-memory stores.
  - Limits:
    - Auth endpoints: 5 attempts per IP per minute.
    - Public read endpoints: 60 requests per minute.
    - Authenticated tier: 300 requests per minute.
  - Return standard HTTP 429 Too Many Requests with a Retry-After: <seconds> header.

### Pillar 3: JWT & Session Token Armor (OWASP API2)
* **The Vulnerability**: Algorithm confusion attacks (
one algorithm bypass), expired token acceptance, or weak signing secrets.
* **The Defense**:
  - Strictly enforce asymmetric signing (RS256 or EdDSA) in production, or high-entropy 256-bit secrets for HS256.
  - Explicitly reject the "none" algorithm in verification options.
  - Check exp (expiration), 
bf (not before), and iss (issuer) on every token verification.
  - Store tokens in browser cookies with HttpOnly, Secure, and SameSite=Strict attributes (never in localStorage).

### Pillar 4: Strict CORS & Secure HTTP Response Headers
* **CORS**:
  - Never set Access-Control-Allow-Origin: * on endpoints handling credentials or cookies.
  - Explicitly whitelist allowed origins (e.g. https://app.yourdomain.com).
* **Security Headers**:
  - Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  - X-Content-Type-Options: nosniff
  - X-Frame-Options: DENY
  - Referrer-Policy: strict-origin-when-cross-origin
  - Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'

### Pillar 5: Input Sanitization & Injection Defense (OWASP API8)
* Treat all request parameters (body, query, headers) as untrusted.
* Use parameterized prepared statements or typed ORMs for all database queries (zero raw SQL string concatenation).
* Validate incoming request payloads against strict Zod, Pydantic, or JSON schemas, rejecting unexpected fields.