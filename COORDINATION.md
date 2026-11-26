# Coordination board

| Task | Status | Owner session | File scope |
|---|---|---|---|
| Site, research, and integration | in progress | arena-84047ba4 | `index.html`, `styles.css`, `app.js`, `data/`, `.github/workflows/pages.yml`, `README.md`, `COORDINATION.md` |

## Work log

### Site, research, and integration — arena-84047ba4
- Sources to verify: official Michelin Guide listings; official hotel, restaurant, transit, attraction and social-media pages where available.
- Verification plan: preserve links to primary sources; identify unconfirmed prices, dates, operations and transit times as unverified rather than estimating them.
- Irregularities: repository initially contains only a one-line README and has no existing site, source data, or coordination board. No other session claims were present at start.
- Sources checked (official): MICHELIN Guide Las Vegas selection (https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurants), Restaurant de Joël Robuchon (https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/restaurant-de-joel-robuchon), L'Atelier de Joël Robuchon (https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/l-atelier-de-joel-robuchon-las-vegas), Restaurant Guy Savoy (https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/guy-savoy-las-vegas), MGM Grand (https://mgmgrand.mgmresorts.com/en.html), Caesars Palace (https://www.caesars.com/caesars-palace), Bellagio (https://bellagio.mgmresorts.com/en.html), The Cosmopolitan (https://www.cosmopolitanlasvegas.com/), Wynn (https://www.wynnlasvegas.com/), RTC transit services and trip planner (https://www.rtcsnv.com/ways-to-travel/transit-services/ and https://www.rtcsnv.com/ways-to-travel/trip-planner/).
- Verification performed: checked Michelin's official 2026 Las Vegas selection and individual star-status pages; site anchor targets validated with Python HTMLParser; JavaScript syntax checked with `node --check`; no claims of exact hotel/restaurant prices, route times, hours, or 2027 operations were invented. The visible restaurant table is an explicitly labeled starred subset, not the complete 24-selection list.
- Irregularities: user requested live verified future prices and best booking date, but no booking inventory/query data source is available in repository; these values remain explicitly unverified. A 3-night preferred window conflicts with requested 7-night totals. No TikTok/Instagram/YouTube profiles are linked because handles were not confirmed from official pages. A ≤1h travel ranking cannot be validated absent selected dates, exact route schedule and start point.
- Publication: site and Pages workflow prepared; must merge via current branch PR and verify Actions/Pages deployment after merge. No PR has been opened or merged yet.

---

## Session arena-b1816fc8 — claims added 2026-11-26 21:58 UTC (branch `arena/b1816fc8-vegas3`)

**Scope conflict noted:** the row "Site, research, and integration" (arena-84047ba4, claimed 21:54 UTC) covers the root site files (`index.html`, `styles.css`, `app.js`, `data/`, `.github/workflows/pages.yml`, `README.md`). This session did **not** start that work and will not edit those files. Instead it claimed the non-overlapping scopes below, so the two sets of work can be merged without conflicts.

| Task | Status | Owner session | File scope | Claimed (UTC) |
|---|---|---|---|---|
| R0 — Repo review, line-by-line (repo state, irregularities, links to official sources) | in progress | arena-b1816fc8 | `research/repo-review.json` | 2026-11-26 21:58 |
| R1 — Hotel research (8 Strip/Downtown hotels: official room, bathroom, Michelin proximity, booking-window facts) | in progress | arena-b1816fc8 | `research/data/hotels.json` | 2026-11-26 21:58 |
| R2 — Michelin restaurants (all 24 LVCVA-listed Las Vegas distinctions; star/Bib/Recommended status; hours & social where officially verifiable) | in progress | arena-b1816fc8 | `research/data/restaurants.json` | 2026-11-26 21:58 |
| R3 — Activities & transport (official park/attraction/RTC sources; hours; no-subway check) | in progress | arena-b1816fc8 | `research/data/activities.json`, `research/data/transport.json` | 2026-11-26 21:58 |
| R4 — Research sub-site at `/research/` (category pages, questions, suggestions, Flagged for Review, generator) | in progress | arena-b1816fc8 | `research/**` (generator `research/build.py`) | 2026-11-26 21:58 |
| I1 — Integration of `research/` into root navigation, combined re-verification, PR, merge, Pages check | unclaimed | — | root `index.html` nav only | — |

### Requests for the owner of the root site (arena-84047ba4) — logged, not edited by this session

1. Add a navigation link from the root `index.html` to `research/index.html` (the category sub-site built by R4). It is a static page set and needs no build step.
2. Keep `.github/workflows/pages.yml` uploading the repository root (it already does via `path: .`) so `/research/` is published with the root site.
3. When both sides are done, the integration session should merge branch `arena/b1816fc8-vegas3` (R0–R4 files only) and re-check the combined site.

### Log — arena-b1816fc8

- 2026-11-26 21:57 UTC — Found `main` already has the root site from arena-84047ba4 (claim at 21:54 UTC, active). Did not take over its work (claim is < 60 min old with commits).
- 2026-11-26 21:58 UTC — Merged `origin/main` into `arena/b1816fc8-vegas3`; resolved the `COORDINATION.md` add/add conflict by keeping arena-84047ba4's board verbatim and appending this section. No other content was discarded.
