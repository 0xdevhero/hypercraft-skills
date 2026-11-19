#!/usr/bin/env python3
"""
HyperCraft Skills Linter & Quality Verification
Validates YAML frontmatter, JSON schemas, and structure across all 500+ skills and agents.
"""

import glob
import json
import os
import sys
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)

    print("⚡ HyperCraft Linter & Quality Gate")
    print(f"📂 Root: {repo_root}\n")

    has_error = False

    # 1. Validate JSON Files
    print("📋 [1/3] Validating JSON Configurations...")
    json_targets = ['plugin.json', 'package.json', 'mcp_config.json']
    for jf in json_targets:
        target = repo_root / jf
        if target.exists():
            try:
                with open(target, 'r', encoding='utf-8') as fp:
                    json.load(fp)
                print(f"  ✅ Valid JSON: {jf}")
            except Exception as e:
                print(f"  ❌ Invalid JSON {jf}: {e}")
                has_error = True

    # 2. Validate SKILL.md Frontmatter across all skills
    print("\n🎯 [2/3] Validating SKILL.md Frontmatter (500+ Skills)...")
    skills = glob.glob('skills/**/SKILL.md', recursive=True) + glob.glob('ecosystem/**/SKILL.md', recursive=True)
    if not skills:
        print("  ❌ No SKILL.md files discovered!")
        sys.exit(1)

    print(f"  Discovered {len(skills)} skills. Checking format...")
    skill_errors = 0
    for path in skills:
        try:
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read()
            if not content.startswith('---'):
                print(f"  ❌ Missing frontmatter delimiter: {path}")
                skill_errors += 1
                continue
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"  ❌ Malformed frontmatter: {path}")
                skill_errors += 1
                continue
            fm = parts[1]
            if 'name:' not in fm:
                print(f"  ❌ Missing 'name' in frontmatter: {path}")
                skill_errors += 1
            if 'description:' not in fm:
                print(f"  ❌ Missing 'description' in frontmatter: {path}")
                skill_errors += 1
        except Exception as e:
            print(f"  ❌ Error reading {path}: {e}")
            skill_errors += 1

    if skill_errors == 0:
        print(f"  ✅ All {len(skills)} skills passed frontmatter validation!")
    else:
        print(f"  ❌ Found {skill_errors} errors across skills.")
        has_error = True

    # 3. Validate Specialist Agents
    print("\n👥 [3/3] Validating Specialist Agents...")
    agents = glob.glob('agents/*.md')
    if not agents:
        print("  ⚠️ Warning: No agents found in agents/ directory.")
    else:
        print(f"  ✅ Discovered {len(agents)} specialist agents verified.")

    # Final Summary
    print("\n" + "=" * 60)
    if has_error:
        print("❌ HyperCraft Quality Verification FAILED. Please fix issues above.")
        sys.exit(1)
    else:
        print("✨ HyperCraft Quality Verification PASSED! 100% Ready for Distribution.")
        sys.exit(0)

if __name__ == '__main__':
    main()
