---
name: framer-motion-react
description: Framer Motion (Motion) patterns for React — page transitions, layout animations, gestures, scroll-triggered reveals, exit animations, and shared layout animations. Use when building animated React/Next.js UIs with Framer Motion.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Framer Motion for React

## When to Activate
- User wants React component animations
- User mentions Framer Motion, motion/react, or "motion"
- User needs page transitions in Next.js
- User wants gesture-based animations (drag, hover, tap)
- User needs layout animations or shared element transitions

## Installation
```bash
npm install motion
```

## Core Patterns

### 1. Basic Animation
```tsx
import { motion } from "motion/react";

<motion.div
  initial={{ opacity: 0, y: 40 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
>
  Content
</motion.div>
```

### 2. Exit Animation
```tsx
import { AnimatePresence } from "motion/react";

<AnimatePresence mode="wait">
  {isVisible && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.3 }}
    >
      Modal Content
    </motion.div>
  )}
</AnimatePresence>
```

### 3. Scroll-Triggered Reveal
```tsx
"use client";
import { motion, useInView } from "motion/react";
import { useRef } from "react";

function RevealOnScroll({ children }: { children: React.ReactNode }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 75 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 75 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  );
}
```

### 4. Stagger Children
```tsx
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.2 },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1, y: 0,
    transition: { duration: 0.5, ease: [0.22, 1, 0.36, 1] },
  },
};

<motion.ul variants={containerVariants} initial="hidden" animate="visible">
  {items.map((item) => (
    <motion.li key={item.id} variants={itemVariants}>
      {item.name}
    </motion.li>
  ))}
</motion.ul>
```

### 5. Page Transitions (Next.js App Router)
```tsx
// app/template.tsx
"use client";
import { motion } from "motion/react";

export default function Template({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  );
}
```

### 6. Gesture Animations
```tsx
// Hover + Tap
<motion.button
  whileHover={{ scale: 1.05, backgroundColor: "#6366f1" }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
>
  Click Me
</motion.button>

// Drag
<motion.div
  drag
  dragConstraints={{ left: -100, right: 100, top: -50, bottom: 50 }}
  dragElastic={0.2}
  whileDrag={{ scale: 1.1, cursor: "grabbing" }}
/>
```

### 7. Magnetic Cursor Effect
```tsx
function MagneticButton({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouse = (e: React.MouseEvent) => {
    const { clientX, clientY } = e;
    const { left, top, width, height } = ref.current!.getBoundingClientRect();
    setPosition({
      x: (clientX - (left + width / 2)) * 0.3,
      y: (clientY - (top + height / 2)) * 0.3,
    });
  };

  return (
    <motion.div
      ref={ref}
      animate={{ x: position.x, y: position.y }}
      transition={{ type: "spring", stiffness: 150, damping: 15 }}
      onMouseMove={handleMouse}
      onMouseLeave={() => setPosition({ x: 0, y: 0 })}
    >
      {children}
    </motion.div>
  );
}
```

### 8. Layout Animations
```tsx
<motion.div layout layoutId={`card-${item.id}`}>
  <motion.h2 layout="position">{item.title}</motion.h2>
  <AnimatePresence>
    {isExpanded && (
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      >
        {item.description}
      </motion.p>
    )}
  </AnimatePresence>
</motion.div>
```

### 9. Text Animation
```tsx
function AnimatedText({ text }: { text: string }) {
  const words = text.split(" ");
  return (
    <motion.p
      initial="hidden"
      animate="visible"
      variants={{ visible: { transition: { staggerChildren: 0.05 } } }}
    >
      {words.map((word, i) => (
        <motion.span
          key={i}
          className="inline-block mr-[0.25em]"
          variants={{
            hidden: { opacity: 0, y: 20, filter: "blur(8px)" },
            visible: { opacity: 1, y: 0, filter: "blur(0px)", transition: { duration: 0.4 } },
          }}
        >
          {word}
        </motion.span>
      ))}
    </motion.p>
  );
}
```

## Easing Presets
```typescript
const easings = {
  smooth: [0.22, 1, 0.36, 1],
  snappy: [0.16, 1, 0.3, 1],
  bounce: { type: "spring", stiffness: 400, damping: 17 },
  gentle: { type: "spring", stiffness: 120, damping: 14 },
  slow: { duration: 0.8, ease: [0.22, 1, 0.36, 1] },
};
```

## Performance Rules
1. Use `layout` prop sparingly — it forces re-measurement
2. Prefer `transform` and `opacity` (GPU-accelerated)
3. Use `AnimatePresence mode="wait"` for sequential page transitions
4. Memoize variants objects — don't create inline on every render

## Accessibility
```tsx
import { useReducedMotion } from "motion/react";

function MyComponent() {
  const shouldReduceMotion = useReducedMotion();
  return (
    <motion.div
      animate={{ x: 100 }}
      transition={{ duration: shouldReduceMotion ? 0 : 0.5 }}
    />
  );
}
```

