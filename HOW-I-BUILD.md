# How I build products with AI

🇷🇺 [По-русски](HOW-I-BUILD.ru.md)

The code in my repositories is written by Claude Code. The decisions are mine: what to build and what not to, the words the product says to a person, what leaves the server, what gets merged into `main`, what gets thrown out. Below is how that works in practice, with links to specific pull requests: it can be checked rather than taken on trust.

The products are for myself so far: I close my own tasks and my own risks. They are open source because that costs nothing. I will sell when there is a signal that someone else needs them; there is none yet, and I am not inventing one.

## Who does what

- **I** state the task, choose what goes into a release, read every screen and every alert as the user would, decide what stays and what goes, check the result on the live bot and in its logs.
- **The agent** writes the code, the tests, the first draft of the docs.
- Review happens in the session with the agent. The pull request on GitHub is the record of the decision and the CI run, not the place for discussion: there are no comments in the PRs because they happened before the PR. These projects have no independent reviewer. That is a known gap; see the last section.

## The rules live apart from the code

- All my Telegram bots follow one file of principles, kept outside the repositories. Each repository carries the short version ([CONTRIBUTING, "Principles"](https://github.com/morgunovtech/social-tracker-bot/blob/main/CONTRIBUTING.md#principles); [DEVELOPMENT, «Принципы»](https://github.com/morgunovtech/Tofs_DevOps_bot/blob/main/docs/DEVELOPMENT.md#принципы)). A principle changes in that file first, then in the code.
- The repositories the agent works in most carry a `CLAUDE.md` (both bots also an `AGENTS.md` for other agents): only what an agent needs to know before changing anything — commands, conventions, what not to do. Every product's history lives in its `CHANGELOG.md`, not there.
- A new project starts from a template (a private repository): a README with the table of what the project creates outside the repo, `CLAUDE.md` and `AGENTS.md`, CI with secret scanning, Dependabot.

## How I state a task

- Not "make it good" but a numbered list. One commit per item, so any item rolls back with one `git revert`. The PR description has a section "what to check before merging": what changes for someone already running the bot. Example: [audit, phase A, 10 P0 items](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/45).
- Big work is cut into phases in a fixed order: first what loses alerts and secrets ([A](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/45)), then the bot's self-checks ([B](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/46), [B2](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/47)), then outgoing requests and third parties ([C](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/48), [C2](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/49), [C3](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/50)), texts and screens last ([D](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/51)).
- My instruction goes into the PR verbatim, so it is visible where a decision came from: ["pull the menu buttons out of the hamburger menu and make them primary"](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/42).
- A code review is a recurring kind of PR, not a one-off: [#17](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/17), [#62](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/62), [1.4.0](https://github.com/morgunovtech/social-tracker-bot/pull/50).

## An incident becomes a rule, the rule becomes a test

| What happened | What changed | Where |
|---|---|---|
| The image on a new Python did not build on Railway; the bot ran the old version for two days and said nothing | The image build is a required CI check; once an hour the bot compares its build with `main` and says "the new version did not start" | [#15](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/15) |
| GitHub had an incident and answered 504 to anonymous requests; the bot called a link to it broken | 5xx and timeouts count as broken only when they hold for three hours | [#29](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/29) |
| The output schema for the Claude API had `minimum`/`maximum`, which the API refuses; after the release not one comment was checked — seen in the Railway logs | The bounds moved into the code; before a release, one real request to the API, which no fake replaces | [#49](https://github.com/morgunovtech/social-tracker-bot/pull/49), [`test_classifier_live.py`](https://github.com/morgunovtech/social-tracker-bot/blob/main/tests/test_classifier_live.py) |
| The README named screens the bot no longer had | `test_docs.py`: links lead somewhere, screens are named as in the code, `cp .env.example .env` changes nothing but the token | [`tests/test_docs.py`](https://github.com/morgunovtech/Tofs_DevOps_bot/blob/main/tests/test_docs.py) |
| Jargon crept back into the help screen | A test for words the user is not expected to know | [#26](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/26) |
| The lock file fell behind `requirements.in` | A test that catches it | [`tests/test_build.py`](https://github.com/morgunovtech/Tofs_DevOps_bot/blob/main/tests/test_build.py) |

## What the product says and what it does not promise

- Silent while everything is fine. An alert only when a state changes, once until it recovers; the recovery is one message with how long it was down.
- Two levels of urgency and one dictionary of icons across every screen and message; the icon always matches the delivery: 🔴 rings, 🟠 arrives silently ([#8](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/8), [#34](https://github.com/morgunovtech/social-tracker-bot/pull/34)).
- Numbers, not adjectives: "0.12 s", not "fast"; "down for 12 min", not "99.9 %".
- What cannot be measured from outside is named as such: for sites behind Cloudflare the bot does not say "AI crawlers can see you", it shows where to check that in the dashboard ([#41](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/41)); no CrUX data for a small site is not an error; the LinkedIn scraping risk is in the README next to the instructions.
- Silence must not lie: an undelivered message is repeated with a mark, the bot's own downtime is not counted as a site's, a test alert is offered after the first site ([#24](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/24)).

## Automation only after labels

- Comment moderation: the bot sends a card with buttons and deletes nothing itself. The owner's taps are labels; they build an accuracy table, and only on that table can any automatic action be calibrated ([#43](https://github.com/morgunovtech/social-tracker-bot/pull/43)).
- Everything the bot does on its own (redeploy, container restart, disk cleanup) is visible in the chat, switched off there, and logged ([FEATURES, "Self-healing"](https://github.com/morgunovtech/Tofs_DevOps_bot/blob/main/docs/FEATURES.en.md)).

## What leaves the server and what is left after deletion

- Each bot's README has a table of data recipients: where, what, when, how to switch it off. Internal addresses go nowhere ([TofsDevOps](https://github.com/morgunovtech/Tofs_DevOps_bot/blob/main/README.md#what-leaves-your-server), [Social Tracker](https://github.com/morgunovtech/social-tracker-bot/blob/main/README.md#privacy)).
- A table of what the project creates outside the repository — bots, keys, volumes, DNS — and how to remove each. Without it a project cannot be deleted completely.
- Everything that names a person has a retention period: joins and leaves 90 days, comment verdicts 30 ([1.4.0](https://github.com/morgunovtech/social-tracker-bot/pull/50)).

## Removing is as easy as adding

- My own page-speed measurement on the visitor's side: built ([#39](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/39)) and removed the same day in favour of Google's data ([#40](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/40)) — my number added nothing to theirs.
- The "Export" and "Import" buttons are gone; the backup is made by itself, restoring is sending the file back ([#34](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/34)).
- The "updates available" message is gone: updates install themselves, there is nothing to report ([#15](https://github.com/morgunovtech/Tofs_DevOps_bot/pull/15)).

## What is not here

- Users other than me, and usage metrics. The products are for myself so far; the audience in the README is a hypothesis not yet tested by a single conversation.
- Independent review. The same agent writes and checks the code, so the blind spots coincide; mistakes like [#49](https://github.com/morgunovtech/social-tracker-bot/pull/49) are caught only by a live test and the logs.
- Continuous work. These are sessions every week or two, ten to twenty PRs a day.
- Short documentation. The tests keep it honest, not short.
