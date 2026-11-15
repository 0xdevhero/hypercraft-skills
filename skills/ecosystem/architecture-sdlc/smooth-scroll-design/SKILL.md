---
name: smooth-scroll-design
description: Smooth scrolling patterns with Lenis and Locomotive Scroll — parallax, horizontal scroll, scroll-linked animations, and premium scroll experiences. Use when adding smooth scroll, parallax, or scroll-driven design to a website.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Smooth Scroll Design

## When to Activate
- User wants smooth/butter scrolling
- User mentions Lenis, Locomotive Scroll
- User wants parallax or scroll-linked effects
- User wants premium scroll feel like Awwwards sites

## Installation
```bash
npm install lenis
```

## Lenis Setup

### 1. Next.js App Router Integration
```tsx
"use client";
import Lenis from "lenis";
import { useEffect } from "react";

export function SmoothScroll({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
      touchMultiplier: 2,
    });

    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
    return () => lenis.destroy();
  }, []);

  return <>{children}</>;
}
```

### 2. Lenis + GSAP ScrollTrigger Sync
```tsx
"use client";
import Lenis from "lenis";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useEffect } from "react";

gsap.registerPlugin(ScrollTrigger);

export function useSmoothScroll() {
  useEffect(() => {
    const lenis = new Lenis();
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);
    return () => { lenis.destroy(); };
  }, []);
}
```

### 3. CSS Requirements
```css
html.lenis, html.lenis body { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto !important; }
.lenis.lenis-smooth [data-lenis-prevent] { overscroll-behavior: contain; }
.lenis.lenis-stopped { overflow: hidden; }
.lenis.lenis-scrolling iframe { pointer-events: none; }
```

## Scroll Patterns

### 4. Horizontal Scroll Section
```tsx
function HorizontalScroll({ panels }: { panels: { content: React.ReactNode }[] }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const scrollEl = scrollRef.current!;
    const totalWidth = scrollEl.scrollWidth - window.innerWidth;
    gsap.to(scrollEl, {
      x: -totalWidth,
      ease: "none",
      scrollTrigger: {
        trigger: containerRef.current,
        start: "top top",
        end: () => `+=${totalWidth}`,
        scrub: 1,
        pin: true,
        anticipatePin: 1,
      },
    });
  });

  return (
    <div ref={containerRef} className="overflow-hidden">
      <div ref={scrollRef} className="flex gap-8">
        {panels.map((panel, i) => (
          <div key={i} className="h-screen w-screen flex-shrink-0">{panel.content}</div>
        ))}
      </div>
    </div>
  );
}
```

### 5. Parallax Section
```tsx
function ParallaxSection({ children, speed = 0.5, className }: {
  children: React.ReactNode; speed?: number; className?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  useGSAP(() => {
    gsap.to(ref.current, {
      yPercent: -100 * speed,
      ease: "none",
      scrollTrigger: { trigger: ref.current, start: "top bottom", end: "bottom top", scrub: true },
    });
  });
  return (
    <div className={cn("overflow-hidden", className)}>
      <div ref={ref}>{children}</div>
    </div>
  );
}
```

### 6. Scroll Progress Indicator
```tsx
"use client";
import { motion, useScroll } from "motion/react";

function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  return (
    <motion.div
      className="fixed left-0 right-0 top-0 z-50 h-1 origin-left bg-indigo-500"
      style={{ scaleX: scrollYProgress }}
    />
  );
}
```

### 7. Reusable Scroll Reveal
```tsx
function ScrollReveal({ children, direction = "up", delay = 0, className }: {
  children: React.ReactNode; direction?: "up" | "down" | "left" | "right"; delay?: number; className?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const directionMap = { up: { y: 80 }, down: { y: -80 }, left: { x: 80 }, right: { x: -80 } };

  useGSAP(() => {
    gsap.from(ref.current, {
      ...directionMap[direction], opacity: 0, duration: 1, delay, ease: "power3.out",
      scrollTrigger: { trigger: ref.current, start: "top 85%", toggleActions: "play none none reverse" },
    });
  });

  return <div ref={ref} className={className}>{children}</div>;
}
```

## Accessibility
```typescript
const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (!prefersReduced) {
  // Initialize Lenis only when motion is OK
}
```

