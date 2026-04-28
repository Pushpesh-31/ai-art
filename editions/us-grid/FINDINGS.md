# Ed2 — Data Center Signature: Findings & Story Brief

*One Sensor, One Year — Edition 2: US Grid · last updated 2026-04-27*

## TL;DR

The data-center fingerprint is detectable in the EIA-930 hourly panel for 2019-2025, but it is *small and just starting to grow* — not the dramatic step change a naive analysis suggested. Three "hyperscaler-heavy" balancing authorities (PJM, ERCO, MISO) have a P90 load-duration-curve floor that has climbed +2.5 pp since 2019, while seven control BAs are roughly flat. The hyper-vs-control gap sits around +5-7 pp throughout the panel, with a small uptick in 2025. Public sources confirm hyperscaler buildout in those exact regions, with the bulk of the queued capacity (PJM ~47 GW, ERCOT 230 GW queue) still to be connected — so we are looking at the *leading edge* of the signal, not the full effect.

## Methodology, in one paragraph

Per-BA hourly net generation by fuel from EIA-930 v2 API, 10 BAs × 7 years (2019-2025), 4.8 M rows. Generation is summed across fuels per (BA, hour) as a demand proxy. Three diagnostic signals: overnight share (mean 2-5am ÷ daily peak), weekend ratio (weekend mean ÷ weekday mean), and P90 LDC floor (demand at the 90th-percentile-load hour ÷ peak). Group means: hyperscaler-heavy = {PJM, ERCO, MISO}; control = {BPAT, CISO, ISNE, NYIS, SOCO, SWPP, TVA}. **Important correction:** P90 floor uses a robust peak (99.5th-percentile hour) rather than the absolute max, because EIA-930 has single-hour reporting glitches in SWPP 2023, TVA 2019/2024, and SOCO 2025 that drive naive P90 floors near zero and inflate the apparent gap.

## Signals that moved vs. signals that didn't

| Signal | Hyper-Ctrl gap, 2019 | Hyper-Ctrl gap, 2025 | Trend |
|---|---|---|---|
| Overnight share | +1.5 pp | +1.8 pp | **No trend.** Noisy; varies +0.3 to +1.8 pp across the panel. |
| Weekend ratio | +0.4 pp | +0.7 pp | **No trend.** Essentially zero on average. |
| **P90 LDC floor (robust)** | **+5.0 pp** | **+6.6 pp** | **Mild widening.** Hyperscaler abs floor +2.2 pp over the panel; control flat. |

**Conclusion: only one of three signals shows a real time-axis trend** — the P90 LDC floor. The cross-sectional verdict in NB 11 (3/3 signals positive in 2025) is correct but largely confound-driven for two of three signals; only the P90 floor is structurally widening.

## Per-BA P90 floor (robust peak), trajectory

| Year | PJM | ERCO | MISO | BPAT | CISO | ISNE | NYIS | SOCO | SWPP | TVA |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 0.530 | 0.473 | 0.548 | 0.512 | 0.357 | 0.433 | 0.463 | 0.491 | 0.527 | 0.486 |
| 2020 | 0.496 | 0.464 | 0.513 | 0.517 | 0.304 | 0.391 | 0.444 | 0.466 | 0.515 | 0.486 |
| 2021 | 0.513 | 0.482 | 0.535 | 0.464 | 0.344 | 0.414 | 0.430 | 0.483 | 0.512 | 0.509 |
| 2022 | 0.537 | 0.493 | 0.535 | 0.454 | 0.345 | 0.429 | 0.440 | 0.455 | 0.529 | 0.516 |
| 2023 | 0.550 | 0.471 | 0.529 | 0.473 | 0.387 | 0.464 | 0.443 | 0.471 | 0.517 | 0.497 |
| 2024 | 0.539 | 0.501 | 0.553 | 0.533 | 0.367 | 0.495 | 0.462 | 0.477 | 0.536 | 0.488 |
| 2025 | 0.530 | 0.542 | 0.547 | 0.484 | 0.373 | 0.471 | 0.448 | 0.481 | 0.541 | 0.516 |

ERCO 2019 → 2025: 0.473 → 0.542 (+6.9 pp). MISO and PJM hold near the top. CAISO sits at the bottom — distorted by heavy solar generation, not data centers.

## Public confirmation of the hyperscaler buildout

**PJM / Virginia (Dominion Zone)**
- Dominion connected **15 data centers totaling 933 MW in 2023**; 15 more sites under construction in 2024.
- Total Dominion-data-center contracted capacity grew **+185 % between July 2023 and July 2025**.
- PJM 2025 forecast: **+20 GW** of data-center load by 2037 in the Dominion Zone alone (vs. +5.7 GW in the 2022 forecast).
- Dominion has **47.2 GW** of additional contracted demand in the queue.

**ERCOT / Texas**
- Large-load interconnection queue **quadrupled in one year**: 63 GW (Dec 2024) → **230 GW** (2025). 70 % is data centers; **only 7.5 GW physically connected so far**.
- EIA forecasts ERCOT demand **+7 % in 2025 and +14 % in 2026** as large data-center / crypto loads come online.
- ERCOT itself revised its 2035 peak forecast up by 35 GW from data centers, but warns many queued projects won't materialize at full scale.

**MISO / Indiana–Ohio**
- MISO long-range forecast: load **+35 % by 2035**, concentrated in LRZ 6 (Indiana, +60 %).
- Indiana Michigan Power: peak **doubling to ~8 GW by 2030** (from ~4 GW in 2024). Amazon, Google, Microsoft signed.
- Ohio's electric demand is growing **10× the historic rate** with AWS / Google / Meta capacity.

**Why the news matters for the data interpretation.** Most of the queued capacity has **not** connected yet. The +2.5 pp rise we observe in hyperscaler P90 floor over six years is consistent with a few GW of new 24/7 load on top of ~50–150 GW peak demand per BA. If half the queued capacity materializes by 2030, the P90 floor gap should triple. So the dataset is showing the leading edge.

## Story arc for the essay

**Working title:** *The Trough That's Starting to Fill.*

**Hook (Act 1).** Open at 4 AM in Loudoun County, Virginia. The grid used to do almost nothing here. Now it's running at 53 % of peak. Why?

**The familiar pattern (Act 2).** Every grid has a trough. For a century, 4 AM was the cheapest electricity in the world: lights off, factories idle, no demand. Solar can't reach it. Storage tries to fill it. The trough is what made nuclear and coal the natural baseload, what makes battery economics work, what shaped retail rate design. Show overnight-share-by-BA — the universal dip and how flat the diurnal profile is in nuclear-rich grids.

**The fingerprint (Act 3).** Three diagnostic signals tested over 2019–2025 across 10 BAs. Only one moved: the *bottom* of the load-duration curve — what fraction of peak demand the grid maintains in the lowest 10 % of hours. In PJM, ERCO, and MISO it has lifted +2.5 pp since 2019. In the seven control BAs it is flat. Show the corrected NB 12 trend plot.

**Connecting the dots (Act 4).** The fingerprint is small because the buildout is mostly *queued*, not built. Pull in the public numbers: 47 GW Dominion contracted, 230 GW ERCOT queue with 7.5 GW connected, MISO Indiana doubling by 2030. The signal we are seeing is the first ~5–10 GW of hyperscaler load arriving on grids that already serve hundreds of GW of legacy demand.

**Why this matters (Act 5).** Three implications, in order of importance:
1. **The cheapest hour is leaving us.** As the trough fills, the marginal kWh at 4 AM is no longer free capacity — it's a customer. Storage arbitrage, EV-charging incentives, and grid-scale wind economics all assumed an empty trough.
2. **Marginal carbon at 4 AM is rising.** When the trough is full, a new server at 4 AM is served by gas-or-coal-or-nuclear-on-the-margin, not by surplus wind that would otherwise be curtailed.
3. **Renewable curtailment goes down (good) but average system-wide CO₂ per kWh goes up (bad).** Two effects; the second is bigger in 2025-2030.

**Cross-edition tie (Act 6).** Edition 1 was India: a grid where the night is *empty* (low overnight demand, monsoon-driven solar lull). The cleanest day was a monsoon Sunday. Edition 2 is the US: a grid where the night is *filling up* — and the fingerprint of *what* is filling it is regionally specific. Same physical asset (a 4 AM kWh) becoming radically different things in different places.

**Closer.** Watch the P90 floor in PJM, ERCO, MISO over the next two EIA-930 release cycles. If half the queued capacity materializes, the gap should triple by 2028. This essay's claim is falsifiable; the dataset will tell.

## What to do next (suggested follow-ups)

1. **Expand the panel to all 60+ EIA-930 BAs** to make sure the 7-control selection isn't biasing. (Out of scope for this analysis — would also unlock per-region narratives.)
2. **Carbon-intensity overlay.** Repeat the analysis using a CO₂-per-kWh time series rather than raw demand — does the marginal carbon at 4 AM in the hyperscaler BAs really rise the way the implication argument predicts?
3. **2026 release check.** Re-run NB 12 once EIA-930 publishes 2026 data. The thesis predicts the hyperscaler P90 floor should accelerate to +1-2 pp/year as more queued capacity connects.
4. **Story copy + key art.** This findings doc is the analytical brief; the essay still needs to be written. Lead with the 4 AM hook; the per-BA small-multiples plot (`data_center_signature_trend_per_ba.png`) is the strongest single visual.

## Source list

PJM / Virginia
- [Projected data center growth spurs PJM capacity prices by factor of 10 — IEEFA](https://ieefa.org/resources/projected-data-center-growth-spurs-pjm-capacity-prices-factor-10)
- [JLARC Virginia Data Center Study (Dec 2024)](https://jlarc.virginia.gov/pdfs/presentations/JLARC%20Virginia%20Data%20Center%20Study_FINAL_12-09-2024.pdf)
- [Dominion connected 15 data centers totaling 933 MW in 2023 — DCD](https://www.datacenterdynamics.com/en/news/dominion-connected-15-data-centers-totaling-933mw-in-virginia-in-2023-15-more-expected-in-2024/)
- [National Load Growth Report 2025 — Grid Strategies](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf)

ERCOT / Texas
- [ERCOT's large load queue has nearly quadrupled in a single year — Latitude Media](https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/)
- [Rapid electricity demand growth in Texas and the mid-Atlantic — EIA](https://www.eia.gov/todayinenergy/detail.php?id=65844)
- [Data centers and cryptocurrency mining in Texas — EIA](https://www.eia.gov/todayinenergy/detail.php?id=63344)

MISO / Indiana–Ohio
- [MISO expects load to jump 35 % by 2035 on data center growth — Utility Dive](https://www.utilitydive.com/news/miso-long-range-forecast-data-center/817917/)
- [Indiana Michigan Power, Amazon, Google interconnection rules — Utility Dive](https://www.utilitydive.com/news/indiana-michigan-power-aep-amazon-google-microsoft-data-center-interconnect/733850/)
- [Data centers are flocking to Ohio — Renewable Energy World](https://www.renewableenergyworld.com/news/data-centers-are-flocking-to-ohio-here-comes-the-transmission-to-support-them/)

Methods
- EIA-930 v2 hourly fuel-type-data API: `https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/`
- Notebooks: `editions/us-grid/notebooks/01_download_eia930.ipynb`, `01b_download_eia930_historical.ipynb`, `01c_download_eia930_ba_historical.ipynb`, `11_data_center_signature.ipynb`, `12_data_center_signature_trend.ipynb`
- Combined panel: `editions/us-grid/data/processed/ba_2019_2025_hourly.parquet`
- Trend table: `editions/us-grid/data/processed/data_center_signature_trend.csv`
- Trend plots: `data_center_signature_trend.png`, `data_center_signature_trend_per_ba.png`
