#!/usr/bin/env python3
"""Rebuild the projects table in README.md from projects.json and the GitHub API.

projects.json holds what a person writes (name, link, what it does, who it is
for); GitHub supplies what changes (open or closed source, licence, last push).
The table sits between <!-- projects:start --> and <!-- projects:end -->.

Token: GITHUB_TOKEN (or PROFILE_TOKEN) from the environment. A token that cannot
see a private repo leaves that row's last date as it was, so a scheduled run
with the default Actions token does not erase what a local run filled in.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = os.environ.get("PROFILE_OWNER", "morgunovtech")
START, END = "<!-- projects:start -->", "<!-- projects:end -->"


def graphql(query: str, token: str) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-readme"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch(repos: list[str], token: str) -> dict[str, dict | None]:
    parts = [
        f'r{i}: repository(owner: "{OWNER}", name: "{name}") '
        "{ isPrivate pushedAt licenseInfo { spdxId } }"
        for i, name in enumerate(repos)
    ]
    data = graphql("query { " + " ".join(parts) + " }", token).get("data") or {}
    return {name: data.get(f"r{i}") for i, name in enumerate(repos)}


def previous_dates(readme: str) -> dict[str, str]:
    """Last dates already in the table, keyed by project name."""
    dates = {}
    for line in readme.splitlines():
        m = re.match(r"\| \*\*\[?([^\]|*]+)\]?.*\| (\d{4}[-‑]\d{2}[-‑]\d{2}|—) \|$", line)
        if m:
            dates[m.group(1).strip()] = m.group(2)
    return dates


def render(projects: list[dict], info: dict, old: dict[str, str]) -> str:
    rows = [
        "| Project | What it does | For whom | Code | Updated |",
        "|---|---|---|---|---|",
    ]
    for p in projects:
        repo = info.get(p["repo"])
        name = f"[{p['name']}]({p['url']})" if p["url"] else p["name"]
        if repo and not repo["isPrivate"]:
            lic = (repo.get("licenseInfo") or {}).get("spdxId") or "no licence"
            code = f"[Open source]({'https://github.com/' + OWNER + '/' + p['repo']}) · {lic}"
        else:
            code = "Closed source"
        # Non-breaking hyphens keep the date on one line in a narrow column.
        updated = repo["pushedAt"][:10].replace("-", "\u2011") if repo else old.get(p["name"], "—")
        rows.append(f"| **{name}** | {p['what']} | {p['for']} | {code} | {updated} |")
    return "\n".join(rows)


def main() -> int:
    token = os.environ.get("PROFILE_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("set GITHUB_TOKEN (or PROFILE_TOKEN)", file=sys.stderr)
        return 1
    projects = json.loads((ROOT / "projects.json").read_text())
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()
    if START not in readme or END not in readme:
        print(f"README.md has no {START} … {END} block", file=sys.stderr)
        return 1
    info = fetch([p["repo"] for p in projects], token)
    table = render(projects, info, previous_dates(readme))
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{table}\n{END}{tail}"
    if new != readme:
        readme_path.write_text(new)
        print("README.md updated")
    else:
        print("README.md unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
