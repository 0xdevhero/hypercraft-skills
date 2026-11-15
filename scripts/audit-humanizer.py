#!/usr/bin/env python3
"""
HyperCraft Humanizer Audit Tool
Checks prose files for AI writing patterns, stock tells, and stylistic artifacts.
Based on the Humanizer engine in skills/ecosystem/tools-workflow/humanizer/SKILL.md
"""

import sys
import os
import re
from typing import List, Dict, Any

AI_STOCK_WORDS = [
    "seamlessly", "harness", "unleash", "cutting-edge", "revolutionize",
    "elevate", "groundbreaking", "pivotal", "game-changer", "dive into",
    "delve", "testament", "tapestry", "beacon", "multifaceted", "paramount",
    "foster", "spearhead", "robust", "plethora", "myriad", "cornerstone",
    "quintessential", "underpin", "holistic", "burgeoning", "synergy"
]

CHAT_WRAPPERS = [
    r"^certainly", r"^sure thing", r"^in conclusion", r"^to summarize",
    r"^in today'?s fast-paced", r"^it is worth noting", r"^first and foremost",
    r"^without further ado", r"^as an ai", r"^here is the"
]

def audit_text(text: str, filename: str = "") -> Dict[str, Any]:
    lines = text.splitlines()
    total_words = len(re.findall(r"\b\w+\b", text))
    
    # 1. Stock AI Words
    found_buzzwords = []
    for word in AI_STOCK_WORDS:
        matches = len(re.findall(r"\b" + word + r"\b", text, re.IGNORECASE))
        if matches > 0:
            found_buzzwords.append((word, matches))
            
    # 2. Em-Dashes (AI loves excessive em-dashes)
    em_dashes = len(re.findall(r"—", text))
    
    # 3. Chat wrappers / Staged Openers
    found_wrappers = []
    for pattern in CHAT_WRAPPERS:
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line.strip(), re.IGNORECASE):
                found_wrappers.append((i, line.strip()[:60]))
                
    # 4. Not-X-but-Y Contrasts
    contrasts = re.findall(r"not\s+[^,.]+,\s*but\s+[^.]+", text, re.IGNORECASE)
    
    # Human score calculation (100 = perfectly natural human prose)
    penalty = (len(found_buzzwords) * 10) + (max(0, em_dashes - 5) * 2) + (len(found_wrappers) * 15) + (len(contrasts) * 5)
    human_score = max(0, 100 - penalty)
    
    return {
        "filename": filename,
        "total_words": total_words,
        "buzzwords": found_buzzwords,
        "em_dashes": em_dashes,
        "wrappers": found_wrappers,
        "contrasts": len(contrasts),
        "score": human_score
    }

def print_report(res: Dict[str, Any]):
    print(f"\n📄 File: {res['filename']} ({res['total_words']} words)")
    print(f"📊 Humanizer Score: {res['score']}/100 " + ("✅ [Natural Human Prose]" if res['score'] >= 85 else "⚠️ [Needs Humanizing]"))
    
    if res['buzzwords']:
        print("  ❌ Stock AI Words:")
        for w, count in res['buzzwords']:
            print(f"     - '{w}': {count} occurrences")
    else:
        print("  ✅ Stock AI Words: None (Zero buzzwords detected)")
        
    print(f"  {'⚠️' if res['em_dashes'] > 5 else '✅'} Em-dashes count: {res['em_dashes']}")
    
    if res['wrappers']:
        print("  ❌ Chat Wrappers / Staged Openers:")
        for line_no, snip in res['wrappers']:
            print(f"     - Line {line_no}: \"{snip}\"")
    else:
        print("  ✅ Chat Wrappers: None")
        
    print(f"  ✅ Not-X-but-Y Contrasts: {res['contrasts']}")
    print("-" * 60)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isfile(target):
            with open(target, "r", encoding="utf-8", errors="ignore") as f:
                res = audit_text(f.read(), os.path.basename(target))
                print_report(res)
        elif os.path.isdir(target):
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith((".md", ".txt")):
                        p = os.path.join(root, file)
                        with open(p, "r", encoding="utf-8", errors="ignore") as f:
                            res = audit_text(f.read(), os.path.relpath(p, target))
                            if res['score'] < 90:
                                print_report(res)
    else:
        # Default audit on key repo docs
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        for doc in ["README.md", "CONTRIBUTING.md", "SECURITY.md"]:
            p = os.path.join(repo_root, doc)
            if os.path.exists(p):
                with open(p, "r", encoding="utf-8", errors="ignore") as f:
                    res = audit_text(f.read(), doc)
                    print_report(res)
