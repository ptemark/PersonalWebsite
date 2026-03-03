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
- [x] **27** — Accessibility pass: verify all images have `alt`, all icon buttons have `aria-label`, all sections have logical heading hierarchy (`h1` in hero, `h2` for section headings, `h3` for job titles/project names), confirm keyboard navigation works for all interactive elements
- [x] **28** — Final build verification: run `npm run build`, confirm `dist/` contains `index.html`, `css/style.css`, `js/app.js`, `img/`, `CNAME`, `favicon.ico`, `robots.txt`, `site.webmanifest`, `404.html`. Confirm no build errors or warnings

### Phase 11 — Performance & SEO

- [x] **30** — Image performance pass: add `loading="eager"` and `fetchpriority="high"` to the hero photo (above the fold, critical); add `loading="lazy"` to the project card thumbnail (below the fold). Add explicit `width` and `height` attributes to all `<img>` elements to help the browser reserve space and prevent layout shift.
- [x] **31** — Education section: add `<section id="education">` between Experience and Projects with the B.Eng from Carleton University (May 2017), capstone project, and scholarship. Add "Education" anchor link to the navbar. Style consistent with Experience section but simpler (no timeline, just card or entry).
- [x] **32** — Open Graph image: create a `img/og-image.png` social preview (1200×630) using a Python script that renders name + title text on a dark background matching the site palette. Add `<meta property="og:image" content="https://petermark.dev/img/og-image.png">` to `index.html`. Add `img/og-image.png` to webpack CopyPlugin.

### Phase 12 — SEO & Metadata

- [x] **33** — JSON-LD structured data: add a `<script type="application/ld+json">` block to `<head>` in `index.html` with a Person schema — `name`, `jobTitle`, `url`, `email`, `sameAs` (GitHub + LinkedIn URLs). Helps search engines understand who Peter Mark is and may enable rich results.
- [x] **34** — Twitter Card meta tags: add `<meta name="twitter:card" content="summary_large_image">`, `twitter:title`, `twitter:description`, and `twitter:image` to `index.html`. These ensure correct previews when the site is shared on X/Twitter (which no longer reliably falls back to OG tags for all card types).
- [x] **35** — Sitemap.xml: create `sitemap.xml` in the project root with a single `<url>` entry for `https://petermark.dev/`. Add `sitemap.xml` to the webpack CopyPlugin patterns so it is included in `dist/`.

### Phase 13 — Final SEO & Polish

- [x] **36** — SEO meta improvements: add `<link rel="canonical" href="https://petermark.dev">` and `<meta name="author" content="Peter Mark">` to `<head>` in `index.html`. Update `robots.txt` to add `Sitemap: https://petermark.dev/sitemap.xml` directive so crawlers discover the sitemap directly.
- [x] **37** — Project screenshot: generate a representative screenshot-style placeholder for `img/projects/personal-website.png` using Python/Pillow — render a simplified preview of the dark-theme site (nav bar, hero name, section labels) on a `640×360` canvas to replace the plain solid-color placeholder.
- [x] **38** — Leadership section: add `<section id="leadership">` between Hobbies and Footer with the three bullets from the "Leadership & Collaboration" section of the resume. Style as a simple bullet list with a section heading (no timeline, no card). Add "Leadership" anchor link to the navbar.
- [x] **39** — Periodic codebase review (iteration 39): full review of `index.html`, `css/style.css`, and `js/app.js` — check for stale BEM inconsistencies, dead CSS, redundant rules, hardcoded values, and any security/accessibility regressions. Refactor and clean up; confirm `npm run build` passes.

### Phase 14 — Technical Skills

- [x] **40** — Technical Skills section: add `<section id="skills">` between Education and Projects with the six skill categories from `spec/Peter_Mark_Resume.md` (Languages, Cloud & Infrastructure, Messaging & Streaming, Databases, Tools, Methodologies). Use a `<dl>` (category name as `<dt>`, tag pills as `<dd>`) layout. On desktop, category name is left-aligned with min-width, tags wrap to the right. Style tags as neutral surface chips (not accent-tinted) to differentiate from project tech tags. No nav link needed (nav already has 4 links; Skills is discoverable by scroll like Hobbies).

### Phase 15 — UX Polish

- [x] **41** — Back to top button: add a fixed bottom-right `<button class="back-to-top">` with an up-arrow SVG and `aria-label="Back to top"`. Hidden by default (opacity 0, pointer-events none). JS scroll listener shows it (adds `.back-to-top--visible`) when `scrollY > window.innerHeight`, hides otherwise. Click scrolls to `window.scrollTo({ top: 0, behavior: 'smooth' })`. Respect `prefers-reduced-motion` (use `behavior: 'instant'` when reduced motion is preferred). BEM classes, accent color, surface background, transition.

### Phase 16 — Print Styles

- [x] **42** — CSS print styles: enhance the existing `@media print` block in `css/style.css` with portfolio-specific rules. Hide nav, back-to-top button, hero CTA/social/photo, footer social icons, and footer meta. Remove body top padding (nav is hidden). Force all `.section` elements to `opacity: 1; transform: none` (scroll animations default them to invisible). Compact hero layout. Add `page-break-inside: avoid` to `.timeline__entry`, `.education__entry`, and `.projects__card`. Collapse project grid to single column. Keep name/location footer text visible.

### Phase 17 — Mobile UX

- [x] **43** — Mobile hamburger menu: the nav now has 4 links which overflow on narrow screens. Restructure nav HTML: wrap links in `div.nav__links#nav-links`, move theme toggle out as a sibling, add `button.nav__hamburger#nav-hamburger` with a three-line / X SVG toggle. CSS: links hidden on mobile by default; `.nav--open .nav__links` shows as absolute full-width dropdown below the nav bar with vertical link layout; hamburger hidden on desktop (`≥ 768px`), links inline. JS: toggle `.nav--open` + `aria-expanded` on hamburger click; close on link click, outside click, or resize to desktop.

### Phase 18 — Branded Error Page & PWA Metadata

- [x] **44** — Custom 404 page: rewrite `404.html` to match the site's design. Link `css/style.css` and the Inter font. Show the accent-colored "404" numeral, a plain-language heading, a short message, and a "Go Back Home" button (reuse `.hero__btn--primary`). Add a `.body--no-nav` class to the 404 body to zero out the nav padding-top; add that rule to `css/style.css`. No inline styles — CSP stays clean. Use same CSP as `index.html` (drop `script-src` since there is no JS on 404).
- [x] **45** — Update `site.webmanifest`: set `short_name` to `"Peter Mark"`, `name` to `"Peter Mark — Senior Software Engineer"`, `theme_color` to `"#0f0f0f"` (dark bg, matches `<meta name="theme-color">` in index.html), `background_color` to `"#0f0f0f"`.

---

## Completed Tasks

| # | Date | Task | Files Changed | Notes |
|---|------|------|---------------|-------|
| 23 | 2026-03-02 | Style footer | css/style.css | Centered flex column, border-top divider, muted text throughout, social icon row matching hero, 2.5rem vertical padding, subtle built-link hover to accent |
| 24 | 2026-03-03 | Implement scroll animations | js/app.js, css/style.css | IntersectionObserver adds .is-visible to sections on scroll; hero starts visible; CSS opacity+translateY fade-in transition |
| 25 | 2026-03-03 | Responsive pass | css/style.css | scroll-padding-top on html for fixed nav; nav__links gap 1rem mobile/1.5rem 768px+; hero opacity:1 override (always visible); overflow-wrap:break-word on body |
| 26 | 2026-03-03 | Hero font scale at 1024px+ | css/style.css | @media (min-width: 1024px) overrides --font-size-hero-name to 4rem and .hero__tagline to 1.125rem |
| 27 | 2026-03-03 | Accessibility pass | index.html, css/style.css | Added :focus-visible outline styles for keyboard nav; aria-labelledby on hero section; prefers-reduced-motion disables scroll animations and smooth scroll |
| 28 | 2026-03-03 | Final build verification | — | npm run build passes; dist/ contains all 9 required files; 2 non-blocking warnings (peter.jpg size expected; code-split not applicable for static site) |
| 29 | 2026-03-03 | Periodic codebase review (iteration 29) | css/style.css | Removed dead CSS: fieldset+textarea rules (no forms on site), .visually-hidden+.visually-hidden.focusable (unused in HTML); build still passes |
| 30 | 2026-03-03 | Image performance pass | index.html | loading="eager" fetchpriority="high" on hero photo (LCP); loading="lazy" on project thumbnail; width/height on both images for CLS prevention |
| 31 | 2026-03-03 | Education section | index.html, css/style.css | Added <section id="education"> between Experience and Projects; B.Eng Carleton University, capstone + scholarship bullets; "Education" nav link; card-style entry (no timeline); scroll spy works automatically |
| 32 | 2026-03-03 | Open Graph image | img/og-image.png, index.html, scripts/generate-og-image.py | 1200×630 PNG generated via Pillow script; dark bg + accent text + dot decoration; og:image/width/height meta tags added; img/ already copied by webpack |
| 33 | 2026-03-03 | JSON-LD structured data | index.html | Person schema with name, jobTitle, url, email, address, sameAs (GitHub + LinkedIn); <script type="application/ld+json"> in <head>; not blocked by existing CSP |
| 34 | 2026-03-03 | Twitter Card meta tags | index.html | summary_large_image card; twitter:title, twitter:description, twitter:image added after OG block; reuses og-image.png |
| 35 | 2026-03-03 | Sitemap.xml | sitemap.xml, webpack.config.prod.js | Single-URL sitemap for https://petermark.dev/; added to CopyPlugin so dist/sitemap.xml is included in deploy |
| 36 | 2026-03-03 | SEO meta improvements | index.html, robots.txt | Added canonical URL + meta author to <head>; Sitemap directive added to robots.txt pointing to /sitemap.xml |
| 37 | 2026-03-03 | Project screenshot placeholder | img/projects/personal-website.png, scripts/generate-project-screenshot.py | 640×360 PNG via Pillow: navbar, hero text, CTA buttons, Experience section peek; replaces solid-color placeholder |
| 38 | 2026-03-03 | Leadership section | index.html, css/style.css | Added <section id="leadership"> between Hobbies and Footer; three resume bullets as disc list; "Leadership" nav link added; no timeline/card styling |
| 39 | 2026-03-03 | Periodic codebase review (iteration 39) | css/style.css | Replaced 4× hardcoded line-height: 1.6 with var(--line-height-base); removed 3 redundant hover rules (.nav__link:hover, .hero__social-link:hover, .footer__social-link:hover) that duplicated global a:hover |
| 40 | 2026-03-03 | Technical Skills section | index.html, css/style.css | Added <section id="skills"> between Education and Projects; dl/dt/dd layout with six categories; neutral surface-chip tags; desktop: category label left-aligned with min-width, tags flex-wrap right |
| 41 | 2026-03-03 | Back to top button | index.html, css/style.css, js/app.js | Fixed bottom-right button with up-arrow SVG; shows after scrolling past one viewport height; smooth scroll to top; respects prefers-reduced-motion; BEM classes; build passes |
| 42 | 2026-03-03 | CSS print styles | css/style.css | Portfolio-specific @media print rules: hide nav/back-to-top/hero CTAs+social+photo/footer social+meta; force .section opacity:1 (scroll animations); compact hero; break-inside: avoid on timeline/education/project entries; single-column projects grid; remove body top padding |
| 43 | 2026-03-03 | Mobile hamburger menu | index.html, css/style.css, js/app.js | Nav had 4 links overflowing on mobile; added hamburger button with menu/X icons; links dropdown on mobile via .nav--open; JS closes on link click/outside click/resize; desktop unchanged |
| 44 | 2026-03-03 | Custom 404 page | 404.html, css/style.css | Rewrote boilerplate 404 to match site design: Inter font, dark theme, accent 404 numeral, Go Back Home button reusing .hero__btn--primary; .body--no-nav utility class zeros out nav padding-top; no inline styles |
| 45 | 2026-03-03 | Update site.webmanifest | site.webmanifest | Set short_name "Peter Mark", name "Peter Mark — Senior Software Engineer", theme_color "#0f0f0f", background_color "#0f0f0f"; build passes |

