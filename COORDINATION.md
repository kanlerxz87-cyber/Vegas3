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
| T7 Integration (link from dashboard to subpages, PR, merge, Pages check) | done | arena-b9d64425 | `index.html` (one link added), `README.md` (section appended) | See PR record below. |

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

- PR: https://github.com/kanlerxz87-cyber/Vegas3/pull/6 — "Las Vegas planner subpages, verification and integration" (arena/b9d64425-vegas3 → main)
- Merge result: MERGED via `gh pr merge 6 --merge`; merge commit 6c9fb007127fd633b29587fbe072e6f96cc237cf (2026-11-26 22:03 UTC)
- Pages deploy: GitHub Actions "Deploy static site to GitHub Pages" run 45902257572 completed success; Pages build status "built" for 6c9fb00. Live check: https://kanlerxz87-cyber.github.io/Vegas3/pages/index.html and /pages/hotels.html returned the new content.
- Verification before merge: `python3 scripts/verify_site.py` → VERIFY OK (11 pages, 36 table rows, 21 sources; restaurant tiers 4/3/17).
- Flagged items and unverified values are published on https://kanlerxz87-cyber.github.io/Vegas3/pages/flagged.html and did not block the merge.

---

# Session arena/870aacb9 (branch `arena/870aacb9-vegas3`) — evidence review handoff

Status: research and integration review completed; no changes to the `pages/` site/data were made because that scope was already integrated by session `arena-b9d64425` in PR #6. An early draft on this branch duplicated root-level pages; after PR #6 merged, the branch was synchronized to main and the current PR diff contains only this coordination handoff, preserving the live implementation.

## Findings and source checks (2026-11-26)

- MICHELIN's official 2026 Southwest announcement: https://www.michelin.com/en/publications/products-and-services/michelin-guide-reveals-first-ever-southwest-restaurant-selection-in-the-u-s. It says Las Vegas has four starred restaurants: Restaurant de Joël Robuchon (Two Stars), and L’Atelier de Joël Robuchon, é by José Andrés, and Guy Savoy (One Star each). That is **five stars across four restaurants**. The live planner hub currently labels a count of “4 Michelin stars”; this should be changed to “4 starred restaurants” or the aggregate should be 5. Request logged for the integration owner; this branch does not edit their page files.
- Direct MGM room source: MGM Two Queen, 446 sq ft, two queens, marble-adorned bathroom: https://mgmgrand.mgmresorts.com/en/hotel/mgm-two-queen.html. Direct Cosmopolitan City Room Queen: 460 sq ft, two queen beds, large bathroom: https://cosmopolitanlasvegas.mgmresorts.com/en/hotel/city-room.html. Caesars room directory: https://www.caesars.com/caesars-palace/hotel.rooms. Room descriptions do not explicitly say “private/en-suite”; confirm before booking. No dated Feb. 2027 final price was obtained.
- Official restaurant pages checked: Joël Robuchon https://mgmgrand.mgmresorts.com/en/restaurants/joel-robuchon-french-restaurant.html; L’Atelier https://mgmgrand.mgmresorts.com/en/restaurants/latelier-joel-robuchon-french-restaurant.html; é https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/e-by-jose-andres.html; China Poblano https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/china-poblano.html; Guy Savoy https://www.caesars.com/caesars-palace/restaurants/restaurant-guy-savoy; COTE https://www.venetianlasvegas.com/dining/restaurants/cote.html; Mott 32 https://www.venetianlasvegas.com/dining/restaurants/mott-32.html.
- Michael Mina operator page: https://bellagio.mgmresorts.com/en/restaurants/michael-mina.html. It displayed the venue as temporarily closed / closed each day at review time and a $295++ tasting menu/person. That is $590++ for two by arithmetic only, but do not recommend or reserve until reopening and 2027 menu availability are confirmed.
- Bellagio fountain official schedule and weather exception: https://bellagio.mgmresorts.com/en/entertainment/fountains-of-bellagio.html. Conservatory page (seasonal display; hours not established from the source capture): https://bellagio.mgmresorts.com/en/entertainment/conservatory-botanical-garden.html. KÀ weekly schedule and dark-date page: https://mgmgrand.mgmresorts.com/en/entertainment/ka-cirque-du-soleil-show.html.
- RTC official fares https://rtcws.rtcsnv.com/mobile/geoFares.html and route guide https://rtcws.rtcsnv.com/routepdf/transitguide.pdf show current Strip/Downtown fare products; no official route-specific journey times from a selected hotel to each venue were established.
- Social profile links found in platform search (not represented as verified hotel/operator booking sources): MGM Grand https://www.instagram.com/mgmgrand/; Cosmopolitan https://www.instagram.com/cosmopolitan_lv/; Caesars Palace https://www.instagram.com/caesarspalace/; Bellagio https://www.instagram.com/bellagio/; Guy Savoy https://www.instagram.com/guysavoylasvegas/; Joël Robuchon https://www.instagram.com/joelrobuchon.lasvegas/; L’Atelier https://www.instagram.com/latelierjoelrobuchonlv/; é https://www.instagram.com/ebyjoseandres/; Mott 32 https://www.instagram.com/mott32vegas/; KÀ https://www.instagram.com/ka.cirquedusoleil/. No matching venue account was confirmed for China Poblano, COTE, or Michael Mina in this review.

## Integration and deployment verified

- PR #6 (the detailed subpage integration): https://github.com/kanlerxz87-cyber/Vegas3/pull/6 — merged 2026-11-26; merge commit `6c9fb007127fd633b29587fbe072e6f96cc237cf`.
- Main deployment workflow run `45902257572` completed successfully. GitHub Pages API reported status `built`; public URL: https://kanlerxz87-cyber.github.io/Vegas3/ . The public landing page and linked planner hub at https://kanlerxz87-cyber.github.io/Vegas3/pages/index.html were fetched successfully.
- The live integrated site passed `python3 scripts/verify_site.py`: 11 pages, 36 table rows, 21 sources, with restaurant tier counts 4 / 3 / 17.
- PR #5 was initially drafted as a competing root-site redesign. Its current branch diff is now coordination-only to avoid conflicting with the already-published PR #6 integration; source audit and correction request are recorded here.

## Remaining flagged decisions

No independently verified official 7-night 2027 checkout total, cheapest booking day, private-bath confirmation, or ≤60-minute transit route comparison is available. Keep those fields blank/flagged. The Feb. 15–18 preferred window remains three nights and conflicts with the requested 1–2 week duration.
