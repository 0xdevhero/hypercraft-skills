---
name: hyper-ui-craft
description: Enforces human-grade frontend craftsmanship and bans generic AI-generated aesthetic slop. Governs visual hierarchy, theme systems, shadcn/ui components, Tailwind utilities, and strict accessibility. Use when building landing pages, web dashboards, UI components, or refactoring existing interfaces to look professional and authentic.
version: 1.0.0
---

# HyperUI Craft: Anti-AI-Slop & Component Crafting

> **Core Philosophy**: A coding assistant generates template slop by default. HyperUI Craft establishes an unbreachable floor of senior design standards: one strong idea per screen, authentic material feel, and zero cliché shortcuts.

---

## The HyperCraft Floor (Non-Negotiable Rules)

Every web page, component, or layout generated MUST comply with these 14 strict rules:

1. **Tokens at :root**: Every color, font-family, radius, and shadow must be declared as a CSS variable at :root. Never write raw hex colors or hardcoded font names inside component utility classes.
2. **Never 	ransition: all**: Animate only composite properties (	ransform, opacity). Never animate width, height, 	op, or left.
3. **No Unearned Gradients**: Never use generic purple-to-blue or rainbow gradient backgrounds. Use rich, intentional background neutrals (#020617, #09090b, #f8fafc).
4. **No Emojis as Icons**: Never use emojis (ðŸš€, âœ…, â­) as UI icons. Use precision SVG icons (Lucide, Heroicons, Phosphor).
5. **No Nested Cards**: Never put a card inside a card. Use subtle background tinting, divider lines, or whitespace for visual grouping.
6. **Instant :focus-visible**: Every interactive element (button, link, input) must have a crisp, visible focus ring for keyboard navigation. Never outline: none without replacement.
7. **Overflow Safety**: Always set overflow-x: clip on html and ody. Never allow horizontal scrollbars to leak on mobile or desktop viewports.
8. **Reduced Motion**: Every CSS animation must include a @media (prefers-reduced-motion: reduce) override.
9. **Typography Hierarchy**: Use max 2 font families (e.g. Geist Sans + Geist Mono or Inter + Fira Code). Base body size: 16px, line-height 1.5 to 1.6.
10. **Touch Targets**: All clickable and touch targets must be at least 44x44px with a minimum 8px gap on touch viewports.
11. **Contrast Ratio**: Text against backgrounds must pass WCAG 2.1 AA contrast ratio (minimum 4.5:1 for body text, 3:1 for large headers).
12. **Hero Discipline**: In 1280x800 desktop viewports, the hero headline, sub-headline, and primary call-to-action (CTA) must all be visible above the fold without scrolling.
13. **Real Copy Only**: Never invent fake testimonials, fake company logos, or placeholder metrics ("10M+ Users") unless provided by the user.
14. **Cursor Pointers**: Always ensure cursor-pointer is applied to all buttons, clickable cards, and interactive toggles.

---

## Component Architecture (shadcn/ui + Tailwind)

### Layer 1: Radix Primitives
Build complex interactive components (Dialogs, Dropdowns, Tabs, Command Palettes) on unstyled accessible primitives to guarantee full keyboard and ARIA compliance.

### Layer 2: Tailwind Utility Classes
Compose layouts with responsive utility classes:
* Mobile-first breakpoints: sm: (640px), md: (768px), lg: (1024px), xl: (1280px).
* CSS Grid for dashboards: grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4.
* Card surfaces: g-card text-card-foreground border border-border/40 shadow-sm rounded-xl p-6.

---

## Commands & Workflows

* **Full Redesign Mode**:
  When asked to redesign an existing messy page, keep all underlying form state, API hooks, and event handlers 100% intact while completely replacing the visual layout and CSS tokens.
* **Audit Mode**:
  Scan an existing HTML/JSX/Vue file and list every violation of the HyperCraft Floor rules with exact line numbers and proposed fixes.