# Vegas3 · Las Vegas Trip Planner

A mobile-friendly, source-linked dashboard for planning a Las Vegas vacation for two adults between **15 February and 23 March 2027**. Preferred dates are **15–18 February 2027**. The hotel price table uses **15–22 February (7 nights)** as a separate comparison interval because the request also asks for a seven-night total.

## Dashboard

- [Overview](index.html)
- [Executive summary](summary.html)
- [Hotels](hotels.html)
- [MICHELIN restaurants](restaurants.html)
- [Activities & transit](activities.html)
- [Questions & missing information](questions.html)
- [Suggestions](suggestions.html)
- [Flagged for Review](flagged.html)

**Live GitHub Pages site:** <https://kanlerxz87-cyber.github.io/Vegas3/> (deployment is being enabled from `main`).

## Verification approach

- The 2026 Las Vegas MICHELIN inventory is based on the [official Visit Las Vegas/LVCVA selection page](https://www.visitlasvegas.com/michelin-guide-restaurants/): 4 starred restaurants, 3 Bib Gourmand and 17 Recommended.
- Hotel room types, restaurant details, activity hours and ticket/menu prices link to the venue’s official site or booking/menu page. RTC route schedules link to the [Regional Transportation Commission of Southern Nevada](https://www.rtcsnv.com/).
- A blank table cell means the value was not confirmed from an official source. It is not zero, free, closed, or within one hour. The reason and source are listed on [Flagged for Review](flagged.html).
- Price totals for two are calculated only from a published per-person or set-menu price, and the basis/exclusions are shown. Partial entrée-only examples are not presented as full dinner totals.
- Travel-time claims are not inferred from a route map. Las Vegas has RTC buses; no RTC subway is listed. The RTC trip planner did not return captured hotel-to-destination itineraries in this research pass.
- Data check date: **26 November 2026**. Published hours, menus, offers and ticket availability can change before the 2027 trip.

## Important unresolved points

- The preferred date range is 3 nights, while the broader target is 1–2 weeks and the hotel comparison requests 7 nights.
- Direct February 2027 hotel booking checks did not return usable, comparable totals; no cheapest booking time is claimed.
- Room pages list bathroom features, but the captured wording does not explicitly say “private bathroom.”
- RTC one-hour route counts and several restaurant costs/hours/social profiles remain unverified and are shown as blank/flagged.

## Site implementation

This is a static GitHub Pages site: no build system or external JavaScript dependency is required. The pages share `assets/site.css`; research notes are in `research/`. For a local static preview, run `python3 -m http.server 8000` from the repository root.
