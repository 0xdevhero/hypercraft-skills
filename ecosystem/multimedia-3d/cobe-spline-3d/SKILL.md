---
name: cobe-spline-3d
description: Modern 3D web experiences using Cobe (ultra-lightweight 5kB interactive 3D WebGL globe) and Spline 3D (@splinetool/react-spline). Use when creating interactive 3D landing pages, global network maps, product showcases, and interactive 3D canvas models.

metadata:
  author: HyperCraft Core Team
  license: Apache-2.0
---

# Cobe & Spline 3D Integration

## When to Activate
- User wants an interactive 3D globe (like Stripe, GitHub, or AI cloud infrastructure).
- User wants interactive 3D scenes designed in Spline embedded into React or Next.js.
- User mentions `cobe`, `Spline`, or lightweight 3D web visualizations.

---

## 1. Cobe: 5kB Interactive WebGL Globe

### Installation
```bash
npm install cobe
```

### Full Next.js React Component
```tsx
"use client";
import createGlobe from "cobe";
import { useEffect, useRef } from "react";

export function InteractiveGlobe({
  className = "w-[500px] h-[500px]",
}: {
  className?: string;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const pointerInteracting = useRef<number | null>(null);
  const pointerInteractionMovement = useRef(0);

  useEffect(() => {
    let phi = 0;
    let width = 0;

    const onResize = () => {
      if (canvasRef.current) {
        width = canvasRef.current.offsetWidth;
      }
    };
    window.addEventListener("resize", onResize);
    onResize();

    const globe = createGlobe(canvasRef.current!, {
      devicePixelRatio: 2,
      width: width * 2,
      height: width * 2,
      phi: 0,
      theta: 0.25,
      dark: 1,
      diffuse: 1.2,
      mapSamples: 16000,
      mapBrightness: 6,
      baseColor: [0.3, 0.3, 0.4],
      markerColor: [0.4, 0.5, 1],
      glowColor: [0.15, 0.2, 0.4],
      markers: [
        // longitude, latitude
        { location: [23.8103, 90.4125], size: 0.08 }, // Dhaka
        { location: [37.7749, -122.4194], size: 0.08 }, // San Francisco
        { location: [51.5074, -0.1278], size: 0.08 }, // London
        { location: [35.6762, 139.6503], size: 0.08 }, // Tokyo
      ],
      onRender: (state) => {
        // Auto-rotation when not dragging
        if (!pointerInteracting.current) {
          phi += 0.003;
        }
        state.phi = phi + pointerInteractionMovement.current;
        state.width = width * 2;
        state.height = width * 2;
      },
    });

    return () => {
      globe.destroy();
      window.removeEventListener("resize", onResize);
    };
  }, []);

  return (
    <div className={`relative flex items-center justify-center ${className}`}>
      <canvas
        ref={canvasRef}
        style={{ width: "100%", height: "100%", contain: "layout paint size" }}
        onPointerDown={(e) => {
          pointerInteracting.current =
            e.clientX - pointerInteractionMovement.current;
          canvasRef.current!.style.cursor = "grabbing";
        }}
        onPointerUp={() => {
          pointerInteracting.current = null;
          canvasRef.current!.style.cursor = "grab";
        }}
        onPointerOut={() => {
          pointerInteracting.current = null;
          canvasRef.current!.style.cursor = "grab";
        }}
        onMouseMove={(e) => {
          if (pointerInteracting.current !== null) {
            const delta = e.clientX - pointerInteracting.current;
            pointerInteractionMovement.current = delta * 0.005;
          }
        }}
      />
    </div>
  );
}
```

---

## 2. Spline 3D Integration (`@splinetool/react-spline`)

### Installation
```bash
npm install @splinetool/react-spline @splinetool/runtime
```

### Full Spline Client Component
```tsx
"use client";
import dynamic from "next/dynamic";
import { useState } from "react";

// Dynamically load to keep client bundle lightweight & avoid SSR issues
const Spline = dynamic(() => import("@splinetool/react-spline"), {
  ssr: false,
  loading: () => (
    <div className="flex h-full w-full items-center justify-center bg-zinc-950">
      <div className="h-8 w-8 animate-spin rounded-full border-2 border-indigo-500 border-t-transparent" />
    </div>
  ),
});

export function SplineHero({
  sceneUrl = "https://prod.spline.design/6Wq1Q7YGyM-iab9i/scene.splinecode",
}: {
  sceneUrl?: string;
}) {
  const [splineApp, setSplineApp] = useState<any>(null);

  function onLoad(spline: any) {
    setSplineApp(spline);
  }

  return (
    <div className="relative h-[600px] w-full overflow-hidden rounded-2xl bg-zinc-950">
      <Spline scene={sceneUrl} onLoad={onLoad} />
    </div>
  );
}
```

## Performance Guidelines
1. **Always lazy load:** Keep 3D canvas runtimes outside the main server bundle via `next/dynamic` with `ssr: false`.
2. **Cobe vs Three.js Globe:** If only showing a globe with pins, **always pick Cobe** (5kB) instead of bulky Three.js models (500kB+).
3. **Spline Asset Optimization:** In Spline export settings, compress texture sizes to WebP/1K resolution to ensure fast load on mobile devices.

