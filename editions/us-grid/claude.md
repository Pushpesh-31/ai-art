# Edition 2: US Grid — EIA-930, 2025

## What This Is

Edition 2 of "One Sensor, One Year." One year of the United States electricity grid — generation by fuel type across the lower-48 and the major balancing authorities — visualized as generative art and paired with narrative.

Originally scoped as Texas-only; pivoted 2026-04-14 to a US-wide lens to match Edition 1's national scope. Texas remains the higher-fidelity *case-study lens* in `editions/texas-grid/` (15-min ERCOT XLSX feed); US-wide work uses EIA-930's hourly API.

## Why The US

- The largest grid in the world by GDP served, fragmented across ~66 balancing authorities
- Distinct regional stories: coal Appalachia, wind Plains, solar Southwest, gas Gulf, nuclear Northeast
- The AI / data-center load thread: PJM's "Data Center Alley" is bending the national load curve
- Renewable build-out is asymmetric — the regional contrasts are the story

## The Data

### Primary: EIA-930 v2 API — Hourly fuel mix by Balancing Authority
- **Endpoint:** `https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/`
- **Auth:** API key in `.env` at repo root (`EIA_API_KEY=...`, gitignored)
- **Resolution:** Hourly
- **Fuel codes (9):** COL, NG, NUC, WND, SUN, WAT, OTH, BAT (signed), UES
- **Coverage:** 2018-present; this edition = 2025 calendar year
- **Scope:** US48 aggregate + top-10 BAs (CISO, PJM, MISO, ERCO, SWPP, NYIS, ISNE, TVA, BPAT, SOCO)

### Future / supplementary
- **EIA Form 860** plant inventory (lat/lon, capacity, fuel) for the headline plant-level map. Standalone ZIP at eia.gov, ~1-year lag.
- **EIA-930 region-data endpoint** for demand + interchange flows
- **ERCOT XLSX (Texas Edition)** as the high-fidelity detail lens

## US Grid Story (Key Context)

- ~4,200 TWh of generation per year (vs Texas's ~530 TWh, India's ~1,700 TWh)
- Natural gas is the largest fuel (~40%); coal continues to decline; renewables ~25% and rising
- ~66 balancing authorities, 7 grid regions; not one grid but a federation
- AI/data-center load is flattening the daily demand curve — historically peaky, now baseload-like
- The clean-energy transition is regional: SPP and CAISO leading, MISO lagging, SOCO coal-heavy

## Comparison Across Editions

|  | Ed1 India Breathes | Ed2 US Grid | Texas (case-study lens) |
|--|--|--|--|
| Dominant fuel | Coal (~75%) | Natural gas (~40%) | Natural gas (~45%) |
| Resolution | Daily | Hourly | 15-minute |
| Source | CEA daily reports | EIA-930 API | ERCOT XLSX |
| Geography | National + 5 regions | National + 10 BAs | One BA (ERCO) |
| Scale | 1.4B people | 330M people | 30M people |

## Style & Visual Conventions

- **Notebooks:** matplotlib + seaborn (NOT plotly like Ed1) — `sns.set_theme(style='whitegrid', palette='muted')`
- **Fuel palette:** reuse the Texas N01 colors, mapped to EIA codes (COL→coal, NG→gas_total, NUC→nuclear, WND→wind, SUN→solar, WAT→hydro, OTH→other, BAT/UES→grey)
- **Stack order:** fossil first (COL, NG), then NUC, then renewables (WND, SUN, WAT, OTH), then storage (BAT, UES)

## Notebook Plan

1. **01_download_eia930** — pull US48 + 10 BAs hourly for 2025; cache raw JSON; write CSV + parquet
2. **02_us_statistics** — annual TWh, fuel shares, daily volatility, peak/trough days, top-10 BA share table
3. **03_emissions** — eGRID factors → CO₂ intensity nationally and per BA
4. **04_seasonal** — monthly stack, regional seasonality (e.g. SPP wind in spring vs CAISO solar in summer)
5. **05_trajectory** — multi-year US48 (separate later pull) — coal decline, renewable build, gas plateau
6. **06_hourly_dispatch** — daily/weekly dispatch curves; AI flat-load thread
7. **07_events** — peak weeks (heat dome, polar vortex, hurricane response)
8. **headline art** — plant-level map from Form 860 (replaces the scrapped animations prototype)
