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

### Phase 19 — Hero Polish & Content Fixes

- [x] **46** — "Open to opportunities" badge: add a `<div class="hero__status">` element between `.hero__tagline` and `.hero__cta` in the hero section. Contains a green dot `<span aria-hidden="true">` and the text "Open to opportunities". Style as a small inline-flex pill with surface background, border, border-radius 999px, and a `--color-status-green: #22c55e` dot. Left-aligned on desktop, centered on mobile (matching existing hero alignment). Adjust `.hero__tagline` margin-bottom to `0.75rem`; give `.hero__status` `margin-bottom: 1.75rem`. Also fix the DynamoDB duplicate in the skills section — remove it from Cloud & Infrastructure tags (it already appears in Databases), keeping only: AWS, S3, EC2, ECS, Lambda, Docker, Kubernetes, Terraform.

### Phase 20 — Accessibility

- [x] **47** — Skip-to-content link: add `<a class="skip-link" href="#main-content">Skip to main content</a>` as the first element in `<body>` in `index.html`. Add `id="main-content"` to `<main>`. CSS: `.skip-link` positioned absolutely, `top: -100%` (off-screen by default), slides to `top: 0` on `:focus`. Accent background, dark text, `border-radius` on bottom-right corner, `z-index: 200`. Hidden in print styles. Implements WCAG 2.4.1 bypass-block pattern for keyboard and screen reader users.

### Phase 21 — Final Polish

- [x] **48** — Pulsing status dot: add a `@keyframes status-pulse` animation (box-shadow ring expansion) to `.hero__status-dot` in `css/style.css`. Wraps in `@media (prefers-reduced-motion: no-preference)` so it only runs when the user hasn't requested reduced motion. 2s infinite ease cycle — soft glow ring expands out from the green dot and fades. No JS changes needed.
- [x] **49** — Periodic codebase review (iteration 49): full review of `index.html`, `css/style.css`, and `js/app.js` — check for BEM inconsistencies, dead CSS, redundant rules, hardcoded values, and security/accessibility regressions. Refactor and clean up; confirm `npm run build` passes. Commit as `refactor: periodic codebase review and cleanup`.

### Phase 22 — Performance & Polish

- [x] **50** — LCP image preload: add `<link rel="preload" as="image" href="img/peter.jpg" fetchpriority="high">` to `<head>` in `index.html` before the stylesheet link. This gives the browser an early signal to fetch the hero photo (the Largest Contentful Paint element) before the HTML parser reaches the `<img>` tag, improving the Core Web Vitals LCP score.
- [x] **51** — Theme-color meta for dark/light OS preference: replace the single `<meta name="theme-color" content="#0f0f0f">` with two `<meta name="theme-color">` tags using `media` attributes — one for `(prefers-color-scheme: dark)` with `#0f0f0f` and one for `(prefers-color-scheme: light)` with `#fafafa`. Makes the browser chrome/status bar on mobile match the user's OS color scheme.
- [x] **52** — Scroll spy robustness: wrap the `IntersectionObserver` scroll-spy in a `requestAnimationFrame` debounce so that when multiple sections enter/leave simultaneously (e.g. fast scroll), only the topmost visible section gets the active class. Currently the last entry processed wins, which can mis-highlight the wrong nav link on fast scrolls.

### Phase 23 — Keyboard UX & Image Performance

- [x] **53** — Keyboard UX + image decode: (a) Add Escape key listener in `js/app.js` — when mobile menu is open, pressing Escape calls `closeMenu()` and returns focus to the hamburger button (WAI-ARIA Disclosure Button pattern). Update `closeMenu()` to accept an optional `returnFocus` flag. (b) Add `decoding="async"` attribute to the project card `<img>` in `index.html` — moves image decoding off the main thread for below-fold images, reducing potential jank. Hero image intentionally stays without this attr (it's LCP/above-fold).

### Phase 24 — Progressive Enhancement

- [x] **54** — `<noscript>` CSS fallback: `.section` elements default to `opacity: 0; transform: translateY(20px)` for scroll animations. Without JS, the page is blank below the nav since `is-visible` is never added. Create `css/noscript.css` with `.section { opacity: 1; transform: none; }`. Add `<noscript><link rel="stylesheet" href="css/noscript.css"></noscript>` to `index.html` after the main stylesheet. The `css/` CopyPlugin pattern already covers the new file — no webpack config change needed.

### Phase 25 — Accessibility Refinements

- [x] **55** — `aria-current` on active nav link: the scroll spy adds/removes `.nav__link--active` visually but never sets the WAI-ARIA `aria-current` attribute, so screen readers have no way to announce which section is active. In `updateActiveLink()` in `js/app.js`, remove `aria-current` from all nav links when clearing active state, and set `aria-current="location"` on the newly active link. No HTML or CSS changes needed.

### Phase 26 — Favicon Branding

- [x] **56** — Custom SVG favicon: replace the HTML5 Boilerplate default `icon.svg` (orange star) with a branded "PM" monogram SVG. Design: 32×32 viewBox, accent-purple rounded-rect background (`#7C3AED`, `rx="7"`), bold white "PM" text centered. This is the SVG favicon served to all modern browsers. The existing `favicon.ico` remains as the legacy fallback. No webpack config changes needed — `icon.svg` is already in the CopyPlugin patterns.

### Phase 27 — Photo & Resume Content Update

- [x] **57** — Hero photo fix: the `img/peter.jpg` file has been physically rotated to the correct orientation (hands up, sky at top). Remove any `transform: rotate()` applied to `.hero__photo` in `css/style.css` that was added as a temporary workaround in task 12 — it is no longer needed and would double-rotate the image. Commit the updated `img/peter.jpg` and `spec/peter.jpg` along with any CSS change. Verify the photo displays correctly in both dark and light themes.
- [x] **58** — Experience section summary blurb: add a `<p class="experience__summary">` paragraph directly below the "Experience" `<h2>` heading and above the timeline `<ul>` in `index.html`. Text: "Senior Software Engineer with 7+ years of experience designing and building scalable, reliable distributed systems. Expert in Java, Python, and AWS, with deep experience in microservices, cloud infrastructure, and system optimization. Proven ability to lead design discussions, mentor peers, and deliver impactful, high-performance software solutions." Add `.experience__summary` to `css/style.css`: `font-size: 0.9375rem`, `color: var(--color-text-muted)`, `line-height: var(--line-height-base)`, `margin-bottom: 2rem`. Verify build passes and commit.
- [x] **59** — Hobbies chip interaction + copy fix: (1) Change "Brandon Sanderson Books" to "Brandon Sanderson Novels" in `index.html`. (2) Rework each `.hobbies__chip` so only the emoji is visible by default and the text label reveals on hover. Wrap each label in `<span class="hobbies__chip-label">`. CSS: `.hobbies__chip-label { max-width: 0; opacity: 0; overflow: hidden; white-space: nowrap; transition: max-width 200ms ease, opacity 200ms ease; }` and `.hobbies__chip:hover .hobbies__chip-label { max-width: 200px; opacity: 1; }`. Also add a small `gap` between emoji and label inside the chip. No JS needed. Verify build passes and commit.
- [x] **60** — Redesign Projects section as a RALPH loop showcase. Replace the current card grid in `index.html` with a two-column feature layout (stacked on mobile, side-by-side on desktop at `≥ 768px`). Left column: `<h3>petermark.dev</h3>`, two-paragraph description of how RALPH built the site, tech tag pills (HTML, CSS, JavaScript, Webpack, GitHub Actions), a prominent filled-accent "View Source on GitHub" button linking to `https://github.com/ptemark/PersonalWebsite`, a secondary "Learn about the RALPH loop" text link to `https://ghuntley.com/ralph/`, and an attribution line "RALPH loop concept by Geoffrey Huntley" linked to `https://ghuntley.com/ralph/` — all external links with `rel="noopener noreferrer" target="_blank"`. Right column: hand-crafted inline SVG flowchart based on `spec/The Ralph Loop` showing the 6-step loop (Design → Initialize → Fresh Context → Read State → Do Work → Exit Check decision diamond with No loop back and Yes path to Update State → Completed). Style SVG nodes using CSS custom properties (`var(--color-surface)`, `var(--color-accent)`, `var(--color-border)`, `var(--color-text)`, `var(--font-family-base)`) so it responds to dark/light theme. SVG: `width="100%"` `max-width: 420px`. Update `css/style.css` with `.projects__feature` BEM layout classes. Remove old `.projects__grid` / `.projects__card` styles if no longer used. Verify build passes and commit.
- [x] **61** — Update site content to match the revised resume (`spec/Peter_Mark_Resume.md`). Three changes: (1) **FIS bullet 1** in `#experience`: replace old text with "Built explainability and compliance framework with SHAP, bias detection, and drift monitoring in Amazon SageMaker, meeting model risk standards that facilitated a multi-million-dollar fintech deal around fraud detection." (2) **Tools** in `#skills`: add `IntelliJ` and `Eclipse` as skill tags to the Tools category. (3) **Leadership** in `#leadership`: remove the third bullet "Communicated complex technical topics effectively through demos and documentation." Verify `npm run build` passes, commit.

### Phase 28 — Hero CTA Cleanup

- [x] **62** — Remove the "View My Work" CTA button from the hero section in `index.html`. Keep only the "Get In Touch" button. Remove the `.hero__btn--primary` element entirely. Verify the CTA row still looks correct on mobile and desktop with a single button. If the single-button layout looks unbalanced, adjust `.hero__cta` spacing accordingly in `css/style.css`. Build passes, commit.

### Phase 29 — Project Metadata & Code Quality

- [x] **63** — Fill in `package.json` metadata: set `name` to `"petermark-dev"`, `description` to `"Personal portfolio website for Peter Mark — petermark.dev"`, `author` to `"Peter Mark <peter.sw.mark@gmail.com>"`, `license` to `"MIT"`, and clear the empty `keywords` array. Build passes, commit.
- [x] **64** — `js/app.js` null safety: before using `toggleBtn`, `nav`, `hamburgerBtn`, and `backToTopBtn`, add a null check for each element before attaching event listeners or calling methods on them. This prevents uncaught TypeErrors if any element is ever absent (e.g. on future pages). Use an early `if (!toggleBtn) return;` guard pattern at the top of the relevant blocks. Build passes, commit.
- [x] **65** — Hobbies chips accessibility: change the chips container from `<div class="hobbies__chips">` to `<ul class="hobbies__chips">` and each `<span class="hobbies__chip">` to `<li class="hobbies__chip">` in `index.html`. Update `css/style.css` BEM selectors if needed (they should still work since class names stay the same). Also wrap the hobbies chip label hover transition (added in Task 59) in `@media (prefers-reduced-motion: no-preference)` so users who prefer reduced motion see the label immediately without animation. Build passes, commit.
- [x] **66** — CSS custom properties for accent tints: the project card tag styles use hardcoded `rgba(167, 139, 250, 0.12)` and `rgba(167, 139, 250, 0.25)` (dark) and `rgba(124, 58, 237, 0.1)` / `rgba(124, 58, 237, 0.2)` (light) values in `css/style.css`. Add `--color-accent-tint: rgba(167, 139, 250, 0.12)` and `--color-accent-tint-border: rgba(167, 139, 250, 0.25)` to `:root` and their light equivalents to `[data-theme="light"]`, then replace all hardcoded rgba values with the new custom properties. Build passes, commit.
- [x] **67** — Fix hero photo rotation: `img/peter.jpg` and `spec/peter.jpg` currently display with hands pointing to the right (over-rotated). Rotate both files 90° counterclockwise using `sips -r 270 img/peter.jpg` and `sips -r 270 spec/peter.jpg` so that hands point up and the sky is at the top. Verify the photo displays correctly in the browser before committing. Ensure no `transform: rotate()` is applied to `.hero__photo` in `css/style.css`. Commit both image files.

### Phase 30 — Visual Refinements

- [x] **68** — Fix hero photo framing: the current hero photo crops Peter at the knees. Inspect how `.hero__photo` is displayed in CSS — check `object-fit` and `object-position`. First try adjusting `object-position` (e.g. `center top` or `center 20%`) in `css/style.css` to shift focus upward. If the image dimensions cause the issue, use `sips --cropOffset <top> <left> --cropBox <height> <width> img/peter.jpg` to remove excess lower-body content from the source file (apply same crop to `spec/peter.jpg`). Goal: Peter should appear centered in the photo with the body visible above the knees at all viewport sizes. Verify at both mobile (where the photo is often square/compact) and desktop (side-by-side layout). Build passes, commit.
- [x] **69** — Dark mode muted text readability: `--color-text-muted` (used for tagline, date ranges, section subtitles, etc.) is a light grey that lacks sufficient contrast in dark mode. Audit its current value in `:root` in `css/style.css`. Update the dark-mode value in `:root` to a lighter, more readable shade — aim for a value around `#a0a0a0` or `#9ca3af` that passes WCAG AA contrast (4.5:1) against the dark surface (`#0f0f0f`). Keep the existing `--color-text-muted` value in `[data-theme="light"]` unchanged. Build passes, commit.
- [x] **70** — Larger PM in favicon: the "PM" monogram in `icon.svg` is too small within the 32×32 canvas. Open `icon.svg` and increase the `font-size` on the `<text>` element (try 18–20px) and adjust `x`/`y` to re-center it within the rounded-rect. Verify the icon renders crisply at 16×16 and 32×32 (view in browser tab). Build passes, commit.

### Phase 31 — RALPH Documentation

- [x] **71** — Update RALPH loop diagram in Projects section: read `spec/The Ralph Loop` (Mermaid flowchart source) to check whether the diagram has been updated since Task 60 built the inline SVG in `index.html`. If the source has changed, update the inline SVG in the Projects section to accurately reflect the current flowchart. If unchanged, verify the existing SVG matches the Mermaid source step-by-step and correct any discrepancies. SVG must continue to use CSS custom properties for theming (`var(--color-surface)`, `var(--color-accent)`, etc.). Build passes, commit.
- [x] **72** — Expand README with RALPH loop explanation: add a `## Built with RALPH` section to `README.md` that goes deeper than the Projects section on the site. Include: (1) what RALPH is — a spec-driven autonomous AI development loop — and credit Geoffrey Huntley as the concept origin with a link to `https://ghuntley.com/ralph/`; (2) how it was used to build this site — Claude CLI as the AI agent, iterative task execution, build verification after every change; (3) specifics: total RALPH iterations run, tools involved (Webpack 5, GitHub Actions, npm, `sips` for image processing, `claude` CLI); (4) the iteration workflow at a glance (read spec → pick task → implement → `npm run build` → commit → push → repeat); (5) link to `RALPH.md` in the repo for full agent instructions. Keep all existing README sections intact. Commit.

---

## Completed Tasks

| # | Date | Task | Files Changed | Notes |
|---|------|------|---------------|-------|
| 72 | 2026-03-04 | Expand README with RALPH loop section | README.md | Added "## Built with RALPH" section: what RALPH is + Geoffrey Huntley credit, how Claude CLI was used, 6-step iteration workflow, by-the-numbers (71+ iterations, Webpack 5/GitHub Actions/npm/sips/claude CLI, zero manual edits), link to RALPH.md; all existing sections preserved; build passes |
| 71 | 2026-03-04 | Update RALPH loop diagram | index.html | Fixed "No" branch: was pointing back to Fresh Context (step 3), now correctly points to Read State (step 4) per Mermaid spec (F -- No --> D); added "Start Next Task" right-side connector from Completed back to Initialize Loop per spec (G --> Start Next Task --> B); updated viewBox from 260 to 275 wide; updated aria-label; build passes |
| 70 | 2026-03-04 | Larger PM in favicon | icon.svg | Increased font-size from 13 to 19px; adjusted y from 21.5 to 23 to keep text vertically centered in 32×32 canvas; build passes |
| 69 | 2026-03-04 | Dark mode muted text readability | css/style.css | Updated --color-text-muted in :root from #888888 to #a0a0a0; light mode #555555 unchanged; #a0a0a0 on #0f0f0f achieves ~6.6:1 contrast ratio, well above WCAG AA 4.5:1; build passes |
| 68 | 2026-03-04 | Fix hero photo framing | img/peter.jpg, spec/peter.jpg, css/style.css | Cropped both files from landscape 4032×3024 to portrait 1800×2500 (top-center, sips -c 2500 1800 --cropOffset 0 1116); changed object-position from center 20% to center top; portrait crop creates Y overflow so position now works; shows sky + raised arms + upper body; build passes |
| 45 | 2026-03-03 | Update site.webmanifest | site.webmanifest | Set short_name "Peter Mark", name "Peter Mark — Senior Software Engineer", theme_color "#0f0f0f", background_color "#0f0f0f"; build passes |
| 46 | 2026-03-03 | Open to opportunities badge + skills fix | index.html, css/style.css | Hero status badge with green dot between tagline and CTA; --color-status-green token; desktop left-aligned/mobile centered; removed DynamoDB duplicate from Cloud & Infrastructure tags |
| 47 | 2026-03-03 | Skip-to-content link | index.html, css/style.css | .skip-link visually hidden (top:-100%), slides to top:0 on focus; id="main-content" on <main>; accent bg, dark text; hidden in print; implements WCAG 2.4.1 bypass-block |
| 48 | 2026-03-03 | Pulsing status dot animation | css/style.css | @keyframes status-pulse box-shadow ring on .hero__status-dot; 2s infinite ease; wrapped in prefers-reduced-motion: no-preference guard; build passes |
| 49 | 2026-03-03 | Periodic codebase review (iteration 49) | css/style.css | Bug fix: added .nav__link--active:hover to prevent global a:hover overriding active nav accent color; removed redundant text-decoration:none and transition:color from .nav__link, .nav__wordmark, .footer__social-link, .footer__built-link, .projects__card-link, .skip-link (all covered by global a rule); removed redundant color declaration from .nav__wordmark:hover |
| 50 | 2026-03-03 | LCP image preload | index.html | Added <link rel="preload" as="image" href="img/peter.jpg" fetchpriority="high"> before stylesheet in <head>; gives browser early fetch signal for hero photo (LCP element); build passes |
| 51 | 2026-03-03 | Dual theme-color meta tags | index.html | Replaced single theme-color meta with two media-conditional tags: dark (#0f0f0f) and light (#fafafa); mobile browser chrome matches OS color scheme |
| 52 | 2026-03-03 | Scroll spy rAF debounce | js/app.js | Maintain Set of intersecting sections; rAF debounce batches simultaneous entries; updateActiveLink picks topmost section (smallest getBoundingClientRect().top); eliminates fast-scroll mis-highlight |
| 53 | 2026-03-03 | Keyboard UX + image decode | js/app.js, index.html | Escape key closes mobile menu and returns focus to hamburger (WAI-ARIA Disclosure pattern); closeMenu() accepts returnFocus flag; decoding="async" on project card img |
| 54 | 2026-03-03 | noscript CSS fallback | css/noscript.css, index.html | Created css/noscript.css to reveal .section elements (opacity:1, transform:none) when JS is disabled; linked via <noscript> tag after main stylesheet; css/ CopyPlugin covers it automatically |
| 59 | 2026-03-03 | Hobbies chip interaction + copy fix | index.html, css/style.css | "Brandon Sanderson Books" → "Brandon Sanderson Novels"; chips restructured to show only emoji by default; .hobbies__chip-label reveals on hover via max-width/opacity transition; transition wrapped in prefers-reduced-motion guard; build passes |
| 55 | 2026-03-03 | aria-current on active nav link | js/app.js | updateActiveLink() now sets aria-current="location" on the active nav link and removes it from all others; screen readers can now announce the current section; no HTML or CSS changes needed |
| 60 | 2026-03-03 | Redesign Projects as RALPH loop showcase | index.html, css/style.css | Replaced card grid with two-column feature layout; left: petermark.dev name, 2-para description, 5 tech tags, "View Source on GitHub" accent button, "Learn about RALPH loop" link, Geoffrey Huntley attribution; right: hand-crafted inline SVG 8-node flowchart (1 Design Task → 2 Initialize Loop → 3 Fresh Context → 4 Read State → 5 Do Work → 6 Exit Criteria? [diamond] → No loops to 3 / Yes → 7 Update State → 8 Completed); SVG styled with CSS custom properties (rl-node/rl-diamond/rl-done/rl-line/rl-arr/rl-text classes); removed old .projects__grid/.projects__card* styles; updated print styles; build passes |
| 62 | 2026-03-03 | Remove "View My Work" hero CTA button | index.html | Removed hero__btn--primary "View My Work" anchor; kept only "Get In Touch" (hero__btn--secondary); CSS styles retained (404.html still uses hero__btn--primary); single-button layout balanced; build passes |
| 61 | 2026-03-03 | Update site content to match revised resume | index.html | FIS bullet 1 updated with SHAP/SageMaker explainability framework text; IntelliJ and Eclipse added to Tools skills; removed third leadership bullet ("Communicated complex technical topics…"); build passes |

