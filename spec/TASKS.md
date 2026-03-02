# TASKS

Track implementation progress for petermark.dev. Each task is one RALPH loop iteration.
See `RALPH.md` for the full loop process. See `DESIGN.md` for all design decisions.

---

## Current Task

_None in progress._

---

## Next Up

Tasks are ordered by dependency. Complete them top to bottom.

### Phase 1 — Project Scaffolding

- [ ] **1** — Create `CNAME` file in project root containing `petermark.dev`
- [ ] **2** — Update `webpack.config.prod.js` CopyPlugin to include `CNAME` in dist output
- [ ] **3** — Create `.github/workflows/deploy.yml` — GitHub Actions workflow that runs `npm run build` on push to `main` and deploys `dist/` to GitHub Pages using `actions/upload-pages-artifact` and `actions/deploy-pages`
- [ ] **4** — Create `README.md` at repo root with project description, live site link (`petermark.dev`), and a spec table linking to `spec/DESIGN.md`, `spec/TASKS.md`, and `RALPH.md` on GitHub

### Phase 2 — Base HTML & CSS

- [ ] **5** — Rewrite `index.html` with full semantic shell: `<nav>`, `<main>` containing `<section id="hero">`, `<section id="experience">`, `<section id="projects">`, `<section id="hobbies">`, and `<footer>`. Include Inter font from Google Fonts, CSP meta tag, and link to `css/style.css` and `js/app.js`
- [ ] **6** — Set up `css/style.css` from scratch: CSS custom properties for full dark and light palettes (colors, spacing, typography tokens), `:root` defaults to dark, `[data-theme="light"]` overrides, `scroll-behavior: smooth` on `html`, base `font-family`, `font-size`, `line-height`
- [ ] **7** — Add layout utilities to `css/style.css`: `.container` max-width `860px` centered, section vertical padding `80px`, horizontal page padding (`24px` mobile / `48px` desktop), global `box-sizing: border-box`, `200ms ease` transition default

### Phase 3 — Navigation

- [ ] **8** — Implement navbar HTML inside `<nav>`: wordmark "Peter Mark" anchor left (links to `#hero`), anchor links "Experience" and "Projects" right, theme toggle `<button>` with `aria-label` and sun/moon icon (SVG inline)
- [ ] **9** — Style navbar in CSS: fixed top, full width, surface background + `backdrop-filter: blur(8px)`, BEM classes, hover states, scrolled state border (JS adds `.nav--scrolled` class), active link style (`.nav__link--active`)
- [ ] **10** — Implement theme toggle in `js/app.js`: detect `prefers-color-scheme` on load, read/write `localStorage` key `theme`, toggle `data-theme` attribute on `<html>`, swap sun/moon icon on toggle. Wrap in `'use strict'` IIFE, use `DOMContentLoaded`
- [ ] **11** — Implement scroll spy in `js/app.js`: use `IntersectionObserver` to watch each `<section>`, add/remove `.nav__link--active` on the corresponding nav link as sections enter/leave viewport. Also add/remove `.nav--scrolled` on `<nav>` when page is scrolled past `0`

### Phase 4 — Hero Section

- [ ] **12** — Copy `spec/peter.jpg` to `img/peter.jpg`. Correct the 90° clockwise rotation — apply `transform: rotate(-90deg)` via CSS on the `<img>` element (or fix the file directly if tooling is available)
- [ ] **13** — Implement hero section HTML: greeting label, name `h1`, title, tagline, two CTA `<a>` buttons ("View My Work" → `#projects`, "Get In Touch" → `#footer`), social icon links row (GitHub, LinkedIn, Email — all with `rel="noopener noreferrer"` and `aria-label`), and photo `<img>` with `alt="Peter Mark on a mountain summit"`
- [ ] **14** — Style hero section: `min-height: 100vh`, flexbox centered layout, two-column layout on desktop (text left, photo right), circular/rounded photo, name in accent color at `3rem+` weight `700`, muted title and tagline, filled accent CTA button and outlined secondary button, social icon row spacing

### Phase 5 — Experience Section

- [ ] **15** — Implement experience section HTML: `<section id="experience">` with heading "Experience", a `<ul>` timeline list with four `<li>` entries (FIS, Amazon SWE II, Amazon SWE I, Ciena). Each entry: role + company in `<h3>`, date range, bullet list of accomplishments from `spec/Peter_Mark_Resume.md`
- [ ] **16** — Style experience section: vertical timeline with `border-left` in accent color, left-padded entries, role bold, date range muted and right-aligned on desktop, entry spacing, BEM classes throughout

### Phase 6 — Projects Section

- [ ] **17** — Create `img/projects/` directory and add a placeholder image `img/projects/personal-website.png` (a solid-color placeholder is fine — screenshot to be added later)
- [ ] **18** — Implement projects section HTML: `<section id="projects">` with heading "Projects", card grid containing one card for "Personal Website" — thumbnail `<img>`, project name, description, tech tag pills (HTML, CSS, JavaScript, Webpack), GitHub icon link (`https://github.com/ptemark/PersonalWebsite`) and live site icon link (`https://petermark.dev`), all external links with `rel="noopener noreferrer"`
- [ ] **19** — Style projects section: CSS Grid single column mobile / two columns at `768px`, card surface background + border + border-radius, thumbnail `aspect-ratio: 16/9` `object-fit: cover`, tag pills accent-tinted, card hover `box-shadow` + `translateY(-4px)` transition

### Phase 7 — Hobbies Section

- [ ] **20** — Implement hobbies section HTML: `<section id="hobbies">` with heading "When I'm not coding..." and a wrapping row of `<span>` chip elements: 🏒 Hockey, 🃏 Poker, 🥾 Hiking, ⛷️ Skiing, 🎮 Gaming, 📚 Brandon Sanderson Books
- [ ] **21** — Style hobbies section: `display: flex; flex-wrap: wrap; gap`, chips with surface background, border, border-radius, muted text, no accent color — intentionally low-key

### Phase 8 — Footer

- [ ] **22** — Implement footer HTML: `<footer id="footer">` with centered "Peter Mark · Seattle, WA" text, social icon links row (GitHub, LinkedIn, Email — same as hero), "How this was built" link to `https://github.com/ptemark/PersonalWebsite` with `rel="noopener noreferrer"`, and "Built by Peter Mark" line
- [ ] **23** — Style footer: centered layout, muted text, divider top border, icon link row matching hero, appropriate vertical padding

### Phase 9 — Scroll Animations

- [ ] **24** — Implement scroll animations in `js/app.js`: `IntersectionObserver` watches all `<section>` elements, adds `.is-visible` class when they enter the viewport. CSS defines `.section { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }` and `.section.is-visible { opacity: 1; transform: none; }`. Hero section starts visible (no animation delay on load)

### Phase 10 — Polish & Accessibility

- [ ] **25** — Responsive pass: verify navbar, hero two-column layout, project grid, and section padding all behave correctly at mobile (`< 768px`), tablet (`768px`), and desktop (`1024px+`). Fix any layout issues
- [ ] **26** — Hero font scale: at `1024px+` increase hero name to `4rem`, tagline to `1.125rem`
- [ ] **27** — Accessibility pass: verify all images have `alt`, all icon buttons have `aria-label`, all sections have logical heading hierarchy (`h1` in hero, `h2` for section headings, `h3` for job titles/project names), confirm keyboard navigation works for all interactive elements
- [ ] **28** — Final build verification: run `npm run build`, confirm `dist/` contains `index.html`, `css/style.css`, `js/app.js`, `img/`, `CNAME`, `favicon.ico`, `robots.txt`, `site.webmanifest`, `404.html`. Confirm no build errors or warnings

---

## Completed Tasks

| # | Date | Task | Files Changed | Notes |
|---|------|------|---------------|-------|

