# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm start        # Start dev server with live reload (webpack-dev-server)
npm run build    # Production build → dist/
```

No test runner is configured (`npm test` exits with an error).

## Architecture

This is a static personal website scaffolded from HTML5 Boilerplate v9.0.1, bundled with Webpack 5.

**Webpack config split:**
- `webpack.common.js` — shared: entry `js/app.js` → `dist/js/app.js`
- `webpack.config.dev.js` — merges common + dev server (live reload, HMR, serves from project root)
- `webpack.config.prod.js` — merges common + HtmlWebpackPlugin (injects bundle into `index.html`) + CopyPlugin (copies `img/`, `css/`, `js/vendor/`, icons, `robots.txt`, `404.html`, `site.webmanifest` into `dist/`)

**Key points:**
- CSS (`css/style.css`) is **not** processed by Webpack — it is copied as-is in production and referenced directly via `<link>` in `index.html`. To add CSS processing (PostCSS, Sass, etc.), a loader and webpack rule would need to be added.
- Third-party scripts go in `js/vendor/` and are copied verbatim to `dist/js/vendor/`.
- The dev server serves the project root (not `dist/`), so changes to `index.html` and `css/style.css` are reflected without a build step.
- Production output is always written to `dist/` (cleaned on each build).
