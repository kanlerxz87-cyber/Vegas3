# Vegas3

Las Vegas trip planner (Feb 2027): hotels, Michelin dining, activities, questions, suggestions, and a flagged-items page.

**Live site:** https://kanlerxz87-cyber.github.io/Vegas3/

## How it is built

- All content lives in `data/site.json` (every table row cites official source IDs; unverified values are blank and flagged).
- `scripts/build_site.py` generates the static HTML pages (`index.html`, `pages/*.html`, `assets/style.css`). Standard library only.
- `scripts/verify_site.py` checks that each row has a source (or is flagged), that source IDs and internal links resolve, and that Michelin tier counts match the source list.

```bash
python3 scripts/build_site.py
python3 scripts/verify_site.py
```

Coordination and task status: see [COORDINATION.md](COORDINATION.md).
