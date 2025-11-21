# knowledge-garden

My personal public notes managed with Logseq.

**Logseq Version**: 0.10.14

## Project Structure

This repository contains the source for my personal knowledge garden.

- **assets/**: Contains static assets like images and PDFs referenced in the notes.
- **journals/**: Daily notes and journal entries.
- **logseq/**: Logseq configuration files and metadata.
- **pages/**: The main content of the knowledge base, containing individual notes and pages.

## GitHub Actions

This project uses GitHub Actions for continuous integration and deployment.

- **CI (`.github/workflows/main.yml`)**: This workflow is triggered on pushes to the `main` branch. It uses the official `logseq/publish-spa` action (v0.3.0) with Logseq version 0.10.14 to build the static site and then deploys it to GitHub Pages (the `gh-pages` branch).
- **Test (`.github/workflows/test.yml`)**: This workflow allows for manual triggering (`workflow_dispatch`). It builds the site with the same action and version, then copies a custom CSS file, useful for testing build integrity and style changes.

## Usage

- **Adding Notes**: Notes are added by creating Markdown files in the `pages/` or `journals/` directories.
- **Deployment**: Changes pushed to the `main` branch are automatically built and deployed to [https://pengx17.github.io/knowledge-garden/#/all-journals](https://pengx17.github.io/knowledge-garden/#/all-journals).

## Development Tools

This repository uses [pixi](https://pixi.sh) for Python dependency management and task execution.

### Setup

Install pixi (if not already installed):
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Install project dependencies:
```bash
pixi install
```

### Available Tasks

- **Fix Hierarchy**: Validates and fixes the `type` field in all markdown files to ensure they reference their immediate parent folder:
  ```bash
  pixi run fix-hierarchy
  ```

- **Cleanup Metadata**: Removes redundant metadata fields (`feature:`, `**Parent:**` lines):
  ```bash
  pixi run cleanup-metadata
  ```

### Architecture Documentation

See the [specs/002-update-architecture/](specs/002-update-architecture/) directory for detailed architecture documentation:

- **[categories_structure.md](specs/002-update-architecture/categories_structure.md)**: Complete hierarchical structure of all 17 domains
- **[hierarchy_principle.md](specs/002-update-architecture/hierarchy_principle.md)**: Explains the "Immediate Parent Principle" for type fields
- **[cleanup_summary.md](specs/002-update-architecture/cleanup_summary.md)**: Summary of metadata cleanup (removed 65 `feature:` fields and 117 `**Parent:**` lines)
- **[structured_architecture.md](specs/002-update-architecture/structured_architecture.md)**: Core architectural principles and navigation rules
- **[tasks.md](specs/002-update-architecture/tasks.md)**: Implementation task tracking
