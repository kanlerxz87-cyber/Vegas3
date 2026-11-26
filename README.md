# Vegas3 — Las Vegas 2027 trip-planning brief

A mobile-friendly, static dashboard for planning a Las Vegas trip for two adults. Open `index.html` locally or publish the repository root with GitHub Pages.

## Current research snapshot

The preferred Feb 15–18, 2027 window is three nights, while the brief also asks for a 7-night total and a 1–2 week trip. These requirements conflict. No live bookable 2027 hotel rates, exact room configurations, transit journey durations, restaurant operating schedules, social-media accounts, or two-person dining totals are claimed. Those fields are deliberately blank and explained in the Flagged for Review section.

The MICHELIN Guide directory and linked individual pages are linked inline. The two individual pages identify Restaurant de Joël Robuchon as two-star and L'Atelier de Joël Robuchon as one-star for the cited 2026 guide page; awards can change before travel. Directory membership alone is not a star award.

## Files

- `index.html` — overview, hotel and dining tables, activities, decision questions and review flags.
- `styles.css` — responsive dashboard styling.
- `app.js` — optional active-section navigation enhancement.
- `COORDINATION.md` — task status, sources and verification notes.

## Publishing

Configure GitHub Pages for the `main` branch, repository root (`/(root)`) in Settings → Pages. This is a plain static site and requires no build command or dependencies. Review all date-sensitive details and replace blank fields only after confirming each against an official source.

## Full planner site (subpages and data)

The detailed planner (hotels, all 24 Michelin distinctions, activities, questions, suggestions, repo review, Flagged for Review and sources) lives in `pages/`. Start at **`pages/index.html`** (also linked from the dashboard above).

- `data/site.json` — single source for every row; each row cites official source IDs, or is blank and flagged.
- `scripts/build_site.py` — regenerates `pages/*.html` (standard library only).
- `scripts/verify_site.py` — checks row sourcing, source-ID integrity, Michelin tier counts (4 starred / 3 Bib / 17 Recommended) and that every internal link resolves.

```bash
python3 scripts/build_site.py
python3 scripts/verify_site.py
```
