---
name: hyper
description: Master HyperCraft autonomous router. Also triggered by the /hyper slash command. Search and dynamically invoke any of the 511+ HyperCraft enterprise skills and 76 specialist agents.
---

# ⚡ /hyper — Master HyperCraft Autonomous Skill Router

The `/hyper` slash command is your universal entrypoint into the **511+ enterprise skills** and **76 specialist agents** of HyperCraft.

## How to Use
- `/hyper <topic>` (e.g. `/hyper remotion`, `/hyper solana`, `/hyper postgres`, `/hyper docker`)
- Or simply state what you need: `/hyper create a 4K product teaser with dynamic text`

## Execution Protocol for the Agent:
1. **Analyze User Intent:** Identify the technical domain from the query.
2. **Execute On-Disk Search:** Run:
   ```bash
   python scripts/search-skills.py "<topic>"
   ```
3. **Load and Follow Runbook:** Inspect the matched `SKILL.md` using `read_file` and execute the task following its strict anti-slop guidelines and verification steps.
4. **Adopt Persona if Applicable:** If the task requires specialized architecture, review, or debugging, adopt the matching agent persona from `agents/*.md`.
