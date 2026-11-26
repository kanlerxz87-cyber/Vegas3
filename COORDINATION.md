# Coordination board

| Task | Status | Owner session | File scope |
|---|---|---|---|
| Trip-planning dashboard, research, and integration | done | arena-84047ba4 | `index.html`, `styles.css`, `app.js`, `README.md`, `.github/workflows/pages.yml`, `COORDINATION.md` |

## Work log — arena-84047ba4

- Repository reviewed; it initially contained only README. A concurrently active session had created a dashboard on main while this session built a separate alternative; overlap was resolved by preserving the main-branch dashboard rather than overwriting another session's work. This branch added the GitHub Pages workflow and source/verification records.
- Official sources reviewed: MICHELIN Guide Las Vegas directory https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurants; Restaurant de Joël Robuchon https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/restaurant-de-joel-robuchon; L'Atelier de Joël Robuchon https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/l-atelier-de-joel-robuchon-las-vegas; Restaurant Guy Savoy https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/guy-savoy-las-vegas; official hotel sites (MGM Grand, Caesars Palace, Bellagio, Cosmopolitan, Wynn) and RTC transit planner.
- Verification: individual Michelin award pages checked; JavaScript syntax and anchor targets checked on the dashboard draft. The deployed main dashboard remains the other session's implementation and is authoritative after preserving the overlap. The site displays unverified future hotel prices, transit, hours and restaurant cost as unknown rather than fabricated.
- Irregularities: user's preferred Feb 15–18 trip is 3 nights, conflicting with requested 7-night totals. Live 2027 rates and an evidence-based cheapest booking date were not available. No handles were verified for social links. Transit under one hour cannot be confirmed without actual route/time and selected hotel. Guide has more entries than the verified starred subset.
- PR #1: https://github.com/kanlerxz87-cyber/Vegas3/pull/1 — merged 2026-11-26 (merge commit `bc5782a7d3405eb917f362504f366955193e28d6`). GitHub Actions static deployment run 45901530495 succeeded; GitHub Pages build/deploy run 45901530986 succeeded.

---

# Session arena-b9d64425 (branch `arena/b9d64425-vegas3`)

Added 2026-11-26. This session worked on its own branch and integrated with the existing dashboard on `main` without overwriting it. The branch-naming difference is logged below.

## Task board (this session)

| Task | Status | Owner session | File scope | Notes |
|---|---|---|---|---|
| Coordination board entry | done | arena-b9d64425 | `COORDINATION.md` | Appended only; earlier rows untouched. |
| T1 Repo review, line by line | done | arena-b9d64425 | `data/site.json` (repo_review), `pages/repo-review.html` | Irregularities listed on Repo review page. |
| T2 Hotels (room types, beds, bathroom, Michelin count, booking timing) | done, partial data | arena-b9d64425 | `data/site.json` (hotels, dates), `pages/hotels.html`, `pages/trip-dates.html` | 4 hotels with official room data; 3 not fetchable. 7-night totals NOT verified. |
| T3 Michelin dining (2026 LV list, hours, price symbols) | done, partial data | arena-b9d64425 | `data/site.json` (restaurants), `pages/restaurants.html` | 24 distinctions verified against LVCVA; hours for 5; cost and social not verified. |
| T4 Activities | done, partial data | arena-b9d64425 | `data/site.json` (activities), `pages/activities.html` | Red Rock and Hoover Dam partly verified. |
| T5 Subpage site generator | done | arena-b9d64425 | `scripts/build_site.py`, `assets/style.css`, `pages/*` | Generated from `data/site.json`. |
| T6 Verification script | done | arena-b9d64425 | `scripts/verify_site.py` | Last run: VERIFY OK. |
| T7 Integration (link from dashboard to subpages, PR, merge, Pages check) | in progress | arena-b9d64425 | `index.html` (one link added), `README.md` (section appended) | See PR record below. |

## Integration notes

- Root `index.html`, `styles.css`, `app.js`, `.github/workflows/pages.yml` from arena-84047ba4 kept unchanged except for one added link in the page header pointing to `pages/index.html`.
- `README.md`: their content kept in full; a planner section appended.
- Both sessions' Michelin pages: the individual guide.michelin.com pages cited in the other session's dashboard were NOT reachable from this sandbox (fetch failed), so they are not re-verified here. Logged as IRR-M1.
- Branch-naming: brief asks for `session-<id>/<task>`; this session is fixed to `arena/b9d64425-vegas3`. Logged as REPO-05.

## Sources used by this session (accessed 2026-11-26)

- LVCVA Michelin page (S1): https://www.visitlasvegas.com/michelin-guide-restaurants/
- MGM Grand, Joël Robuchon (S2): https://mgmgrand.mgmresorts.com/en/restaurants/joel-robuchon-french-restaurant.html
- MGM Grand, L'Atelier (S3): https://mgmgrand.mgmresorts.com/en/restaurants/latelier-joel-robuchon-french-restaurant.html
- Cosmopolitan, é by José Andrés (S4): https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/e-by-jose-andres.html
- Caesars Palace, Restaurant Guy Savoy (S5): https://www.caesars.com/caesars-palace/restaurants/restaurant-guy-savoy
- Cosmopolitan, China Poblano (S6): https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/china-poblano.html
- Esther's Kitchen (S7): https://www.estherslv.com/ · Yen Viet Kitchen (S8): https://www.yenvietkitchen.com/
- Venetian, COTE (S9): https://www.venetianlasvegas.com/dining/restaurants/cote.html
- Cosmopolitan rooms (S10): https://cosmopolitanlasvegas.mgmresorts.com/en/hotel.html
- ARIA rooms (S11): https://aria.mgmresorts.com/en/hotel.html
- Venetian hotel (S12): https://www.venetianlasvegas.com/hotel.html
- Caesars Palace hotel (S13): https://www.caesars.com/caesars-palace/hotel
- OPM 2027 federal holidays (S14): https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/
- RTC of Southern Nevada (S15): https://www.rtcsnv.com/
- BLM Red Rock Canyon NCA (S16): https://www.blm.gov/visit/red-rock-canyon-national-conservation-area
- Bureau of Reclamation, Hoover Dam (S17): https://www.usbr.gov/lc/hooverdam/
- Venetian, Mott 32 (S18): https://www.venetianlasvegas.com/dining/restaurants/mott-32.html
- GitHub API Pages config (S19): https://api.github.com/repos/kanlerxz87-cyber/Vegas3/pages
- MICHELIN Guide directory (S21): https://guide.michelin.com/us/en/restaurants (reachable; individual LV listings not verified)

Full list with types on the site's Sources page: `pages/sources.html`.

## Irregularities (this session)

- IRR-01 7-night totals NOT verified for any hotel.
- IRR-02 Private bathroom not stated on fetched room pages (Cosmopolitan, ARIA, Caesars).
- IRR-03 MGM Grand, Bellagio, Wynn room pages not fetchable in this run.
- IRR-04 Bus/subway ≤ 1 hr not calculated; Red Rock has no public transit (BLM).
- IRR-05 Restaurant hours unverified for 19 of 24 venues; Guy Savoy partial.
- IRR-06 Restaurant cost for 2 adults NOT verified (Michelin $ symbols only).
- IRR-07 No social-media links verified.
- IRR-08 COTE's own page claims "first-ever Michelin-starred Korean BBQ restaurant"; LVCVA lists COTE Las Vegas as Recommended only.
- IRR-09 Trip-length conflict: 3 nights vs 1–2 weeks and 7-night totals.
- IRR-10 Hoover Dam tour page snapshot: tickets "not currently available".
- IRR-11 RTC alert: F1 construction changing bus service around the Strip.
- IRR-M1 Michelin individual guide pages (guide.michelin.com/…/las-vegas_2935077/…) cited by the dashboard not reachable from this sandbox.
- REPO-05 Branch naming differs from the brief (see above).

## PR and publish record

- PR: _pending_
- Merge result: _pending_
- Pages deploy: _pending_
