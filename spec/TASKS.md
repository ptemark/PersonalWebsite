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

- [x] **1** — Create `CNAME` file in project root containing `petermark.dev`
- [x] **2** — Update `webpack.config.prod.js` CopyPlugin to include `CNAME` in dist output
- [x] **3** — Create `.github/workflows/deploy.yml` — GitHub Actions workflow that runs `npm run build` on push to `main` and deploys `dist/` to GitHub Pages using `actions/upload-pages-artifact` and `actions/deploy-pages`
- [x] **4** — Create `README.md` at repo root with project description, live site link (`petermark.dev`), and a spec table linking to `spec/DESIGN.md`, `spec/TASKS.md`, and `RALPH.md` on GitHub

### Phase 2 — Base HTML & CSS

- [x] **5** — Rewrite `index.html` with full semantic shell: `<nav>`, `<main>` containing `<section id="hero">`, `<section id="experience">`, `<section id="projects">`, `<section id="hobbies">`, and `<footer>`. Include Inter font from Google Fonts, CSP meta tag, and link to `css/style.css` and `js/app.js`
- [x] **6** — Set up `css/style.css` from scratch: CSS custom properties for full dark and light palettes (colors, spacing, typography tokens), `:root` defaults to dark, `[data-theme="light"]` overrides, `scroll-behavior: smooth` on `html`, base `font-family`, `font-size`, `line-height`
- [x] **7** — Add layout utilities to `css/style.css`: `.container` max-width `860px` centered, section vertical padding `80px`, horizontal page padding (`24px` mobile / `48px` desktop), global `box-sizing: border-box`, `200ms ease` transition default

### Phase 3 — Navigation

- [x] **8** — Implement navbar HTML inside `<nav>`: wordmark "Peter Mark" anchor left (links to `#hero`), anchor links "Experience" and "Projects" right, theme toggle `<button>` with `aria-label` and sun/moon icon (SVG inline)
- [x] **9** — Style navbar in CSS: fixed top, full width, surface background + `backdrop-filter: blur(8px)`, BEM classes, hover states, scrolled state border (JS adds `.nav--scrolled` class), active link style (`.nav__link--active`)
- [x] **10** — Implement theme toggle in `js/app.js`: detect `prefers-color-scheme` on load, read/write `localStorage` key `theme`, toggle `data-theme` attribute on `<html>`, swap sun/moon icon on toggle. Wrap in `'use strict'` IIFE, use `DOMContentLoaded`
- [x] **11** — Implement scroll spy in `js/app.js`: use `IntersectionObserver` to watch each `<section>`, add/remove `.nav__link--active` on the corresponding nav link as sections enter/leave viewport. Also add/remove `.nav--scrolled` on `<nav>` when page is scrolled past `0`

### Phase 4 — Hero Section

- [x] **12** — Copy `spec/peter.jpg` to `img/peter.jpg`. Correct the 90° clockwise rotation — apply `transform: rotate(-90deg)` via CSS on the `<img>` element (or fix the file directly if tooling is available)
- [x] **13** — Implement hero section HTML: greeting label, name `h1`, title, tagline, two CTA `<a>` buttons ("View My Work" → `#projects`, "Get In Touch" → `#footer`), social icon links row (GitHub, LinkedIn, Email — all with `rel="noopener noreferrer"` and `aria-label`), and photo `<img>` with `alt="Peter Mark on a mountain summit"`
- [x] **14** — Style hero section: `min-height: 100vh`, flexbox centered layout, two-column layout on desktop (text left, photo right), circular/rounded photo, name in accent color at `3rem+` weight `700`, muted title and tagline, filled accent CTA button and outlined secondary button, social icon row spacing

### Phase 5 — Experience Section

- [x] **15** — Implement experience section HTML: `<section id="experience">` with heading "Experience", a `<ul>` timeline list with four `<li>` entries (FIS, Amazon SWE II, Amazon SWE I, Ciena). Each entry: role + company in `<h3>`, date range, bullet list of accomplishments from `spec/Peter_Mark_Resume.md`
- [x] **16** — Style experience section: vertical timeline with `border-left` in accent color, left-padded entries, role bold, date range muted and right-aligned on desktop, entry spacing, BEM classes throughout

### Phase 6 — Projects Section

- [x] **17** — Create `img/projects/` directory and add a placeholder image `img/projects/personal-website.png` (a solid-color placeholder is fine — screenshot to be added later)
- [x] **18** — Implement projects section HTML: `<section id="projects">` with heading "Projects", card grid containing one card for "Personal Website" — thumbnail `<img>`, project name, description, tech tag pills (HTML, CSS, JavaScript, Webpack), GitHub icon link (`https://github.com/ptemark/PersonalWebsite`) and live site icon link (`https://petermark.dev`), all external links with `rel="noopener noreferrer"`
- [x] **19** — Style projects section: CSS Grid single column mobile / two columns at `768px`, card surface background + border + border-radius, thumbnail `aspect-ratio: 16/9` `object-fit: cover`, tag pills accent-tinted, card hover `box-shadow` + `translateY(-4px)` transition

### Phase 7 — Hobbies Section

- [x] **20** — Implement hobbies section HTML: `<section id="hobbies">` with heading "When I'm not coding..." and a wrapping row of `<span>` chip elements: 🏒 Hockey, 🃏 Poker, 🥾 Hiking, ⛷️ Skiing, 🎮 Gaming, 📚 Brandon Sanderson Books
- [x] **21** — Style hobbies section: `display: flex; flex-wrap: wrap; gap`, chips with surface background, border, border-radius, muted text, no accent color — intentionally low-key

### Phase 8 — Footer

- [x] **22** — Implement footer HTML: `<footer id="footer">` with centered "Peter Mark · Seattle, WA" text, social icon links row (GitHub, LinkedIn, Email — same as hero), "How this was built" link to `https://github.com/ptemark/PersonalWebsite` with `rel="noopener noreferrer"`, and "Built by Peter Mark" line
- [x] **23** — Style footer: centered layout, muted text, divider top border, icon link row matching hero, appropriate vertical padding

### Phase 9 — Scroll Animations

- [x] **24** — Implement scroll animations in `js/app.js`: `IntersectionObserver` watches all `<section>` elements, adds `.is-visible` class when they enter the viewport. CSS defines `.section { opacity: 0; transform: translateY(20px); transition: opacity 0.5s ease, transform 0.5s ease; }` and `.section.is-visible { opacity: 1; transform: none; }`. Hero section starts visible (no animation delay on load)

### Phase 10 — Polish & Accessibility

- [x] **25** — Responsive pass: verify navbar, hero two-column layout, project grid, and section padding all behave correctly at mobile (`< 768px`), tablet (`768px`), and desktop (`1024px+`). Fix any layout issues
- [x] **26** — Hero font scale: at `1024px+` increase hero name to `4rem`, tagline to `1.125rem`
- [ ] **27** — Accessibility pass: verify all images have `alt`, all icon buttons have `aria-label`, all sections have logical heading hierarchy (`h1` in hero, `h2` for section headings, `h3` for job titles/project names), confirm keyboard navigation works for all interactive elements
- [ ] **28** — Final build verification: run `npm run build`, confirm `dist/` contains `index.html`, `css/style.css`, `js/app.js`, `img/`, `CNAME`, `favicon.ico`, `robots.txt`, `site.webmanifest`, `404.html`. Confirm no build errors or warnings

---

## Completed Tasks

| # | Date | Task | Files Changed | Notes |
|---|------|------|---------------|-------|
| 1 | 2026-03-02 | Create CNAME file | CNAME | Contains petermark.dev for GitHub Pages custom domain |
| 2 | 2026-03-02 | Update webpack CopyPlugin to include CNAME | webpack.config.prod.js | Added toType: 'file' to ensure CNAME copies as a file, not directory |
| 3 | 2026-03-02 | Create GitHub Actions deploy workflow | .github/workflows/deploy.yml | Builds on push to main, deploys dist/ to GitHub Pages |
| 4 | 2026-03-02 | Create README.md | README.md | Project description, live site link, spec table with GitHub links |
| 5 | 2026-03-02 | Rewrite index.html with semantic shell | index.html, webpack.config.prod.js | Inter font, CSP, nav/main/sections/footer structure; fixed HtmlWebpackPlugin duplicate script via inject:false |
| 6 | 2026-03-02 | Set up css/style.css with design tokens and base styles | css/style.css | Dark/light CSS custom properties, :root dark defaults, [data-theme="light"] overrides, smooth scroll, base reset |
| 7 | 2026-03-02 | Add layout utilities to css/style.css | css/style.css | .container (860px centered), .section (80px padding), .section__heading, desktop padding override at 768px |
| 8 | 2026-03-02 | Implement navbar HTML | index.html | nav__inner, nav__wordmark, nav__links with Experience/Projects anchors, nav__theme-toggle with inline sun+moon SVGs |
| 9 | 2026-03-02 | Style navbar in CSS | css/style.css | Fixed + blurred nav, --nav-height/--color-nav-bg tokens, BEM hover/active states, scrolled border, sun/moon icon toggling |
| 10 | 2026-03-02 | Implement theme toggle in js/app.js | js/app.js | prefers-color-scheme detection, localStorage persistence, data-theme toggle on html, aria-label update on button |
| 11 | 2026-03-02 | Implement scroll spy | js/app.js | IntersectionObserver with -10%/0px/-60% rootMargin for section active state; scroll event for nav--scrolled class |
| 12 | 2026-03-02 | Copy and rotation-correct peter.jpg | img/peter.jpg | Used sips -r 270 to fix 90° clockwise rotation directly in file; portrait 3024×4032 |
| 13 | 2026-03-02 | Implement hero section HTML | index.html | Greeting, h1, title, tagline, two CTA buttons, social icon links (GitHub/LinkedIn/Email), photo img; all ext links with rel="noopener noreferrer" and aria-label |
| 14 | 2026-03-02 | Style hero section | css/style.css | min-height calc(100vh - nav-height), flex centered, two-column desktop layout, circular photo 220/300px, accent name, muted title/tagline, filled/outlined CTA buttons, social icon row |
| 15 | 2026-03-02 | Implement experience section HTML | index.html | ul.timeline with four li entries (FIS, Amazon SWE II, Amazon SWE I, Ciena); h3 role+company, date span, ul bullets from resume |
| 16 | 2026-03-02 | Style experience section | css/style.css | Vertical timeline with accent border-left, left-padded entries, role bold, date muted+right-aligned on desktop, disc bullet list |
| 17 | 2026-03-02 | Create img/projects/ placeholder image | img/projects/personal-website.png | Solid-color 640×360 PNG (#1a1a1a) generated via Python; copied to dist/ by webpack CopyPlugin |
| 18 | 2026-03-02 | Implement projects section HTML | index.html | projects__grid ul with one card: thumbnail img, h3 name, desc, tag pills, GitHub + live site icon links with rel="noopener noreferrer" |
| 19 | 2026-03-02 | Style projects section | css/style.css | CSS Grid 1→2 col at 768px, card surface+border+border-radius, 16/9 thumbnail, accent-tinted tag pills, hover box-shadow+translateY(-4px) |
| 20 | 2026-03-02 | Implement hobbies section HTML | index.html | hobbies__chips div with six hobbies__chip span elements (Hockey, Poker, Hiking, Skiing, Gaming, Brandon Sanderson Books) |
| 21 | 2026-03-02 | Style hobbies section | css/style.css | flex+flex-wrap+gap chips row; surface bg, border, 999px border-radius, muted text; no accent — intentionally low-key |
| 22 | 2026-03-02 | Implement footer HTML | index.html | footer__inner with name/location, social icons (GitHub/LinkedIn/Email), How this was built link, Built by Peter Mark line |
| 23 | 2026-03-02 | Style footer | css/style.css | Centered flex column, border-top divider, muted text throughout, social icon row matching hero, 2.5rem vertical padding, subtle built-link hover to accent |
| 24 | 2026-03-03 | Implement scroll animations | js/app.js, css/style.css | IntersectionObserver adds .is-visible to sections on scroll; hero starts visible; CSS opacity+translateY fade-in transition |
| 25 | 2026-03-03 | Responsive pass | css/style.css | scroll-padding-top on html for fixed nav; nav__links gap 1rem mobile/1.5rem 768px+; hero opacity:1 override (always visible); overflow-wrap:break-word on body |
| 26 | 2026-03-03 | Hero font scale at 1024px+ | css/style.css | @media (min-width: 1024px) overrides --font-size-hero-name to 4rem and .hero__tagline to 1.125rem |

