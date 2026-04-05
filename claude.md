# PROJECT: "One Sensor, One Year" — Data Art Series

## What This Is

A recurring series where each edition takes a single data stream, visualizes its entire year as generative art, and pairs it with a narrative essay. See each edition's own `claude.md` for edition-specific context.

## Repo Structure

```
editions/
  india-breathes/    # Edition 1: India's electricity grid, 2024 (complete)
  texas-grid/        # Edition 2: ERCOT electricity grid, 2024 (in progress)
```

Each edition directory contains: `data/`, `notebooks/`, `art/`, `essay/`, `scripts/`, `web/`

## The Creator

Pushpesh Sharma — Director of Product Management at AspenTech (Emerson Electric), PhD in Chemical & Biomolecular Engineering. Based in Houston, TX. Indian-born.

## Output Format (Each Edition)

1. **The Art** — generative visualization, no axes/labels, printable as poster
2. **The Anatomy** — annotated version pointing out key moments
3. **The Story** — ~1,000-word narrative essay for smart general audience
4. **The Interactive** — web page with hover/scrub, toggles, zoom, magazine-quality design

## Technical Preferences

- Python with pandas, matplotlib/seaborn for exploration
- D3.js, Three.js, or p5.js for generative art
- React or vanilla HTML for interactive web pages
- Bright, readable color palette (not dark mode)
- Clean, magazine-quality typography

## Style & Tone

- Think: The Pudding, or an NYT interactive feature
- Data-driven but emotional
- Respect complexity — no simplistic narratives

## Deployment

- Edition 1 (India Breathes): GitHub Pages, deployed from `editions/india-breathes/web/`
