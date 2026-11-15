---
name: tailwindcss-motion
description: Utility-first CSS animation patterns with tailwindcss-motion (by RomboHQ). Provides zero-runtime JS overhead, preset CSS classes (motion-preset-fade, motion-preset-slide, bounce, pulse), fluid custom animations, and built-in accessibility.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Tailwind CSS Motion

## When to Activate
- User wants animations with zero JavaScript bundle overhead (<5kB CSS).
- User prefers utility classes for motion rather than state hooks.
- User mentions `tailwindcss-motion`, RomboHQ, or lightweight Tailwind animations.
- Best for landing page micro-delights, buttons, toasts, modals, and list reveals.

## Installation & Setup

### For Tailwind v3
```bash
npm i -D tailwindcss-motion
```
In `tailwind.config.js`:
```js
module.exports = {
  theme: {
    extend: {},
  },
  plugins: [require("tailwindcss-motion")],
};
```

### For Tailwind v4
In `globals.css`:
```css
@import "tailwindcss";
@plugin "tailwindcss-motion";
```

## Ready-to-Use Presets

### 1. Hero Content Cascade
```html
<div class="flex flex-col items-center text-center space-y-4">
  <!-- Badge enters first with pop -->
  <span class="motion-preset-pop motion-duration-500 rounded-full bg-indigo-500/10 px-3 py-1 text-xs text-indigo-400">
    v2.0 Released
  </span>

  <!-- Headline slides up smoothly -->
  <h1 class="motion-preset-slide-up motion-duration-700 motion-delay-150 text-5xl font-bold tracking-tight text-white">
    Build faster with zero JS runtime
  </h1>

  <!-- Paragraph fades in -->
  <p class="motion-preset-fade motion-duration-700 motion-delay-300 max-w-xl text-zinc-400">
    Pure CSS keyframes generated directly by your Tailwind compiler.
  </p>

  <!-- CTA bounce in -->
  <button class="motion-preset-bounce motion-duration-800 motion-delay-500 rounded-lg bg-indigo-600 px-6 py-2.5 font-medium text-white shadow-lg hover:bg-indigo-500">
    Get Started
  </button>
</div>
```

### 2. Interactive Card Hover & Focus States
```html
<div class="group relative rounded-xl border border-white/10 bg-zinc-900 p-6 transition-all hover:border-indigo-500/50">
  <div class="motion-preset-pulse motion-duration-2000 inline-block p-3 rounded-lg bg-indigo-500/20 text-indigo-400 mb-3">
    ⚡
  </div>
  <h3 class="text-lg font-semibold text-white group-hover:motion-translate-x-in-[4px]">
    Lightning Performance
  </h3>
  <p class="mt-2 text-sm text-zinc-400">
    Hardware-accelerated transforms run completely off the main thread.
  </p>
</div>
```

### 3. Granular Modifiers (Custom Timing & Transforms)
- **Duration:** `motion-duration-300`, `motion-duration-700`, `motion-duration-[1500ms]`
- **Delay:** `motion-delay-100`, `motion-delay-300`, `motion-delay-500`
- **Scale:** `motion-scale-in-[0.8]`, `motion-scale-out-[0.9]`
- **Translate:** `motion-translate-y-in-[-20px]`, `motion-translate-x-in-[10%]`
- **Rotate:** `motion-rotate-in-[45deg]`
- **Blur:** `motion-blur-in-[10px]`

## Common Utility Combinations
```html
<!-- Soft modal entrance -->
<div class="motion-preset-slide-up motion-blur-in-[8px] motion-duration-500">
  Modal Body
</div>

<!-- Floating notification toast -->
<div class="motion-preset-slide-left motion-duration-400 motion-ease-spring-smooth">
  Toast Message
</div>
```

## Performance & Accessibility
- `tailwindcss-motion` automatically adheres to `@media (prefers-reduced-motion: reduce)`.
- All transforms (`translate`, `scale`, `rotate`, `opacity`) utilize CSS GPU composited layers.

