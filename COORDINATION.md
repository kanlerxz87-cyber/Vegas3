# COORDINATION.md: shared task board

Branch for this session: `arena/7dd5ad60-vegas3` (base `ec27311` on `main`).
Session ID: `arena-7dd5ad60`. This session owns every task below. It is the only active session on this branch, so it also performed the final integration step.

Status values: `unclaimed`, `in progress`, `done`, `needs review` (`needs review` is published on the Flagged for Review page and does not block anything).

| Task | Status | Owner | Files touched | Sources | Verification | Irregularities |
|---|---|---|---|---|---|---|
| T1 Repo review | done | arena-7dd5ad60 | `data/repo_review.json`, `docs/repo-review.html` | none (repo state only) | Git state checked (`git status`, `git log`, branch list). | R-01, R-03 (see repo-review page) |
| T2 Michelin restaurants (24) | done | arena-7dd5ad60 | `data/restaurants.json`, `data/sources.json` | S01 (CVA), S03, S04-S10, S11-S14, S22-S24, S27 | Category counts checked against S01 (4 / 3 / 17). Hours and addresses taken only from official pages. | F-01 to F-12 |
| T3 Hotels (8 resorts) | done (partial: prices and room specs unverified) | arena-7dd5ad60 | `data/hotels.json` | S01, S04, S05, S06, S07, S22, S23 | Michelin count per property checked against S01. Rates, bed/bath, transit left blank. | F-13 to F-15 |
| T4 Activities & transit | done (partial) | arena-7dd5ad60 | `data/activities.json` | S15-S21, S25, S26 | Hours and fees taken from official pages. Subway and monorail claims are secondary only. | F-16 to F-21 |
| T5 Dates & booking | done | arena-7dd5ad60 | `data/booking.json` | S01, S04, S06, S14 | Weekdays computed (Python calendar). 3-month booking window computed. | F-22, F-23 |
| T6 Questions & suggestions | done | arena-7dd5ad60 | `data/qa.json`, `data/suggestions.json`, `data/summary.json` | S01-S26 (as cited per item) | Every answered item cites a source. | none |
| T7 Site build and integration | done | arena-7dd5ad60 | `scripts/build_site.py`, `scripts/verify_site.py`, `docs/*`, `README.md`, `COORDINATION.md` | n/a | `python3 scripts/build_site.py` then `python3 scripts/verify_site.py` (exit 0). | none |
| T8 Publish to GitHub Pages | in progress (see log) | arena-7dd5ad60 | Pages settings | n/a | To be confirmed after merge | n/a |

## Verification summary

- Every restaurant, hotel, activity, transit item, answered question and flagged item cites at least one source ID in `data/sources.json`.
- All source URLs are https. All internal links in `docs/` resolve. Every external link in `docs/` is a cited source or a website taken from the data.
- Blank values render as `Unverified`. Nothing is estimated.
- Sandbox limit: only github.com, codeload.github.com, api.github.com, registry.npmjs.org, pypi.org and files.pythonhosted.org are reachable for bash. Official sites were read through the page-fetch tool. Some official pages (guide.michelin.com, rtcsnv.com route pages, hotel room pages, restaurant hours pages) could not be fetched. Those items are flagged, not filled in.

## Log

- 2026-11-26 (arena-7dd5ad60): Created COORDINATION.md. Claimed T1 to T7 on this branch. Built data files and the site. Verifier passed.
- 2026-11-26 (arena-7dd5ad60): Integration step. Re-ran build and verifier on the combined data. Next: commit, push to `arena/7dd5ad60-vegas3`, open PR to `main`, merge, enable Pages from `/docs`, confirm deploy.

## Pull request and merge record

- PR: https://github.com/kanlerxz87-cyber/Vegas3/pull/4 (arena/7dd5ad60-vegas3 -> main)
- Merge result: pending
- Pages deploy: pending
