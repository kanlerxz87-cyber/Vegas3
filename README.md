# Vegas3: Las Vegas Trip Planner

A static planning dashboard for a 2-adult Las Vegas trip (window: Feb 15 to Mar 23 2027), published with GitHub Pages from `docs/`.

- Live site: https://kanlerxz87-cyber.github.io/Vegas3/ (enabled after merge; see COORDINATION.md)
- Data: `data/*.json`. Every row cites source IDs listed in `data/sources.json`.
- Build: `python3 scripts/build_site.py` (writes `docs/`)
- Verify: `python3 scripts/verify_site.py` (checks sources, internal links and external links)
- Task board: `COORDINATION.md`

Blank values are shown as **Unverified**. They are never estimated. Flagged items are listed on the site's *Flagged for Review* page.
