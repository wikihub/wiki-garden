# Wiki Structure Update Plan

## Overview

This plan outlines the systematic approach to update all folders under `/pages` and their subfolders with proper linking structure and improved organization, following the pattern established for the Software page.

## Background

The Software page was recently updated with:
1. **Hierarchical linking** - All immediate subfolders linked using wiki-style `[[Folder Name]]` syntax
2. **Improved structure** - Organized into logical categories with clear sections
3. **Comprehensive coverage** - All standalone markdown files and subfolders properly linked
4. **Better navigation** - Overview section, categorized topics, and technology stacks

This same approach should be applied to all other top-level folders in the wiki.

## Directory Structure Analysis

### Top-Level Folders (17 total)

Based on directory analysis, the following folders exist under `/pages`:

1. **Academia** - 1 child
2. **Agritech** - 1 child
3. **AutomotiveSystems** - 29 children (includes AutonomousVehicles subfolder with 25 children)
4. **Building** - 1 child
5. **Camping** - 1 child
6. **Fintech** - 1 child
7. **Hardware** - 13 children (no subfolders)
8. **Learning** - 11 children
9. **NGO** - 1 child
10. **ProductManagement** - 1 child
11. **ProjectManagement** - 1 child
12. **Robotics** - 32 children (includes ROS, ROS2, Vision subfolders)
13. **Skills** - 1 child
14. **SmallBusiness** - 5 children
15. **Software** - 79 children (includes 11 subfolders) ✅ **COMPLETED**
16. **SystemsEngineering** - 8 children
17. **eMobility** - 1 child

### Identified Subfolders (Depth 2+)

- `AutomotiveSystems/AutonomousVehicles/` (25 children)
- `Robotics/ROS/` (4 children)
- `Robotics/ROS2/` (4 children)
- `Robotics/Vision/` (1 child)
- `Software/Applications/`
- `Software/Blockchain/`
- `Software/Cloud/`
- `Software/Data/`
- `Software/DevOps/`
- `Software/Development/`
- `Software/Games/`
- `Software/Machine Learning/`
- `Software/Programming/`
- `Software/Web Development/` (includes Front-End subfolder)
- `Software/Web Development/Front-End/`
- `Software/WordProcessing/`

## Proposed Changes

### Phase 1: High-Complexity Folders (Priority)

These folders have multiple subfolders and/or many children requiring significant restructuring:

#### 1. Robotics (32 children, 3 subfolders)
- **Main page:** `Robotics/Robotics.md`
- **Subfolders to link:**
  - ROS
  - ROS2
  - Vision
- **Standalone files to review and link:** 23 markdown files including:
  - BLDC Motors, Behavior, Delivery Robots, Fleet Management, GPS, etc.
- **Current state:** Has content but lacks structured subfolder links
- **Action:** Create categorized structure (e.g., "Core Topics", "Hardware", "Software", "Applications")

#### 2. AutomotiveSystems (29 children, 1 subfolder)
- **Main page:** `AutomotiveSystems/Automotive Systems.md`
- **Subfolders to link:**
  - AutonomousVehicles (needs its own restructuring - 25 children)
- **Standalone files:** Electric Vehicles, Engine Control, Vehicle Dynamics
- **Action:** Create structure similar to Software page with categories

#### 3. Hardware (13 children, no subfolders)
- **Main page:** `Hardware/Hardware.md`
- **Current state:** Simple shopping list format
- **Standalone files:** Actuators, Batteries, CAN, Cameras, Embedded Systems, IoT, Network, STM32, Sensors, etc.
- **Action:** Add "Topics" section with links to all standalone files, organize by category

#### 4. Learning (11 children)
- **Action:** Review and structure with proper links

#### 5. SystemsEngineering (8 children)
- **Action:** Review and structure with proper links

#### 6. SmallBusiness (5 children)
- **Action:** Review and structure with proper links

### Phase 2: Medium-Complexity Folders

Folders with fewer children but still requiring attention:

- **Fintech** (1 child)
- **NGO** (1 child)
- **ProductManagement** (1 child)
- **ProjectManagement** (1 child)
- **Skills** (1 child)
- **Academia** (1 child)
- **Agritech** (1 child)
- **Building** (1 child)
- **Camping** (1 child)
- **eMobility** (1 child)

### Phase 3: Subfolder Updates

Update subfolder main pages to link back to parent and to their children:

#### Software Subfolders (Already have links from parent)
- `Software/Applications/` - Add main page with structure
- `Software/Blockchain/` - Add main page with structure
- `Software/Cloud/` - Add main page with structure
- `Software/Data/` - Add main page with structure
- `Software/DevOps/` - Add main page with structure
- `Software/Development/` - Add main page with structure
- `Software/Games/` - Add main page with structure
- `Software/Machine Learning/` - Add main page with structure
- `Software/Programming/` - Add main page with structure
- `Software/Web Development/` - Add main page with structure (includes Front-End subfolder)
- `Software/WordProcessing/` - ✅ Already has proper structure

#### Robotics Subfolders
- `Robotics/ROS/` - Add/update main page
- `Robotics/ROS2/` - Add/update main page
- `Robotics/Vision/` - Add/update main page

#### AutomotiveSystems Subfolders
- `AutomotiveSystems/AutonomousVehicles/` - Add/update main page (25 children!)

## Standardized Structure Template

Each main folder page should follow this structure:

```markdown
---
title: "[Folder Name]"
linkTitle: "[Folder Name]"
weight: [number]
description: [Brief description]
type: [[Folder Name]]
---

## Overview

[Brief introduction to the topic area]

## Core Topics

### [Category 1]
- [[Subfolder 1]]
- [[Subfolder 2]]
- [[Related Page 1]]
- [[Related Page 2]]

### [Category 2]
- [[Subfolder 3]]
- [[Related Page 3]]

## [Additional Sections as Needed]

[Technology stacks, resources, platform-specific info, etc.]
```

## Linking Patterns

### Parent to Child Links
- Use wiki-style links: `[[Folder Name]]` or `[[Page Name]]`
- Organize into logical categories
- List all immediate subfolders first, then standalone pages

### Child to Parent Links
- Add "Related Pages" section at top with: `**Parent:** [[Parent Folder]]`
- Add links to sibling pages/folders as relevant

### Subfolder Main Pages
- Must have a main page named after the folder (e.g., `Robotics/Robotics.md`)
- If missing, create one following the template

## Verification Plan

### Automated Checks
1. **Link validation:** Verify all wiki-style links resolve correctly
2. **File existence:** Ensure all referenced pages exist
3. **Consistency check:** Verify all subfolders have corresponding links in parent pages

### Manual Verification
1. **Navigation testing:** Click through links to ensure proper navigation flow
2. **Structure review:** Verify logical organization and categorization
3. **Completeness check:** Ensure no orphaned pages (pages not linked from anywhere)

## Implementation Approach

### Recommended Order

1. **Start with high-complexity folders** (Robotics, AutomotiveSystems, Hardware)
2. **Move to medium-complexity folders** (Learning, SystemsEngineering, SmallBusiness)
3. **Handle simple folders** (single-child folders)
4. **Update all subfolders** with proper parent/child linking
5. **Create missing main pages** for subfolders that lack them
6. **Final review and validation**

### Per-Folder Workflow

For each folder:
1. **Analyze current state** - List all children (subfolders and files)
2. **Review existing main page** - Understand current structure
3. **Design new structure** - Categorize topics logically
4. **Update main page** - Add links to all subfolders and relevant standalone files
5. **Update subfolder pages** - Add parent links and structure
6. **Verify navigation** - Test all links work correctly

## Estimated Effort

- **High-complexity folders:** 30-45 minutes each (6 folders = 3-4.5 hours)
- **Medium-complexity folders:** 10-15 minutes each (10 folders = 1.5-2.5 hours)
- **Subfolder updates:** 15-20 minutes each (~20 subfolders = 5-6.5 hours)
- **Verification and cleanup:** 1-2 hours

**Total estimated effort:** 10-15 hours

## Success Criteria

1. ✅ All top-level folders have properly structured main pages
2. ✅ All subfolders are linked from their parent pages
3. ✅ All subfolder main pages link back to their parents
4. ✅ All standalone markdown files are linked from appropriate parent pages
5. ✅ Logical categorization and organization throughout
6. ✅ No orphaned pages
7. ✅ Consistent structure across all folders
8. ✅ Easy navigation between related topics

## Notes

- The Software folder serves as the reference implementation
- Maintain consistency in structure while adapting to each folder's unique content
- Some folders may require custom sections beyond the standard template
- Consider creating a "Related Topics" section for cross-folder links where appropriate
