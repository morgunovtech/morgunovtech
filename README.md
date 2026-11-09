# Semyon Morgunov

I build small, useful tools around privacy, monitoring and security — and ship them. Every project below is live, deployed and maintained, most of them in the open.

I design the products and write the code with [Claude Code](https://claude.com/claude-code) as my pair programmer.

[s.morgunov.tech](https://s.morgunov.tech) · [LinkedIn](https://www.linkedin.com/in/semyon-morgunov/) · s@morgunov.tech · Tashkent

## Projects

<!-- projects:start -->
| Project | What it does | For whom | Code | Updated |
|---|---|---|---|---|
| **[TofsDevOps](https://github.com/morgunovtech/Tofs_DevOps_bot)** | Your personal DevOps in Telegram: uptime, SSL, DNS, broken links, search and AI-assistant visibility. Fixes what it can and stays quiet while everything is fine. | Owners of small sites and pet projects without a DevOps person | [Open source](https://github.com/morgunovtech/Tofs_DevOps_bot) · MIT | 2026‑11‑09 |
| **[Found You](https://foundyou.morgunov.tech)** | Shows what a photo gives away before you post it — EXIF, GPS, place context — and makes a clean copy. The photo never leaves your browser. | Anyone who shares photos online | [Open source](https://github.com/morgunovtech/FoundYou) · MIT | 2026‑11‑03 |
| **[Fingerprint](https://fprint.morgunov.tech)** | Shows what any website learns about you the moment you open it, how unique your browser is, and how to hide. | People who want to see how they are tracked | [Open source](https://github.com/morgunovtech/Fingerprint) · MIT | 2026‑11‑07 |
| **[Good Pass](https://good-pass.pages.dev)** | Explains password strength: entropy, crack time, a k-anonymous breach check, a generator and a memory trainer. | Anyone who wants better passwords without a lecture | [Open source](https://github.com/morgunovtech/good-pass) · MIT | 2026‑11‑03 |
| **[Social Tracker Bot](https://github.com/morgunovtech/social-tracker-bot)** | Telegram bot that tracks followers on Telegram, YouTube and LinkedIn: weekly reports, trends, forecasts and alerts. | Creators and professionals growing an audience | [Open source](https://github.com/morgunovtech/social-tracker-bot) · MIT | 2026‑11‑09 |
| **[morgunov.tech](https://s.morgunov.tech)** | My site: zero-build pages, an edge CMS on Cloudflare Pages, KV and R2, and the design system the other projects share. | People who want to know who I am or work with me | [Open source](https://github.com/morgunovtech/about-me-page) · MIT | 2026‑11‑03 |
| **Lenses** | CLI that audits a person's public digital footprint through six perception lenses. | People checking how they look online | Closed source | 2026‑11‑03 |
| **[LatteDrop](https://github.com/morgunovtech/LatteDrop)** | Beat-accurate music visualizer for macOS in the spirit of MilkDrop. Specification stage. | Me — a personal tool, built in the open | [Open source](https://github.com/morgunovtech/LatteDrop) · MIT | 2026‑11‑03 |
<!-- projects:end -->

<sub>The Updated column refreshes itself every day from the GitHub API.</sub>

## How I build

- **Silent when healthy.** My tools speak up only when something needs you, and every alert says what to do next.
- **Privacy by default.** Nothing leaves your device unless the feature can't work otherwise, and the README says exactly what does.
- **Small stacks.** Python and Telegram for bots that run on their own; vanilla JS or TypeScript on Cloudflare for the web; SQLite at most.
- **Shipped properly.** Every repository has CI, Dependabot and secret scanning, and every change goes through a pull request.
