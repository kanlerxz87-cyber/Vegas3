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
