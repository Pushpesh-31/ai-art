# Edition 2: Texas Grid — ERCOT, 2024

## What This Is

Edition 2 of "One Sensor, One Year." One year of Texas's electricity grid — generation by fuel type, demand peaks, seasonal swings — visualized as generative art and paired with narrative.

## Why Texas

- ERCOT is an **island grid** — disconnected from the rest of the US. Texas powers itself.
- Natural gas dominates (~45%), unlike India's coal story — a fundamentally different energy portrait
- Texas is the **US leader in wind**, with solar exploding (surpassed coal in 2025)
- **Winter Storm Uri** (Feb 2021) killed 200+ people and reshaped the grid — 40+ GW added since
- The creator lives in Houston. This is his grid.

## The Data

### Primary: ERCOT Fuel Mix Report
- **Source:** https://www.ercot.com/gridinfo/generation
- **Files:** Fuel Mix Report 2007-2024 (ZIP), Fuel Mix Report 2025 (XLSX)
- **Resolution:** Hourly
- **Fuel types:** Wind, Solar, Coal/Lignite, Natural Gas, Nuclear, Hydro, Other
- **Coverage:** 2007-present

### Supplementary: EIA Hourly Grid Monitor
- **URL:** https://www.eia.gov/electricity/gridmonitor/
- **Coverage:** ERCOT region, hourly, 2015-present
- **Adds:** Demand data, net generation, interchange

### Supplementary: ERCOT Load Archives
- **URL:** https://www.ercot.com/gridinfo/load/load_hist
- **Adds:** Historical hourly load data

## Texas Grid Story (Key Context)

- Texas is the only US state with its own independent grid (ERCOT serves ~90% of Texas load)
- Natural gas provides ~45-50% of generation (vs India's 75% coal)
- Wind generation can exceed 30% on peak days
- Solar capacity growing exponentially — surpassed coal as 3rd-largest source in 2025
- Summer peak demand driven by AC (August heat vs India's May-June pre-monsoon peak)
- Winter vulnerability exposed by Uri — grid hardening is ongoing
- 90% of new capacity additions are renewable (wind, solar, batteries)
- Per capita consumption ~15,000 kWh (vs India's 1,395 kWh) — mature vs growing grid

## Comparison with Edition 1

| | India Breathes | Texas Grid |
|--|--|--|
| Dominant fuel | Coal (~75%) | Natural gas (~45%) |
| Renewable story | Solar + hydro growing | Wind + solar booming |
| Seasonal driver | Monsoon (Jun-Sep) | Summer heat (Jun-Aug) |
| Grid drama | Coal vs renewables race | Independence + Uri aftermath |
| Scale | 1.4B people, 3rd largest globally | 30M people, own isolated grid |
| Hourly data? | Daily only | Hourly available |

## Exploration Phase

1. **Download and parse** ERCOT Fuel Mix data for 2024
2. **Filter to calendar year 2024** (Jan 1 - Dec 31)
3. **Aggregate to daily** (hourly -> daily totals by fuel type) for comparability with Edition 1
4. **Basic statistics:** min, max, mean, std for each fuel type
5. **Time series plots:** overlay all fuel types for the year
6. **Seasonal patterns:** monthly averages — where does summer AC load show up? When does wind peak?
7. **The renewable share:** daily renewable % of total. When did it peak? Trend?
8. **Year-over-year:** 2024 vs 2023 vs 2022 — how fast is solar growing?
9. **Notable events:** highest/lowest generation days, biggest renewable share, any extreme weather events
10. **Weekly patterns:** weekend effect in Texas?
11. **The Uri question:** compare Feb 2024 vs Feb 2021 grid performance
12. **Hourly deep-dive:** since we have hourly data (unlike India), explore intra-day patterns — solar noon peak, wind overnight, gas ramping

## Art Direction

Same three forms as Edition 1 (calendar spiral, heartbeat strip, radial bloom). Texas-appropriate palette — consider:
- Texas sky blues, sunset oranges, dust browns
- Or: ERCOT brand colors adapted
- The proven palettes from Edition 1 (Earth & Sky, Warm Spectrum) may also work well
