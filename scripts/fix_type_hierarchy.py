#!/usr/bin/env python3
"""
Fix type fields in markdown files to match immediate parent folder.
This simplifies the hierarchy: Child → Parent → Grandparent instead of Child → Grandparent.

Special handling for index pages:
- Regular pages: type references parent folder (e.g., JavaScript.md → type: [[Programming]])
- Index pages: type references grandparent (e.g., Programming/Programming.md → type: [[Software]])
"""

import os
import re
from pathlib import Path

def fix_type_fields():
    fixed_count = 0
    errors = []

    for md_file in Path("pages").rglob("*.md"):
        parts = md_file.parts
        if len(parts) >= 3:  # e.g., pages/Software/Programming/JavaScript.md
            filename_base = md_file.stem  # e.g., "Programming" or "JavaScript"
            parent_folder = parts[-2]  # e.g., "Programming"

            # Determine correct type based on whether this is an index page
            is_index_page = (filename_base == parent_folder)

            if is_index_page and len(parts) >= 4:
                # Index page should reference grandparent
                correct_type = parts[-3]  # e.g., "Software"
            else:
                # Regular page should reference parent
                correct_type = parent_folder

            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find current type field
                type_match = re.search(r'^type:\s*\[\[(.+?)\]\]', content, re.MULTILINE)
                if type_match:
                    current_type = type_match.group(1)
                    if current_type != correct_type:
                        # Replace type field
                        new_content = re.sub(
                            r'^type:\s*\[\[.+?\]\]',
                            f'type: [[{correct_type}]]',
                            content,
                            count=1,
                            flags=re.MULTILINE
                        )

                        # Write back
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)

                        fixed_count += 1
                        page_type = "INDEX" if is_index_page else "page"
                        print(f"✓ {md_file} ({page_type})")
                        print(f"  [[{current_type}]] → [[{correct_type}]]")

            except Exception as e:
                errors.append((str(md_file), str(e)))

    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} files")

    if errors:
        print(f"\nErrors encountered ({len(errors)}):")
        for file, error in errors:
            print(f"  {file}: {error}")

    return fixed_count, errors

if __name__ == "__main__":
    fixed, errors = fix_type_fields()
    exit(0 if not errors else 1)
