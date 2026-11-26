# COORDINATION — shared task board

Created 2026-11-26 by session `arena/b9d64425-vegas3` (branch `arena/b9d64425-vegas3`, base `main` @ ec27311).

**Status legend:** unclaimed · in progress · done · needs review
**Scope rule:** each task edits only the files in its scope. Shared outputs (`index.html`, `pages/*`, `assets/style.css`, `data/site.json`) are changed by the integration task only.

**Branch note:** the brief asks for `session-<id>/<task>` branches. This session is fixed to `arena/b9d64425-vegas3` and may not create or push other branches, so all tasks were done on this one branch in small commits. This is logged as an irregularity (REPO-05 in the repo review).

## Task board

| ID | Task | Status | Owner (session) | Files in scope | Notes |
|----|------|--------|-----------------|----------------|-------|
| T0 | Coordination board (this file) | done | arena/b9d64425-vegas3 | `COORDINATION.md` | Created; no prior file existed. |
| T1 | Repo review, line by line | done | arena/b9d64425-vegas3 | `data/site.json` (repo_review) | See Sources and Irregularities below. Flagged on Repo review page. |
| T2 | Hotels: room types, beds, bathroom, Michelin count, booking timing | done (partial data) | arena/b9d64425-vegas3 | `data/site.json` (hotels, dates) | 4 hotels with official room data; 3 unverified. 7-night prices NOT verified. |
| T3 | Michelin restaurants (2026 Las Vegas list, hours, price levels) | done (partial data) | arena/b9d64425-vegas3 | `data/site.json` (restaurants) | 24 distinctions verified against LVCVA; hours verified for 5; social links 0 verified. |
| T4 | Activities (Red Rock, Hoover Dam, shows) | done (partial data) | arena/b9d64425-vegas3 | `data/site.json` (activities) | Red Rock and Hoover Dam partly verified; others flagged. |
| T5 | Site build (static HTML, Pages-ready) | done | arena/b9d64425-vegas3 | `scripts/build_site.py`, `assets/style.css`, `index.html`, `pages/*`, `.nojekyll` | Generated from `data/site.json`. |
| T6 | Verification script | done | arena/b9d64425-vegas3 | `scripts/verify_site.py` | Row-level sourcing, source-ID integrity, tier counts, internal links. Last run: OK. |
| T7 | Integration: merge, re-verify, build, publish | in progress | arena/b9d64425-vegas3 | all | PR to main + merge + Pages check recorded below. |

## Sources used (all accessed 2026-11-26)

- S1 LVCVA Michelin page — https://www.visitlasvegas.com/michelin-guide-restaurants/
- S2 MGM Grand, Joël Robuchon — https://mgmgrand.mgmresorts.com/en/restaurants/joel-robuchon-french-restaurant.html
- S3 MGM Grand, L'Atelier — https://mgmgrand.mgmresorts.com/en/restaurants/latelier-joel-robuchon-french-restaurant.html
- S4 Cosmopolitan, é by José Andrés — https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/e-by-jose-andres.html
- S5 Caesars Palace, Restaurant Guy Savoy — https://www.caesars.com/caesars-palace/restaurants/restaurant-guy-savoy
- S6 Cosmopolitan, China Poblano — https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/china-poblano.html
- S7 Esther's Kitchen — https://www.estherslv.com/
- S8 Yen Viet Kitchen — https://www.yenvietkitchen.com/
- S9 Venetian, COTE — https://www.venetianlasvegas.com/dining/restaurants/cote.html
- S10 Cosmopolitan rooms — https://cosmopolitanlasvegas.mgmresorts.com/en/hotel.html
- S11 ARIA rooms — https://aria.mgmresorts.com/en/hotel.html
- S12 Venetian hotel — https://www.venetianlasvegas.com/hotel.html
- S13 Caesars Palace hotel — https://www.caesars.com/caesars-palace/hotel
- S14 OPM 2027 federal holidays — https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/
- S15 RTC of Southern Nevada — https://www.rtcsnv.com/
- S16 BLM Red Rock Canyon NCA — https://www.blm.gov/visit/red-rock-canyon-national-conservation-area
- S17 Bureau of Reclamation, Hoover Dam — https://www.usbr.gov/lc/hooverdam/
- S18 Venetian, Mott 32 — https://www.venetianlasvegas.com/dining/restaurants/mott-32.html
- S19 GitHub API, Pages config — https://api.github.com/repos/kanlerxz87-cyber/Vegas3/pages
- S20 GitHub, base commit — https://github.com/kanlerxz87-cyber/Vegas3/commit/ec27311da927c8240547b05d9ee65bbd55a5f2a1
- S21 MICHELIN Guide restaurant directory — https://guide.michelin.com/us/en/restaurants

Secondary news sites (Eater, Las Vegas Magazine, Identity Vegas, etc.) were used only to cross-check the 2026 list. No value is cited to them.

## Verification performed

- Michelin distinctions: 24 venues, 4 starred (1 Two Stars, 3 One Star), 3 Bib Gourmand, 17 Recommended — matched across S1 and secondary reports. Individual Michelin guide pages could not be fetched; flagged.
- Starred hours and price symbols: read from official venue pages S2–S5 (Guy Savoy hours incomplete — flagged).
- Bib hours: China Poblano (S6). Esther's Kitchen and Yen Viet Kitchen: no hours on official homepages — flagged.
- COTE hours: S9.
- Hotel room types, beds, sq ft: S10, S11, S12, S13 (where stated). Bathroom wording only on S12 — flagged elsewhere.
- Dates: 2027-02-15 is a Monday; federal holiday (S14). Weekday checked with `date` in the sandbox.
- Red Rock: 17 mi, ~30 min, timed entry, no public transit (S16).
- Build verification: `python3 scripts/verify_site.py` → VERIFY OK (10 pages, 36 rows, 21 sources).

## Irregularities and flags (also on the Flagged for Review page)

- IRR-01: 7-night prices NOT verified for any hotel. Cost columns blank.
- IRR-02: Bathroom not stated on fetched room pages (Cosmopolitan, ARIA, Caesars).
- IRR-03: MGM Grand, Bellagio, Wynn room pages unavailable in this run.
- IRR-04: Bus/subway ≤ 1 hour not calculated. Red Rock has no public transit (S16).
- IRR-05: Restaurant hours unverified for 19 of 24 venues.
- IRR-06: Restaurant costs for 2 adults NOT verified (Michelin $ symbols only).
- IRR-07: No social-media links verified.
- IRR-08: COTE's own page calls it the "first-ever Michelin-starred Korean BBQ restaurant"; S1 lists COTE Las Vegas as Recommended only.
- IRR-09: Trip length conflict — preferred 3 nights vs 1–2 week rule.
- IRR-10: Hoover Dam tour page snapshot shows tickets "not currently available".
- IRR-11: RTC home page alert — F1 construction changing bus service around the Strip.
- REPO-01: README was a single heading line.
- REPO-02: No COORDINATION.md existed (created).
- REPO-03: No LICENSE or .gitignore.
- REPO-04: Pages is enabled from `main` / `/` in legacy mode; `.nojekyll` added.
- REPO-05: Brief asked for `session-<id>/<task>` branches; session rule fixed this to one branch.

## Handoffs / conflicts

- None. Single session on this branch; no other session claimed tasks. No merge conflicts.

## Pull request and publish

- PR: _to be recorded after creation_
- Merge result: _to be recorded_
- Pages deploy: _to be recorded_
