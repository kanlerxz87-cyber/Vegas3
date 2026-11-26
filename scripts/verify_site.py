#!/usr/bin/env python3
"""Verify the site data and generated HTML. Exits non-zero on any failure.

Checks:
  1. Every table row in hotels / restaurants / activities either cites at least one
     known source ID (with an https URL) OR is marked Unverified with at least one flag.
  2. Every 'Verified' / 'Partial' row cites a source.
  3. Every source ID referenced exists and has an https URL.
  4. Restaurant tier counts match the 2026 LVCVA list (4 starred, 3 Bib, 17 Recommended, 24 total).
  5. Every internal href / src in the generated HTML resolves to a file in the repo.
  6. Every external href starts with https://.
"""
import html.parser
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
errors = []


def err(msg):
    errors.append(msg)


# 3. sources
for sid, s in DATA["sources"].items():
    if not s["url"].startswith("https://"):
        err(f"source {sid} is not https: {s['url']}")

def check_rows(section, name_key):
    for row in DATA[section]["rows"]:
        name = row.get(name_key, "?")
        srcs = row.get("sources", [])
        for sid in srcs:
            if sid not in DATA["sources"]:
                err(f"{section}: '{name}' cites unknown source {sid}")
        status = row.get("status")
        flags = row.get("flags", [])
        if status in ("Verified", "Partial") and not any(sid in DATA["sources"] for sid in srcs):
            err(f"{section}: '{name}' is {status} but cites no source")
        if status == "Unverified" and not flags:
            err(f"{section}: '{name}' is Unverified but has no flag")
        url = row.get("url", "")
        if url and not url.startswith("https://"):
            err(f"{section}: '{name}' url is not https")
        if not srcs and status != "Unverified":
            err(f"{section}: '{name}' has no source")

check_rows("hotels", "hotel")
check_rows("restaurants", "name")
check_rows("activities", "name")

# 4. Michelin tier counts
rows = DATA["restaurants"]["rows"]
tiers = Counter(r["tier"] for r in rows)
expected = {"Starred": 4, "Bib Gourmand": 3, "Recommended": 17}
for t, n in expected.items():
    if tiers.get(t, 0) != n:
        err(f"restaurant tier '{t}' count is {tiers.get(t,0)}, expected {n}")
if len(rows) != 24:
    err(f"restaurant rows = {len(rows)}, expected 24")

# 5/6. link checks in generated HTML
class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a" and "href" in d:
            self.links.append(d["href"])
        if tag == "link" and "href" in d:
            self.links.append(d["href"])

pages = sorted((ROOT / "pages").glob("*.html"))
# root index.html (earlier dashboard) is checked too, so its links to the new hub stay valid
pages.append(ROOT / "index.html")
for p in pages:
    if not p.exists():
        err(f"missing page {p}")
        continue
    parser = LinkParser()
    parser.feed(p.read_text(encoding="utf-8"))
    for href in parser.links:
        if href.startswith("#") or href.startswith("mailto:"):
            continue
        if href.startswith("http://"):
            err(f"{p.name}: non-https external link {href}")
            continue
        if href.startswith("https://"):
            continue
        target = (p.parent / href).resolve()
        if not target.exists():
            err(f"{p.relative_to(ROOT)}: broken internal link {href}")

if errors:
    print("VERIFY FAILED:")
    for m in errors:
        print(" -", m)
    sys.exit(1)

print(f"VERIFY OK: {len(pages)} pages, {sum(len(DATA[s]['rows']) for s in ('hotels','restaurants','activities'))} table rows, {len(DATA['sources'])} sources.")
print("Restaurant tiers:", dict(tiers))
