---
name: opus-video-prompts
description: Curated viral motion graphics, 3D scenes, HTML5 Canvas, SVG, and Remotion video prompts for code-driven animation. Use when building programmatic videos, high-end product showreels, kinetic typography, or mathematical explainers.
---

# Code-Driven Video & Motion Architecture Studio

Design and generate publication-grade, programmatic video animations, kinetic graphics, and generative 3D scenes. All animations are strictly deterministic, code-based, and rendered without video diffusion artifacts.

---

## 🏛️ Core Architecture Principles (Code-as-Video)

1. **Deterministic Frame-Based Rendering:**
   Every frame `f` is a pure mathematical function of `time` or `frameNumber`.
   - Never use `Date.now()`, `setTimeout()`, or unseeded `Math.random()`.
   - Ensure 100% reproducibility across renders.
2. **Mathematical Spring Physics & Closed-Form Easing:**
   - Use closed-form damped harmonic oscillator equations or Remotion `spring()` / cubic-bezier curves.
   - Avoid linear transitions; natural motion accelerates with anticipation and settles smoothly.
3. **Zero Diffusion Artifacts (Vector & Canvas Fidelity):**
   - 100% sharp SVG paths, HTML5 Canvas 2D contexts, WebGL/Three.js fragment shaders, or React/Remotion compositions.
   - Crisp typography, perfectly rasterized curves, and zero temporal flickering.
4. **Beat-Locked Synchronization:**
   - Align cuts, transitions, camera moves, and typography reveals precisely to an audio BPM grid.
   - Example: at 120 BPM and 30 FPS, each musical beat is exactly 15 frames.

---

## 🎨 Supported Video Stacks & Implementation Patterns

### 1. React & Remotion (Programmatic 4K/60fps Video)
```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

export const HeroIntro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.8 },
  });

  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#09090b", justifyContent: "center", alignItems: "center" }}>
      <h1 style={{ transform: `scale(${scale})`, opacity, color: "#fafafa", fontSize: 72, fontFamily: "sans-serif" }}>
        Autonomous Code Engine
      </h1>
    </AbsoluteFill>
  );
};
```

### 2. High-Performance HTML5 Canvas Loop
```javascript
// Deterministic canvas render loop
function renderFrame(ctx, width, height, frame, totalFrames) {
  const progress = frame / totalFrames;
  ctx.fillStyle = "#0a0a0c";
  ctx.fillRect(0, 0, width, height);

  const radius = 80 + Math.sin(progress * Math.PI * 4) * 20;
  const cx = width / 2;
  const cy = height / 2;

  const gradient = ctx.createRadialGradient(cx, cy, 10, cx, cy, radius * 1.5);
  gradient.addColorStop(0, "rgba(99, 102, 241, 0.9)");
  gradient.addColorStop(1, "rgba(99, 102, 241, 0)");

  ctx.fillStyle = gradient;
  ctx.beginPath();
  ctx.arc(cx, cy, radius, 0, Math.PI * 2);
  ctx.fill();
}
```

### 3. Kinetic SVG Typography & Morphing
- Use SVG `stroke-dasharray` and `stroke-dashoffset` for self-drawing line art and technical schematics.
- Wrap titles in letter-staggered `transform: translateY()` reveals with easing: `cubic-bezier(0.16, 1, 0.3, 1)`.

### 4. Three.js / WebGL Procedural 3D
- Bind scene rotation, camera focal length, and lighting uniforms to normalized `time = frame / fps`.
- Apply post-processing bloom and chromatic aberration subtly to enhance depth without degrading legibility.

---

## 🎬 Curated Prompt Archetypes

| Category | Primary Visual Hook | Recommended Stack | Frame Budget (at 30 FPS) |
|---|---|---|---|
| **Product Showreel** | Dark-mode isometric card exploding into layers | Remotion + Three.js | 180 frames (6s) |
| **Technical Explainer** | Flowchart connecting microservices with glowing data packets | SVG + Canvas | 240 frames (8s) |
| **Kinetic Title Sequence** | Beat-synced typography with variable font weight shifts | Remotion + CSS | 90 frames (3s) |
| **Data Visualization** | 3D bar chart rising with particle burst on milestone | Three.js + Spring | 150 frames (5s) |

---

## 🛠️ Verification Checklist Before Rendering

- [ ] Zero unseeded randomness: replace random seeds with deterministic hashes based on index or frame.
- [ ] Explicit resolution bounds: test at 1920x1080 (16:9) and 1080x1920 (9:16 vertical reels).
- [ ] Frame rate locked: standard 30 FPS for web/social, 60 FPS for ultra-smooth UI animations.
- [ ] Contrast ratio: text elements must maintain a minimum 4.5:1 contrast against motion backgrounds.
