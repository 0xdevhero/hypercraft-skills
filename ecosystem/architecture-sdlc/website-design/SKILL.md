---
name: website-design
description: Master skill for stunning, animated website design. Covers architecture decisions, tech stack selection, design systems, and orchestrates sub-skills (GSAP, Framer Motion, Three.js, Magic UI, Aceternity UI). Use when building or designing any modern animated website.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Website Design — Master Orchestrator

## When to Activate
- User wants to build a website with animations
- User asks for "beautiful", "stunning", "hype", "animated" web design
- User needs help choosing between animation libraries
- User wants a landing page, portfolio, SaaS site, or creative website

## Tech Stack Decision Tree

```
What kind of site?
│
├── Landing Page / Marketing
│   ├── Static → Next.js + GSAP + Lenis + Tailwind
│   └── CMS → Next.js + Sanity + Framer Motion
│
├── Portfolio / Creative
│   ├── 2D Animations → GSAP + Lenis + Locomotive
│   └── 3D / Immersive → Three.js + React Three Fiber + Drei
│
├── SaaS Dashboard
│   └── shadcn/ui + Framer Motion + Tailwind
│
├── E-Commerce
│   └── Next.js + Framer Motion + Magic UI
│
└── Experimental / Awwwards
    └── Three.js + GSAP + Custom Shaders + Lenis
```

## Design Principles

### 1. Motion Design Rules
- **Purpose**: Every animation must have a reason — guide attention, show state change, or create delight
- **Duration**: 200-500ms for UI, 800-1500ms for page transitions, 60fps always
- **Easing**: Use `cubic-bezier` or GSAP's built-in easings — never `linear` for UI
- **Reduce Motion**: Always respect `prefers-reduced-motion` media query

### 2. Performance First
```
Animation Performance Tier List:
├── S Tier: transform, opacity (GPU composited)
├── A Tier: filter (blur, brightness)
├── B Tier: clip-path, background-position
├── C Tier: width, height, margin, padding (triggers layout — AVOID)
└── F Tier: box-shadow animation (paint heavy — use pseudo-elements instead)
```

### 3. Scroll Animation Pattern
```javascript
// Always use Intersection Observer or GSAP ScrollTrigger
// NEVER use scroll event listener for animations

// ✅ Good
gsap.to(".element", {
  scrollTrigger: {
    trigger: ".element",
    start: "top 80%",
    end: "bottom 20%",
    scrub: true
  },
  y: 0,
  opacity: 1
});

// ❌ Bad
window.addEventListener("scroll", () => { /* animate here */ });
```

### 4. Layout & Spacing System
```css
/* 4px grid system */
--space-1: 0.25rem;  /* 4px */
--space-2: 0.5rem;   /* 8px */
--space-3: 0.75rem;  /* 12px */
--space-4: 1rem;     /* 16px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-12: 3rem;    /* 48px */
--space-16: 4rem;    /* 64px */
--space-24: 6rem;    /* 96px */
--space-32: 8rem;    /* 128px */
```

### 5. Typography Scale
```css
/* Modern type scale — fluid */
--text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.875rem);
--text-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
--text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
--text-lg: clamp(1.125rem, 1rem + 0.6vw, 1.25rem);
--text-xl: clamp(1.25rem, 1rem + 1vw, 1.5rem);
--text-2xl: clamp(1.5rem, 1rem + 2vw, 2rem);
--text-3xl: clamp(2rem, 1.2rem + 3vw, 3rem);
--text-4xl: clamp(2.5rem, 1rem + 5vw, 4.5rem);
--text-hero: clamp(3rem, 1rem + 8vw, 7rem);
```

## Color Patterns

### Dark Mode (Hype Sites)
```css
--bg-primary: #0a0a0a;
--bg-secondary: #111111;
--bg-elevated: #1a1a1a;
--border-subtle: rgba(255, 255, 255, 0.06);
--border-default: rgba(255, 255, 255, 0.1);
--text-primary: #fafafa;
--text-secondary: #a1a1aa;
--text-muted: #71717a;
--accent: #6366f1;        /* Indigo */
--accent-glow: rgba(99, 102, 241, 0.15);
```

### Gradient Patterns
```css
/* Mesh gradient — trendy */
background: radial-gradient(at 27% 37%, #3a8bfd 0, transparent 50%),
            radial-gradient(at 97% 21%, #9772fe 0, transparent 50%),
            radial-gradient(at 52% 99%, #fd3a4e 0, transparent 50%),
            radial-gradient(at 10% 29%, #5afc7d 0, transparent 50%);

/* Aurora gradient — subtle */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Glass morphism */
background: rgba(255, 255, 255, 0.05);
backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 0.08);
```

## Project Structure (Recommended)
```
src/
├── app/                    # Next.js app router
│   ├── layout.tsx          # Root layout with providers
│   ├── page.tsx            # Home page
│   └── (sections)/         # Page sections as components
├── components/
│   ├── ui/                 # Base UI components (shadcn)
│   ├── animated/           # Animated wrapper components
│   │   ├── reveal.tsx      # Scroll reveal wrapper
│   │   ├── magnetic.tsx    # Magnetic cursor effect
│   │   ├── parallax.tsx    # Parallax container
│   │   └── text-split.tsx  # Character/word split animation
│   ├── sections/           # Page sections
│   │   ├── hero.tsx
│   │   ├── features.tsx
│   │   ├── testimonials.tsx
│   │   └── footer.tsx
│   └── layout/             # Navigation, cursor, loaders
├── hooks/
│   ├── use-smooth-scroll.ts
│   ├── use-mouse-position.ts
│   └── use-in-view.ts
├── lib/
│   ├── animations.ts       # Shared animation configs
│   ├── utils.ts
│   └── fonts.ts            # Font loading
└── styles/
    ├── globals.css
    └── animations.css       # Keyframe definitions
```

## Accessibility Requirements (Non-Negotiable)
```typescript
// Always wrap animations with reduced motion check
const prefersReducedMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)"
).matches;

// React hook
function useReducedMotion() {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReduced(mq.matches);
    const handler = (e: MediaQueryListEvent) => setReduced(e.matches);
    mq.addEventListener("change", handler);
    return () => mq.removeEventListener("change", handler);
  }, []);
  return reduced;
}
```

## Sub-Skills (Delegated)
When deeper expertise is needed, delegate to:
- `gsap-animations` — GSAP ScrollTrigger, timelines, advanced tweens
- `framer-motion-react` — Framer Motion for React apps
- `threejs-webgl` — 3D scenes, shaders, particle systems
- `animated-ui-components` — Magic UI, Aceternity UI, copy-paste components
- `smooth-scroll-design` — Lenis, Locomotive, parallax patterns

