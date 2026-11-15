---
name: animated-ui-components
description: Copy-paste animated UI components from Magic UI, Aceternity UI, and custom patterns — shimmer buttons, spotlight cards, animated gradients, text effects, bento grids, and hero sections. Use when the user wants hype animated components without building from scratch.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Animated UI Components

## When to Activate
- User wants "hype", "cool", "animated" UI components
- User mentions Magic UI, Aceternity UI, or animated component libraries
- User wants shimmer, glow, spotlight, gradient, or particle effects
- User needs a hero section, bento grid, or animated card

## Dependencies
```bash
npm install motion clsx tailwind-merge
```

## Utility
```typescript
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

---

## Component Library

### 1. Shimmer Button
```tsx
function ShimmerButton({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <button className={cn(
      "group relative inline-flex items-center justify-center overflow-hidden rounded-lg",
      "bg-zinc-900 px-6 py-3 text-sm font-medium text-white",
      "transition-all duration-300 hover:scale-105", className
    )}>
      <span className="absolute inset-0 overflow-hidden rounded-lg">
        <span className="absolute inset-0 -translate-x-full animate-[shimmer_2s_infinite] bg-gradient-to-r from-transparent via-white/10 to-transparent" />
      </span>
      <span className="absolute inset-0 rounded-lg bg-gradient-to-r from-indigo-500/20 to-purple-500/20 opacity-0 transition-opacity group-hover:opacity-100" />
      <span className="relative">{children}</span>
    </button>
  );
}
```

### 2. Spotlight Card
```tsx
"use client";
import { useRef, useState } from "react";

function SpotlightCard({ children, className }: { children: React.ReactNode; className?: string }) {
  const divRef = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [opacity, setOpacity] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!divRef.current) return;
    const rect = divRef.current.getBoundingClientRect();
    setPosition({ x: e.clientX - rect.left, y: e.clientY - rect.top });
  };

  return (
    <div ref={divRef} onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)} onMouseLeave={() => setOpacity(0)}
      className={cn("relative overflow-hidden rounded-xl border border-white/10 bg-zinc-950 p-8", className)}>
      <div className="pointer-events-none absolute -inset-px transition-opacity duration-300"
        style={{ opacity, background: `radial-gradient(600px circle at ${position.x}px ${position.y}px, rgba(99,102,241,0.1), transparent 40%)` }} />
      <div className="relative">{children}</div>
    </div>
  );
}
```

### 3. Animated Gradient Text
```tsx
function GradientText({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <span className={cn(
      "inline-block bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500",
      "bg-[length:200%_auto] bg-clip-text text-transparent",
      "animate-[gradient_3s_linear_infinite]", className
    )}>{children}</span>
  );
}
```

### 4. Bento Grid
```tsx
function BentoGrid({ children }: { children: React.ReactNode }) {
  return <div className="grid auto-rows-[18rem] grid-cols-3 gap-4">{children}</div>;
}

function BentoCard({ title, description, icon, className, children }: {
  title: string; description: string; icon?: React.ReactNode; className?: string; children?: React.ReactNode;
}) {
  return (
    <div className={cn("group relative overflow-hidden rounded-xl border border-white/10 bg-zinc-950 transition-all duration-300 hover:border-white/20", className)}>
      <div className="relative z-10 p-6">
        {icon && <div className="mb-4 text-indigo-400">{icon}</div>}
        <h3 className="text-lg font-semibold text-white">{title}</h3>
        <p className="mt-2 text-sm text-zinc-400">{description}</p>
      </div>
      {children}
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/5 to-purple-500/5 opacity-0 transition-opacity group-hover:opacity-100" />
    </div>
  );
}
```

### 5. Animated Counter
```tsx
"use client";
import { useInView, useMotionValue, useSpring } from "motion/react";
import { useEffect, useRef } from "react";

function AnimatedCounter({ value, className }: { value: number; className?: string }) {
  const ref = useRef<HTMLSpanElement>(null);
  const motionValue = useMotionValue(0);
  const springValue = useSpring(motionValue, { damping: 60, stiffness: 100 });
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  useEffect(() => { if (isInView) motionValue.set(value); }, [motionValue, isInView, value]);
  useEffect(() => {
    return springValue.on("change", (latest) => {
      if (ref.current) ref.current.textContent = Intl.NumberFormat("en-US").format(Math.floor(latest));
    });
  }, [springValue]);

  return <span ref={ref} className={className} />;
}
```

### 6. Marquee / Infinite Scroll
```tsx
function Marquee({ children, speed = 40, direction = "left", className }: {
  children: React.ReactNode; speed?: number; direction?: "left" | "right"; className?: string;
}) {
  return (
    <div className={cn("flex overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_10%,black_90%,transparent)]", className)}>
      <div className="flex animate-marquee gap-4"
        style={{ animationDuration: `${speed}s`, animationDirection: direction === "right" ? "reverse" : "normal" }}>
        {children}{children}
      </div>
    </div>
  );
}
```

### 7. Glow Border Card
```tsx
function GlowCard({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={cn("relative rounded-xl p-[1px]", className)}>
      <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 opacity-75 blur-sm" />
      <div className="absolute inset-0 rounded-xl bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500" />
      <div className="relative rounded-[11px] bg-zinc-950 p-6">{children}</div>
    </div>
  );
}
```

### 8. Animated Hero Section (Full Pattern)
```tsx
export function HeroSection() {
  return (
    <section className="relative flex min-h-screen items-center justify-center overflow-hidden bg-zinc-950">
      {/* Gradient orbs */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -left-[10%] top-[20%] h-[500px] w-[500px] rounded-full bg-indigo-500/20 blur-[120px]" />
        <div className="absolute -right-[10%] top-[10%] h-[400px] w-[400px] rounded-full bg-purple-500/20 blur-[120px]" />
        <div className="absolute bottom-[10%] left-[30%] h-[300px] w-[300px] rounded-full bg-pink-500/15 blur-[120px]" />
      </div>
      {/* Grid overlay */}
      <div className="absolute inset-0 opacity-20"
        style={{ backgroundImage: `linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)`, backgroundSize: "64px 64px" }} />
      {/* Content */}
      <div className="relative z-10 mx-auto max-w-4xl px-6 text-center">
        <motion.div initial={{ opacity: 0, y: 40 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}>
          <span className="mb-4 inline-block rounded-full border border-indigo-500/30 bg-indigo-500/10 px-4 py-1.5 text-sm text-indigo-400">
            ✨ Something amazing
          </span>
          <h1 className="mt-6 text-5xl font-bold tracking-tight text-white sm:text-7xl">
            Build something <GradientText>incredible</GradientText>
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg text-zinc-400">
            Create stunning websites with beautiful animations.
          </p>
          <div className="mt-10 flex items-center justify-center gap-4">
            <ShimmerButton>Get Started</ShimmerButton>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
```

## Tailwind Keyframes (Add to tailwind.config.ts)
```typescript
keyframes: {
  shimmer: { "100%": { transform: "translateX(100%)" } },
  gradient: { "0%, 100%": { backgroundPosition: "0% center" }, "50%": { backgroundPosition: "100% center" } },
  marquee: { "0%": { transform: "translateX(0)" }, "100%": { transform: "translateX(-50%)" } },
}
```

## References
- Magic UI: magicui.design
- Aceternity UI: ui.aceternity.com
- shadcn/ui: ui.shadcn.com

