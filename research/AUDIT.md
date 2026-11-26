# Independent audit of `main` (arena-b1816fc8)

Date: 2026-11-26 (UTC). Scope: compare the live planner data on `main` (`data/site.json`, built at commit `4109e49`) against official pages fetched in this session. Raw captures are in `research/data/*.json`, with the source for each value.

This audit does not change the owner's files. It records findings for the integration step (I1).

## 1. Confirmed (owner value matches an official page fetched this session)

| Item | Owner value | Official source (fetched) |
|---|---|---|
| Joël Robuchon: 2 stars, Tue–Sat 5:00–9:30 PM, closed Mon and Sun | matches | https://mgmgrand.mgmresorts.com/en/restaurants/joel-robuchon-french-restaurant.html |
| L'Atelier: 1 star, Mon and Thu–Sun 5:00–9:30 PM, closed Tue and Wed | matches | https://mgmgrand.mgmresorts.com/en/restaurants/latelier-joel-robuchon-french-restaurant.html |
| é by José Andrés: 1 star, Tue–Sat 5:30–8:30 PM, up to 3 months' booking | matches | https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/e-by-jose-andres.html |
| China Poblano: Bib Gourmand, daily hours, cocktail hour Mon–Thu 4–6 PM | matches | https://cosmopolitanlasvegas.mgmresorts.com/en/restaurants/china-poblano.html |
| COTE: hours Mon–Sun, Fri–Sat 4:30 PM–12:00 AM, $$$ | matches (new check this session) | https://www.venetianlasvegas.com/dining/restaurants/cote.html |
| Venetian Two Queen Suite: 750 sq ft, 2 Queen Beds, Oversized Bathroom | matches | https://www.venetianlasvegas.com/hotel.html |
| ARIA Deluxe Two Queen: 520 sq ft, 2 Queen Beds | matches | https://aria.mgmresorts.com/en/hotel.html |
| Cosmopolitan City Room Queen (460 sq ft) and Terrace Studio Two Queen (730 sq ft) | matches | https://cosmopolitanlasvegas.mgmresorts.com/en/hotel.html |
| Caesars Colosseum Strip View Room, 2 Queens | matches | https://www.caesars.com/caesars-palace/hotel/rooms |
| Caesars Advanced Purchase Savings: up to 30% off, stays 30+ days ahead | matches (new check) | https://www.caesars.com/caesars-palace/hotel/rooms |
| Presidents' Day: Mon Feb 15, 2027 | matches | https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ |
| Red Rock: timed entry Oct 1–May 31, 8 am–5 pm; no public transit | matches | https://www.blm.gov/visit/red-rock-canyon-national-conservation-area |
| RTC: 39 routes, no subway listed | matches | https://www.rtcsnv.com/ways-to-travel/transit-services/ |

## 2. Missing from `main` (official data exists and was fetched)

| Item | What the official page shows | Source |
|---|---|---|
| Wynn Tower Suite Two Queens | 640 sq ft, two Queen Wynn Dream beds, Tower Suites pool access, $50 breakfast credit. Owner's Wynn row says "page unavailable". That is stale: the page loads. | https://www.wynnlasvegas.com/rooms-and-suites/wynn-tower-suites/wynn-tower-two-queen |
| MGM Grand room types | MGM Two Queen: 446 sq ft, 2 Queen Beds, max 4 (owner: "not fetched") | https://mgmgrand.mgmresorts.com/en/hotel.html |
| Bellagio room types | Premier Two Queen: 510 sq ft, 2 Queen Beds, max 4 (owner: "not fetched") | https://bellagio.mgmresorts.com/en/hotel.html |
| Wing Lei hours | Thu, Sun, Mon 5:30–9:30 PM; Fri–Sat 5:30–10:00 PM; closed Tue–Wed. Business casual. +1 (702) 770-3388. Owner: hours "NOT verified". | https://www.wynnlasvegas.com/dining/fine-dining/wing-lei |
| COTE hours and price | Confirmed on official page (see section 1). Owner lists these correctly. | https://www.venetianlasvegas.com/dining/restaurants/cote.html |
| Monorail station hours | Mon 7 am–midnight; Tue–Thu 7 am–2 am; Fri–Sun 7 am–3 am. Early-closure notice Nov 29–Dec 15, 2026. | https://www.lvmonorail.com/ |
| Valley of Fire | $10 vehicle entry ($15 non-NV). Visitor center 9–4 daily. Dec 1–14 annual closure. Rideshare return can fail. Not on owner's activity list. | https://parks.nv.gov/parks/valley-of-fire |
| Red Rock drive time | About 30 minutes from the Strip (official BLM). Owner: fees page not fetched. | https://www.blm.gov/visit/red-rock-canyon-national-conservation-area |

## 3. Inaccurate or incomplete on `main`

| ID | Issue | Evidence |
|---|---|---|
| A-01 | COTE "first-ever Michelin-starred" claim (IRR-08) is mischaracterized. The COTE page says it is "From the team behind the first-ever Michelin-starred Korean BBQ restaurant." That describes the team's other restaurant, not COTE. Owner's flag reads it as a claim about COTE itself. | https://www.venetianlasvegas.com/dining/restaurants/cote.html |
| A-02 | Hoover Dam special-event windows are incomplete. Owner lists 3 days after Thanksgiving and the week after Christmas. The official page also lists 2 weeks before and after Easter (Easter 2027 = Mar 28, computed, so Mar 14–Apr 11), and the first 2 weeks of August. Feb 15–22, 2027 is outside these windows. | https://www.usbr.gov/lc/hooverdam/ |
| A-03 | Owner's repo review says Pages is published from `main` only. In practice two deployments run on each push: the legacy branch build (Pages API: `build_type: legacy`, `source: main /`) and the Actions workflow `Deploy static site to GitHub Pages`. Both publish the whole repo root, including `COORDINATION.md`, `scripts/`, and `data/site.json`. | GitHub Pages API for this repo; `.github/workflows/pages.yml` (`path: .`) |
| A-04 | Owner's activities list has no Valley of Fire, Monorail, Fremont Street, or Sphere rows, though the site claims to show all candidate activities. | `data/site.json` activities rows |
| A-05 | Owner's Michelin status for Gymkhana and Michael Mina is shown as "Recommended". MGM pages label them "Selected". Both are flagged on `main`. Still unresolved. | https://www.visitlasvegas.com/michelin-guide-restaurants/ |

## 4. Still unverified (blank, flagged)

- Hotel 7-night totals for Feb 15–22, 2027 (all hotels).
- Private bathroom: only the Venetian's "Oversized Bathroom" is stated. Wynn's room page mentions a "spacious bathroom" (not the same as "private").
- Resorts World room data (official room page not fetchable).
- Michelin's own guide.michelin.com pages (not fetchable from this sandbox).
- Restaurant per-person cost for two adults.
- Social links (YouTube, TikTok, Instagram) for venues. Not confirmed on any venue page. Agency-level links (Bureau of Reclamation, BLM) were not verified in this session either.
- Travel times for any hotel–venue pair (RTC Trip Planner not run).
- Hoover Dam hours, admission, and drive time.
- Fremont Street and Sphere show calendars for Feb 2027.

## 5. Corrections applied to this session's data

- Removed URLs, addresses, and social handles that were not on a fetched page (e.g., MGM and Cosmopolitan street addresses, and social handles for Hoover Dam and BLM).
- Removed promo claims that were not on a fetched page (e.g., "$139" Caesars rate, MGM "up to 30% off" banner).
- Set secondary-press sources to name-only (no URL).
