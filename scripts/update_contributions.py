#!/usr/bin/env python3
"""Rewrite the contributions section of README.md from GitHub.

Searches every pull request and issue AUTHOR opened in PROJECTS, so a new one appears on the
next run with no list to edit. Merged and open (including draft) pull requests are shown; ones
closed without merging are left out. Issues (bug reports) are shown open or fixed; ones closed as
not planned or as duplicates are left out. labels.json can give any pull request or issue a short
description; without one, its upstream title is shown with leading tags like "[Bugfix]" or
"fix(x):" dropped. Only the text between the two markers in README.md is replaced.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

AUTHOR = "divyvasal"
PROJECTS = [  # (display name, repo), in the order they appear
    ("vLLM", "vllm-project/vllm"),
    ("SGLang", "sgl-project/sglang"),
    ("LMCache", "LMCache/LMCache"),
    ("FlashInfer", "flashinfer-ai/flashinfer"),
]
START, END = "<!-- contributions:start -->", "<!-- contributions:end -->"
ROOT = Path(__file__).resolve().parent.parent
ICON = {"merged": "🟣", "open": "🟢", "draft": "⚪"}
ORDER = {"merged": 0, "open": 1, "draft": 2}
ISSUE_ICON = {"fixed": "✅", "open": "🐞"}  # an issue AUTHOR reported: open, or resolved
ISSUE_ORDER = {"open": 0, "fixed": 1}


def search(repo: str, kind: str = "pr") -> list[dict]:
    q = f"is:{kind} author:{AUTHOR} repo:{repo}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": q, "per_page": 100})
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": f"{AUTHOR}-profile"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get("incomplete_results"):
        raise SystemExit(f"GitHub returned incomplete results for {repo}; not rewriting")
    return data["items"]


def clean(title: str) -> str:
    t = re.sub(r"^(\s*\[[^\]]*\])+\s*", "", title)          # [Bugfix][MP]
    t = re.sub(r"^\s*[a-z]+(\([^)]*\))?!?:\s*", "", t)       # fix(mp):
    t = re.sub(r"^\s*:\s*", "", t)                           # [Bug]: left a colon
    return t[:1].upper() + t[1:]


def state(item: dict) -> str | None:
    if (item.get("pull_request") or {}).get("merged_at"):
        return "merged"
    if item["state"] == "open":
        return "draft" if item.get("draft") else "open"
    return None  # closed without merging


def issue_state(item: dict) -> str | None:
    if item["state"] == "open":
        return "open"
    if item.get("state_reason") == "completed":
        return "fixed"
    return None  # closed as not planned, or a duplicate


def render(labels: dict) -> str:
    rows, merged, opened, reported = [], 0, 0, 0
    for name, repo in PROJECTS:
        prs = [(s, it) for it in search(repo) if (s := state(it))]
        issues = [(s, it) for it in search(repo, "issue") if (s := issue_state(it))]
        if not prs and not issues:
            continue
        prs.sort(key=lambda p: (ORDER[p[0]], -int(p[1]["number"])))
        issues.sort(key=lambda p: (ISSUE_ORDER[p[0]], -int(p[1]["number"])))
        m = sum(1 for s, _ in prs if s == "merged")
        merged += m
        opened += len(prs) - m
        reported += len(issues)
        counts = f"{m} merged · {len(prs) - m} open" + (f" · {len(issues)} reported" if issues else "")
        rows.append(f"**{name}** <sub>· {counts}</sub>  ")
        for s, it in prs:
            key = f"{repo}#{it['number']}"
            text = labels.get(key) or clean(it["title"])
            rows.append(f"{ICON[s]} [#{it['number']}]({it['html_url']}) {text}  ")
        for s, it in issues:
            key = f"{repo}#{it['number']}"
            text = labels.get(key) or clean(it["title"])
            rows.append(f"{ISSUE_ICON[s]} [#{it['number']}]({it['html_url']}) {text}  ")
        rows.append("")
    head = f"#### Open-source contributions · {merged} merged · {opened} open · {reported} reported\n"
    foot = ("<sub>🟣 merged · 🟢 open · ⚪ draft · 🐞 issue reported · ✅ issue resolved · "
            "updated automatically every day</sub>")
    return head + "\n" + "\n".join(rows) + "\n" + foot


def main() -> int:
    labels = json.loads((ROOT / "labels.json").read_text())
    readme = ROOT / "README.md"
    text = readme.read_text()
    if START not in text or END not in text:
        raise SystemExit("README.md is missing the contributions markers")
    new = text.split(START)[0] + START + "\n" + render(labels) + "\n" + END + text.split(END, 1)[1]
    if new != text:
        readme.write_text(new)
        print("README.md updated")
    else:
        print("no change")
    return 0


if __name__ == "__main__":
    sys.exit(main())
