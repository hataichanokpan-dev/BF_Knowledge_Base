# BF Knowledge Base

> A personal knowledge base and digital garden built with [Quartz](https://quartz.jzhao.xyz/)

![Quartz](https://img.shields.io/badge/Quartz-4.5.2-blue)
![Node](https://img.shields.io/badge/Node-%3E22-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

This is a static website generated from my Obsidian vault (`BF-Vault`), containing research notes, stock analyses, project documentation, and learning materials.

## Features

- **Wikilinks Support** - Full `[[wikilink]]` compatibility from Obsidian
- **Backlinks** - Automatic backlink generation for connected thinking
- **Graph View** - Visual representation of note connections
- **Full-text Search** - Fast client-side search across all content
- **Dark/Light Mode** - Automatic theme switching
- **Responsive Design** - Works on desktop and mobile

## Content Structure

```
content/
├── Companies/        # Company research and analysis
├── Concepts/         # Mental models and frameworks
├── Knowledge/        # Learning notes and courses
├── MOCs/             # Maps of Content (hub pages)
├── Processes/        # Workflows and procedures
├── Projects/         # Project documentation
├── Reviews/          # Stock reviews and analysis
├── Templates/        # Note templates
└── Watchlists/       # Investment watchlists
```

## Quick Start

### Prerequisites

- Node.js >= 22
- npm >= 10.9

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/bf-knowledge-base.git
cd bf-knowledge-base

# Install dependencies
npm install
```

### Development

```bash
# Build and start local server
npx quartz build --serve
```

Open http://localhost:8080 in your browser.

### Build for Production

```bash
# Generate static files
npx quartz build
```

Output will be in the `public/` directory.

## Deployment

### GitHub Pages

1. Push to GitHub repository
2. Go to Settings → Pages
3. Set Source to "GitHub Actions"
4. Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Quartz site to GitHub Pages

on:
  push:
    branches:
      - main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - run: npm ci
      - run: npx quartz build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: public

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

### Vercel / Netlify

Both platforms support automatic deployment from GitHub:

1. Connect your GitHub repository
2. Set build command: `npx quartz build`
3. Set output directory: `public`

## Configuration

Main configuration file: `quartz.config.ts`

Key settings:

| Setting | Description |
|---------|-------------|
| `pageTitle` | Site title displayed in browser |
| `baseUrl` | Your domain (for sitemap/RSS) |
| `ignorePatterns` | Folders to exclude from build |

## Customization

### Change Theme Colors

Edit `quartz.config.ts`:

```typescript
theme: {
  colors: {
    lightMode: {
      secondary: "#your-color",
      // ...
    },
  },
}
```

### Add Components

Quartz supports custom components. See [Quartz Documentation](https://quartz.jzhao.xyz/) for details.

## Tech Stack

- [Quartz](https://quartz.jzhao.xyz/) - Static site generator for Obsidian
- [TypeScript](https://www.typescriptlang.org/) - Configuration
- [Node.js](https://nodejs.org/) - Runtime

## License

MIT License - feel free to use this as a template for your own knowledge base.

## Acknowledgments

- [Quartz](https://quartz.jzhao.xyz/) by jackyzha0
- [Obsidian](https://obsidian.md/) - The best note-taking app

---

Made with Quartz
