# [TITLE — TBD]

*Draft for SPE Journal of Petroleum Technology — first-person analytical voice — ~2,400 words*

*Author: Pushpesh Sharma*

*Working title candidates (pick one or veto):*
1. *The Trough Is Starting to Fill: What EIA-930 Already Tells Us About AI Power Demand*
2. *Power Is the Bottleneck: Reading the Leading Edge of AI's Grid Footprint*
3. *AI's First Energy Bill: A Leading-Edge Fingerprint, and a Gas Story Hiding in Plain Sight*

---

## [HOOK A — Loudoun]

It is 4 a.m. on a Tuesday in Loudoun County, Virginia. Most of the East Coast is asleep, and on most weeknights of most decades the PJM grid would be drifting through its overnight trough — power plants throttled back, wholesale prices near floor, the night shift waiting for daybreak.

Tonight, demand has barely moved off the evening peak.

A few miles down the road, behind a chain-link fence and a row of pine trees, a 200-megawatt data hall is running an inference workload at full utilization. There are dozens like it in the county. Dominion Energy, the local utility, now has 47 gigawatts of contracted data-center load in its development pipeline[^1] — roughly two-thirds of the entire ERCOT system peak, dedicated to a 30-mile radius of Northern Virginia.

That number is not a forecast. It is signed contracts. And it is why, for the first time in fifteen years, the U.S. power industry is running out of trough.

## [HOOK B — Permian / Abilene]

The Lancium Clean Campus in Abilene, Texas was, until recently, an unremarkable patch of West Texas land — flat, dry, useful mainly for cattle and a wind farm. Today it is the first site of OpenAI's Stargate project. By the time it is complete it will draw 1.2 gigawatts of power.

Roughly 360 megawatts of that power will come from ten gas turbines installed on the site itself: five Solar Turbines Titan 350s and five GE LM2500 aeroderivatives. In January 2025 the operator filed a permit modification with the Texas Commission on Environmental Quality raising the LM2500 annual run-hours from 5,880 to 8,760 — continuous, year-round operation — for, in the permit's words, "onsite use only for data centers and computing."[^16]

The grid was not consulted. The grid could not have helped if it had been.

Across the country, deals like this are being signed faster than the wholesale market can price them. Dominion Energy alone now has 47 gigawatts of contracted data-center load in its PJM pipeline.[^1] Power has stopped being a line item on the AI industry's balance sheet. It is becoming the binding constraint.

---

## Why this is a power story, not a tech story

The AI buildout is unusual as an electricity load. A modern hyperscaler campus does not look like the data centers we built in the 2010s, and it does not look like the office parks and shopping malls that drove the last several decades of demand growth. It looks more like a smelter.

Three properties matter.

**First, capacity factor.** Training runs are batchable in principle, but in practice the training is now near-continuous and inference is constant by definition. GPU clusters in production AI sites run at near-full utilization 24 hours a day, every day. The load shape is flat.

**Second, density.** A 2015-era cloud data center drew 10 to 30 megawatts at full build. A modern AI campus targets 100 to 300 megawatts. The largest in the queue — Stargate's Abilene phase, xAI's Memphis Colossus, the Homer City Energy Campus in Pennsylvania — are crossing the 1-gigawatt mark. That is the scale of a small refinery.

**Third, siting timeline.** Hyperscaler campuses are built on 18-to-36-month construction cycles. New gas plants take four to six years from permit application to commercial operation. Long-haul transmission lines move on seven-to-ten-year cycles. New nuclear takes longer than any of these. The mismatch between when load wants to connect and when generation can be delivered is the central economic fact of the next five years.

The forecast headlines have caught up to this reality. Lawrence Berkeley National Laboratory's December 2024 update[^2] put 2023 U.S. data-center electricity consumption at 176 TWh, or 4.4 percent of total U.S. electricity, and projected a 2028 range of 325 to 580 TWh — 6.7 to 12 percent. The International Energy Agency's *Energy and AI* report (April 2025)[^3] put global data-center demand at 415 TWh in 2024 and projected 945 TWh by 2030, with the U.S. contributing roughly half of net growth. Goldman Sachs Research projects U.S. data-center share of total power consumption rising from 3 percent in 2022 to 8 percent in 2030, requiring approximately $50 billion of new generation capital.[^4] EIA's *Annual Energy Outlook 2025*[^5] is the cleanest signal: the projected 2024-to-2050 electricity demand growth is 117 percent larger than the same projection in AEO 2023. That is the first material upward revision in seven editions.

These are forecasts. What follows is what is already in the data.

## The leading-edge fingerprint

I pulled hourly generation data by fuel type for ten U.S. balancing authorities from EIA Form 930, covering 2019 through 2025.[^6] I grouped the BAs into two cohorts: a *hyperscaler-heavy* cohort — PJM (which includes Loudoun County), ERCOT, and MISO (which includes the Indiana data-center cluster) — and a *control* cohort of seven BAs without significant data-center buildout (BPA, CAISO, ISO-NE, NYISO, Southern Company, SPP, and TVA).

For each BA and year I computed three demand-shape statistics intended to surface a 24/7 baseload signature:

- **Overnight share.** Mean 2-to-5 a.m. demand divided by daily peak.
- **Weekend ratio.** Weekend mean divided by weekday mean.
- **P90 floor of the load duration curve.** Demand at the 90th-percentile hour, normalized to the 99.5th-percentile peak.

The first two statistics show a positive cross-section in 2025 — hyperscaler grids run higher than the control on both — but no time trend. They are confounded by fuel mix (nuclear-heavy grids structurally have higher overnight share) and by behavioral patterns that have nothing to do with data centers. They are not the signal.

The third is.

The hyperscaler cohort's mean P90 floor rose from 0.517 in 2019 to 0.539 in 2025 — a 2.5-percentage-point absolute increase, with the largest steps in 2024 and 2025. The control cohort's P90 floor stayed flat at approximately 0.47 across the same period.

The trend, however, is not uniform across the three hyperscaler grids. ERCOT alone moved from 0.473 to 0.542 — a 6.9-percentage-point jump that is, by itself, doing essentially all of the cohort-mean work. PJM is roughly flat in the EIA-930 data; MISO is roughly flat. This is consistent with the rest of the article. Dominion Energy's 47 GW of contracted Northern Virginia data-center load is overwhelmingly *contracted*, not *operating* — and EIA-930 reports only PJM aggregate, where Dominion is roughly a third of total peak. MISO's Indiana data-center cluster is similarly mostly queued. ERCOT, smaller and more concentrated, is where the operating data-center load is large enough relative to the BA total to surface as a load-shape signal. The fingerprint is showing up exactly where we should expect it to show up first.

> **[CHART 1 — primary visual]**
> *Per-BA P90 LDC floor, 2019–2025. McKinsey-style small multiples; hyperscaler panels highlighted; ERCOT trend annotated as the largest single-BA shift in the panel.*

A methodological note for readers who want to reproduce the analysis. EIA-930 contains single-hour reporting glitches at several BAs in several years — SPP in 2023, TVA in 2024, Southern Company in 2025 — each with a single anomalous "peak" hour roughly two orders of magnitude above normal operating levels. A naive load-duration-curve normalization that uses the single maximum hour as the denominator collapses the LDC for those BA-years. The 99.5-percentile robust peak used here is standard load-research practice and is immune to the issue. The naive computation produces an apparent hyper-vs-control gap of 11.6 percentage points in 2025; the corrected number is 6.6 percentage points, stable across the panel. The corrected number is the right one to quote.

The interpretation is constrained, and it should be. EIA-930 reports balancing-authority totals; we cannot see individual data centers. The +2.5-percentage-point hyperscaler floor rise over six years is small in absolute terms, consistent with a few gigawatts of new 24/7 baseload arriving on top of a 50-to-150-gigawatt-peak system. It is real, it is in the right places, and it is the leading edge of a buildout that has not yet arrived.

The body of the curve is in the queue.

## Who is buying, and how fast

Hyperscaler power procurement has changed character over the past 24 months. Microsoft, Google, Amazon, and Meta — the original four large buyers — have moved from purchasing clean megawatt-hours on the open market to signing 20-year power purchase agreements for dedicated nuclear units, funding small modular reactor developers, and writing checks for behind-the-meter gas generation. The pace is unprecedented for an industry that historically did not own its own power supply.

The headline deals on the nuclear side. In September 2024 Microsoft and Constellation Energy announced a 20-year PPA to restart Three Mile Island Unit 1 — renamed the Crane Clean Energy Center — 835 MW, with online-date pulled forward from 2028 to 2027.[^8] In October 2024 Google contracted with Kairos Power for 500 MW of fluoride-salt small modular reactors.[^10] The same month Amazon led a $500 million Series C-1 in X-energy and signed agreements with Energy Northwest (320 MW initial) and Dominion (a memorandum of understanding for ~300 MW at North Anna), with a joint target of more than 5 GW of SMR capacity by 2039.[^11] Meta issued a nuclear request for proposals in December 2024 soliciting 1 to 4 GW; the awards were announced in January 2026 to Vistra (a 2.2 GW PPA from existing Comanche Peak units), Oklo, and TerraPower, totaling approximately 6.6 GW.[^12]

Not every nuclear deal has held up. Amazon's behind-the-meter agreement with Talen Energy at Susquehanna nuclear, originally for 300 MW with a contract envelope to 1,920 MW, was rejected by FERC in November 2024 and again on rehearing in April 2025. The matter is now before the Fifth Circuit.[^9] Behind-the-meter colocation at existing nuclear, once seen as the fastest path to signed power, is no longer clean.

The infrastructure-money side is larger and faster. The Stargate project — OpenAI, Oracle, SoftBank, and MGX — was announced in January 2025 with a stated investment of up to $500 billion by 2029.[^13] First site is the 1.2-gigawatt Crusoe-built campus in Abilene, Texas. Five additional sites were announced in September 2025; Oracle subsequently added 4.5 GW more, putting total planned capacity at roughly 7+ GW. CoreWeave-OpenAI signed approximately $11.9 billion in March 2025; CoreWeave-Meta is structured at $21 billion through 2032; Lambda-Microsoft signed multi-billion in November 2025.[^14]

The clearest market signal, however, is in the wholesale capacity price. PJM's 2025/2026 capacity auction cleared at $269.92 per megawatt-day in July 2024 — roughly nine times the prior year's $28.92.[^15] The 2026/2027 auction one year later cleared at $329.17, hitting the FERC-imposed price cap; the uncapped simulation was $388.57. In Dominion's zone the cleared price was $444. In Baltimore Gas & Electric's zone, $466. This is the grid operator telling the market that supply is structurally short.

> **[CHART 2 — capacity auction step]**
> *PJM RTO-wide capacity auction clearing prices, $/MW-day, 2023/2024 through 2026/2027. McKinsey-style stepped column chart with the takeaway as the title: "PJM's capacity price has risen 11× in two years."*

## The gas wedge

This is the section that matters most to readers of this journal, because it describes what the oil and gas industry is about to be selling.

Nuclear gets the headlines. But nuclear cannot be online by 2027. The hyperscalers know this, and they are building gas — sometimes through utility PPAs, increasingly behind the meter, at scales the data-center industry has never previously contemplated.

Three things are happening simultaneously.

**First, behind-the-meter gas at hyperscaler campuses is moving from prototype to industrial scale.** The Crusoe-built Stargate Phase 1 campus in Abilene is permitted for approximately 360 MW of on-site simple-cycle generation — five Solar Turbines Titan 350s and five GE LM2500 aeroderivatives. The January 2025 TCEQ permit modification raised the LM2500 annual run-hours from 5,880 to 8,760 (continuous) "for onsite use only for data centers and computing."[^16] Crusoe's broader supply agreement with GE Vernova — 29 LM2500XPRESS aeroderivative units totaling roughly 1 GW, ordered in two tranches in December 2024 and June 2025[^17] — is the largest single aeroderivative order on record. In March 2025 Crusoe and Engine No. 1 launched a joint venture to develop 4.5 GW of co-located gas-fired data-center campuses.[^18] VoltaGrid, the modular-gas-turbine specialist that has emerged as the dominant supplier in this segment, ended 2025 with a contracted backlog above 4,350 MW including 2.3 GW for Oracle in Texas (with Energy Transfer fuel supply), more than 1 GW with Vantage Data Centers, and a 400 MW Halliburton commitment for Eastern Hemisphere data centers in 2028.[^19] INNIO Jenbacher booked its largest-ever order — 92 of its 25 MW power packs, 2.3 GW total — for the VoltaGrid fleet. xAI's Memphis Colossus operates a similar architecture; the EPA found xAI in violation of the Clean Air Act in January 2026 over turbine units operating beyond permitted limits.[^20] These are not small experiments. Aggregated, the announced behind-the-meter gas capacity at AI campuses is now in the multiple-gigawatt range and growing monthly.

**Second, oil majors are entering the power business as a primary line.** ExxonMobil disclosed in December 2024 that it was in front-end engineering on a more than 1.5-gigawatt dedicated, off-grid, gas-fired plant for a single data-center customer with greater than 90 percent CCS capture, ready within five years. Dan Ammann, president of Low Carbon Solutions, framed it bluntly: *"We're in a unique position to provide low-carbon power at large scale on a very competitive and accelerated timeline."*[^21] In January 2025 Chevron announced a joint venture with Engine No. 1 and GE Vernova to deliver up to 4 GW of co-located gas-fired generation for U.S. data centers, using seven GE Vernova 7HA frames (slot-reserved), CCS-capable, with first power in 2027.[^22] EQT signed an agreement in July 2025 to be the exclusive supplier — approximately 0.66 Bcf/d — to the 4.4 GW Homer City Energy Campus in Pennsylvania, the largest gas-powered data-center campus announced in North America, with first power in 2027.[^23] Diamondback's CEO Travis Stice confirmed in February 2025 that Diamondback was forming a joint venture with a hyperscaler and a power developer to use Permian associated gas — more than 1 Bcf/d available — for behind-the-meter data-center power.[^24]

**Third, the OEM bottleneck.** This is the data point that should focus everyone's attention. GE Vernova ended 2025 with an 80-gigawatt heavy-frame gas-turbine backlog stretching through 2029, projected to grow to roughly 110 GW by year-end 2026. Q1 2026 hyperscaler-direct electrification orders alone hit $2.4 billion — more than the company booked in all of 2025 combined. H-class slots are effectively sold out through 2027; 2028 is approximately 90 percent booked; 2029 is approximately 70 percent booked.[^25] Siemens Energy sold 194 gas turbines in fiscal year 2025 (versus 100 in FY24) and is sitting on a €146 billion order backlog with more than €2 billion of grid-tech orders directly from hyperscalers.[^26] Mitsubishi Heavy Industries has announced it will double large-frame production capacity within two years.[^27] Wood Mackenzie projects gas-turbine prices will rise 195 percent by 2027 on the supply crunch.[^28]

> **[CHART 3 — OEM backlog table or chart]**
> *Heavy-frame gas-turbine backlogs by major OEM (GE Vernova, Siemens Energy, MHI), with hyperscaler-attributable orders called out. McKinsey-style horizontal bar with dual encoding (total backlog GW; hyperscaler share shaded).*

For midstream, the demand math is becoming concrete. On Kinder Morgan's Q2 2025 earnings call, CEO Kim Dang put the figure at 3 to 10 Bcf/d of incremental U.S. gas demand from AI data centers by 2030 — approximately 9 percent of current U.S. gas consumption. KMI's project backlog grew by $6 billion in twelve months.[^29] Energy Transfer's Q3 2025 call announced a $1.6 billion agreement to provide on-site gas and power for an unnamed investment-grade client; the CEO said: *"We have never seen this level of activity from a demand-pull standpoint."*[^30] Williams' commercialized backlog has crossed $5 billion.[^31] Wood Mackenzie's Henry Hub forecast — $5/MMBtu by 2030, $6 by 2035 — bakes in the data-center pull alongside continued LNG growth and reshoring of manufacturing.[^32]

The competition between LNG export and data-center buildout for the same molecules is now the central question for U.S. natural gas. EIA projects LNG gross exports rising from 14.9 Bcf/d in 2025 to 16.3 Bcf/d in 2026, with more than 15 Bcf/d of incremental production needed through 2030.[^33] The Haynesville and the Permian are the marginal molecules. They will not be marginal for long.

## What the queues are telling us

The data so far is the leading edge. The body of the curve is in two interconnection queues, and the energy industry knows to distinguish them — *queued generation* (power plants seeking to connect to the grid) is a different queue from *queued load* (data centers and large industrial customers seeking to connect *as a load*), with different processes, different scrutiny, and very different completion rates. Both matter.

The generation side is sobering. LBNL's *Queued Up 2025* edition, published December 2025, found that only 13 percent of capacity that requested interconnection between 2000 and 2019 reached commercial operation by the end of 2024. Seventy-seven percent withdrew. Median IR-to-COD time has roughly doubled, from less than two years for the 2000-2007 cohort to more than four years for the 2018-2024 cohort. Total active U.S. queue volume actually fell 12 percent year-over-year in 2024 — the first decline on record, attributable to FERC Order 2023 cleanouts of speculative projects.[^34]

The load side is where the headlines are. PJM's 2025 Long-Term Load Forecast projects approximately 32 GW of peak-load growth between 2024 and 2030, of which approximately 30 GW (94 percent) is attributable to data centers.[^35] ERCOT's large-load interconnection queue stood at approximately 233 GW in December 2025, up roughly 4× year-over-year, with more than 70 percent attributable to data centers; connected and operating large load is in the single-digit gigawatts.[^36] Texas Senate Bill 6 (signed in June 2025) added a $50,000-per-megawatt non-refundable interconnection fee, 100 percent contribution-in-aid-of-construction, and curtailment-during-emergency-shed obligations for loads connecting after December 31, 2025 — the state is now actively trying to slow the rush.[^37] MISO's MTEP25 plan includes 11.6 GW of large-load additions and 49 expedited project reviews; Indiana Michigan Power's peak demand is forecast to grow from 2.8 GW to more than 7 GW by 2030, driven by AWS in New Carlisle, Google in Fort Wayne, and Microsoft in LaPorte.[^38]

> **[CHART 4 — queue waterfall]**
> *Three-bar comparison for PJM, ERCOT, MISO: queued large-load (top of bar), signed/under-study (middle), connected/operating (bottom). McKinsey-style with the gap between top and bottom annotated as "the bottleneck."*

Even if half of the queued load actually materializes, the leading-edge fingerprint described above should approximately triple by 2028.

## A falsifiable prediction

A forecast that cannot be falsified is not useful, so I will commit to one.

If half of the currently queued hyperscaler load materializes by 2028, the hyperscaler-cohort mean P90 floor I computed in Section 3 should rise from today's 0.539 to roughly 0.58 to 0.60 — a 4-to-6 percentage-point move on top of the 2.5 already in the data. ERCOT alone, the cleanest single-BA instance, should cross 0.60.

If we see those numbers in 2028 EIA-930 data, the bottleneck thesis is confirmed and the gas industry's bet is paying off. If we don't, either the queues did not materialize — the project-withdrawal rates documented by LBNL suggest this is the central risk — or the hyperscalers found their power outside the EIA-930 lens, which would mean behind-the-meter gas had moved from a complement to the grid to a substitute for it. Either outcome is a story, with very different implications for the upstream side of the gas business.

Three indicators worth watching in the next 18 months:

1. **PJM's 2027/2028 capacity auction clearing price.** Above $300 per megawatt-day means the bottleneck is still binding.
2. **Heavy-frame slot availability at GE Vernova, Siemens Energy, and Mitsubishi for 2030.** If 2030 frames are placed in 2026, the OEM bottleneck has tightened beyond what current backlog implies.
3. **The EIA Form 930 P90 floors for ERCOT and PJM.** These update monthly and are the leading indicator that no one outside the load-research community is currently watching.

Power has been a cost on the AI industry's balance sheet. It is becoming a bottleneck. For the oil and gas industry, that bottleneck is a customer.

---

## Footnotes

[^1]: Dominion Energy quarterly load report to PJM Load Forecast Working Group, October 2025. https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/dominion-documentation.pdf

[^2]: Shehabi et al., *2024 United States Data Center Energy Usage Report*, LBNL-2001637, December 20, 2024. https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf

[^3]: International Energy Agency, *Energy and AI*, April 10, 2025. https://www.iea.org/reports/energy-and-ai

[^4]: Goldman Sachs Research, "AI is poised to drive 160% increase in data center power demand," May 14, 2024 (updated February 4, 2025). https://www.goldmansachs.com/insights/articles/AI-poised-to-drive-160-increase-in-power-demand

[^5]: U.S. Energy Information Administration, *Annual Energy Outlook 2025*, April 15, 2025. https://www.eia.gov/outlooks/aeo/

[^6]: U.S. Energy Information Administration, Form EIA-930 (Hourly Electric Grid Monitor). https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48

[^7]: EIA, "U.S. electricity demand reached an all-time high in summer 2024," September 2024. https://www.eia.gov/todayinenergy/detail.php?id=65864

[^8]: Constellation Energy, "Constellation to Launch Crane Clean Energy Center, Restoring Jobs and Carbon-Free Power to The Grid," September 20, 2024. https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html

[^9]: Utility Dive, "FERC rejects Talen-Amazon ISA," November 2024. https://www.utilitydive.com/news/ferc-interconnection-isa-talen-amazon-data-center-susquehanna-exelon/731841/ ; American Nuclear Society on April 2025 rehearing denial. https://www.ans.org/news/2025-04-16/article-6937/ferc-denies-talen-amazon-agreementagain/

[^10]: Kairos Power, "Google and Kairos Power Partner to Deploy 500 MW of Clean Electricity Generation," October 14, 2024. https://kairospower.com/external_updates/google-and-kairos-power-partner-to-deploy-500-mw-of-clean-electricity-generation/

[^11]: Amazon News, "Amazon nuclear small modular reactor net carbon zero," October 16, 2024. https://www.aboutamazon.com/news/sustainability/amazon-nuclear-small-modular-reactor-net-carbon-zero

[^12]: Meta Sustainability, "Accelerating the next wave of nuclear to power AI innovation," December 3, 2024. https://sustainability.atmeta.com/blog/2024/12/03/accelerating-the-next-wave-of-nuclear-to-power-ai-innovation/

[^13]: OpenAI, "Announcing the Stargate Project," January 21, 2025. https://openai.com/index/announcing-the-stargate-project/

[^14]: Data Center Frontier on Crusoe Abilene project finance, May 2025. https://www.datacenterfrontier.com/hyperscale/article/55276169/crusoe-adds-45-gw-natural-gas-to-fuel-ai-expands-abilene-data-center-to-12-gw ; CNBC on Lambda–Microsoft. https://www.cnbc.com/2025/11/03/lambda-ai-microsoft-nvidia.html

[^15]: PJM Inside Lines, "PJM Auction Procures 134,311 MW of Generation Resources," July 22, 2025. https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/ ; S&P Global Commodity Insights on the $269.92 clearing price. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/073024-pjm-power-capacity-auction-clears-at-record-high-price-of-26992mw-day-for-most-of-footprint

[^16]: TCEQ permit docket for Lancium Clean Campus / Crusoe Abilene. https://records.tceq.texas.gov/cs/idcplg?IdcService=TCEQ_EXTERNAL_SEARCH_GET_FILE&dID=8600163

[^17]: GE Vernova, "GE Vernova, Crusoe announce major 29-unit aeroderivative gas turbine deliver AI data centers," June 2025. https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers

[^18]: Business Wire, "Crusoe and Engine No. 1 Launch Joint Venture for 4.5 GW of Co-Located Gas-Fired Data-Center Campuses," March 17, 2025. https://www.businesswire.com/news/home/20250317173370/en/

[^19]: Power Magazine, "Oracle Taps VoltaGrid for 2.3 GW Modular Gas Fleet to Power AI Data Centers Across Texas." https://www.powermag.com/oracle-taps-voltagrid-for-2-3-gw-modular-gas-fleet-to-power-ai-data-centers-across-texas/ ; Vantage Data Centers and VoltaGrid release. https://vantage-dc.com/news/vantage-data-centers-and-voltagrid-establish-partnership-to-deploy-more-than-one-gigawatt-of-power-generation/ ; Halliburton, "VoltaGrid, Halliburton Accelerate Data Center Eastern Hemisphere." https://www.halliburton.com/en/about-us/press-release/voltagrid-halliburton-accelerate-data-center-eastern-hemisphere

[^20]: Inside Climate News on the EPA finding and the underlying permit history. https://insideclimatenews.org/news/17072025/elon-musk-xai-data-center-gas-turbines-memphis/ ; Southern Environmental Law Center on the appeal. https://www.selc.org/press-release/groups-appeal-permit-for-xais-south-memphis-data-center-decisions-around-unpermitted-methane-gas-turbines/

[^21]: Semafor, "ExxonMobil wants to make bespoke carbon-capture power plants for data centers," December 13, 2024. https://www.semafor.com/article/12/13/2024/exxonmobil-wants-to-make-bespoke-carbon-capture-power-plants-for-data-centers ; ExxonMobil corporate. https://corporate.exxonmobil.com/what-we-do/delivering-industrial-solutions/carbon-capture-and-storage/steel-ammonia-ai-what-cant-ccs-help-decarbonize

[^22]: Chevron press release, "Power Solutions for U.S. Data Centers," January 28, 2025. https://www.chevron.com/newsroom/2025/q1/power-solutions-for-us-data-centers ; S&P Global coverage. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/012825-chevron-engine-no-1-ge-vernova-to-power-us-data-centers

[^23]: Homer City Redevelopment release, July 15, 2025. https://www.homercityredevelopment.com/post/press-release-homer-city-redevelopment-announces-agreement-in-principle-for-eqt-corporation-to-supp ; Natural Gas Intelligence coverage. https://naturalgasintel.com/news/eqt-snags-two-natural-gas-supply-contracts-including-for-massive-44-gw-ai-campus-in-pennsylvania/

[^24]: Hart Energy, "Diamondback Talks Build Permian Natgas Power Data Centers," February 2025. https://www.hartenergy.com/exclusives/diamondback-talks-build-permian-natgas-power-data-centers-212124

[^25]: Utility Dive, "GE Vernova gas turbine investor day," December 9, 2025. https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/ ; GE Vernova investor presentation. https://www.gevernova.com/sites/default/files/gev_webcast_presentation_12092025.pdf

[^26]: Energy Connects, "Siemens Energy boosts outlook on turbine, data center demand," November 2025. https://www.energyconnects.com/news/gas-lng/2025/november/siemens-energy-boosts-outlook-on-turbine-data-center-demand/

[^27]: Mitsubishi Heavy Industries press release, November 7, 2025. https://www.mhi.com/news/25110701.html

[^28]: Utility Dive, "Gas turbine supply crunch set to raise prices 195% by 2027: WoodMac." https://www.utilitydive.com/news/gas-turbine-supply-crunch-set-to-raise-prices-195-by-2027-woodmac/816904/

[^29]: Fortune, "Gas pipeline construction ramps to meet LNG, data center demand," July 17, 2025 (citing Kinder Morgan Q2 2025 earnings call). https://fortune.com/2025/07/17/gas-pipeline-construction-ramps-meet-lng-data-center-demand/

[^30]: IndexBox / NGI on Energy Transfer Q3 2025. https://www.indexbox.io/blog/natural-gas-infrastructure-boom-energy-transfer-and-kinder-morgan-lead-2026-growth/

[^31]: Natural Gas Intelligence, "Williams cautions natural gas demand could outpace pipeline capacity," 2025. https://naturalgasintel.com/news/midstream-giant-williams-cautions-natural-gas-demand-could-further-outpace-pipeline-capacity/

[^32]: Pipeline & Gas Journal on Wood Mackenzie Henry Hub forecast, June 2025. https://pgjonline.com/news/2025/june/wood-mackenzie-us-gas-sector-set-to-benefit-as-henry-hub-prices-poised-to-climb

[^33]: RBAC, "Data Centers and LNG Play 3D Chess for Natural Gas, Part 1." https://rbac.com/data-centers-and-lng-play-3d-chess-for-natural-gas-part-1/ ; American Oil & Gas Reporter, "LNG and Data Center Demand International Wildcards Top 2025 Demand Drivers." https://www.aogr.com/magazine/cover-story/lng-and-data-center-demand-international-wildcards-top-2025-demand-drivers

[^34]: Lawrence Berkeley National Laboratory, *Queued Up: 2025 Edition*, December 15, 2025. https://eta-publications.lbl.gov/sites/default/files/2025-12/queued_up_2025_edition_12.15.2025.pdf

[^35]: Data Center Dynamics on PJM 2025 Long-Term Load Forecast. https://www.datacenterdynamics.com/en/news/pjm-reports-peak-load-growth-of-30gw-through-2030-from-data-center-sector/

[^36]: Utility Dive, "ERCOT's large-load queue jumped almost 300% last year, official says," December 2025. https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/ ; ERCOT 2025 Long-Term Load Forecast Update, April 2025. https://www.ercot.com/files/docs/2025/04/07/8.1-Long-Term-Load-Forecast-Update-2025-2031-and-Methodology-Changes.pdf

[^37]: Baker Botts on Texas SB 6. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation ; ERCOT Q&A on the new large-load process. https://www.ercot.com/files/docs/2025/12/24/Large-Load-Interconnection-Process-Q-A.pdf

[^38]: MISO MTEP25 report. https://cdn.misoenergy.org/MTEP25%20Report731648.pdf ; Utility Dive on Indiana Michigan Power load growth. https://www.utilitydive.com/news/indiana-michigan-power-aep-amazon-google-microsoft-data-center-interconnect/733850/
