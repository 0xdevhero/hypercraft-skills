#!/usr/bin/env python3
"""
HyperCraft Skill Intelligence Search Engine
Fast, zero-dependency on-disk skill retrieval for AI agents and developers.
"""

import sys
import os
import re
import argparse
from typing import List, Dict, Any

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

def parse_skill_file(filepath: str) -> Dict[str, Any]:
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return {}

    name = os.path.basename(os.path.dirname(filepath))
    description = ""
    category = "general"

    rel_path = os.path.relpath(filepath, SKILLS_DIR)
    parts = rel_path.split(os.sep)
    if len(parts) >= 3 and parts[0] == "ecosystem":
        category = parts[1]
    elif len(parts) >= 2 and parts[0] == "core":
        category = "core"

    if content.startswith("---"):
        sections = content.split("---", 2)
        if len(sections) >= 3:
            fm = sections[1]
            name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
            if name_match:
                name = name_match.group(1).strip().strip("\"'")
            desc_match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
            if desc_match:
                description = desc_match.group(1).strip().strip("\"'")

    return {
        "name": name,
        "description": description,
        "category": category,
        "path": filepath,
        "rel_path": rel_path,
        "content": content
    }

def score_skill(skill: Dict[str, Any], query_terms: List[str]) -> float:
    score = 0.0
    name_lower = skill["name"].lower()
    desc_lower = skill["description"].lower()
    cat_lower = skill["category"].lower()
    content_lower = skill["content"][:2000].lower()

    for term in query_terms:
        term_clean = term.lower().strip()
        if not term_clean:
            continue
        if term_clean == name_lower:
            score += 100.0
        elif term_clean in name_lower:
            score += 40.0
        if term_clean in cat_lower:
            score += 25.0
        if term_clean in desc_lower:
            score += 20.0
        matches_in_body = len(re.findall(re.escape(term_clean), content_lower))
        score += min(matches_in_body * 3.0, 30.0)

    # Core master skills get a small boost for general queries
    if skill["category"] == "core":
        score += 5.0

    return score

def extract_excerpt(content: str, query_terms: List[str], max_lines: int = 12) -> str:
    lines = content.splitlines()
    # Skip frontmatter
    start_idx = 0
    if len(lines) > 0 and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                start_idx = idx + 1
                break

    body_lines = lines[start_idx:]
    # Find line with highest term match
    best_idx = 0
    best_count = -1
    for i, line in enumerate(body_lines):
        c = sum(1 for t in query_terms if t.lower() in line.lower())
        if c > best_count:
            best_count = c
            best_idx = i

    selected = body_lines[max(0, best_idx - 2): min(len(body_lines), best_idx + max_lines)]
    return "\n".join(selected).strip()

def search_skills(query: str, category_filter: str = None, top_k: int = 3):
    query_terms = [t.strip() for t in query.split() if t.strip()]
    if not query_terms:
        print("Please provide a search query.")
        return

    skills = []
    for root, _, files in os.walk(SKILLS_DIR):
        if "SKILL.md" in files:
            path = os.path.join(root, "SKILL.md")
            skill_info = parse_skill_file(path)
            if skill_info:
                if category_filter and skill_info["category"].lower() != category_filter.lower():
                    continue
                score = score_skill(skill_info, query_terms)
                if score > 0:
                    skills.append((score, skill_info))

    skills.sort(key=lambda x: x[0], reverse=True)
    results = skills[:top_k]

    print(f"\n⚡ HyperCraft Skill Search | Query: \"{query}\"")
    if category_filter:
        print(f"📁 Filtered by Category: [{category_filter}]")
    print(f"🔍 Found {len(skills)} matches (showing top {len(results)}):\n" + "=" * 60)

    if not results:
        print("No matching skills discovered. Try broader keywords.")
        return

    for rank, (score, skill) in enumerate(results, 1):
        print(f"\n### [{rank}] {skill['name']}  (Score: {score:.1f} | Category: {skill['category']})")
        print(f"📖 Description: {skill['description']}")
        print(f"📍 Location: skills/{skill['rel_path']}")
        print("\n--- Relevant Excerpt ---")
        excerpt = extract_excerpt(skill["content"], query_terms)
        print(excerpt)
        print("-" * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HyperCraft Skill Intelligence Search")
    parser.add_argument("query", help="Keywords to search for (e.g. 'quant rsi', 'flutter router')")
    parser.add_argument("--category", "-c", help="Optional category filter (e.g. 'trading', 'languages', 'frameworks')")
    parser.add_argument("--limit", "-n", type=int, default=3, help="Number of results to return (default: 3)")

    args = parser.parse_args()
    search_skills(args.query, category_filter=args.category, top_k=args.limit)
