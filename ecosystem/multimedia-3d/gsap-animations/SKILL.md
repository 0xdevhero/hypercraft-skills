---
name: gsap-animations
description: GSAP (GreenSock Animation Platform) patterns for web animations — ScrollTrigger, timelines, text splitting, parallax, and Awwwards-level scroll experiences. Use when building scroll-driven animations, complex timelines, or high-performance web animations.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# GSAP Animations

## When to Activate
- User wants scroll-triggered animations
- User mentions GSAP, GreenSock, or ScrollTrigger
- User wants parallax, text reveal, pin sections
- User wants Awwwards / creative agency style animations

## Installation
```bash
npm install gsap @gsap/react
# Premium plugins (free for public repos)
npm install gsap@npm:@gsap/shockingly
```

## Core Concepts

### 1. Basic Tween
```typescript
import gsap from "gsap";

// To
gsap.to(".box", {
  x: 200,
  rotation: 360,
  duration: 1,
  ease: "power3.out"
});

// From
gsap.from(".box", {
  y: 100,
  opacity: 0,
  duration: 0.8,
  ease: "power2.out"
});

// FromTo
gsap.fromTo(".box",
  { y: 100, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.8 }
);
```

### 2. Timeline (Sequencing)
```typescript
const tl = gsap.timeline({
  defaults: { duration: 0.8, ease: "power3.out" }
});

tl.from(".hero-title", { y: 100, opacity: 0 })
  .from(".hero-subtitle", { y: 60, opacity: 0 }, "-=0.4")
  .from(".hero-cta", { y: 40, opacity: 0 }, "-=0.3")
  .from(".hero-image", { scale: 0.8, opacity: 0 }, "-=0.5");
```

### 3. ScrollTrigger (Most Important)
```typescript
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// Reveal on scroll
gsap.from(".section", {
  scrollTrigger: {
    trigger: ".section",
    start: "top 80%",
    end: "bottom 20%",
    toggleActions: "play none none reverse",
  },
  y: 100,
  opacity: 0,
  duration: 1,
});

// Scrub animation (tied to scroll position)
gsap.to(".progress-bar", {
  scrollTrigger: {
    trigger: ".content",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.5,
  },
  scaleX: 1,
});

// Pin section
gsap.to(".pinned-content", {
  scrollTrigger: {
    trigger: ".pin-section",
    start: "top top",
    end: "+=200%",
    pin: true,
    scrub: 1,
  },
  x: "-300%",
});
```

### 4. Text Split Animation
```typescript
function splitTextToChars(element: HTMLElement) {
  const text = element.textContent || "";
  element.innerHTML = text
    .split("")
    .map((char) =>
      char === " "
        ? '<span class="char">&nbsp;</span>'
        : `<span class="char">${char}</span>`
    )
    .join("");
  return element.querySelectorAll(".char");
}

const chars = splitTextToChars(document.querySelector(".title")!);
gsap.from(chars, {
  y: 100,
  opacity: 0,
  rotateX: -90,
  stagger: 0.02,
  duration: 0.8,
  ease: "back.out(1.7)",
  scrollTrigger: {
    trigger: ".title",
    start: "top 80%",
  },
});
```

### 5. Parallax Pattern
```typescript
gsap.to(".parallax-bg", {
  scrollTrigger: {
    trigger: ".parallax-section",
    start: "top bottom",
    end: "bottom top",
    scrub: true,
  },
  y: "-30%",
  ease: "none",
});

gsap.to(".parallax-mid", {
  scrollTrigger: {
    trigger: ".parallax-section",
    start: "top bottom",
    end: "bottom top",
    scrub: true,
  },
  y: "-15%",
  ease: "none",
});
```

### 6. Batch Scroll Reveal
```typescript
ScrollTrigger.batch("[data-animate]", {
  onEnter: (elements) => {
    gsap.from(elements, {
      y: 60,
      opacity: 0,
      duration: 0.8,
      ease: "power3.out",
      stagger: 0.15,
    });
  },
  start: "top 85%",
});
```

## React Integration
```typescript
"use client";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useRef } from "react";

gsap.registerPlugin(ScrollTrigger);

export function AnimatedSection({ children }: { children: React.ReactNode }) {
  const containerRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const elements = containerRef.current?.querySelectorAll("[data-animate]");
    if (!elements) return;

    elements.forEach((el) => {
      gsap.from(el, {
        scrollTrigger: {
          trigger: el,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
        y: 60,
        opacity: 0,
        duration: 0.8,
        ease: "power3.out",
      });
    });
  }, { scope: containerRef });

  return <div ref={containerRef}>{children}</div>;
}
```

## Common Easings
```
UI Interactions:    "power2.out"          — snappy, natural
Page Transitions:   "power3.inOut"        — smooth, elegant
Scroll Reveals:     "power3.out"          — decelerating entry
Bouncy Elements:    "back.out(1.7)"       — playful overshoot
Elastic:            "elastic.out(1, 0.3)" — spring-like
Smooth Scrub:       "none"                — linear for scroll-tied
```

## Performance Rules
1. Animate ONLY `transform` and `opacity` when possible
2. Use `will-change: transform` sparingly on animated elements
3. Use `gsap.set()` for initial states instead of CSS
4. Kill ScrollTriggers on component unmount
5. Use `scrub: 0.5` instead of `scrub: true` for smoother feel
6. Batch similar animations with `ScrollTrigger.batch()`

## Accessibility
```typescript
const prefersReducedMotion = gsap.matchMedia();
prefersReducedMotion.add("(prefers-reduced-motion: reduce)", () => {
  gsap.globalTimeline.timeScale(10);
});
```

