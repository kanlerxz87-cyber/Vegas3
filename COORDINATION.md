# Shared task board

Session ID: `arena/e34b50a1-vegas3` (current branch fixed by Arena)

| Task | Status | Owner | Files |
|---|---|---|---|
| Build trip-planning dashboard, transparent sourcing and review flags | in progress | arena/e34b50a1-vegas3 | COORDINATION.md, index.html, styles.css, app.js, README.md |

## Sources and verification log

- MICHELIN Guide Las Vegas official directory: https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurants (accessed 2026-11-26). Directory currently includes Las Vegas entries. Directory inclusion is not equivalent to a star; individual restaurant pages must be checked for award labels.
- Individual official guide pages: https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/restaurant-de-joel-robuchon (2 stars per result), https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/l-atelier-de-joel-robuchon-las-vegas (1 star per result). User must recheck awards for trip dates.
- Hotel rates/availability for 2027, transport itineraries/hours, full restaurant hours and social accounts were not independently confirmed from official sources in this session; left blank and flagged rather than inferred.

Verification: repository initially contained only README.md; static build has no dependencies. Check HTML/CSS/JS manually and ensure source links are explicit. No other sessions or claims are visible in the repo. Irregularity: user asks both a preferred 3-night Feb 15–18 window and a 7-night price comparison; these are distinct trip lengths and need to be resolved. Las Vegas directory listings should not be presented as universally Michelin-starred.