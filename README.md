# Semyon Morgunov

I build small, useful tools around privacy, monitoring and security — and ship them. Most of the projects below are live and maintained; the table says which are open source and when each was last updated.

[Claude Code](https://claude.com/claude-code) writes the code; the decisions are mine: what to build and what not to, what the product says, what leaves the server and what gets merged.

[s.morgunov.tech](https://s.morgunov.tech/en/) · [LinkedIn](https://www.linkedin.com/in/semyon-morgunov/) · s@morgunov.tech · Tashkent

## Projects

<!-- projects:start -->
| Project | What it does | For whom | Code | Updated |
|---|---|---|---|---|
| **[TofsDevOps](https://github.com/morgunovtech/Tofs_DevOps_bot)** | Your personal DevOps in Telegram: uptime, SSL, DNS, broken links, search and AI-assistant visibility. Fixes what it can and stays quiet while everything is fine. | Owners of small sites and pet projects without a DevOps person | [Open source](https://github.com/morgunovtech/Tofs_DevOps_bot) · MIT | 2026‑11‑25 |
| **[Found You](https://foundyou.morgunov.tech/en/)** | Shows what a photo gives away before you post it — EXIF, GPS, place context — and makes a clean copy. The photo never leaves your browser. | Anyone who shares photos online | [Open source](https://github.com/morgunovtech/FoundYou) · MIT | 2026‑11‑25 |
| **[Fingerprint](https://fprint.morgunov.tech/en/)** | Online privacy in six steps, from opening your laptop to a loaded site: who learns what about you at each step, shown on your real data, and what to do about it. | Non-technical people who want to see who learns what about them online | [Open source](https://github.com/morgunovtech/Fingerprint) · MIT | 2026‑11‑25 |
| **[Social Tracker Bot](https://github.com/morgunovtech/social-tracker-bot)** | Self-hosted Telegram bot for your social accounts: followers on Telegram, YouTube, Instagram and LinkedIn, the life of your channel, account security alerts and a weekly reputation report. | Creators and professionals growing an audience | [Open source](https://github.com/morgunovtech/social-tracker-bot) · MIT | 2026‑11‑25 |
| **[morgunov.tech](https://s.morgunov.tech/en/)** | My site: zero-build pages, an edge CMS on Cloudflare Pages, KV and R2, and the design system the other projects share. | People who want to know who I am or work with me | [Open source](https://github.com/morgunovtech/about-me-page) · MIT | 2026‑11‑25 |
| **Lenses** | CLI that audits a person's public digital footprint through six perception lenses. | People checking how they look online | Closed source | 2026‑11‑25 |
<!-- projects:end -->

<sub>The Updated column refreshes itself every day from the GitHub API for the open-source rows; the closed-source row is updated by hand.</sub>

## How I build

- **Silent when healthy.** My tools speak up only when something needs you, and every alert says what to do next.
- **Privacy by default.** Nothing leaves your device unless the feature can't work otherwise, and the README says exactly what does.
- **Small stacks.** Python and Telegram for bots that run on their own; vanilla JS or TypeScript on Cloudflare for the web; SQLite at most.
- **Shipped properly.** Every repository has CI, Dependabot and secret scanning, and every change goes through a pull request.

The long version, with links to the pull requests behind each point: [HOW-I-BUILD.md](HOW-I-BUILD.md) · [по-русски](HOW-I-BUILD.ru.md).
