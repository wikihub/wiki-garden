# Architecture Update Tasks

## Refinement Phase (Structured Hierarchy)

### Robotics Domain
- [x] Clean up `pages/Robotics/Robotics.md`
    - [x] Remove inline `(See also: ...)` links
    - [x] Ensure strict adherence to `categories_structure.md`
    - [x] Move essential cross-references to "Related Domains" section (if not already there)

### Automotive Systems Domain
- [x] Clean up `pages/AutomotiveSystems/Automotive Systems.md`
    - [x] Remove inline `(See also: ...)` links
    - [x] Ensure strict adherence to `categories_structure.md`

### Hardware Domain
- [x] Clean up `pages/Hardware/Hardware.md`
    - [x] Remove inline `(See also: ...)` links
    - [x] Ensure strict adherence to `categories_structure.md`

### Systems Engineering Domain
- [x] Clean up `pages/Systems Engineering/Systems Engineering.md`
    - [x] Structure according to `categories_structure.md`
    - [x] Remove inline `(See also: ...)` links

### Learning Domain
- [x] Clean up `pages/Learning/Learning.md`
    - [x] Structure according to `categories_structure.md`
    - [x] Remove inline `(See also: ...)` links

### Small Business Domain
- [x] Clean up `pages/SmallBusiness/Small Business.md`
    - [x] Structure according to `categories_structure.md`
    - [x] Remove inline `(See also: ...)` links

### Verification
- [x] Verify Clean Structure
    - [x] Ensure no "entangled" inline links remain
    - [x] Verify clear parent-child navigation

## Restructuring Phase (Folder Organization)

### Software Domain
- [x] Create `pages/Software/Applications` folder
- [x] Move loose files to sub-folders:
    - [x] `JavaScript.md` -> `Programming/`
    - [x] `Linux.md`, `ssh.md`, `Packages.md` -> `DevOps/`
    - [x] `Enterprise.md` -> `Cloud/`
    - [x] `Robotic Process Automation.md` -> `Applications/`
- [x] Move `Freelancing.md` to `pages/Learning/`

### Robotics Domain
- [x] Move `Intel Robotics.md` to `Platforms/` (or appropriate location)
- [x] Ensure `Safety.md` is correctly placed

### Hardware Domain
- [x] Ensure `Makers.md` and `Rapid Prototyping.md` are in `Development & Prototyping` section (logical check)

### Verification
- [x] Verify file paths and links

## Cleanup Phase (Structure Consistency)
- [x] Fix `Robotics/Platforms` structure
    - [x] Move `pages/Robotics/Platforms.md` to `pages/Robotics/Platforms/Platforms.md`
- [x] Fix `Software/Applications` structure
    - [x] Rename `Software Applications.md` to `Applications.md` (if applicable)
- [x] Verify `AutomotiveSystems/AutonomousVehicles` structure
    - [x] Ensure index page exists

## Final Consistency Checks
- [x] Update `categories_structure.md`
    - [x] Add `[[NVIDIA Robotics]]` to Robotics domain
    - [x] Add `[[Freelancing]]` to Learning domain
- [x] Fix `Robotics` file placement
    - [x] Move `Intel Robotics.md` back to `pages/Robotics/` (it is a category, not a child of Platforms)
