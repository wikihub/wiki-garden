# Hierarchy Principle for Type Fields

**Date:** 2025-11-20
**Status:** Implemented

## Overview

This document defines the **Immediate Parent Principle** for the `type` field in all wiki pages. This principle simplifies the knowledge network by ensuring each page points only to its immediate parent, creating a clear hierarchical chain.

## The Principle

> **Every page's `type` field MUST reference its immediate parent folder, not the top-level domain.**

### Two Types of Pages

#### 1. Regular Pages
Files where the filename differs from the parent folder.

**Example:** `pages/Software/Programming/JavaScript.md`

**Hierarchical Chain:**
```
JavaScript → Programming → Software
```

**Correct `type` field:**
```yaml
type: [[Programming]]  # ✓ References parent folder
```

**Incorrect:**
```yaml
type: [[Software]]  # ❌ Skips the immediate parent
```

#### 2. Index Pages
Files where the filename matches the parent folder (category index pages).

**Example:** `pages/Software/Programming/Programming.md`

**Hierarchical Chain:**
```
Programming → Software
```

**Correct `type` field:**
```yaml
type: [[Software]]  # ✓ References grandparent (parent of folder)
```

**Incorrect:**
```yaml
type: [[Programming]]  # ❌ Self-reference
```

### Rule Summary

| Page Type | File Path | `type` Field |
|-----------|-----------|--------------|
| Regular | `Programming/JavaScript.md` | `[[Programming]]` |
| Index | `Programming/Programming.md` | `[[Software]]` |

## Rationale

### Before: Ambiguous Network
When pages referenced top-level domains, the hierarchy was unclear:
- JavaScript → Software
- Python → Software
- React → Software

This created a flat network where the relationship between Programming languages and the Programming category was lost.

### After: Clear Hierarchy
With the immediate parent principle:
- JavaScript → Programming → Software
- Python → Programming → Software
- React → Front-End → WebDevelopment → Software

This creates a clear, navigable tree structure where:
1. Each page has exactly one primary parent
2. The folder structure matches the logical hierarchy
3. Navigation paths are predictable and unambiguous

## Implementation Status

**Phase 1:** 116 regular page files updated (2025-11-20)
**Phase 2:** 12 index page files updated (2025-11-20)
**Total:** 128 files fixed

### Domains Affected:
1. **Software** (67 regular + 8 index = 75 files)
   - Regular pages: Programming/* → `[[Programming]]`
   - Index pages: Programming/Programming.md → `[[Software]]`
   - Other categories: Cloud, DevOps, Development, WebDevelopment, MachineLearning, etc.

2. **Robotics** (6 regular + 4 index = 10 files)
   - Regular pages: ROS/* → `[[ROS]]`
   - Index pages: ROS/ROS.md → `[[Robotics]]`
   - Other categories: ROS2, Vision, Platforms

3. **Automotive Systems** (27 files)
   - AutonomousVehicles/* → `[[AutonomousVehicles]]`

4. **Systems Engineering** (8 files)
   - All files → `[[SystemsEngineering]]`

5. **Small Business** (5 files)
   - All files → `[[SmallBusiness]]`

6. **Learning** (1 file)
   - Freelancing.md → `[[Learning]]`

## Navigation Pattern

### Three-Level Example
```
Software/Programming/JavaScript.md
├── type: [[Programming]]
│   └── type: [[Software]]
│       └── (top-level domain)
```

### Four-Level Example
```
Software/WebDevelopment/Front-End/React.md
├── type: [[Front-End]]
│   └── type: [[Web Development]]
│       └── type: [[Software]]
│           └── (top-level domain)
```

## Benefits

1. **Simplified Network Complexity**
   - Reduces cross-references
   - Eliminates ambiguous parent relationships
   - Each page has exactly one `type` parent

2. **Predictable Navigation**
   - Users can follow the breadcrumb trail
   - Folder structure mirrors logical structure
   - Easy to understand where content belongs

3. **Maintainability**
   - Clear rules for where new content goes
   - No decisions about which parent to reference
   - Automated validation possible

## Validation

To verify all files follow this principle:

```python
# See fix_type_hierarchy.py in repository root
python3 fix_type_hierarchy.py
```

## Related Documents

- [categories_structure.md](./categories_structure.md) - Complete domain structure
- [structured_architecture.md](./structured_architecture.md) - Core architectural principles
