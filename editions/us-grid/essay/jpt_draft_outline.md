# JPT Article — Citation-Backed Outline

**Audience:** SPE Journal of Petroleum Technology readers — oil & gas / energy industry professionals.
**Length target:** 2,000–2,500 words. LinkedIn carve: ~400 words from sections 4 + 5 + 7.
**Tone:** Authoritative, sourced, slightly skeptical of hype. Lead with structural framing, not violations.

---

## Working title — pick one

1. **"The Trough Is Starting to Fill: What EIA-930 Already Tells Us About AI Power Demand"**
2. **"Power Is the Bottleneck: Reading the Leading Edge of AI's Grid Footprint"**
3. **"AI's First Energy Bill: A Leading-Edge Fingerprint, and a Gas Story Hiding in Plain Sight"**

My pick: **#3** — names the gas wedge in the title, signals "data + analysis" not "hype," and the JPT editors will instantly understand the framing.

---

## Spine

### Section 1 — Hook (≈150 words)

**Scene:** 4 AM in Loudoun County, Virginia. Server-room lights on, training run mid-step. Across PJM, demand has barely dropped from the evening peak. This is new.

**Claim to anchor the section:** Dominion Energy now has **47 GW of contracted data-center load** in its development pipeline (Oct 2025), up from 16.5 GW in mid-2023 and 33 GW at end of 2024.[^1] That single utility's contracted load is roughly **two-thirds of the entire ERCOT system peak**.

**Visual:** none — text scene only.

---

### Section 2 — Why this is a power story, not a tech story (≈250 words)

**Frame:** AI compute is unusual as a load — it looks more like a smelter than a hospital. Three properties matter:

1. **High capacity factor.** Training runs are batchable but inference is constant; GPU clusters run near full utilization 24/7.
2. **Density.** Modern AI campuses target 100–300 MW per site, vs. 10–30 MW for a 2015-era cloud DC. Some new sites (Stargate Abilene, xAI Memphis Colossus) are crossing 1 GW.
3. **Fast siting timeline.** Hyperscaler buildouts move on 18–36 month construction cycles; the grid moves on 7–10 year transmission cycles. The mismatch is the story.

**Sources:**
- LBNL 2024 Data Center Energy Usage Report — 2023 actuals **176 TWh / 4.4% of US electricity**, projected **325–580 TWh / 6.7–12% by 2028**.[^2]
- IEA *Energy and AI* (Apr 10, 2025) — global DC demand **415 TWh (2024) → 945 TWh (2030)**; US contributes +240 TWh (+130%).[^3]
- Goldman Sachs Research — US DC share **3% (2022) → 8% (2030)**, ~$50B in new generation capex needed.[^4]

**Visual:** small table — LBNL low/base/high scenarios for 2028, plus IEA 2030 figure, plus EIA AEO 2025 revision (+117% larger growth than AEO 2023).[^5]

---

### Section 3 — The leading-edge fingerprint (≈500 words) — *original analysis*

**This is the differentiated section. Everyone else is quoting forecasts; we are reading the meter.*

**What I did:** Pulled hourly generation by fuel for 10 US Balancing Authorities from EIA-930, 2019–2025. Defined three "data-center signatures" derived from load shape:
1. Overnight share (2–5 AM mean ÷ daily peak)
2. Weekend / weekday ratio
3. P90 load-duration-curve floor (90th-percentile hour ÷ 99.5th-percentile peak)

**Why that comparison:** Group the 10 BAs into "hyperscaler-heavy" (PJM, ERCO, MISO — where the contracted data-center buildout is largest) vs "control" (BPAT, CISO, ISNE, NYIS, SOCO, SWPP, TVA).

**What the data says:**
- Signatures 1 and 2 show a **positive cross-section but no time trend** — confounded by fuel mix and behavioral patterns.
- Signature 3 is the only one with movement on the time axis, and the movement is in **absolute hyperscaler floors**, not in the gap.

**Numbers:**
- Hyperscaler P90 floor: **0.517 (2019) → 0.539 (2025)**, +2.5 pp absolute, biggest steps in 2024 and 2025.
- Control P90 floor: ~0.47 throughout, flat.
- Hyper − Ctrl gap: **5–7 pp, stable** across all seven years (the often-cited 11.6 pp 2025 gap is an artifact of single-hour reporting glitches in SWPP-2023, TVA-2024, SOCO-2025; corrected here using a 99.5th-percentile robust peak per standard load-research practice).
- **ERCOT alone: 0.473 → 0.542 (+6.9 pp)** — the cleanest single-BA instance.

**Honest framing:** The trough is starting to fill. The fingerprint is small, the trend is real, and the trend is in the right places (PJM, ERCO, MISO). What we're seeing in EIA-930 is the leading edge of a buildout that is mostly still queued. The body of the load curve has not arrived yet.

**Visual:** primary chart from `editions/us-grid/notebooks/12_data_center_signature_trend.ipynb` — `data_center_signature_trend_per_ba.png` (per-BA small multiples). Secondary: the hyper-vs-ctrl absolute series.

**Sources:**
- EIA Form 930 hourly grid monitor data, 2019–2025.[^6]
- Methodology: 99.5th-percentile robust peak normalization (standard load-research practice; documented in NB12 sanity check).
- Cross-check: EIA reported 2024 lower-48 peak hit a new all-time record of **759 GW** on Jul 29, 2024.[^7]

---

### Section 4 — Who's buying, and how fast (≈400 words)

**Frame:** Hyperscaler power procurement has moved from "buy clean MWh on the open market" to "sign 20-year PPAs for dedicated nuclear units, fund SMR developers, and build their own gas-fired campuses." The pace and dollar size are unprecedented.

**Cluster 1 — nuclear, the headline play:**
- **MSFT + Constellation, Three Mile Island restart**: 835 MW, 20-yr PPA, online ~2027 (pulled forward from 2028); ~$1.6B Constellation investment.[^8]
- **AMZN + Talen, Susquehanna behind-the-meter**: 300→480 MW initial, contract envelope to 1,920 MW. **Status: BLOCKED by FERC twice (Nov 2024, Apr 2025); now in Fifth Circuit appeal.** The cautionary tale: behind-the-meter at existing nuclear is no longer a clean path.[^9]
- **GOOG + Kairos Power**: 500 MW SMR fleet (KP-FHR), first reactor 2030, full deployment 2035.[^10]
- **AMZN + X-energy**: $500M Series C-1; 320 MW initial at Energy Northwest, MoU for ~300 MW with Dominion at North Anna; joint target >5 GW SMR by 2039.[^11]
- **META nuclear RFP** (Dec 2024): solicited 1–4 GW; awarded Jan 2026 to **Vistra (2.2 GW from existing Comanche Peak), Oklo, and TerraPower** — combined ~6.6 GW.[^12]

**Cluster 2 — the new infrastructure money:**
- **Stargate** (OpenAI / Oracle / SoftBank / MGX, Jan 21, 2025): up to **$500B by 2029**, $100B initial. First site Abilene TX (Crusoe-built, 1.2 GW at full build). Five additional sites announced Sept 2025; Oracle later added 4.5 GW. Total planned ~7+ GW.[^13]
- **CoreWeave–OpenAI** ~$11.9B (Mar 2025) + **CoreWeave–Meta** $21B through 2032; **Lambda–MSFT** multi-billion (Nov 2025); **IREN–MSFT** $9.7B / 200 MW Childress TX.[^14]

**Cluster 3 — the price signal:**
- **PJM 2025/2026 capacity auction**: cleared **$269.92/MW-day** (~9× prior $28.92, Jul 30, 2024). 2026/2027 auction: **$329.17/MW-day at the FERC-imposed cap**, uncapped sim would have cleared **$388.57**. Dominion zone $444; BGE $466.[^15] This is the grid operator's price signal screaming.

**Sources:** see footnotes 8–15.

---

### Section 5 — The gas angle (≈600 words) — *the JPT wedge*

**Frame:** Nuclear gets the headlines because it's the climate-friendly answer. But the answer that can actually be online by 2027 is gas. The hyperscaler buildout is, in the near term, a gas demand story — and the oil & gas industry is already moving.

**The behind-the-meter wave:**
- **Crusoe Abilene (Stargate Phase 1):** TCEQ-permitted **~360 MW of behind-the-meter simple-cycle generation** — five Solar Turbines Titan 350s + five GE LM2500 aero-turbines. The Jan 2025 modification raised LM2500 annual run-hours from 5,880 to 8,760 (continuous 24/7) "for onsite use only for data centers and computing."[^16]
- **Crusoe + GE Vernova:** **29 LM2500XPRESS aeroderivative units (~1 GW total)** ordered in two tranches (10 in Dec 2024, 19 in June 2025).[^17]
- **Crusoe + Engine No. 1 JV:** **4.5 GW of co-located gas-fired data-center campuses** announced Mar 2025.[^18]
- **VoltaGrid** (the modular-gas-turbine specialist): contracted backlog **>4,350 MW** by late 2025, including **2.3 GW for Oracle in Texas** (with Energy Transfer fuel supply), >1 GW with Vantage Data Centers, and a 400 MW Halliburton + VoltaGrid commitment for Eastern Hemisphere DCs in 2028. INNIO Jenbacher booked its largest-ever order (92 × 25 MW packs = 2.3 GW) for the VoltaGrid fleet.[^19]
- **xAI Memphis Colossus** (one paragraph, narrative not focus): currently ~150 MW from TVA plus on-site Solar Turbines and VoltaGrid units. EPA found the company in violation of the Clean Air Act on Jan 16, 2026 for operating turbines beyond permitted limits.[^20] Mention as a single example of how aggressively hyperscalers are willing to bypass grid timelines, not as the article's frame.

**Oil majors entering the power business:**
- **ExxonMobil** (Dan Ammann, Dec 11, 2024): in FEED on a **>1.5 GW dedicated, off-grid, gas-fired plant for a data-center customer with >90% CCS capture**, ready within five years. Quote: *"We're in a unique position to provide low-carbon power at large scale on a very competitive and accelerated timeline."*[^21]
- **Chevron + Engine No. 1 + GE Vernova** (Jan 28, 2025): JV to deliver **up to 4 GW** using seven GE Vernova 7HA frames (slot reservation), CCS-capable, first power 2027.[^22]
- **EQT + Homer City Energy Campus** (Jul 15, 2025): exclusive supply of **0.66 Bcf/d** to the **4.4 GW Homer City campus in PA** — the largest gas-powered DC campus in North America. First power 2027.[^23]
- **Diamondback** (Travis Stice, Feb 2025): JV in formation with a hyperscaler and a power developer, leveraging >1 Bcf/d of associated Permian gas.[^24]

**The OEM bottleneck — the killer data point for this audience:**
- **GE Vernova**: ended 2025 with an **80 GW gas-turbine backlog stretching to 2029**, rising to ~110 GW projected by end-2026. **Q1 2026 hyperscaler-direct electrification orders alone hit $2.4B — more than all of 2025 combined.** H-class slots effectively sold out through 2027; 2028 ~90% booked, 2029 ~70% booked.[^25]
- **Siemens Energy**: 194 gas turbines in FY25 (vs 100 in FY24); **€146B order backlog** (Q1 FY26); **>€2B in grid-tech orders directly from hyperscalers.**[^26]
- **Mitsubishi Heavy Industries**: announced doubling of large-frame production within two years; 23 large-frame units booked in H1 FY25.[^27]
- **Wood Mackenzie**: gas turbine prices set to rise **+195% by 2027** on the supply crunch.[^28]

**Demand math the readers will care about:**
- **Kinder Morgan (Q2 2025 earnings, Kim Dang):** **3–10 Bcf/d incremental gas demand from AI data centers by 2030 (~9% of US consumption)**. KMI backlog +$6B in 12 months.[^29]
- **Energy Transfer (Q3 2025):** signed $1.6B agreement for on-site gas/power for an unnamed IG client; CEO: *"We have never seen this level of activity from a demand-pull standpoint."*[^30]
- **Williams (Q3 2025):** commercialized backlog **>$5B**.[^31]
- **Wood Mackenzie:** Henry Hub forecast **$5/MMBtu by 2030, $6 by 2035**, driven by data centers + LNG + manufacturing.[^32]
- **The 3D-chess angle:** Haynesville and Permian are the marginal molecules being fought over by both LNG export and data-center buildout. EIA projects LNG gross exports **14.9 → 16.3 Bcf/d (2025 → 2026)**, needing >15 Bcf/d incremental production through 2030.[^33]

**Sources:** footnotes 16–33.

---

### Section 6 — The queue (≈300 words)

**Frame:** Critical distinction up front — *queued generation* and *queued load* are different things. Both queues matter; conflating them is a credibility-killer.

**Generation side:**
- LBNL "Queued Up" 2025 edition (Dec 15, 2025, end-2024 data): only **13%** of capacity that requested interconnection 2000–2019 reached commercial operation by end-2024. **77% withdrew.** Median IR-to-COD doubled from <2 yrs (2000–2007 cohort) to **>4 yrs** (2018–2024 cohort). Total active US queue volume **fell 12% YoY** in 2024 — first decline, due to FERC Order 2023 cleanouts.[^34]

**Load side (the real story):**
- **PJM:** 2025 Long-Term Load Forecast — peak load growth ~32 GW 2024→2030, **~30 GW (~94%) attributable to data centers**. ~140 GW in active study queue; ~57 GW with signed/offered GIAs.[^35]
- **ERCOT:** **~233 GW of large-load interconnection requests** (Dec 2025), up ~4× YoY; >70% data centers. Connected/operating large load is single-digit GW. The gap is the story. ERCOT's 2025 Long-Term Load Forecast: 138 GW of large loads expected on grid by 2030.[^36]
  - Texas SB 6 (signed Jun 20, 2025): $50,000/MW non-refundable interconnection fee + 100% CIAC + curtailment-during-shed obligation for loads connecting after Dec 31, 2025. The state is trying to slow the rush.[^37]
- **MISO:** MTEP25 includes **11.6 GW of large-load additions**, 49 Expedited Project Reviews. Indiana Michigan Power peak: **2.8 → 7+ GW by 2030** (~2.5×) driven by AWS New Carlisle, Google Fort Wayne, Microsoft LaPorte.[^38]

**The math:** even if half of the queued load materializes, the leading-edge fingerprint we measured in Section 3 should triple by 2028.

**Sources:** footnotes 34–38.

---

### Section 7 — Falsifiable prediction + what to watch (≈250 words)

**The prediction (must be specific, must be falsifiable):**

If half of the currently queued hyperscaler load materializes by 2028, hyperscaler-mean P90 LDC floors should rise from today's **0.539 to ~0.58–0.60** (a +4 to +6 pp move on top of the +2.5 pp move we already saw). ERCOT, the cleanest single instance, should see its P90 floor cross 0.60.

**If we see those numbers in 2028 EIA-930 data, the bottleneck thesis is confirmed and the gas industry's bet is paying off.** If we don't, either the queues didn't materialize or hyperscalers found the power outside the EIA-930 lens (behind-the-meter gas at scale, which would itself be the story).

**Three indicators to watch in the next 18 months:**
1. **PJM 2027/2028 capacity auction** (cleared price). Above $300/MW-day = the bottleneck is still binding.
2. **GE Vernova / Siemens Energy / Mitsubishi 2029 slot availability.** If 2030 slots fill in 2026, the OEM bottleneck has tightened.
3. **EIA Form 930 P90 floors** for ERCO and PJM — these update monthly and are the leading indicator the rest of the analyst world isn't watching.

**Closing line:** *Power has been a cost on the AI industry's balance sheet. It is becoming a bottleneck. For the oil and gas industry, that bottleneck is a customer.*

---

## Sources / footnotes

[^1]: Dominion Energy quarterly load report to PJM Load Forecast Working Group, Oct 2025. https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/dominion-documentation.pdf

[^2]: Shehabi et al., *2024 United States Data Center Energy Usage Report*, LBNL-2001637, Dec 20, 2024. https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf

[^3]: IEA, *Energy and AI*, Apr 10, 2025. https://www.iea.org/reports/energy-and-ai

[^4]: Goldman Sachs Research, "AI is poised to drive 160% increase in data center power demand," May 14, 2024 (updated Feb 4, 2025). https://www.goldmansachs.com/insights/articles/AI-poised-to-drive-160-increase-in-power-demand

[^5]: EIA *Annual Energy Outlook 2025*, Apr 15, 2025 — first AEO in seven editions to materially revise electricity demand growth upward; 2024–2050 growth is 117% larger than AEO 2023. https://www.eia.gov/outlooks/aeo/

[^6]: EIA Form 930 (Hourly Grid Monitor). https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48

[^7]: EIA, "U.S. electricity demand reached an all-time high in summer 2024," Sept 2024. https://www.eia.gov/todayinenergy/detail.php?id=65864

[^8]: Constellation Energy, "Constellation to Launch Crane Clean Energy Center," Sep 20, 2024. https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html

[^9]: Utility Dive, "FERC rejects Talen-Amazon ISA," Nov 2024. https://www.utilitydive.com/news/ferc-interconnection-isa-talen-amazon-data-center-susquehanna-exelon/731841/ ; ANS Newswire on Apr 2025 rehearing denial. https://www.ans.org/news/2025-04-16/article-6937/ferc-denies-talen-amazon-agreementagain/

[^10]: Kairos Power, "Google and Kairos Power Partner to Deploy 500 MW," Oct 14, 2024. https://kairospower.com/external_updates/google-and-kairos-power-partner-to-deploy-500-mw-of-clean-electricity-generation/

[^11]: Amazon News, "Amazon nuclear small modular reactor net carbon zero," Oct 16, 2024. https://www.aboutamazon.com/news/sustainability/amazon-nuclear-small-modular-reactor-net-carbon-zero

[^12]: Meta Sustainability, "Accelerating the next wave of nuclear to power AI innovation," Dec 3, 2024. https://sustainability.atmeta.com/blog/2024/12/03/accelerating-the-next-wave-of-nuclear-to-power-ai-innovation/

[^13]: OpenAI, "Announcing the Stargate Project," Jan 21, 2025. https://openai.com/index/announcing-the-stargate-project/

[^14]: Data Center Frontier on Crusoe Abilene project finance, May 2025. https://www.datacenterfrontier.com/hyperscale/article/55276169/crusoe-adds-45-gw-natural-gas-to-fuel-ai-expands-abilene-data-center-to-12-gw ; CNBC on Lambda–Microsoft. https://www.cnbc.com/2025/11/03/lambda-ai-microsoft-nvidia.html

[^15]: PJM Inside Lines, "PJM Auction Procures 134,311 MW," Jul 22, 2025. https://insidelines.pjm.com/pjm-auction-procures-134311-mw-of-generation-resources-supply-responds-to-price-signal/ ; S&P Global on $269.92 clearing price. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/073024-pjm-power-capacity-auction-clears-at-record-high-price-of-26992mw-day-for-most-of-footprint

[^16]: TCEQ permit docket for Lancium Clean Campus / Crusoe Abilene. https://records.tceq.texas.gov/cs/idcplg?IdcService=TCEQ_EXTERNAL_SEARCH_GET_FILE&dID=8600163

[^17]: GE Vernova press release, "GE Vernova, Crusoe announce major 29-unit aeroderivative gas turbine deliver AI data centers," June 2025. https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers

[^18]: Business Wire, "Crusoe and Engine No. 1 launch JV for 4.5 GW of co-located gas-fired data-center campuses," Mar 17, 2025. https://www.businesswire.com/news/home/20250317173370/en/

[^19]: Power Magazine, "Oracle taps VoltaGrid for 2.3 GW modular gas fleet," 2025. https://www.powermag.com/oracle-taps-voltagrid-for-2-3-gw-modular-gas-fleet-to-power-ai-data-centers-across-texas/ ; Vantage Data Centers + VoltaGrid release. https://vantage-dc.com/news/vantage-data-centers-and-voltagrid-establish-partnership-to-deploy-more-than-one-gigawatt-of-power-generation/ ; Halliburton + VoltaGrid release. https://www.halliburton.com/en/about-us/press-release/voltagrid-halliburton-accelerate-data-center-eastern-hemisphere

[^20]: Inside Climate News, "EPA finds xAI in violation of Clean Air Act," Jan 2026 — see also Shelby County Health Dept. permit and SELC appeal documentation. https://insideclimatenews.org/news/17072025/elon-musk-xai-data-center-gas-turbines-memphis/ ; SELC. https://www.selc.org/press-release/groups-appeal-permit-for-xais-south-memphis-data-center-decisions-around-unpermitted-methane-gas-turbines/

[^21]: Semafor, "ExxonMobil wants to make bespoke carbon-capture power plants for data centers," Dec 13, 2024. https://www.semafor.com/article/12/13/2024/exxonmobil-wants-to-make-bespoke-carbon-capture-power-plants-for-data-centers ; Exxon corporate page. https://corporate.exxonmobil.com/what-we-do/delivering-industrial-solutions/carbon-capture-and-storage/steel-ammonia-ai-what-cant-ccs-help-decarbonize

[^22]: Chevron press release, "Power Solutions for U.S. Data Centers," Jan 28, 2025. https://www.chevron.com/newsroom/2025/q1/power-solutions-for-us-data-centers ; S&P Global coverage. https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/012825-chevron-engine-no-1-ge-vernova-to-power-us-data-centers

[^23]: Homer City Redevelopment release, Jul 15, 2025. https://www.homercityredevelopment.com/post/press-release-homer-city-redevelopment-announces-agreement-in-principle-for-eqt-corporation-to-supp ; Natural Gas Intelligence coverage. https://naturalgasintel.com/news/eqt-snags-two-natural-gas-supply-contracts-including-for-massive-44-gw-ai-campus-in-pennsylvania/

[^24]: Hart Energy, "Diamondback Talks Build Permian Natgas Power Data Centers," Feb 2025. https://www.hartenergy.com/exclusives/diamondback-talks-build-permian-natgas-power-data-centers-212124

[^25]: Utility Dive, "GE Vernova gas turbine investor day," Dec 9, 2025. https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/ ; GE Vernova investor presentation. https://www.gevernova.com/sites/default/files/gev_webcast_presentation_12092025.pdf

[^26]: Energy Connects, "Siemens Energy boosts outlook on turbine, data center demand," Nov 2025. https://www.energyconnects.com/news/gas-lng/2025/november/siemens-energy-boosts-outlook-on-turbine-data-center-demand/

[^27]: MHI press release, Nov 7, 2025. https://www.mhi.com/news/25110701.html

[^28]: Utility Dive, "Gas turbine supply crunch set to raise prices 195% by 2027: WoodMac." https://www.utilitydive.com/news/gas-turbine-supply-crunch-set-to-raise-prices-195-by-2027-woodmac/816904/

[^29]: Fortune, "Gas pipeline construction ramps to meet LNG, data center demand," Jul 17, 2025 (citing KMI Q2 2025 earnings call). https://fortune.com/2025/07/17/gas-pipeline-construction-ramps-meet-lng-data-center-demand/

[^30]: IndexBox / NGI on Energy Transfer Q3 2025. https://www.indexbox.io/blog/natural-gas-infrastructure-boom-energy-transfer-and-kinder-morgan-lead-2026-growth/

[^31]: Natural Gas Intelligence, "Williams cautions natural gas demand could outpace pipeline capacity," 2025. https://naturalgasintel.com/news/midstream-giant-williams-cautions-natural-gas-demand-could-further-outpace-pipeline-capacity/

[^32]: Pipeline & Gas Journal on WoodMac Henry Hub forecast, June 2025. https://pgjonline.com/news/2025/june/wood-mackenzie-us-gas-sector-set-to-benefit-as-henry-hub-prices-poised-to-climb

[^33]: RBAC, "Data Centers and LNG Play 3D Chess for Natural Gas." https://rbac.com/data-centers-and-lng-play-3d-chess-for-natural-gas-part-1/ ; American Oil & Gas Reporter, "LNG and Data Center Demand." https://www.aogr.com/magazine/cover-story/lng-and-data-center-demand-international-wildcards-top-2025-demand-drivers

[^34]: LBNL, "Queued Up 2025 Edition," Dec 15, 2025. https://eta-publications.lbl.gov/sites/default/files/2025-12/queued_up_2025_edition_12.15.2025.pdf

[^35]: PJM 2025 Long-Term Load Forecast, via DCD coverage. https://www.datacenterdynamics.com/en/news/pjm-reports-peak-load-growth-of-30gw-through-2030-from-data-center-sector/

[^36]: Utility Dive, "ERCOT's large-load queue jumped almost 300% last year," Dec 2025. https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/ ; ERCOT 2025 Long-Term Load Forecast Update, Apr 2025. https://www.ercot.com/files/docs/2025/04/07/8.1-Long-Term-Load-Forecast-Update-2025-2031-and-Methodology-Changes.pdf

[^37]: Baker Botts on Texas SB 6. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-senate-bill-6-understanding-the-impacts-to-large-loads-and-co-located-generation ; ERCOT Q&A. https://www.ercot.com/files/docs/2025/12/24/Large-Load-Interconnection-Process-Q-A.pdf

[^38]: MISO MTEP25 report. https://cdn.misoenergy.org/MTEP25%20Report731648.pdf ; Utility Dive on I&M load growth. https://www.utilitydive.com/news/indiana-michigan-power-aep-amazon-google-microsoft-data-center-interconnect/733850/

---

## Visuals plan

1. **Section 2 — small inset table:** LBNL 2028 low/mid/high + IEA 2030 + AEO 2025 revision (4 rows, 3 cols).
2. **Section 3 — primary chart:** `data_center_signature_trend_per_ba.png` (per-BA small multiples). This is the lead visual.
3. **Section 3 — secondary chart:** hyper-vs-ctrl absolute series (use the existing `data_center_signature_trend.png` panel 3, P90 floor only).
4. **Section 4 — capacity auction price step chart:** $28.92 → $269.92 → $329.17/MW-day, three years.
5. **Section 5 — OEM backlog table:** GE Vernova / Siemens / MHI rows; backlog GW, hyperscaler-attributable order $, slot availability.
6. **Section 6 — queue waterfall:** PJM ~140 GW study / ~57 GW signed / actually built; ERCOT 233 GW queued / single-digit connected.

We may need to make charts 4 and 6 — the underlying data is from the agent briefs and PJM/ERCOT primary sources. Doable in matplotlib/seaborn consistent with NB12 style.

---

## LinkedIn carve plan (~400 words)

- **Hook (50 words):** ERCOT's overnight floor jumped 6.9 pp from 2019 to 2025. Most analysts haven't noticed. Here's what's coming next.
- **The chart (1 image):** ERCOT P90 floor trend (carved from Section 3's per-BA panel).
- **The numbers (200 words):** Dominion 47 GW contracted. ERCOT 233 GW queued. PJM capacity price 9× in two years. GE Vernova 80 GW backlog through 2029.
- **The frame (100 words):** Power is the AI revolution's next bottleneck. The leading edge is already in EIA-930 data. The body of the curve is queued. And the answer that can be online by 2027 is not nuclear — it's gas.
- **Link to JPT article + invitation to discuss.**

---

## Open decisions (need your call before I draft)

1. **Title** — pick from the three above (or veto and I'll propose more).
2. **Hook anchor** — Loudoun (default) or substitute with a Permian / Abilene scene that lands the gas frame harder for JPT readers from the very first paragraph?
3. **Visuals** — am I OK to build charts 4 and 6 as new matplotlib figures in NB12-compatible style, or do you want to draw those yourself / skip them?
4. **First-person voice or third-person reportorial?** JPT runs both. Reportorial is safer for a first submission; first-person works if you want the analytical-author byline.
