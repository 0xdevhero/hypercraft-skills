---
name: opus-video-prompts
description: Access and query 700+ curated viral Claude Opus 5.5 motion graphics, 3D scenes, Canvas, SVG, and Remotion video prompts from the awesome-opus5-5-videos library. Use when building code-driven animations, high-end product showreels, or kinetic video designs.
---

# Awesome Opus 5.5 Video Prompts & Code-Driven Animation Skill

This skill connects to the local database of 703 curated viral video prompts located at:
`assets/awesome-opus5-5-videos`

## Global CLI Commands

Run via powershell or command prompt:
- `opus-video.cmd stats` — Summary of categories and tech tags (motion, 3D, explainer, interactive).
- `opus-video.cmd search "<query>"` — Search prompts by keyword, tech stack, or author.
- `opus-video.cmd show <slug>` — Display the complete prompt and architecture.
- `opus-video.cmd random` — Fetch a random inspirational prompt.
- `opus-video.cmd list [category]` — List prompts by category (`motion`, `explainer`, `3d`, `interactive`).

## Core Architecture Principles (Code-as-Video)

1. **Deterministic Frame-Based Rendering:**
   Every frame `f` is a pure function of `time` or `frameNumber`. Zero `Date.now()`, zero `setTimeout()`, zero non-deterministic random rolls.
2. **Mathematical Spring Physics:**
   Use closed-form step responses or Remotion `spring()` / bezier easings instead of linear animations.
3. **No After Effects / No Video Diffusion Artifacts:**
   100% vector-sharp SVG, HTML5 Canvas, WebGL/Three.js, or React/Remotion. Crisp typography and zero AI warping.
4. **Beat-Locked Synchronization:**
   Align cuts, scene envelopes, and typography reveals precisely to audio BPM grids (e.g. 15 frames per beat at 120 BPM / 30 FPS).
