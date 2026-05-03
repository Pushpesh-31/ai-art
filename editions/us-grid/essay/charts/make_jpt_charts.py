"""Build the four JPT-article visuals in a clean editorial style.

Outputs PNGs to ./ (the charts/ directory). One figure per chart.

Style notes:
- White background, no top/right spines, faint horizontal gridlines only.
- Descriptive title (the takeaway, not the variable). Subtitle for context.
- Single accent color (red) on the data of interest; greys for context.
- Direct labels on data points instead of legends where possible.
- Source line bottom-left.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).resolve().parent
PROCESSED = HERE.parent.parent / 'data' / 'processed'

# -----------------------------------------------------------------------------
# Editorial style
# -----------------------------------------------------------------------------
ACCENT      = '#C0392B'   # hyperscaler / spotlight
ACCENT_FILL = '#FBE9E7'   # very light tint for highlighted panels
NEUTRAL     = '#2C3E50'   # dark slate (titles, primary text)
GREY        = '#7F8C8D'   # secondary text + control series
LIGHT_GREY  = '#BDC3C7'   # baseline bars, deemphasized
GRID        = '#ECEFF1'   # gridlines

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10.5,
    'axes.edgecolor': GREY,
    'axes.labelcolor': NEUTRAL,
    'axes.titlecolor': NEUTRAL,
    'xtick.color': GREY,
    'ytick.color': GREY,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})


def style_axis(ax, ygrid=True):
    ax.tick_params(axis='both', length=0)
    if ygrid:
        ax.yaxis.grid(True, color=GRID, lw=0.8, zorder=0)
        ax.set_axisbelow(True)


def add_source(fig, text, x=0.02, y=0.005):
    fig.text(x, y, text, fontsize=8, color=GREY, style='italic')


def add_title(fig, headline, subtitle=None, x=0.02, y_head=0.96, y_sub=0.92):
    fig.text(x, y_head, headline, fontsize=14, fontweight='bold', color=NEUTRAL)
    if subtitle:
        fig.text(x, y_sub, subtitle, fontsize=10.5, color=GREY)


# =============================================================================
# CHART 1 — Per-BA P90 LDC floor small multiples
# =============================================================================
def chart1_perba_ldc_floor():
    panel_raw = pd.read_parquet(PROCESSED / 'ba_2019_2025_hourly.parquet')

    HYPER = ['PJM', 'ERCO', 'MISO']
    CTRL  = ['BPAT', 'CISO', 'ISNE', 'NYIS', 'SOCO', 'SWPP', 'TVA']
    BA_LABEL = {
        'PJM': 'PJM',  'ERCO': 'ERCOT', 'MISO': 'MISO',
        'BPAT': 'BPA', 'CISO': 'CAISO', 'ISNE': 'ISO-NE',
        'NYIS': 'NYISO', 'SOCO': 'Southern Co.', 'SWPP': 'SPP', 'TVA': 'TVA',
    }

    def ldc_floor_p90(s, q=99.5):
        v = s.dropna().values
        if len(v) == 0:
            return np.nan
        peak = np.percentile(v, q)
        if peak <= 0:
            return np.nan
        sorted_desc = np.sort(v)[::-1] / peak
        return min(float(sorted_desc[int(len(sorted_desc) * 0.9)]), 1.0)

    years = sorted(panel_raw['year'].unique())
    rows = []
    for year in years:
        sub = panel_raw[panel_raw['year'] == year]
        gen = (sub.groupby(['respondent', 'period'])['value_mwh']
                  .sum().unstack('respondent').sort_index())
        gen.index = pd.to_datetime(gen.index)
        for ba in HYPER + CTRL:
            if ba in gen.columns:
                rows.append({'year': year, 'ba': ba, 'p90': ldc_floor_p90(gen[ba])})
    df = pd.DataFrame(rows)

    order = HYPER + CTRL  # 3 hyper, then 7 control
    fig, axes = plt.subplots(2, 5, figsize=(13.5, 5.6), sharey=True)
    fig.subplots_adjust(left=0.06, right=0.985, top=0.82, bottom=0.13,
                        wspace=0.18, hspace=0.45)

    for ax, ba in zip(axes.flat, order):
        sub = df[df['ba'] == ba].sort_values('year')
        is_hyper = ba in HYPER
        line_color = ACCENT if is_hyper else GREY
        if is_hyper:
            ax.set_facecolor(ACCENT_FILL)
        ax.plot(sub['year'], sub['p90'], color=line_color,
                lw=2.4 if is_hyper else 1.6, marker='o',
                markersize=4.5 if is_hyper else 3.5, zorder=3)

        ax.set_ylim(0.40, 0.60)
        ax.set_xlim(2018.5, 2025.5)
        ax.set_xticks([2019, 2022, 2025])
        ax.set_yticks([0.40, 0.45, 0.50, 0.55, 0.60])
        ax.set_yticklabels(['0.40', '', '0.50', '', '0.60'])
        style_axis(ax)

        first, last = sub['p90'].iloc[0], sub['p90'].iloc[-1]
        delta_pp = (last - first) * 100
        sign = '+' if delta_pp >= 0 else ''
        ax.set_title(f'{BA_LABEL[ba]}', fontsize=11,
                     fontweight='bold' if is_hyper else 'normal',
                     color=ACCENT if is_hyper else NEUTRAL,
                     loc='left', pad=4)
        ax.text(0.98, 0.05, f'{sign}{delta_pp:.1f} pp', transform=ax.transAxes,
                fontsize=9, ha='right', va='bottom',
                color=ACCENT if is_hyper else GREY,
                fontweight='bold' if is_hyper else 'normal')

    # ERCOT callout
    ercot_ax = axes[0, 1]
    ercot_ax.annotate('Largest single-BA\nshift in the panel',
                      xy=(2025, df[(df.ba == 'ERCO') & (df.year == 2025)]['p90'].iloc[0]),
                      xytext=(2020.5, 0.43),
                      fontsize=8.5, color=ACCENT, ha='left',
                      arrowprops=dict(arrowstyle='-', color=ACCENT, lw=0.8))

    add_title(fig,
              "Only ERCOT — where data-center load is actually operating — shows a sharp overnight-floor lift; PJM and MISO remain flat",
              'P90 of load duration curve (90th-percentile hour ÷ 99.5th-percentile peak), by US balancing authority, 2019–2025')
    add_source(fig, 'Source: EIA Form 930 hourly data; analysis by author. Hyperscaler cohort (red panels) = PJM, ERCOT, MISO. PJM and MISO mask their data-center signal at the BA aggregate; ERCOT is small enough that it surfaces.')

    out = HERE / 'chart1_perba_p90_floor.png'
    plt.savefig(out, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'wrote {out.name}')


# =============================================================================
# CHART 2 — PJM capacity auction step
# =============================================================================
def chart2_pjm_capacity_auction():
    auctions = [
        ('2024/2025', 28.92,  False, '$28.92'),
        ('2025/2026', 269.92, False, '$269.92'),
        ('2026/2027', 329.17, True,  '$329.17\n(at FERC cap)'),
    ]
    labels  = [a[0] for a in auctions]
    prices  = [a[1] for a in auctions]
    capped  = [a[2] for a in auctions]
    annot   = [a[3] for a in auctions]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    fig.subplots_adjust(left=0.07, right=0.97, top=0.78, bottom=0.18)

    bar_colors = [LIGHT_GREY, ACCENT, ACCENT]
    bars = ax.bar(labels, prices, color=bar_colors, width=0.55, zorder=3)

    for i, (bar, lbl, is_cap) in enumerate(zip(bars, annot, capped)):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 8, lbl,
                ha='center', va='bottom', fontsize=11.5, fontweight='bold',
                color=NEUTRAL)

    # Multiplier annotations between bars
    def step_annotation(x_left, x_right, y, label):
        ax.annotate('', xy=(x_right, y), xytext=(x_left, y),
                    arrowprops=dict(arrowstyle='->', color=GREY, lw=1.2))
        ax.text((x_left + x_right) / 2, y + 6, label, ha='center', va='bottom',
                fontsize=11, color=NEUTRAL, fontweight='bold')

    step_annotation(0.27, 0.73, 90, '~9× increase')
    step_annotation(1.27, 1.73, 300, '+22% to the cap')

    # Side annotation: uncapped sim and Dominion zone
    ax.text(2.32, 380, 'Uncapped sim:\n$388.57', fontsize=9.5, color=GREY,
            va='top', ha='left')
    ax.text(2.32, 320, 'Dominion zone:\n$444 / MW-day', fontsize=9.5,
            color=ACCENT, va='top', ha='left', fontweight='bold')

    ax.set_ylim(0, 470)
    ax.set_ylabel('Cleared price, $ per MW-day', fontsize=10.5, color=NEUTRAL)
    ax.set_yticks([0, 100, 200, 300, 400])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'${v:.0f}'))
    style_axis(ax)
    ax.set_xlabel('PJM Base Residual Auction (delivery year)', fontsize=10.5,
                  color=NEUTRAL, labelpad=8)

    add_title(fig,
              "PJM's capacity price has risen ~11× in two years; the most recent auction hit the FERC-imposed cap",
              'PJM Base Residual Auction clearing price, RTO-wide, $ per megawatt-day, three most recent delivery years')
    add_source(fig, 'Source: PJM Inside Lines, July 2025; S&P Global Commodity Insights, July 2024.')

    out = HERE / 'chart2_pjm_capacity_auction.png'
    plt.savefig(out, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'wrote {out.name}')


# =============================================================================
# CHART 3 — GE Vernova H-class slot booking through 2030
# =============================================================================
def chart3_gevernova_slots():
    years = ['2026', '2027', '2028', '2029', '2030']
    booked_pct  = [100, 100, 90, 70, 35]   # 2030 estimated from "10 GW remaining"
    remaining_pct = [100 - b for b in booked_pct]

    fig, ax = plt.subplots(figsize=(11, 5.4))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.78, bottom=0.16)

    x = np.arange(len(years))
    width = 0.55
    ax.bar(x, booked_pct, width=width, color=ACCENT, label='Booked', zorder=3)
    ax.bar(x, remaining_pct, width=width, bottom=booked_pct, color=LIGHT_GREY,
           label='Remaining', zorder=3)

    for xi, b in zip(x, booked_pct):
        if b >= 100:
            ax.text(xi, 50, 'Sold\nout', ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white')
        else:
            ax.text(xi, b / 2, f'{b}%', ha='center', va='center',
                    fontsize=12, fontweight='bold', color='white')
            ax.text(xi, b + (100 - b) / 2, f'{100 - b}%', ha='center', va='center',
                    fontsize=10, color=NEUTRAL)

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=11)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:.0f}%'))
    ax.set_ylim(0, 105)
    ax.set_ylabel('Heavy-frame production capacity', fontsize=10.5, color=NEUTRAL)
    ax.set_xlabel('Delivery year', fontsize=10.5, color=NEUTRAL, labelpad=8)
    style_axis(ax)

    # Q1 2026 hyperscaler order callout
    ax.text(0.98, 0.95,
            "Q1 2026 hyperscaler-direct\nelectrification orders: $2.4 B\n— more than all of 2025 combined",
            transform=ax.transAxes, ha='right', va='top', fontsize=9.5,
            color=NEUTRAL,
            bbox=dict(facecolor=ACCENT_FILL, edgecolor=ACCENT, lw=0.8,
                      boxstyle='round,pad=0.5'))

    add_title(fig,
              "GE Vernova's heavy-frame production is sold out through 2027; only 2030 has meaningful slots left",
              'GE Vernova H-class gas-turbine production capacity, % booked vs. remaining, by delivery year (year-end 2025)')
    add_source(fig, 'Source: GE Vernova investor day, December 9, 2025 (via Utility Dive). 2030 booked share estimated from disclosed remaining capacity.')

    out = HERE / 'chart3_gevernova_slots.png'
    plt.savefig(out, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'wrote {out.name}')


# =============================================================================
# CHART 4 — Large-load queue waterfall by grid
# =============================================================================
def chart4_load_queue_waterfall():
    """Per-grid: queued large load vs. connected and operating large load.
    PJM:    ~30 GW DC-attributable load growth 2024-2030 in PJM forecast / ~few GW "operating today"
    ERCOT:  233 GW large-load IR queue / single-digit GW operating today
    MISO:   11.6 GW MTEP25 large-load additions / ~few GW operating today
    """
    grids = ['ERCOT', 'PJM', 'MISO']
    queued = [233, 32, 12]      # GW: ERCOT large-load queue, PJM 2024-30 DC growth in load forecast, MISO MTEP25 large-load
    operating = [9, 5, 3]        # GW: connected/operating large load — approximate
    note = [
        'Large-load IR\nqueue (Dec 2025)',
        '2024–2030 forecast\nload growth (94% DC)',
        'MTEP25 large-load\nadditions',
    ]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.78, bottom=0.16)

    x = np.arange(len(grids))
    width = 0.34
    bars_q = ax.bar(x - width / 2, queued, width=width, color=ACCENT,
                    label='Queued / projected', zorder=3)
    bars_o = ax.bar(x + width / 2, operating, width=width, color=LIGHT_GREY,
                    label='Connected & operating today', zorder=3)

    for bar, val in zip(bars_q, queued):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 4, f'{val} GW',
                ha='center', va='bottom', fontsize=11, fontweight='bold',
                color=ACCENT)
    for bar, val in zip(bars_o, operating):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 4, f'~{val} GW',
                ha='center', va='bottom', fontsize=10, color=NEUTRAL)

    # Per-grid sub-label under each pair
    for xi, n in zip(x, note):
        ax.text(xi - width / 2, -18, n, ha='center', va='top', fontsize=8.5,
                color=GREY)

    ax.set_xticks(x)
    ax.set_xticklabels(grids, fontsize=12, fontweight='bold', color=NEUTRAL)
    ax.set_ylim(0, 260)
    ax.set_ylabel('Large-load capacity, gigawatts', fontsize=10.5, color=NEUTRAL)
    ax.set_yticks([0, 50, 100, 150, 200, 250])
    style_axis(ax)
    ax.legend(loc='upper right', frameon=False, fontsize=10)

    # Inline annotation: ERCOT gap
    ax.annotate(
        'ERCOT alone is sitting on ~225 GW of\ndata-center load that wants to connect',
        xy=(-0.17, 233), xytext=(0.6, 200), fontsize=9.5, color=NEUTRAL,
        arrowprops=dict(arrowstyle='-', color=GREY, lw=0.8),
    )

    add_title(fig,
              'Large-load interconnection queues dwarf what is actually connected today across PJM, ERCOT, and MISO',
              'Queued / projected vs. operating large-load capacity, gigawatts, by major US balancing authority (most recent disclosures)')
    add_source(fig, 'Source: ERCOT large-load queue (Dec 2025); PJM 2025 Long-Term Load Forecast; MISO MTEP25. Operating figures are approximate.')

    out = HERE / 'chart4_load_queue_waterfall.png'
    plt.savefig(out, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'wrote {out.name}')


# =============================================================================
if __name__ == '__main__':
    chart1_perba_ldc_floor()
    chart2_pjm_capacity_auction()
    chart3_gevernova_slots()
    chart4_load_queue_waterfall()
