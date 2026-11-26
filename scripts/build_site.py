#!/usr/bin/env python3
"""Build the static GitHub Pages site in docs/ from data/*.json.

Stdlib only. Blank data values are rendered as 'Unverified' and are never filled in.
Run: python3 scripts/build_site.py
"""
import html
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return json.load(f)


SOURCES = {s["id"]: s for s in load("sources.json")["sources"]}
ACCESSED = load("sources.json")["accessed"]

NAV = [
    ("index.html", "Home"),
    ("hotels.html", "Hotels"),
    ("restaurants.html", "Michelin restaurants"),
    ("activities.html", "Activities & transit"),
    ("booking.html", "Dates & booking"),
    ("questions.html", "Questions"),
    ("suggestions.html", "Suggestions"),
    ("flagged.html", "Flagged for Review"),
    ("sources.html", "Sources"),
    ("repo-review.html", "Repo review"),
]


def e(value):
    return html.escape(str(value)) if value is not None else ""


def unv(text=""):
    """Blank or unknown value. Rendered as an explicit unverified marker."""
    if text is None or str(text).strip() == "":
        return '<span class="unv">Unverified</span>'
    return e(text)


def src_links(ids):
    if not ids:
        return '<span class="unv">No source</span>'
    parts = []
    for sid in ids:
        s = SOURCES.get(sid)
        if s is None:
            parts.append(f'<span class="unv">{e(sid)} missing</span>')
        else:
            parts.append(
                f'<a href="{e(s["url"])}" target="_blank" rel="noopener" title="{e(s["title"])}">{e(sid)}</a>'
            )
    return ", ".join(parts)


def link(url, label=None):
    if not url:
        return unv("")
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label or url)}</a>'


def social_cell(items):
    if not items:
        return unv("")
    return "<br>".join(
        f'<a href="{e(i["url"])}" target="_blank" rel="noopener">{e(i["platform"])}</a>' for i in items
    )


def table(headers, rows, cls="data"):
    """rows: list of lists of pre-rendered HTML strings. Mobile: each cell gets data-label."""
    th = "".join(f"<th>{e(h)}</th>" for h in headers)
    body = []
    for r in rows:
        tds = "".join(f'<td data-label="{e(headers[i])}">{c}</td>' for i, c in enumerate(r))
        body.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="table-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead>'
        f"<tbody>{''.join(body)}</tbody></table></div>"
    )


def nav_html(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<a href="{href}"{cur}>{e(label)}</a>')
    return "<nav class=\"nav\">" + "".join(items) + "</nav>"


def page(filename, title, body, intro=""):
    flagged_banner = ""
    if filename != "flagged.html":
        flagged_banner = (
            '<div class="banner">Flagged items (unverified or conflicting data) are listed on '
            '<a href="flagged.html">Flagged for Review</a>.</div>'
        )
    content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Las Vegas Trip Planner</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top">
  <a class="brand" href="index.html">Las Vegas Trip Planner</a>
  <span class="asof">Data as of {e(ACCESSED)}</span>
</header>
{nav_html(filename)}
<main>
<h1>{e(title)}</h1>
{('<p class="intro">' + intro + '</p>') if intro else ''}
{flagged_banner}
{body}
</main>
<footer>
<p>Every table row links to an official source. Blank cells show <span class="unv">Unverified</span> and are not estimated.
Verify before you book. Sources are listed on the <a href="sources.html">Sources</a> page.</p>
</footer>
</body>
</html>
"""
    (DOCS / filename).write_text(content, encoding="utf-8")


def render_index():
    summary = load("summary.json")
    flagged = load("flagged.json")["items"]
    stat_html = []
    stats = [
        ("24", "Las Vegas Michelin distinctions (2026)"),
        ("4", "Michelin-starred restaurants"),
        ("8", "Hotels on shortlist"),
        (str(len(flagged)), "Flagged items for review"),
    ]
    for num, label in stats:
        stat_html.append(f'<div class="stat"><div class="num">{e(num)}</div><div>{e(label)}</div></div>')
    points = "".join(
        f'<tr><td data-label="Topic"><strong>{e(p["label"])}</strong></td><td data-label="Summary">{e(p["value"])}</td></tr>'
        for p in summary["points"]
    )
    cards = []
    card_info = [
        ("hotels.html", "Hotels", "Shortlist ranked by Michelin restaurants on property. Prices pending."),
        ("restaurants.html", "Michelin restaurants", "All 24 Las Vegas distinctions with status, hours and sources."),
        ("activities.html", "Activities & transit", "Red Rock, Valley of Fire, Lake Mead, Hoover Dam, plus transit notes."),
        ("booking.html", "Dates & booking", "Date options for Feb 15-18 2027 and 7-night stays. Booking timing facts."),
        ("questions.html", "Questions", "What is answered and what still needs your input."),
        ("suggestions.html", "Suggestions", "Site and planning improvements. Nothing changes until you approve."),
        ("flagged.html", "Flagged for Review", "Irregularities and unverified items with source links."),
        ("sources.html", "Sources", "Every official and secondary source used, with links."),
    ]
    for href, title, desc in card_info:
        cards.append(f'<a class="card" href="{href}"><strong>{e(title)}</strong><span>{e(desc)}</span></a>')
    body = f"""
<div class="stats">{''.join(stat_html)}</div>
<h2>Executive summary</h2>
<p class="intro">{e(summary["headline"])}</p>
<div class="table-wrap"><table class="data"><thead><tr><th>Topic</th><th>Summary</th></tr></thead><tbody>{points}</tbody></table></div>
<p><strong>Next step:</strong> {e(summary["next_step"])}</p>
<h2>Pages</h2>
<div class="cards">{''.join(cards)}</div>
"""
    page("index.html", "Las Vegas Trip Planner: Dashboard", body)


def render_hotels():
    d = load("hotels.json")
    headers = ["Rank", "Hotel", "Official site", "Address", "Michelin restaurants on property", "Starred", "Michelin total",
               "7-night total", "Queen + private bath", "Source"]
    rows = []
    for h in d["rows"]:
        rows.append([
            e(h["rank"]),
            f"<strong>{e(h['name'])}</strong>",
            link(h["url"], "Official site"),
            unv(h["address"]),
            e(h["michelin_on_property"]),
            e(h["starred_count"]),
            e(h["michelin_total"]),
            unv(h["rate_7_nights_total"]),
            unv(h["queen_private_bath"]),
            src_links(h["src"]),
        ])
    body = f"""
<h2>Ranking method</h2>
<p>{e(d["description"])}</p>
<h2>Shortlist</h2>
{table(headers, rows)}
<h2>Hotel requirements status</h2>
<ul>
<li>Private bathroom and queen or larger bed: <strong>Unverified for all 8 hotels</strong> (see Flagged F-14).</li>
<li>7-night totals for Feb 15-22 2027: <strong>Unverified for all 8 hotels</strong> (see Flagged F-13).</li>
<li>Cheapest time to book: <strong>Unverified</strong>. Requires dated rate history from official booking pages.</li>
<li>Travel time under 1 hour by bus/subway: <strong>Unverified</strong>. See RTC trip planner on the Activities page.</li>
</ul>
"""
    page("hotels.html", "Hotels", body,
         intro="Eight Strip resorts that host Michelin-listed restaurants. Prices and room details are not yet verified.")


def render_restaurants():
    d = load("restaurants.json")
    headers = ["#", "Restaurant", "Michelin status (2026)", "Cuisine", "Area", "Property", "Address", "Hours",
               "Open Feb 15-18 2027", "Exceptions / notes", "Price for two (total)", "Price level", "Reservations",
               "Website", "Social (TikTok / YouTube / Instagram)", "Source"]
    rows = []
    for r in d["rows"]:
        rows.append([
            e(r["rank"]),
            f"<strong>{e(r['name'])}</strong>",
            e(r["status"]),
            unv(r["cuisine"]),
            unv(r["area"]),
            unv(r["property"]),
            unv(r["address"]),
            unv(r["hours"]),
            unv(r["open_feb_15_18_2027"]),
            unv(r["exceptions"]),
            unv(r["price_couple"]),
            unv(r["price_level"]),
            unv(r["reservations"]),
            link(r["website"], "Official site"),
            social_cell(r["social"]),
            src_links(r["src"]),
        ])
    # Summary of clusters, computed from the table itself
    counts = {}
    for r in d["rows"]:
        counts.setdefault(r["area"], 0)
        counts[r["area"]] += 1
    cluster_rows = [[e(a), e(c)] for a, c in sorted(counts.items(), key=lambda x: -x[1])]
    star_rows = [[e(r["name"]), e(r["status"]), e(r["property"] or r["area"]), e(r["hours"] or "")]
                 for r in d["rows"] if r["status"].startswith(("1 ", "2 "))]
    body = f"""
<p>{e(d["description"])}</p>
<h2>Starred restaurants (currently listed with stars)</h2>
{table(["Restaurant", "Status", "Property / area", "Hours"], star_rows)}
<h2>Clusters by area (counts from this table)</h2>
{table(["Area", "Michelin distinctions"], cluster_rows)}
<h2>All 24 Las Vegas Michelin distinctions</h2>
<p>Listed = Michelin Recommended. Bib Gourmand and Recommended restaurants are generally walk-in friendly (S01). Starred restaurants usually release tables 30 to 60 days ahead (S01).</p>
{table(headers, rows)}
"""
    page("restaurants.html", "Michelin restaurants", body,
         intro="All 24 Las Vegas distinctions in the 2026 MICHELIN Guide Southwest. Status: 1 or 2 stars, Bib Gourmand, or Recommended (Michelin 'listed').")


def render_activities():
    d = load("activities.json")
    headers = ["Activity", "Type", "Distance from Strip", "Hours", "Tickets / reservations", "Public transit",
               "Exceptions", "Feb 15-18 2027", "Official site", "Social", "Source"]
    rows = []
    for a in d["activities"]:
        rows.append([
            f"<strong>{e(a['name'])}</strong>",
            e(a["type"]),
            unv(a["distance_from_strip"]),
            unv(a["hours"]),
            unv(a["tickets_reservations"]),
            unv(a["public_transit"]),
            unv(a["exceptions"]),
            unv(a["open_feb_15_18_2027"]),
            link(a["url"], "Official site"),
            social_cell(a["social"]),
            src_links(a["src"]),
        ])
    t_headers = ["Item", "Claim", "Source type", "Status", "Source"]
    t_rows = [[e(t["item"]), e(t["claim"]), e(t["source_type"]), e(t["status"]), src_links(t["src"])] for t in d["transit"]]
    body = f"""
<p>{e(d["description"])}</p>
<h2>Activities</h2>
{table(headers, rows)}
<h2>Getting around</h2>
<p>The 1-hour test (by bus or subway) cannot be applied until RTC travel times are checked. Las Vegas has no subway (secondary source only).</p>
{table(t_headers, t_rows)}
"""
    page("activities.html", "Activities & transit", body,
         intro="Day trips with official sources. A drive or transit time appears only when an official source states it.")


def render_booking():
    d = load("booking.json")
    w = d["trip_window"]
    opts = [[e(o["label"]), e(o["check_in"]), e(o["check_out"]), e(o["nights"]), e(o["note"])] for o in d["date_options"]]
    facts = "".join(
        f"<li>{e(f['fact'])} {src_links(f['src'])}</li>" for f in d["booking_timing_facts"]
    )
    unver = "".join(f"<li>{e(u)}</li>" for u in d["unverified"])
    body = f"""
<h2>Trip window</h2>
<p>Earliest {e(w['earliest'])} to latest {e(w['latest'])}. Length {e(w['length_nights'])}. Preferred {e(w['preferred'])}.</p>
<h2>Date options</h2>
{table(["Option", "Check-in", "Check-out", "Nights", "Note"], opts)}
<h2>Booking timing (verified)</h2>
<ul>{facts}</ul>
<h2>Still unverified</h2>
<ul>{unver}</ul>
<p>Hotel prices and cheapest booking time will be added only from official booking pages, with the date and time of each check.</p>
"""
    page("booking.html", "Dates & booking", body,
         intro="Date options inside the Feb 15 to Mar 23 2027 window, plus verified booking-timing facts.")


def render_questions():
    d = load("qa.json")
    ans = [[e(a["q"]), e(a["a"]), src_links(a["src"])] for a in d["answered"]]
    opn = [[e(q["q"]), e(q["why"]), e(q["discover"]), e(q["owner"])] for q in d["open"]]
    body = f"""
<h2>Answered (verified)</h2>
{table(["Question", "Answer", "Source"], ans)}
<h2>Open (needs information before a decision)</h2>
<p>Each item says what is missing and how to find it. Items marked You need your input.</p>
{table(["Question", "Why it matters", "How to find out", "Owner"], opn)}
"""
    page("questions.html", "Questions", body,
         intro="What we know, what we still need, and how to get the missing information.")


def render_suggestions():
    d = load("suggestions.json")
    rows = [[e(s["id"]), f"<strong>{e(s['title'])}</strong>", e(s["detail"]), e(s["impact"]), e(s["effort"]),
             "Awaiting your approval" if s["needs_approval"] else "Not needed"] for s in d["items"]]
    body = f"""
<p class="banner">{e(d["status"])}</p>
{table(["ID", "Suggestion", "Detail", "Impact", "Effort", "Status"], rows)}
<p>To choose: reply with the IDs you want (for example, SG-01, SG-02). Anything not chosen stays unimplemented.</p>
"""
    page("suggestions.html", "Suggestions", body,
         intro="Proposed improvements to the site and planning process. Review and choose before any change is made.")


def render_flagged():
    d = load("flagged.json")
    rows = [[e(i["id"]), e(i["area"]), e(i["issue"]), src_links(i["src"]), e(i["action"])] for i in d["items"]]
    body = f"""
<p>{e(d["description"])}</p>
<p class="banner">Flagged items do not block the merge. Review them after the site is live and tell us what to change.</p>
{table(["ID", "Area", "Issue", "Source", "Suggested action"], rows)}
"""
    page("flagged.html", "Flagged for Review", body,
         intro="Irregularities, conflicts and unverified items, each with source links for manual review.")


def render_sources():
    rows = []
    for s in SOURCES.values():
        rows.append([e(s["id"]), f"<strong>{e(s['title'])}</strong>", link(s["url"], s["url"]), e(s["publisher"]),
                     e(s["type"]), e(ACCESSED), e(s["note"])])
    body = table(["ID", "Title", "Link", "Publisher", "Type", "Accessed", "Notes"], rows)
    page("sources.html", "Sources", body,
         intro="Each source used in this build. Type 'official' means a government, resort, restaurant or agency site. 'secondary' means press or reference sites.")


def render_repo_review():
    d = load("repo_review.json")
    rows = [[e(f["id"]), e(f["item"]), e(f["finding"]), e(f["status"]), e(f["action"])] for f in d["findings"]]
    body = f"""
<p>{e(d["scope"])}</p>
{table(["ID", "Item", "Finding", "Status", "Action"], rows)}
"""
    page("repo-review.html", "Repo review", body,
         intro="Review of the repository state, with irregularities flagged for review.")


def main():
    DOCS.mkdir(exist_ok=True)
    (DOCS / "assets").mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    render_index()
    render_hotels()
    render_restaurants()
    render_activities()
    render_booking()
    render_questions()
    render_suggestions()
    render_flagged()
    render_sources()
    render_repo_review()
    print("built", len(NAV), "pages into", DOCS)


if __name__ == "__main__":
    main()
