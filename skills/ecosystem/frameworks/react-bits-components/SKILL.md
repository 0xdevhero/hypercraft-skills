---
name: react-bits-components
description: Interactive, animated components and dynamic backgrounds from React Bits (reactbits.dev). Covers canvas/WebGL backgrounds, text animations (split, scramble, decrypt), particle waves, gravity buttons, and magnetic lines for modern landing pages.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# React Bits Components

## When to Activate
- User wants modern, interactive micro-animations and eye-catching UI elements.
- User requests particle backgrounds, glitch/decrypted text, pixel grids, or magnetic elements.
- User references React Bits (`reactbits.dev` or `DavidHDev/react-bits`).
- Ideal for AI product showcases, developer tools, and cutting-edge landing pages.

## Core Patterns & Recipes

### 1. Decrypted Text (Cyberpunk / Terminal Scramble)
```tsx
"use client";
import { useEffect, useState, useRef } from "react";

interface DecryptedTextProps {
  text: string;
  speed?: number;
  maxIterations?: number;
  characters?: string;
  className?: string;
}

export function DecryptedText({
  text,
  speed = 50,
  maxIterations = 10,
  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+",
  className,
}: DecryptedTextProps) {
  const [displayText, setDisplayText] = useState(text);
  const [isHovering, setIsHovering] = useState(false);
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  const scramble = () => {
    let iteration = 0;
    if (intervalRef.current) clearInterval(intervalRef.current);

    intervalRef.current = setInterval(() => {
      setDisplayText((prev) =>
        text
          .split("")
          .map((char, index) => {
            if (char === " ") return " ";
            if (index < iteration) return text[index];
            return characters[Math.floor(Math.random() * characters.length)];
          })
          .join("")
      );

      if (iteration >= text.length) {
        if (intervalRef.current) clearInterval(intervalRef.current);
      }
      iteration += 1 / maxIterations;
    }, speed);
  };

  useEffect(() => {
    scramble();
    return () => {
      if (intervalRef.current) clearInterval(intervalRef.current);
    };
  }, [text]);

  return (
    <span
      className={className}
      onMouseEnter={() => {
        setIsHovering(true);
        scramble();
      }}
      onMouseLeave={() => setIsHovering(false)}
    >
      {displayText}
    </span>
  );
}
```

### 2. Interactive Pixel Background Grid
```tsx
"use client";
import React, { useEffect, useRef } from "react";

export function PixelGrid({
  gridSize = 30,
  glowColor = "rgba(99, 102, 241, 0.4)",
  baseColor = "rgba(255, 255, 255, 0.03)",
}: {
  gridSize?: number;
  glowColor?: string;
  baseColor?: string;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrameId: number;
    let mouse = { x: -1000, y: -1000 };

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    handleResize();
    window.addEventListener("resize", handleResize);

    const handleMouseMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
    };
    window.addEventListener("mousemove", handleMouseMove);

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cols = Math.ceil(canvas.width / gridSize);
      const rows = Math.ceil(canvas.height / gridSize);

      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          const x = i * gridSize;
          const y = j * gridSize;
          const dx = mouse.x - (x + gridSize / 2);
          const dy = mouse.y - (y + gridSize / 2);
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 120) {
            ctx.fillStyle = glowColor;
            ctx.fillRect(x + 1, y + 1, gridSize - 2, gridSize - 2);
          } else {
            ctx.fillStyle = baseColor;
            ctx.fillRect(x + 1, y + 1, gridSize - 2, gridSize - 2);
          }
        }
      }
      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      window.removeEventListener("resize", handleResize);
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(animationFrameId);
    };
  }, [gridSize, glowColor, baseColor]);

  return (
    <canvas
      ref={canvasRef}
      className="pointer-events-none fixed inset-0 z-0 h-full w-full"
    />
  );
}
```

### 3. Magnet Lines / Cursor Pull
```tsx
"use client";
import React, { useRef, useState, useEffect } from "react";

export function MagnetItem({
  children,
  strength = 30,
}: {
  children: React.ReactNode;
  strength?: number;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e: MouseEvent) => {
    if (!ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const dist = Math.hypot(e.clientX - centerX, e.clientY - centerY);

    if (dist < 150) {
      const x = ((e.clientX - centerX) / 150) * strength;
      const y = ((e.clientY - centerY) / 150) * strength;
      setPosition({ x, y });
    } else {
      setPosition({ x: 0, y: 0 });
    }
  };

  useEffect(() => {
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, [strength]);

  return (
    <div
      ref={ref}
      style={{
        transform: `translate3d(${position.x}px, ${position.y}px, 0)`,
        transition: "transform 0.15s ease-out",
      }}
    >
      {children}
    </div>
  );
}
```

## Best Practices
- Keep interactive canvas backgrounds in separate client components using `pointer-events-none` so clicks pass through to UI content.
- Use `requestAnimationFrame` and throttled mouse listeners for performance.
- Respect `prefers-reduced-motion` by freezing scrambles or random motion.
