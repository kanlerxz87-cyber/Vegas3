#!/usr/bin/env python3
"""Build the static GitHub Pages site from data/site.json.

Run:  python3 scripts/build_site.py
Output: pages/*.html (hub = pages/index.html), assets/style.css, .nojekyll.
The root index.html belongs to the earlier dashboard and is NOT generated here.
No external dependencies (Python 3 standard library only).
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
SRC = DATA["sources"]
META = DATA["meta"]


def e(text):
    return html.escape(str(text if text is not None else ""), quote=True)


def badge(status):
    cls = {"Verified": "ok", "Partial": "warn", "Unverified": "bad", "Calculated": "ok"}.get(status, "bad")
    return f'<span class="badge {cls}">{e(status)}</span>'


def src_links(ids):
    if not ids:
        return '<span class="muted">none</span>'
    parts = []
    for sid in ids:
        if sid in SRC:
            parts.append(f'<a href="{e(SRC[sid]["url"])}" rel="noopener" target="_blank" title="{e(SRC[sid]["label"])}">{e(sid)}</a>')
        else:
            parts.append(f'<span class="bad">{e(sid)} (missing)</span>')
    return " · ".join(parts)


def src_field(value):
    """Render a 'source' field that may hold one ID or several IDs separated by '·' or ','.
    Plain-text sources (for example 'User brief') are shown as text."""
    text = str(value or "")
    ids = [s.strip() for s in re.split(r"[·,]", text) if s.strip()]
    if ids and all(re.fullmatch(r"S\d+", s) for s in ids):
        return src_links(ids)
    return e(text) if text else '<span class="muted">none</span>'


def flags_html(flags):
    if not flags:
        return ""
    return "<ul class=\"flags\">" + "".join(f"<li>{e(f)}</li>" for f in flags) + "</ul>"


def blank(v, label="NOT VERIFIED"):
    if v in ("", None):
        return f'<span class="bad">{label}</span>'
    return e(v)


def url_html(url):
    if not url:
        return '<span class="bad">NOT VERIFIED</span>'
    return '<a href="' + e(url) + '" target="_blank" rel="noopener">Official page</a>'


def table(headers, rows_html, wide=True):
    cls = "table wide" if wide else "table"
    th = "".join(f"<th>{e(h)}</th>" for h in headers)
    return f'<div class="table-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(rows_html)}</tbody></table></div>'


def page(path, title, active, body, desc=""):
    """All generated pages live in pages/ (one level deep). Nav hrefs are pages-relative."""
    prefix = "../"
    nav_items = [
        ("index.html", "Home"),
        ("trip-dates.html", "Trip dates"),
        ("hotels.html", "Hotels"),
        ("restaurants.html", "Michelin dining"),
        ("activities.html", "Activities"),
        ("questions.html", "Questions"),
        ("suggestions.html", "Suggestions"),
        ("repo-review.html", "Repo review"),
        ("flagged.html", "Flagged for Review"),
        ("sources.html", "Sources"),
    ]
    active = active.replace("pages/", "")
    nav_parts = ['<a href="../index.html">← Main dashboard</a>']
    for href, label in nav_items:
        cls = ' class="active"' if href == active else ""
        nav_parts.append(f'<a href="{href}"{cls}>{e(label)}</a>')
    nav = "".join(nav_parts)
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · Vegas3</title>
<meta name="description" content="{e(desc or 'Las Vegas trip planner: hotels, Michelin dining, activities, questions and flagged items. Every row links to an official source.')}">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="topbar">
  <div class="brand"><a href="index.html">Vegas3</a><span>Las Vegas trip planner</span></div>
  <nav class="nav">{nav}</nav>
</header>
<main class="wrap">
{body}
</main>
<footer class="footer">
  <p>Data checked {e(META["access_date"])}. Every table row links to an official source. Blank cells are <span class="bad">NOT VERIFIED</span> and listed on the <a href="flagged.html">Flagged for Review</a> page.</p>
  <p><a href="{e(META["repo"])}">Repository</a></p>
</footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


def pill(label, value, cls=""):
    return f'<div class="stat {cls}"><div class="stat-v">{e(value)}</div><div class="stat-l">{e(label)}</div></div>'


# ---------------- Pages ----------------

def build_home():
    r = DATA["restaurants"]["rows"]
    h = DATA["hotels"]["rows"]
    a = DATA["activities"]["rows"]
    body = f"""
<section class="hero">
  <h1>Las Vegas trip plan — dashboard</h1>
  <p class="lead">Preferred trip: <strong>Mon Feb 15 – Thu Feb 18, 2027</strong> (3 nights). Alternative: 7 nights, Feb 15–22. Two adults. Private bathroom, queen-or-larger bed.</p>
  <div class="stats">
    {pill("Michelin distinctions (LV, 2026)", "24")}
    {pill("Michelin stars (LV, 2026)", "4")}
    {pill("Hotels reviewed", str(len(h)))}
    {pill("Hotel 7-night totals verified", "0 of " + str(len(h)), "bad")}
    {pill("Restaurant hours verified", str(sum(1 for x in r if x["status"] == "Verified")) + " of " + str(len(r)), "warn")}
    {pill("Items flagged for review", str(len(DATA["flagged"])), "warn")}
  </div>
</section>

<section class="card">
  <h2>Executive summary</h2>
  <ul class="bullets">
    <li><strong>Dates.</strong> Feb 15, 2027 is Presidents' Day (a federal holiday) — <a href="{SRC['S14']['url']}" target="_blank" rel="noopener">OPM 2027 holidays</a>. A 3-night stay (Feb 15–18) conflicts with the 1–2 week rule; a 7-night stay (Feb 15–22) meets it. <strong>You need to choose.</strong></li>
    <li><strong>Michelin in Las Vegas (2026).</strong> Four starred: Joël Robuchon (Two Stars), L'Atelier de Joël Robuchon, Restaurant Guy Savoy, é by José Andrés (One Star each). Three Bib Gourmand. Seventeen Recommended. Thirteen of the 24 are on the Strip (<a href="{SRC['S1']['url']}" target="_blank" rel="noopener">LVCVA</a>).</li>
    <li><strong>Hotels.</strong> Preliminary ranking by Michelin venues on the Strip: The Venetian/Palazzo (4 Recommended), MGM Grand (2 starred), The Cosmopolitan (1 star + 1 Bib). Four hotels have verified room types (2 queens or king); <strong>no live 7-night prices were verifiable</strong>, so cost columns are blank and flagged.</li>
    <li><strong>Travel.</strong> Red Rock Canyon is ~30 min from the Strip, requires timed entry (Oct 1–May 31), and has <strong>no public transit</strong> (<a href="{SRC['S16']['url']}" target="_blank" rel="noopener">BLM</a>). The 1-hour bus test has not been run for any pair.</li>
    <li><strong>Booking timing (official rules only).</strong> Starred restaurants usually release tables 30–60 days out. é takes bookings up to three months ahead. Caesars Palace advertises up to 30% off for stays booked 30+ days ahead, terms apply. The cheapest booking date is <strong>not yet known</strong>.</li>
    <li><strong>Repo.</strong> Only a README existed. Site built as static HTML from one data file; COORDINATION.md created. Irregularities are listed on the Repo review page.</li>
  </ul>
</section>

<section class="grid">
  <a class="tile" href="trip-dates.html"><h3>Trip dates</h3><p>Options A and B, booking-window facts, holiday check.</p></a>
  <a class="tile" href="hotels.html"><h3>Hotels</h3><p>Room types, beds, Michelin count, status per hotel.</p></a>
  <a class="tile" href="restaurants.html"><h3>Michelin dining</h3><p>All 24 Las Vegas distinctions, starred vs listed, hours, links.</p></a>
  <a class="tile" href="activities.html"><h3>Activities</h3><p>Red Rock, Hoover Dam, shows, hours and travel notes.</p></a>
  <a class="tile" href="questions.html"><h3>Questions</h3><p>What is answered, what you must decide, and how to find the rest.</p></a>
  <a class="tile" href="suggestions.html"><h3>Suggestions</h3><p>Ways to improve this site. Choose before anything changes.</p></a>
  <a class="tile" href="repo-review.html"><h3>Repo review</h3><p>Line-by-line repo review and irregularities.</p></a>
  <a class="tile warn" href="flagged.html"><h3>Flagged for Review</h3><p>Every unverified value and irregularity, with sources.</p></a>
</section>
"""
    page("pages/index.html", "Home", "index.html", body, desc="Las Vegas trip planner dashboard — Feb 2027 trip, hotels, Michelin dining, activities.")


def build_trip_dates():
    d = DATA["dates"]
    facts = [
        [e(f["item"]), e(f["value"]), src_field(f["source"]), badge(f["status"])]
        for f in d["facts"]
    ]
    win = [
        [f'<strong>{e(w["label"])}</strong>', e(w["start"]), e(w["end"]), str(w["nights"]), e(w["note"])]
        for w in d["windows"]
    ]
    body = f"""
<h1>Trip dates</h1>
<p class="lead">Allowed window: Feb 15 – Mar 23, 2027. Trip length: 1–2 weeks. Preferred: Feb 15–18, 2027.</p>
<section class="card"><h2>Date options</h2>
{table(["Option", "Start", "End", "Nights", "Notes"], [f"<tr>{''.join(f'<td>{c}</td>' for c in row)}</tr>" for row in win])}
<p class="muted">Option A conflicts with the 1–2 week rule. Choose A or B (see <a href="questions.html">Questions</a>).</p>
</section>
<section class="card"><h2>Verified facts and booking-timing rules</h2>
{table(["Item", "Value", "Source", "Status"], [f"<tr>{''.join(f'<td>{c}</td>' for c in row)}</tr>" for row in facts])}
</section>
"""
    page("pages/trip-dates.html", "Trip dates", "pages/trip-dates.html", body)


def build_hotels():
    H = DATA["hotels"]
    rows = []
    for r in H["rows"]:
        rows.append(
            "<tr>"
            f"<td>{r['rank']}</td>"
            f"<td><strong>{e(r['hotel'])}</strong></td>"
            f"<td>{blank(r['rooms'], 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['beds'])}</td>"
            f"<td>{blank(r['bath'], 'NOT STATED')}</td>"
            f"<td>{e(r['michelin'])}</td>"
            f"<td>{blank(r['total'])}</td>"
            f"<td>{blank(r['book'], 'NOT VERIFIED') if r['book'] else blank('', 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['transit'])}</td>"
            f"<td>{src_links(r['sources'])}</td>"
            f"<td>{badge(r['status'])}{flags_html(r['flags'])}</td>"
            "</tr>"
        )
    body = f"""
<h1>Hotels</h1>
<p class="lead">Two adults. Private bathroom and queen-or-larger bed are required. Every value below comes from an official hotel or venue page; blank cells are NOT VERIFIED.</p>
<section class="card">
<p><strong>Ranking method:</strong> {e(H["method"])}</p>
{table(H["columns"], rows)}
</section>
<section class="card">
<h2>What is still needed for hotels</h2>
<ul class="bullets">
<li>Live 7-night totals (Feb 15–22, 2027) and 3-night totals (Feb 15–18, 2027) from each hotel's booking page.</li>
<li>Bathroom wording on each room page (only The Venetian lists it on the fetched page).</li>
<li>Room data for MGM Grand, Bellagio and Wynn (pages unavailable this run).</li>
<li>Bus travel times ≤ 1 hour to each venue (RTC Trip Planner).</li>
</ul>
</section>
"""
    page("pages/hotels.html", "Hotels", "pages/hotels.html", body)


def build_restaurants():
    R = DATA["restaurants"]
    rows = []
    for i, r in enumerate(R["rows"], 1):
        star = r["tier"] == "Starred"
        row_cls = "starred" if star else ""
        star_mark = "★ " if star else ""
        if star:
            tier_html = '<span class="badge star">Starred</span>'
        else:
            tier_html = '<span class="badge">' + e(r["tier"]) + " (listed, no star)</span>"
        rows.append(
            f'<tr class="{row_cls}">'
            f"<td>{i}</td>"
            f'<td><strong>{e(r["name"])}</strong><br><span class="muted">{star_mark}{e(r["distinction"])}</span></td>'
            f"<td>{tier_html}</td>"
            f"<td>{e(r['cuisine_area'])}</td>"
            f"<td>{blank(r['hours'])}</td>"
            f"<td>{blank(r['price'], 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['cost'], 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['social'], 'NOT VERIFIED')}</td>"
            f'<td><a href="{e(r["url"])}" target="_blank" rel="noopener">Official site</a></td>'
            f"<td>{src_links(r['sources'])}</td>"
            f"<td>{badge(r['status'])}{flags_html(r['flags'])}</td>"
            "</tr>"
        )
    body = f"""
<h1>Michelin dining — Las Vegas (2026)</h1>
<p class="lead">{e(R["summary"])}</p>
<section class="card">
<p class="muted">Starred rows are highlighted. Michelin price symbols ($ to $$$$) are the Michelin category, not a dollar amount. Exact costs for 2 adults are NOT VERIFIED and left blank. Social links are NOT VERIFIED.</p>
{table(R["columns"], rows)}
</section>
<section class="card">
<h2>Michelin reading guide</h2>
<ul class="bullets">
<li><strong>Two Stars:</strong> excellent cooking, worth a detour. Joël Robuchon only.</li>
<li><strong>One Star:</strong> very good cooking, worth a stop. L'Atelier, Guy Savoy, é.</li>
<li><strong>Bib Gourmand:</strong> good quality, good value. China Poblano, Esther's Kitchen, Yen Viet Kitchen.</li>
<li><strong>Recommended:</strong> listed in the guide, no star. 17 venues.</li>
</ul>
<p class="muted">Source: <a href="{SRC['S1']['url']}" target="_blank" rel="noopener">LVCVA</a> (official). Primary Michelin pages were not individually verified in this run.</p>
</section>
"""
    page("pages/restaurants.html", "Michelin dining", "pages/restaurants.html", body)


def build_activities():
    A = DATA["activities"]
    rows = []
    for r in A["rows"]:
        rows.append(
            "<tr>"
            f"<td><strong>{e(r['name'])}</strong></td>"
            f"<td>{blank(r['hours'])}</td>"
            f"<td>{blank(r['exceptions'], 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['travel'])}</td>"
            f"<td>{blank(r['cost'], 'NOT VERIFIED')}</td>"
            f"<td>{blank(r['social'], 'NOT VERIFIED')}</td>"
            f"<td>{url_html(r['url'])}</td>"
            f"<td>{src_links(r['sources'])}</td>"
            f"<td>{badge(r['status'])}{flags_html(r['flags'])}</td>"
            "</tr>"
        )
    body = f"""
<h1>Activities</h1>
<p class="lead">Activities are limited to places with an official page. Travel times are shown only where an official source gives them.</p>
<section class="card">
{table(A["columns"], rows)}
</section>
"""
    page("pages/activities.html", "Activities", "pages/activities.html", body)


def build_questions():
    Q = DATA["questions"]
    ans = "".join(
        f"<tr><td>{e(x['q'])}</td><td>{e(x['a'])}</td></tr>" for x in Q["answered"]
    )
    need = "".join(
        f"<tr><td>{i}</td><td>{e(x['q'])}</td><td>{e(x['why'])}</td><td>{e(x['how_to_resolve'])}</td></tr>"
        for i, x in enumerate(Q["needed"], 1)
    )
    body = f"""
<h1>Questions and information gaps</h1>
<section class="card"><h2>Answered from official sources</h2>
<div class="table-wrap"><table class="table"><thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>{ans}</tbody></table></div>
</section>
<section class="card"><h2>Still needed before deciding</h2>
<div class="table-wrap"><table class="table"><thead><tr><th>#</th><th>Question / missing info</th><th>Why it matters</th><th>How to resolve</th></tr></thead><tbody>{need}</tbody></table></div>
</section>
"""
    page("pages/questions.html", "Questions", "pages/questions.html", body)


def build_suggestions():
    rows = "".join(
        f"<tr><td>{e(s['id'])}</td><td><strong>{e(s['title'])}</strong></td><td>{e(s['detail'])}</td><td>{e(s['effort'])}</td><td>{e(s['needs'])}</td><td><span class=\"badge\">Awaiting your choice</span></td></tr>"
        for s in DATA["suggestions"]
    )
    body = f"""
<h1>Suggestions</h1>
<p class="lead">Review each suggestion. <strong>Nothing here has been implemented.</strong> Reply with the IDs you approve (for example, “SG-1, SG-3, SG-7”) and the answers on the Questions page.</p>
<section class="card">
<div class="table-wrap"><table class="table wide"><thead><tr><th>ID</th><th>Suggestion</th><th>Detail</th><th>Effort</th><th>Needs from you</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table></div>
</section>
"""
    page("pages/suggestions.html", "Suggestions", "pages/suggestions.html", body)


def build_repo_review():
    rows = "".join(
        f"<tr><td>{e(x['item'])}</td><td>{e(x['observation'])}</td><td>{src_field(x['source'])}</td><td>{e(x['action'])}</td></tr>"
        for x in DATA["repo_review"]
    )
    body = f"""
<h1>Repo review</h1>
<p class="lead">Repository <a href="{e(META['repo'])}" target="_blank" rel="noopener">kanlerxz87-cyber/Vegas3</a>, base commit ec27311. The repo had one README and one commit. Items below are irregularities or open points, each with a source.</p>
<section class="card">
<div class="table-wrap"><table class="table wide"><thead><tr><th>Item</th><th>Observation</th><th>Source</th><th>Suggested action</th></tr></thead><tbody>{rows}</tbody></table></div>
</section>
"""
    page("pages/repo-review.html", "Repo review", "pages/repo-review.html", body)


def build_flagged():
    rows = "".join(
        f"<tr><td>{e(x['item'])}</td><td>{e(x['issue'])}</td><td>{src_field(x['source'])}</td></tr>"
        for x in DATA["flagged"]
    )
    body = f"""
<h1>Flagged for Review</h1>
<p class="lead">Unverified values, conflicts, and irregularities. These do not block publishing. Each item shows its source (or “—” if none exists) so you can check it.</p>
<section class="card">
<div class="table-wrap"><table class="table wide"><thead><tr><th>Item</th><th>Issue</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>
</section>
"""
    page("pages/flagged.html", "Flagged for Review", "pages/flagged.html", body)


def build_sources():
    rows = "".join(
        f"<tr><td>{e(k)}</td><td>{e(v['label'])}</td><td>{e(v['type'])}</td><td><a href=\"{e(v['url'])}\" target=\"_blank\" rel=\"noopener\">{e(v['url'])}</a></td></tr>"
        for k, v in SRC.items()
    )
    body = f"""
<h1>Sources</h1>
<p class="lead">All sources accessed {e(META['access_date'])}. Official sources are preferred. S1 is LVCVA (an official destination marketing organization) and was used for the Michelin list. Secondary news sites were used only for cross-checking and are not cited for any value.</p>
<section class="card">
<div class="table-wrap"><table class="table wide"><thead><tr><th>ID</th><th>Title</th><th>Type</th><th>Link</th></tr></thead><tbody>{rows}</tbody></table></div>
</section>
"""
    page("pages/sources.html", "Sources", "pages/sources.html", body)


def write_assets():
    css = """
:root{--ink:#1d2433;--muted:#5d6678;--line:#e3e7ef;--bg:#f6f7fb;--card:#fff;--brand:#1f4fd1;--ok:#11794a;--okbg:#e5f6ee;--warn:#8a5a00;--warnbg:#fff4da;--bad:#b42318;--badbg:#fdecea;--star:#7a4b00;--starbg:#fff1c8}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--brand)}
.topbar{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5;padding:10px 16px}
.brand{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.brand a{font-weight:700;font-size:18px;color:var(--ink);text-decoration:none}
.brand span{color:var(--muted);font-size:13px}
.nav{display:flex;gap:6px;overflow-x:auto;margin-top:8px;padding-bottom:4px}
.nav a{white-space:nowrap;padding:6px 10px;border-radius:999px;text-decoration:none;color:var(--ink);background:var(--bg);border:1px solid var(--line);font-size:14px}
.nav a.active{background:var(--brand);color:#fff;border-color:var(--brand)}
.wrap{max-width:1200px;margin:0 auto;padding:16px}
h1{font-size:26px;margin:8px 0 6px}
h2{font-size:19px;margin:0 0 10px}
h3{margin:0 0 4px;font-size:17px}
.lead{color:var(--muted);margin-top:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:14px 0}
.hero{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin-top:8px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:12px}
.stat{border:1px solid var(--line);border-radius:10px;padding:12px;background:#fbfcfe}
.stat-v{font-size:22px;font-weight:700}
.stat-l{color:var(--muted);font-size:13px}
.stat.bad .stat-v{color:var(--bad)}
.stat.warn .stat-v{color:var(--warn)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:14px 0}
.tile{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;text-decoration:none;color:var(--ink)}
.tile:hover{border-color:var(--brand)}
.tile.warn{border-color:#e7c46b;background:#fffaf0}
.tile p{margin:0;color:var(--muted);font-size:14px}
.bullets li{margin:6px 0}
.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:10px;background:#fff}
.table{border-collapse:collapse;width:100%;font-size:14px}
.table.wide{min-width:900px}
.table th,.table td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
.table th{background:#f2f5fb;position:sticky;top:0;font-weight:600}
.table tr.starred td{background:#fffbea}
.badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:12px;font-weight:600;background:#eef1f7;color:var(--ink);white-space:nowrap}
.badge.ok{background:var(--okbg);color:var(--ok)}
.badge.warn{background:var(--warnbg);color:var(--warn)}
.badge.bad{background:var(--badbg);color:var(--bad)}
.badge.star{background:var(--starbg);color:var(--star)}
.bad{color:var(--bad);font-weight:600}
.muted{color:var(--muted)}
.flags{margin:6px 0 0;padding-left:18px;font-size:12.5px;color:var(--muted)}
.footer{max-width:1200px;margin:24px auto;padding:0 16px 32px;color:var(--muted);font-size:13px}
@media (max-width:640px){
  body{font-size:15px}
  h1{font-size:22px}
  .wrap{padding:10px}
  .card{padding:12px}
  .table{font-size:13px}
}
"""
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(css.strip() + "\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


def main():
    write_assets()
    build_home()
    build_trip_dates()
    build_hotels()
    build_restaurants()
    build_activities()
    build_questions()
    build_suggestions()
    build_repo_review()
    build_flagged()
    build_sources()
    print("Built site into", ROOT)


if __name__ == "__main__":
    main()
