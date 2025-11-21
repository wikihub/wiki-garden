#!/usr/bin/env python3
"""
Clean up redundant metadata in markdown files:
1. Remove 'feature:' field (redundant with 'type:')
2. Remove '**Parent:**' markdown lines (redundant with 'type:')
"""

import re
from pathlib import Path

def cleanup_file(file_path):
    """Clean up a single markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Remove feature: field from frontmatter
    if re.search(r'^feature:', content, re.MULTILINE):
        content = re.sub(r'^feature:.*\n', '', content, flags=re.MULTILINE)
        changes.append("Removed 'feature:' field")

    # Remove **Parent:** line from markdown body
    if re.search(r'^\*\*Parent:\*\*.*\n', content, re.MULTILINE):
        content = re.sub(r'^\*\*Parent:\*\*.*\n', '', content, flags=re.MULTILINE)
        changes.append("Removed '**Parent:**' line")

    # Also remove empty lines that might be left after Parent removal
    # This handles cases where Parent line was followed by blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes

    return None

def main():
    feature_count = 0
    parent_count = 0
    files_modified = 0

    for md_file in Path("pages").rglob("*.md"):
        changes = cleanup_file(md_file)

        if changes:
            files_modified += 1
            print(f"✓ {md_file}")
            for change in changes:
                print(f"  - {change}")
                if "feature" in change.lower():
                    feature_count += 1
                if "parent" in change.lower():
                    parent_count += 1

    print(f"\n{'='*60}")
    print(f"Modified {files_modified} files")
    print(f"Removed {feature_count} 'feature:' fields")
    print(f"Removed {parent_count} '**Parent:**' lines")

if __name__ == "__main__":
    main()
