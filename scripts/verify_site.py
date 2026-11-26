#!/usr/bin/env python3
"""Verify the data and the built site.

Checks:
  1. Every data row (restaurants, hotels, activities, transit, questions, flagged, repo review)
     cites at least one source ID that exists in sources.json, and that source has an https URL.
  2. Every row with a website/URL field uses https.
  3. Every internal link in docs/*.html resolves to a file in docs/.
  4. Every external link in docs/*.html is either a source URL or a URL that appears in the data.
  5. Counts of blank (unverified) fields are reported, not filled in.
Exit code is non-zero if any check fails.
"""
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

errors = []
warnings = []


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


src_doc = load("sources.json")
SOURCES = {s["id"]: s for s in src_doc["sources"]}
known_urls = {s["url"] for s in src_doc["sources"]}

for sid, s in SOURCES.items():
    if not s["url"].startswith("https://"):
        errors.append(f"source {sid} URL is not https: {s['url']}")


def check_src(label, ids):
    if not ids:
        errors.append(f"{label}: no source cited")
        return
    for sid in ids:
        if sid not in SOURCES:
            errors.append(f"{label}: cites unknown source {sid}")


data_urls = set()

# restaurants
rest = load("restaurants.json")["rows"]
blank_counts = {}
for r in rest:
    check_src(f"restaurant '{r['name']}'", r["src"])
    if not r["website"].startswith("https://"):
        errors.append(f"restaurant '{r['name']}': website missing or not https")
    data_urls.add(r["website"])
    for s in r["social"]:
        data_urls.add(s["url"])
        if not s["url"].startswith("https://"):
            errors.append(f"restaurant '{r['name']}': social link not https")
    for k in ("address", "hours", "price_couple", "reservations", "cuisine", "area", "property"):
        if not str(r.get(k, "")).strip():
            blank_counts[k] = blank_counts.get(k, 0) + 1
print(f"restaurants: {len(rest)} rows; blank counts {blank_counts}")
if len(rest) != 24:
    errors.append(f"restaurants: expected 24 Las Vegas distinctions, found {len(rest)}")
stars = [r for r in rest if r["status"].startswith(("1 ", "2 "))]
bibs = [r for r in rest if r["status"] == "Bib Gourmand"]
recs = [r for r in rest if r["status"] == "Michelin Recommended"]
print(f"  starred {len(stars)}, bib {len(bibs)}, recommended {len(recs)}")
if (len(stars), len(bibs), len(recs)) != (4, 3, 17):
    errors.append("restaurants: category counts differ from CVA list (expected 4 / 3 / 17)")

# hotels
hotels = load("hotels.json")["rows"]
for h in hotels:
    check_src(f"hotel '{h['name']}'", h["src"])
    if not h["url"].startswith("https://"):
        errors.append(f"hotel '{h['name']}': url not https")
    data_urls.add(h["url"])
    if h["rate_7_nights_total"]:
        if not h.get("rate_checked_date"):
            errors.append(f"hotel '{h['name']}': a rate is present without a check date")
print(f"hotels: {len(hotels)} rows")

# activities + transit
acts = load("activities.json")
for a in acts["activities"]:
    check_src(f"activity '{a['name']}'", a["src"])
    if not a["url"].startswith("https://"):
        errors.append(f"activity '{a['name']}': url not https")
    data_urls.add(a["url"])
for t in acts["transit"]:
    check_src(f"transit '{t['item']}'", t["src"])
print(f"activities: {len(acts['activities'])}; transit items: {len(acts['transit'])}")

# booking facts
for f in load("booking.json")["booking_timing_facts"]:
    check_src(f"booking fact '{f['fact'][:40]}'", f["src"])

# Q&A
qa = load("qa.json")
for a in qa["answered"]:
    if a["src"]:
        check_src(f"answered Q '{a['q'][:40]}'", a["src"])
    else:
        errors.append(f"answered Q without source: {a['q']}")

# flagged, repo review (flagged item sources may be empty only for date-only items)
for i in load("flagged.json")["items"]:
    for sid in i["src"]:
        if sid not in SOURCES:
            errors.append(f"flagged {i['id']}: unknown source {sid}")
    if not i["src"] and i["area"] != "Dates":
        errors.append(f"flagged {i['id']}: no source")

# ---- built site checks ----
pages = sorted(DOCS.glob("*.html"))
if not pages:
    errors.append("docs/ has no HTML pages. Run scripts/build_site.py first.")


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.hrefs.append(v)


allowed_external = known_urls | data_urls
external_seen = set()
# Root dashboard (index.html, shared with the other session) is checked too.
# Its external links are reviewed on the Flagged page (F-24) rather than auto-approved.
root_index = ROOT / "index.html"
check_pages = [(p, DOCS) for p in pages]
if root_index.exists():
    check_pages.append((root_index, ROOT))
for p, base in check_pages:
    parser = LinkParser()
    parser.feed(p.read_text(encoding="utf-8"))
    for href in parser.hrefs:
        if href.startswith("#"):
            continue
        if href.startswith(("http://", "https://")):
            external_seen.add(href)
            if p == root_index:
                continue
            if href not in allowed_external:
                errors.append(f"{p.name}: external link not in sources or data: {href}")
            if href.startswith("http://"):
                errors.append(f"{p.name}: insecure http link: {href}")
            continue
        target = href.split("#")[0]
        if target == "":
            continue
        if not (base / target).exists():
            errors.append(f"{p.relative_to(ROOT)}: broken internal link -> {href}")

print(f"built pages: {len(pages)}; unique external links: {len(external_seen)}")
for w in warnings:
    print("WARN", w)
if errors:
    print(f"FAILED with {len(errors)} problem(s):")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK: every row cites a source; all internal links resolve; all external links are sourced.")
