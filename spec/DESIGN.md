# DESIGN

Personal portfolio website for Peter Mark, a Senior Software Engineer based in Seattle, WA.
All content is drawn from `spec/Peter_Mark_Resume.md`. The reference site is https://www.nathanstanley.dev/.

---

## Code Standards

- **Secrets — CRITICAL:** Never commit API keys, tokens, passwords, credentials, or `.env` files to the repository under any circumstances. This applies to every file, every commit, every iteration. No exceptions.
- **Security:** All external links use `rel="noopener noreferrer"`. No inline event handlers (`onclick`, etc.) — all event listeners attached in JS. No `innerHTML` with dynamic content — use `textContent` or DOM methods. Content Security Policy meta tag included in `index.html`.
- **CSS:** BEM naming convention for all classes. No `!important`. Custom properties for all design tokens (colors, spacing, typography).
- **JS:** Strict mode (`'use strict'`). No global variables — wrap in an IIFE or use ES modules. Prefer `const`/`let`, no `var`.
- **HTML:** Semantic elements throughout (`<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`). All images have descriptive `alt` attributes. ARIA labels on icon-only buttons.

---

## Architecture

- **Single-page application** — all sections live on `index.html`, linked via smooth-scroll anchor navigation.
- **No framework** — plain HTML, CSS, and vanilla JS. Webpack bundles `js/app.js`; CSS lives in `css/style.css` and is copied as-is to `dist/`.
- **No skills section** — expertise is implied through experience bullets and project descriptions.
- **Hosting:** GitHub Pages at custom domain `petermark.dev`. A `CNAME` file containing `petermark.dev` must be included in `dist/` (add to CopyPlugin patterns in `webpack.config.prod.js`).
- **Deployment:** GitHub Actions workflow on push to `main` — runs `npm run build` and deploys `dist/` to GitHub Pages using `actions/upload-pages-artifact` and `actions/deploy-pages`. Workflow file: `.github/workflows/deploy.yml`.

---

## Theme

- **Default:** follows OS system preference (`prefers-color-scheme`).
- **Toggle:** a sun/moon icon in the navbar lets the user override. Preference is persisted in `localStorage`.
- **Accent color:** purple (`#7C3AED` as base; lighter tint `#A78BFA` for hover/highlights on dark backgrounds).
- **Dark palette:**
  - Background: `#0f0f0f`
  - Surface (cards, navbar): `#1a1a1a`
  - Primary text: `#e5e5e5`
  - Muted text: `#888888`
  - Accent: `#A78BFA`
  - Border/divider: `#2a2a2a`
- **Light palette:**
  - Background: `#fafafa`
  - Surface: `#ffffff`
  - Primary text: `#111111`
  - Muted text: `#555555`
  - Accent: `#7C3AED`
  - Border/divider: `#e5e5e5`
- Implement via CSS custom properties on `:root` with a `[data-theme="light"]` override. JS toggles the attribute on `<html>`.

---

## Typography

- **Font:** `Inter` from Google Fonts (weights: 400, 500, 600, 700).
- Base size: `16px`, line-height `1.6`.
- Section headings: `1.75rem`, weight `600`, letter-spacing slightly tight (`-0.02em`).
- Name in hero: `3rem+`, weight `700`.

---

## Layout & Spacing

- Max content width: `860px`, centered with `auto` margins.
- Section vertical padding: `80px` top/bottom.
- Consistent horizontal page padding: `24px` on mobile, `48px` on desktop.

---

## Navigation

- **Fixed top navbar**, full-width, `background` matches surface color + `backdrop-filter: blur(8px)` for glassmorphism effect.
- Left: name "Peter Mark" as a logo/wordmark (plain text, accent color, links to `#hero`).
- Right: anchor links — `Experience`, `Projects` — plus a theme toggle icon button.
- On scroll, navbar gets a subtle bottom border to separate from content.
- Active section highlighted in navbar via scroll spy (IntersectionObserver).

---

## Sections

### Hero (`#hero`)

- Full-viewport-height (`100vh`) centered layout.
- Content (vertically centered):
  - Small label above name: `"Hi, I'm"` in muted text.
  - Name: `Peter Mark` — large, bold, accent-colored.
  - Title: `Senior Software Engineer` — medium weight, muted.
  - Tagline (from resume summary, condensed): `"7+ years building scalable distributed systems. Java · AWS · Microservices."`
  - CTA buttons: `View My Work` (scrolls to `#projects`, filled accent) and `Get In Touch` (scrolls to footer, outlined).
- Social icon links row below CTA: GitHub (`https://github.com/ptemark`), LinkedIn (`https://linkedin.com/in/peter-mark-55641094`), Email (`peter.sw.mark@gmail.com`).
- **Photo:** `spec/peter.jpg` — summit shot with arms raised, Cape Town coastline backdrop. File at `img/peter.jpg`. Rotation corrected. Display as a circular or rounded avatar alongside the hero text.

### Experience (`#experience`)

- Section heading: `Experience`.
- **Summary blurb:** a short paragraph directly below the section heading, before the timeline. Text sourced from the resume summary: *"Senior Software Engineer with 7+ years of experience designing and building scalable, reliable distributed systems. Expert in Java, Python, and AWS, with deep experience in microservices, cloud infrastructure, and system optimization. Proven ability to lead design discussions, mentor peers, and deliver impactful, high-performance software solutions."* Style as muted text, `0.9375rem`, `margin-bottom: 2rem`, same line-height as body.
- Vertical timeline list. Each entry:
  - **Company** + **role** (bold), date range (muted, right-aligned on desktop).
  - Bullet points from resume.
  - Thin left accent border in purple to indicate timeline.
- Entries (chronological, newest first):
  1. **Senior Software Engineer — FIS** | June 2025 – July 2025
  2. **Software Engineer II — Amazon** | July 2022 – April 2025
  3. **Software Engineer I — Amazon** | August 2020 – July 2022
  4. **Software Engineer — Ciena** | September 2017 – June 2020

### Projects (`#projects`)

- Section heading: `Projects`.
- This section is a focused showcase of this website itself and the RALPH loop methodology used to build it. It is not a generic project card grid — it is a feature/case study layout.

**Layout (two columns on desktop, stacked on mobile):**
- **Left column:** written content — project name, description, tech tags, links
- **Right column:** the RALPH loop flowchart diagram

**Written content (left):**
- Project name: `petermark.dev` as an `<h3>`
- Short description: "This site was built entirely using RALPH — a spec-driven autonomous development loop where an AI agent works through a prioritised task list, one iteration at a time, committing verified code at each step."
- Second paragraph: "Each section of the site, from the navigation to the print styles, was implemented by RALPH reading the design spec, picking the next task, building it, verifying the build, and pushing — without manual intervention."
- Tech tags: `HTML`, `CSS`, `JavaScript`, `Webpack`, `GitHub Actions`
- **Links row** (prominent, not just icon-only):
  - Primary button (filled accent): `View Source on GitHub` → `https://github.com/ptemark/PersonalWebsite` (opens in new tab, `rel="noopener noreferrer"`)
  - Secondary text link: `Learn about the RALPH loop` → `https://ghuntley.com/ralph/` (opens in new tab, `rel="noopener noreferrer"`)
- Attribution line below links: `RALPH loop concept by Geoffrey Huntley` — linked to `https://ghuntley.com/ralph/`

**Flowchart diagram (right):**
- Render as an **inline SVG** — no external library, no Mermaid.js dependency. Hand-crafted SVG based on the flowchart in `spec/The Ralph Loop`.
- Nodes and flow match the original diagram logic:
  1. Design Task / Goal
  2. Initialize Loop
  3. Fresh Context
  4. Read State
  5. Do Work
  6. Check Exit Criteria (decision diamond)
     - No → back to Fresh Context
     - Yes → Update State → Completed
- **Styled to match the site palette** using CSS custom properties so it responds to dark/light theme toggle:
  - Step nodes: `fill: var(--color-surface)`, `stroke: var(--color-accent)`
  - Decision diamond: `fill: var(--color-accent)` with dark text
  - "Completed" node: `fill: var(--color-accent)` at full opacity
  - Arrow/connector lines: `stroke: var(--color-border)`
  - Text: `fill: var(--color-text)`, `font-family: var(--font-family-base)`
- SVG must be responsive: `width: 100%`, `max-width: 420px`, `height: auto`

---

### Hobbies (`#hobbies`)

- Informal section between Projects and Footer, inspired by the reference site's emoji-based hobby display.
- Section heading: `When I'm not coding...`
- Display as a horizontal wrapping row of pill/chip elements, each with an emoji and text label:
  - 🏒 Hockey
  - 🃏 Poker
  - 🥾 Hiking
  - ⛷️ Skiing
  - 🎮 Gaming
  - 📚 Brandon Sanderson Novels
- **Interaction:** by default each chip shows only the emoji. On hover, the text label fades/slides in beside the emoji. Implement by wrapping the label in a `<span class="hobbies__chip-label">` that is hidden by default (`max-width: 0; opacity: 0; overflow: hidden`) and expands on `.hobbies__chip:hover` (`max-width: 200px; opacity: 1`) with a `200ms ease` transition.
- Chips styled with surface background, border, and muted text — no accent color, intentionally low-key.

---

## Footer

- Minimal: centered text — `"Peter Mark · Seattle, WA"` and `"Built by Peter Mark"`.
- Icon links: GitHub, LinkedIn, Email (same as hero).
- No separate contact section — email link in footer serves as contact.

---

## Responsive Breakpoints

- Mobile-first CSS.
- `768px`: two-column project grid, navbar links visible (no hamburger needed given only 2 links).
- `1024px`: increase hero font size.

---

## Animations & Interactions

- Sections fade-in + slide-up on scroll into view via IntersectionObserver (simple CSS class toggle, no library).
- Smooth scroll behavior: `scroll-behavior: smooth` on `html`.
- All transitions: `200ms ease` default.

---

## GitHub README

A `README.md` must be created at the repo root (`https://github.com/ptemark/PersonalWebsite`) with a dedicated section that links directly to the following files on GitHub:

| File | Description |
|------|-------------|
| `spec/DESIGN.md` | Website design specification |
| `spec/TASKS.md` | Implementation task list |
| `RALPH.md` | RALPH loop — the implementation process used to build this site |

Links should use the full GitHub URL format: `https://github.com/ptemark/PersonalWebsite/blob/main/<file>`.

## Website Links to Spec Files

The website footer must include a subtle "How this was built" link that opens the GitHub repo (`https://github.com/ptemark/PersonalWebsite`). Individual pages within the repo (DESIGN.md, TASKS.md, RALPH.md) are navigable from there via the README links above — no need to deep-link to each from the site itself.

## Implementation Process

This site is built using the **RALPH loop** — an iterative, spec-driven autonomous development process. See `RALPH.md` for the full loop definition. In summary: read the spec, implement one task, verify, repeat.

---

## File Structure (implementation target)

```
index.html          — single page, all sections
css/style.css       — all styles (custom properties, layout, components)
js/app.js           — theme toggle, scroll spy, scroll animations
img/projects/       — project thumbnails
spec/               — design docs, resume (not shipped to dist)
```
