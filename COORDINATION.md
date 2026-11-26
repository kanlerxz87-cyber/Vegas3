# Coordination Board — Vegas3 Trip Planner

Shared task board for agent sessions working on this repo.
Session ID convention: `<branch>/<task>`. Current session: `arena/faf21ab2-vegas3`.

Format per task:
- Task ID, description, status (unclaimed/in progress/done/needs review), owner session ID, files touched, sources/verification notes.

| Task ID | Description | Status | Owner | Files touched | Sources / verification |
|---------|-------------|--------|-------|---------------|------------------------|
| T1 | Create COORDINATION.md shared task board | done | arena/faf21ab2-vegas3 | COORDINATION.md | — |
| T2 | Research: Michelin Guide coverage for Las Vegas (official Michelin/LVCVA sources) | done | arena/faf21ab2-vegas3 | research/michelin.md | visitlasvegas.com/michelin-guide-restaurants/ (official LVCVA); mgmgrand, caesars, cosmopolitan official restaurant pages |
| T3 | Research: Las Vegas hotels (private bath, queen bed+, 2 adults), 7-night pricing Feb 15-22 2027, cheapest booking window | in progress | arena/faf21ab2-vegas3 | research/hotels.md | official hotel sites; rtcsnv.com for transit |
| T4 | Research: activities within 1 hr travel of hotels; restaurants hours/social links | in progress | arena/faf21ab2-vegas3 | research/restaurants.md, research/activities.md | official venue sites; exact transit times left blank when RTC route result is unavailable |
| T5 | Site: landing page + navigation structure (mobile-friendly dashboard) | in progress | arena/faf21ab2-vegas3 | index.html, assets/ | — |
| T6 | Site: data pages (hotels, restaurants, activities) as tables with sources | in progress | arena/faf21ab2-vegas3 | hotels.html, restaurants.html, activities.html | per-row official sources; values marked unverified when unsupported |
| T7 | Site: executive summary, suggestions, Q&A/missing info, Flagged for Review page | in progress | arena/faf21ab2-vegas3 | summary.html, suggestions.html, questions.html, flagged.html | — |
| T8 | Integration: verify all rows line-by-line against official sources, build check, enable GitHub Pages, PR + merge | unclaimed | — | all | per-row sources linked |

Rules:
- Claim a task by writing your session ID into the Owner column and committing/pushing immediately.
- Never start a task another session has claimed.
- Each session works only on files in its claimed scope (branch git worktree named session-<id>/<task>).
- If a task requires changing a file owned by another session, log the request here instead of editing it.
- Small, frequent commits; run `git pull --rebase` before every push.
- On merge conflict: stop, resolve without discarding other session's work, log what happened here.
- When finished: record sources, verification performed, irregularities here; mark done.
- Never mark verified without checking an official source; link that source.
- Shared outputs (table data, index/navigation) changed only by the final integration session (T8).
- Flagged irregularities/unverified items go on the "Flagged for Review" page; they do not block merge.
