# Shared task board

Session ID: `arena/84047ba4-vegas3` (current branch fixed by Arena)

| Task | Status | Owner | Files |
|---|---|---|---|
| Build trip-planning dashboard, transparent sourcing and review flags | needs review | arena/84047ba4-vegas3 | COORDINATION.md, index.html, styles.css, app.js, README.md, .github/workflows/pages.yml |

## Sources and verification log

- MICHELIN Guide Las Vegas official directory: https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurants (accessed 2026-11-26). Directory inclusion is not equivalent to a star; individual restaurant pages checked for award labels.
- Individual official guide pages: https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/restaurant-de-joel-robuchon (2 stars per page), https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/l-atelier-de-joel-robuchon-las-vegas (1 star), https://guide.michelin.com/us/en/nevada/las-vegas_2935077/restaurant/guy-savoy-las-vegas (1 star). Awards are 2026 status and need checking for trip dates.
- Official hotel pages linked in the site: MGM Grand, Caesars Palace, Bellagio, The Cosmopolitan, Wynn. RTC transit services and planner links are included.
- Hotel rates/availability for 2027, transport itineraries/hours, full restaurant hours and social accounts were not independently confirmed from official sources; left blank and flagged rather than inferred.

Verification: static HTML anchor targets validated; JavaScript passes `node --check`. No dependency build required. Irregularities: preferred Feb 15–18 is 3 nights while user asks for 7-night totals; live rates and cheapest booking date cannot be established from available sources; restaurant table is explicitly a starred subset, not all 24 guide entries. Transit times, future schedules, couple meal totals and unverified social handles are flagged.

### Coordination conflict log

During rebase onto updated `main`, a concurrently created coordination board claimed the same broad site task under session `arena/e34b50a1-vegas3`. The conflict is retained in the log rather than silently discarding that session's record. The current Arena branch/session is `arena/84047ba4-vegas3`; this site's files are complete and need review for overlap before further edits.

### Publication

PR: https://github.com/kanlerxz87-cyber/Vegas3/pull/1. Merge/deployment pending; verify GitHub Actions and Pages URL after merge.
