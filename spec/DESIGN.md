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
- **Photo:** `spec/peter.jpg` — outdoor/summit shot with arms outstretched, coastal backdrop. Copy to `img/peter.jpg` for use. **Note: source image is rotated 90° clockwise and must be corrected** (use CSS `transform: rotate(-90deg)` or fix the file itself before shipping). Display as a circular or rounded avatar alongside the hero text.

### Experience (`#experience`)

- Section heading: `Experience`.
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
- Card grid: single column on mobile, two columns on desktop (`≥ 768px`).
- Each card:
  - Thumbnail image (top, full-width of card, `aspect-ratio: 16/9`, `object-fit: cover`).
  - Card body: project name, short description, tech tags (pill-shaped, accent-tinted), and icon links (GitHub, live site).
  - Hover: card lifts with `box-shadow` and subtle `translateY(-4px)` transition.
- **Current project:**
  - **Personal Website** — This portfolio site. Built with HTML5 Boilerplate and Webpack.
    - Tags: `HTML`, `CSS`, `JavaScript`, `Webpack`
    - GitHub: `https://github.com/ptemark/PersonalWebsite`
    - Thumbnail: placeholder (`img/projects/personal-website.png`) — add screenshot later.

---

### Hobbies (`#hobbies`)

- Informal section between Projects and Footer, inspired by the reference site's emoji-based hobby display.
- Section heading: `When I'm not coding...`
- Display as a horizontal wrapping row of pill/chip elements, each with an emoji and label:
  - 🏒 Hockey
  - 🃏 Poker
  - 🥾 Hiking
  - ⛷️ Skiing
  - 🎮 Gaming
  - 📚 Brandon Sanderson Books
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
