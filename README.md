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
