# COORDINATION.md — Shared Task Board (Vegas3)

Created: 2026-11-26 (UTC) by session `arena-b1816fc8` (branch `arena/b1816fc8-vegas3`, base `ec27311` on `main`).

Statuses: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).

Branch policy note: this session works only on its assigned branch `arena/b1816fc8-vegas3` (the session branch named in its instructions). Other sessions must not push to it. Task scopes below are kept non-overlapping by file path.

## Task board

| ID | Task | Status | Owner (session) | File scope | Claimed (UTC) |
|---|---|---|---|---|---|
| T0 | Coordination board + repo review (line-by-line, irregularities) | in progress | arena-b1816fc8 | `COORDINATION.md`, `docs/data/repo_review.json` | 2026-11-26 |
| T1 | Hotel research (official sites, room type, Michelin proximity, booking windows) | in progress | arena-b1816fc8 | `docs/data/hotels.json` | 2026-11-26 |
| T2 | Michelin restaurant research (LVCVA/Michelin list, official restaurant sites, hours, social) | in progress | arena-b1816fc8 | `docs/data/restaurants.json` | 2026-11-26 |
| T3 | Activities + transport research (official park/attraction/RTC sites) | in progress | arena-b1816fc8 | `docs/data/activities.json`, `docs/data/transport.json` | 2026-11-26 |
| T4 | Site build (landing + category pages, generator, GitHub Pages) | in progress | arena-b1816fc8 | `docs/**` (except `docs/data/*.json` owned by T0–T3), `scripts/build_site.py` | 2026-11-26 |
| T5 | Integration: merge, re-verify combined data, check links, publish | unclaimed | — | `docs/index.html` navigation (final pass only) | — |

## Log

- 2026-11-26 — arena-b1816fc8 — Claimed T0–T4 and opened this board. No other sessions appear on this repo (only `main` and the session branch existed at start; no `COORDINATION.md` existed).
