#!/usr/bin/env python3
"""
HyperCraft Watermark Remover & Upstream Brand Sanitizer
Scans and cleans third-party developer watermarks, upstream handles, and personal branding.
"""

import sys
import os
import re
import argparse
from typing import List, Dict, Tuple, Any

COMMON_UPSTREAM_AUTHORS = [
    r'addyosmani', r'mahipal', r'nutlope', r'cathrynlavery', r'blader',
    r'affaan[-_]?m', r'AnandChowdhary', r'enitrat', r'Xabilimon1', r'LEC-AI',
    r'shoyann', r'Keyur Patel', r'Ronald Skelton', r'RapportScore'
]

PROMOTIONAL_PATTERNS = [
    r'https?://(?:www\.)?(?:buymeacoffee|patreon|ko-fi)\.com/[^\s\)\"]*',
    r'https?://(?:www\.)?twitter\.com/[a-zA-Z0-9_]+',
    r'https?://(?:www\.)?x\.com/[a-zA-Z0-9_]+',
    r'credit:\s*@[a-zA-Z0-9_-]+',
    r'contributed by\s+[^\n.,]+',
    r'Created by\s+[^\n.,]+(?:\(credit:[^\)]+\))?'
]

def scrub_file(filepath: str, brand_name: str = "HyperCraft Core Team", repo_url: str = "", dry_run: bool = False) -> List[str]:
    if os.path.basename(filepath) in ["scrub.py", "scrub-watermarks.py"]:
        return []
        
    changes = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        return [f"Read error: {e}"]

    original = content

    # 1. Strip UTF-8 BOM
    if content.startswith("\ufeff"):
        content = content.lstrip("\ufeff")
        changes.append("Stripped UTF-8 BOM")

    # 2. Frontmatter author and origin normalization
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            # Replace origin if not containing HyperCraft
            for line in fm.splitlines():
                if line.strip().lower().startswith("origin:") and "hypercraft" not in line.lower():
                    fm = re.sub(r"^origin:\s*[^\n]+", f"origin: {brand_name} Distribution", fm, flags=re.MULTILINE)
                    changes.append("Normalized frontmatter origin")
                    break
            # Replace author if not containing HyperCraft
            for line in fm.splitlines():
                if line.strip().lower().startswith("author:") and "hypercraft" not in line.lower():
                    fm = re.sub(r"^author:\s*[^\n]+", f"author: {brand_name}", fm, flags=re.MULTILINE)
                    changes.append("Normalized frontmatter author")
                    break
            parts[1] = fm
            content = "---".join(parts)

    # 3. Clean specific upstream developer handles
    for author in COMMON_UPSTREAM_AUTHORS:
        if re.search(r"\b" + author + r"\b", content, re.IGNORECASE):
            content = re.sub(r"\b" + author + r"\b", brand_name, content, flags=re.IGNORECASE)
            changes.append(f"Scrubbed author reference: {author}")

    # 4. Clean promotional links
    for pat in PROMOTIONAL_PATTERNS:
        if re.search(pat, content, re.IGNORECASE):
            content = re.sub(pat, f"Authored by {brand_name}", content, flags=re.IGNORECASE)
            changes.append(f"Scrubbed promotional pattern: {pat[:30]}...")

    # 5. Clean suite references (e.g. ECC suite)
    if re.search(r"\bECC\b", content):
        content = re.sub(r"\bECC Tools\b", "HyperCraft Tools", content)
        content = re.sub(r"\bECC Conventions\b", "HyperCraft Conventions", content)
        content = re.sub(r"\bECC Memory Vault\b", "HyperCraft Memory Vault", content)
        content = re.sub(r"\bECC\b", "HyperCraft", content)
        changes.append("Normalized project suite codename")

    if content != original and not dry_run:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            return [f"Write error: {e}"]

    return changes

def run_scrubber(target_path: str, brand_name: str, repo_url: str, dry_run: bool):
    print(f"\n⚡ HyperCraft Watermark Remover")
    print(f"📁 Target: {target_path}")
    print(f"🏷️ Unified Brand: {brand_name}")
    print(f"⚙️ Mode: {'DRY RUN (Preview Only)' if dry_run else 'APPLY (Modifying Files)'}\n" + "=" * 60)

    total_files = 0
    modified_files = 0

    valid_exts = (".md", ".yml", ".yaml", ".json", ".txt", ".py", ".js", ".ts", ".mjs")

    if os.path.isfile(target_path):
        files_to_check = [target_path]
    else:
        files_to_check = []
        for root, dirs, files in os.walk(target_path):
            if ".git" in dirs:
                dirs.remove(".git")
            for f in files:
                if f.endswith(valid_exts):
                    files_to_check.append(os.path.join(root, f))

    for p in files_to_check:
        total_files += 1
        changes = scrub_file(p, brand_name=brand_name, repo_url=repo_url, dry_run=dry_run)
        if changes:
            modified_files += 1
            rel = os.path.relpath(p, target_path)
            print(f"[{'WOULD CLEAN' if dry_run else 'CLEANED'}] {rel}")
            for c in changes:
                print(f"   - {c}")

    print("=" * 60)
    print(f"Scanned {total_files} files. {'Found watermarks in' if dry_run else 'Successfully sanitized'} {modified_files} files.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HyperCraft Watermark Remover")
    parser.add_argument("target", help="Target file or directory to scrub")
    parser.add_argument("--brand", default="HyperCraft Core Team", help="Brand name to replace with (default: HyperCraft Core Team)")
    parser.add_argument("--repo-url", default="", help="Official repo URL to replace upstream repo links with")
    parser.add_argument("--dry-run", action="store_true", help="Preview matches without modifying files")

    args = parser.parse_args()
    run_scrubber(args.target, args.brand, args.repo_url, args.dry_run)
