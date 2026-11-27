# Semyon Morgunov

I build small, useful tools around privacy, monitoring and security. Most of the projects below are live and maintained; the table says which are open source and when each was last updated.

[Claude Code](https://claude.com/claude-code) writes the code; the product decisions are mine.

[s.morgunov.tech](https://s.morgunov.tech/en/) · [LinkedIn](https://www.linkedin.com/in/semyon-morgunov/) · s@morgunov.tech · Tashkent

## Projects

<!-- projects:start -->
| Project | What it does | For whom | Code | Updated |
|---|---|---|---|---|
| **[TofsDevOps](https://github.com/morgunovtech/Tofs_DevOps_bot)** | Website monitoring for people who have never heard of DNS or a 502. If your site goes down, its certificate is about to expire or search engines and AI assistants stop seeing it, the bot tells you first and explains in plain words what to do. It fixes what it can and stays quiet while all is well. | Owners of small sites and pet projects without a DevOps person | [Open source](https://github.com/morgunovtech/Tofs_DevOps_bot) · MIT | 2026‑11‑27 |
| **[Found You](https://foundyou.morgunov.tech/en/)** | Before you post a photo, see what it gives away: the place, the time, your phone and the people in it. The app makes a clean copy, and the file never leaves your device. | Anyone who shares photos online | [Open source](https://github.com/morgunovtech/FoundYou) · MIT | 2026‑11‑27 |
| **[Fingerprint](https://fprint.morgunov.tech/en/)** | What gets learned about you while a website opens: six steps from switching on your laptop to a loaded page, on your real data and in plain words — and what to do at each step. | Non-technical people who want to see who learns what about them online | [Open source](https://github.com/morgunovtech/Fingerprint) · MIT | 2026‑11‑27 |
| **[Social Tracker Bot](https://github.com/morgunovtech/social-tracker-bot)** | Your followers on Telegram, YouTube, Instagram and LinkedIn in one weekly report. The bot warns you at once if someone tries to take over an account or a comment appears that can get your group blocked. It stays quiet while all is well. | Creators and professionals growing an audience | [Open source](https://github.com/morgunovtech/social-tracker-bot) · MIT | 2026‑11‑27 |
| **[morgunov.tech](https://s.morgunov.tech/en/)** | My site: zero-build pages, an edge CMS on Cloudflare Pages, KV and R2, and the design system the other projects share. | People who want to know who I am or work with me | [Open source](https://github.com/morgunovtech/about-me-page) · MIT | 2026‑11‑27 |
| **Lenses** | CLI that audits a person's public digital footprint through six perception lenses. | People checking how they look online | Closed source | 2026‑11‑25 |
<!-- projects:end -->

<sub>The Updated column refreshes itself every day from the GitHub API for the open-source rows; the closed-source row is updated by hand.</sub>

## How I build

- **Silent when healthy.** My tools speak up only when something needs you, and every alert says what to do next.
- **Privacy by default.** Nothing leaves your device unless the feature can't work otherwise, and the README says exactly what does.
- **Small stacks.** Python and Telegram for bots that run on their own; vanilla JS or TypeScript on Cloudflare for the web; SQLite at most.
- **Shipped properly.** Every repository has CI, Dependabot and secret scanning, and every change goes through a pull request.

The long version, with links to the pull requests behind each point: [HOW-I-BUILD.md](HOW-I-BUILD.md) · [по-русски](HOW-I-BUILD.ru.md).
