import os
import sys

def update_parent(directory, parent_name):
    print(f"Processing {directory} with parent {parent_name}")
    for filename in os.listdir(directory):
        if not filename.endswith(".md"):
            continue
        
        filepath = os.path.join(directory, filename)
        
        # Skip if it's the category file itself (e.g. Programming.md in Programming folder)
        # But usually Category.md is in the parent folder or inside.
        # If it's inside, it should have parent of the *parent* category.
        # e.g. pages/Software/Programming/Programming.md has parent [[Software]].
        # But pages/Software/Programming/Python.md has parent [[Programming]].
        # So I should skip the file that matches the current folder name if I'm setting children's parent.
        
        if filename == f"{os.path.basename(directory)}.md":
            print(f"Skipping category file: {filename}")
            continue

        with open(filepath, "r") as f:
            content = f.read()
        
        if "**Parent:**" in content:
            print(f"Skipping {filename}, already has Parent.")
            continue
            
        # Insert Parent link
        # Find end of frontmatter
        if content.startswith("---"):
            second_dash = content.find("---", 3)
            if second_dash != -1:
                insert_pos = second_dash + 3
                new_content = content[:insert_pos] + f"\n\n**Parent:** [[{parent_name}]]" + content[insert_pos:]
            else:
                # No second dash? Append to top
                new_content = f"**Parent:** [[{parent_name}]]\n\n" + content
        else:
            new_content = f"**Parent:** [[{parent_name}]]\n\n" + content
            
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python update_wiki.py <directory> <parent_name>")
        sys.exit(1)
    
    update_parent(sys.argv[1], sys.argv[2])
