# petermark.dev

Personal portfolio website for Peter Mark, Senior Software Engineer based in Seattle, WA.

**Live site:** [petermark.dev](https://petermark.dev)

---

## Tech Stack

Plain HTML, CSS, and vanilla JavaScript bundled with [Webpack 5](https://webpack.js.org/), deployed to GitHub Pages via GitHub Actions.

---

## Spec & Process

This site is built using the **RALPH loop** — an iterative, spec-driven autonomous development process.

| File | Description |
|------|-------------|
| [`spec/DESIGN.md`](https://github.com/ptemark/PersonalWebsite/blob/main/spec/DESIGN.md) | Website design specification |
| [`spec/TASKS.md`](https://github.com/ptemark/PersonalWebsite/blob/main/spec/TASKS.md) | Implementation task list |
| [`RALPH.md`](https://github.com/ptemark/PersonalWebsite/blob/main/RALPH.md) | RALPH loop — the implementation process used to build this site |

---

## Built with RALPH

This site was built entirely using the **RALPH loop** (Recursive Autonomous Loop for Project Handling) — a spec-driven autonomous AI development methodology. RALPH concept and name by [Geoffrey Huntley](https://ghuntley.com/ralph/).

### What is RALPH?

RALPH is a structured process for using an AI agent to build software autonomously. Instead of chatting with an AI ad hoc, you write a design specification and a task list upfront, then let the agent work through the list one task at a time — reading the spec, implementing, verifying, committing, and stopping cleanly so the next iteration can continue.

### How it was used here

[Claude](https://claude.ai/claude-code) (via the Claude CLI) acted as the AI agent. Each iteration:

1. Reads `spec/DESIGN.md`, `spec/TASKS.md`, and `spec/Peter_Mark_Resume.md`
2. Picks the next unchecked task from the list
3. Implements it — HTML, CSS, and/or JS changes
4. Runs `npm run build` and verifies it passes
5. Updates `spec/TASKS.md` to mark the task complete
6. Commits and pushes all changes
7. Exits cleanly so the next iteration starts fresh

The agent never carried state between iterations. Each loop started by re-reading the full spec, giving it a clean working context every time.

### By the numbers

- **102+ RALPH iterations** completed to build this site
- **Tools:** Webpack 5, GitHub Actions, npm, `sips` (macOS image processing), Claude CLI
- **Zero manual code edits** — all source changes made by the agent within RALPH iterations

### Full agent instructions

See [`RALPH.md`](https://github.com/ptemark/PersonalWebsite/blob/main/RALPH.md) in this repo for the complete loop specification used to drive the agent.

---

## Development

```bash
npm install       # Install dependencies
npm start         # Start dev server with live reload
npm run build     # Production build → dist/
```
