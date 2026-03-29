# PROJECT BRIEF: "One Sensor, One Year" — Edition 1: India's Grid, 2024

## What This Is

"One Sensor, One Year" is a recurring series where each edition takes a single data stream, visualizes its entire year as generative art, and pairs it with a narrative essay that tells the human story the data contains. The art makes you feel it. The story makes you understand it.

This is Edition 1: **"India Breathes"** — India's electricity grid, calendar year 2024.

## The Creator

Pushpesh Sharma — Director of Product Management at AspenTech (Emerson Electric), PhD in Chemical & Biomolecular Engineering, Chair of SPE DSEATS (12,000+ member global community). Deep roots in process engineering, simulation, and industrial AI. Based in Houston, TX. Indian-born. This project bridges his technical depth with a creative vision — data as art, infrastructure as narrative.

## The Data

### Primary Dataset: CEA Daily Generation Report (Robbie Andrew's cleaned version)
- **URL:** https://robbieandrew.github.io/india/data/CEA_DGR_data.csv
- **Metadata:** https://robbieandrew.github.io/india/data/CEA_DGR_metadata.json
- **Resolution:** Daily
- **Coverage:** April 2018 to present (updated as of March 26, 2026)
- **Key columns (all in MU = GWh):**
  - `yyyymmdd` — Date as integer (20240101 format)
  - `CEA.DGR.COL` — Coal generation (~2500-3500 MU/day, dominant source)
  - `CEA.DGR.LIG` — Lignite (~60-110 MU/day)
  - `CEA.DGR.GAS` — Natural gas (~90-190 MU/day, volatile)
  - `CEA.DGR.THM` — Total thermal (coal + lignite + gas + diesel)
  - `CEA.DGR.NUC` — Nuclear (~100-140 MU/day, very steady baseline)
  - `CEA.DGR.HYD` — Hydro (huge seasonal swing: ~200 winter → 700+ monsoon)
  - `CEA.DGR.WND` — Wind (available from July 2019; monsoon peak 400+, winter trough 20-50)
  - `CEA.DGR.SOL` — Solar (available from July 2019; growing year over year)
  - `CEA.DGR.OTH` — Other renewables
  - `CEA.DGR.RES` — Total renewable energy sources
  - `CEA.DGR.TOT` — Total generation (excl. renewables — confusingly named)
  - `CEA.DGR.BHU` — Bhutan hydro imports

### Secondary Dataset: POSOCO/Grid-India (regional + demand)
- **URL:** https://robbieandrew.github.io/india/data/POSOCO_data.csv
- **Metadata:** https://robbieandrew.github.io/india/data/POSOCO_metadata.json
- **Coverage:** March 2013 to present
- **Adds:** Regional demand breakdown (NR, WR, SR, ER, NER) and state-level demand

### Supplementary: Mendeley Hourly Dataset
- **URL:** https://data.mendeley.com/datasets/y58jknpgs8/2
- **Title:** "Electricity Demand, Solar and Wind Generation Data (September 2021 - June 2025) of India at 1-hour interval"
- **Resolution:** Hourly
- **Adds:** Intra-day patterns (when India wakes, peaks, sleeps)

### Supplementary: Ember India Data
- **URL:** https://ember-energy.org/data/india-electricity-data/
- **Adds:** Monthly/yearly generation, capacity, and emissions at national and state level

### Data Citation
Andrew, R. 2025: "Indian Energy and Emissions Data", available at: https://robbieandrew.github.io/india/
Original paper: Andrew, R. 2020: "Timely estimates of India's annual and monthly fossil CO2 emissions", Earth System Science Data 12, 2411–2421

## About Robbie Andrew (credit prominently)
Senior researcher at CICERO Center for International Climate Research, Oslo, Norway. Core member of the Global Carbon Project. He painstakingly compiles India's energy data from dozens of public government sources (Ministry of Coal reports, Coal India monthly reports, CEA daily generation reports, PPAC gas reports, etc.) into clean, machine-readable CSVs — work that India's own government doesn't do in consolidated form. His data is updated regularly (last update: March 26, 2026). This project builds on his research infrastructure.

## India's Grid Story (Key Context for 2024-2025)

- India is the 3rd largest electricity producer/consumer globally
- 75% of power still comes from coal — but renewables were 89% of new capacity additions in FY 2024-25
- Electricity demand grew ~6% in 2024 (+100 TWh year-over-year)
- Solar capacity crossed 100 GW in January 2025
- On July 29, 2025, renewables met 51.5% of India's total electricity demand for the first time ever
- Wind and solar would need to grow 4x faster than 2024 levels for thermal generation to flatline
- The tension: India is sprinting toward renewables AND burning more coal than ever, simultaneously
- Per capita consumption is only 1395 kWh (vs global average 3486 kWh) — massive growth ahead
- In H1 2025, clean energy growth was 3x demand growth, and coal fell 3.1%

## The Output Format (Each Edition)

### 1. The Art
A single generative visualization encoding an entire year of data. No axes, no labels. Just the data's shape, color, and rhythm. Should be printable as a poster. Multiple art forms to explore:
- **Calendar spiral** — 365 days in a circle, color = intensity or fuel mix
- **Heartbeat strip** — horizontal timeline, amplitude = demand
- **Radial bloom** — each day is a petal, shape = generation mix
- Let the data decide which form works best. Try all three, compare.

### 2. The Anatomy
An annotated version of the same art, pointing out key moments:
- Monsoon season (June-September): solar dips, hydro surges, wind peaks
- Summer heatwave (May-June): demand spikes, coal maxes out
- Diwali: demand pattern
- Winter: coal dominance, low renewables
- Weekend vs weekday patterns
- Any anomalies or records

### 3. The Story
A ~1,000-word narrative essay. Not a technical report. A story about what this sensor witnessed over 365 days. Written for a smart general audience — someone who reads The Economist or Wired. The grid as India's metabolism.

### 4. The Interactive
A web page (React or HTML) where users can:
- Hover/scrub through time
- See the generation mix change day by day
- Toggle fuel types on/off
- Zoom into notable events
- Beautiful, magazine-quality design

## Exploration Phase (START HERE)

Before building any final outputs, we need to explore the data together and discover the story. This means:

1. **Download and parse** the CEA_DGR_data.csv
2. **Filter to calendar year 2024** (20240101 to 20241231)
3. **Basic statistics:** min, max, mean, std for each fuel type
4. **Time series plots:** overlay all fuel types for the year
5. **Seasonal patterns:** monthly averages by fuel type — where does the monsoon show up? When does coal peak?
6. **The renewable share:** calculate daily renewable % of total generation. Plot it. When did it peak? What's the trend?
7. **Year-over-year comparison:** 2024 vs 2023 vs 2022 — is solar really growing that fast?
8. **Notable events:** find the days with highest/lowest total generation, biggest renewable share, biggest coal day
9. **Weekly patterns:** is there a weekend effect?
10. **The crossover question:** on how many days in 2024 did renewables generate more than nuclear? More than hydro? Is there a day where wind+solar exceeded gas?

Present findings conversationally. We're discovering the story together, not writing a report.

## Technical Preferences
- Python with pandas, matplotlib/seaborn for exploration
- For final visualizations: D3.js, Three.js, or p5.js for generative art
- For the interactive web page: React with Recharts or D3
- Bright, readable color palette (not dark mode)
- Clean, magazine-quality typography

## Future Editions (Teased in Edition 1)
- Edition 2: **Houston Air** — PM2.5 from the Ship Channel, one year
- Edition 3: **The Heartbeat** — one industrial compressor, vibration data, run to failure
- Edition 4: **The Price** — Brent crude, tick by tick, one year

## Style & Tone
- Stylish but grounded. Think: The Pudding, or an NYT interactive feature
- Data-driven but emotional. The numbers should make you feel something
- Respect the complexity — India's grid story isn't simple "coal bad, solar good"
- Credit Robbie Andrew prominently — this builds on his work

---

*Session origin: Brainstorming session March 2026. Full idea bank saved separately.*
