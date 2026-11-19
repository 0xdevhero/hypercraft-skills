---
name: video
description: Complete video production, Remotion programmatic video, and footage editing studio. Also triggered by the /video slash command. Use when building videos in React, editing footage, adding captions, audio mixing, or rendering.
---

# 🎬 /video — HyperCraft Video & Motion Studio

The `/video` slash command activates the full video production suite in `ecosystem/multimedia-3d/`.

## Capabilities Covered:
1. **Remotion Programmatic Video:** Code-driven 4K/60fps video in React (`ecosystem/multimedia-3d/remotion-video-creation/SKILL.md`).
   - Consult individual rule files for 3D (`rules/3d.md`), animations (`rules/animations.md`), audio (`rules/audio.md`), captions (`rules/display-captions.md`), charts, and transitions.
2. **Footage Cutting & Post-Production:** Real footage trimming, B-roll insertion, Descript/CapCut pipeline (`ecosystem/multimedia-3d/video-editing/SKILL.md`).
3. **Dialogue & Scene Search:** AI video and audio indexing with VideoDB (`ecosystem/multimedia-3d/videodb/SKILL.md`).
4. **Technical & Math Explainers:** 3Blue1Brown-style animations using Manim (`ecosystem/multimedia-3d/manim-video/SKILL.md`).
5. **Generative AI Video & Voice:** Text-to-video, image-to-video, speech-to-speech with fal.ai (`ecosystem/multimedia-3d/fal-ai-media/SKILL.md`).
6. **Automated UI Demo Capture:** Record automated walkthrough videos via Playwright (`ecosystem/multimedia-3d/ui-demo/SKILL.md`).

## Agent Execution Protocol:
- If the user is building video in React, read `ecosystem/multimedia-3d/remotion-video-creation/SKILL.md`.
- If the user is editing raw footage, read `ecosystem/multimedia-3d/video-editing/SKILL.md`.
- Follow strict aspect-ratio guidelines (`16:9` for YouTube/Landscape, `9:16` for TikTok/Shorts/Reels) and maintain audio loudness normalization (-14 LUFS).
