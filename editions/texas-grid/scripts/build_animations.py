"""Build animated GIFs for Texas Grid Edition 2.

Outputs three GIFs to editions/texas-grid/art/:
  duck_deepens.gif      monthly net-load curves stacking through the year
  cold_snap.gif         Feb 13-22 fuel-mix scrubber over Texas's 2025 peak week
  ai_load_overlay.gif   flat AI data-center load growing on Aug dispatch
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

HERE = Path(__file__).resolve().parent
EDITION = HERE.parent
DATA = EDITION / 'data' / 'processed'
ART = EDITION / 'art'
ART.mkdir(parents=True, exist_ok=True)

fuel_colors = {
    'coal':      '#D4890E',
    'gas_total': '#F0C078',
    'nuclear':   '#2A9D8F',
    'hydro':     '#264653',
    'wind':      '#72B352',
    'solar':     '#F4C430',
    'other':     '#9B72CF',
}
fuel_labels = {
    'coal': 'Coal', 'gas_total': 'Gas (all)', 'nuclear': 'Nuclear',
    'hydro': 'Hydro', 'wind': 'Wind', 'solar': 'Solar', 'other': 'Other',
}
stack_order = ['nuclear', 'coal', 'gas_total', 'hydro', 'wind', 'solar', 'other']

BG = '#0E1017'
FG = '#E5E7EB'
MUTED = '#9CA3AF'


def style_axes(ax):
    ax.set_facecolor(BG)
    for s in ax.spines.values():
        s.set_color('#444')
    ax.tick_params(colors=MUTED)
    ax.xaxis.label.set_color(FG)
    ax.yaxis.label.set_color(FG)
    ax.grid(alpha=0.12, color='#666', lw=0.6)


h = pd.read_csv(DATA / 'texas_2025_hourly.csv', parse_dates=['timestamp']).set_index('timestamp')
gw_cols = ['total', 'wind', 'solar', 'coal', 'gas_total', 'nuclear', 'hydro', 'other', 'biomass']
for c in gw_cols:
    h[c + '_gw'] = h[c] / 1000.0
h['net_load_gw'] = h['total_gw'] - h['wind_gw'] - h['solar_gw']
h['hour'] = h.index.hour
h['month'] = h.index.month

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# ============================================================
# 1. The Duck Deepens
# ============================================================
print('Building duck_deepens.gif ...')
monthly_net = h.groupby(['month', 'hour'])['net_load_gw'].mean().unstack(0)

fig, ax = plt.subplots(figsize=(10, 5.6), dpi=90)
fig.patch.set_facecolor(BG)
style_axes(ax)
ax.set_xlim(0, 23)
ax.set_ylim(25, 75)
ax.set_xlabel('Hour of day')
ax.set_ylabel('Net load = total − wind − solar  (GW)')
ax.set_xticks(range(0, 24, 3))
title = ax.text(0.5, 1.06, '', transform=ax.transAxes, ha='center',
                color=FG, fontsize=14, weight='bold')
subtitle = ax.text(0.5, 0.98, '', transform=ax.transAxes, ha='center',
                   color=MUTED, fontsize=10)
ax.text(0.99, 0.02, 'Texas Grid 2025 · ERCOT IntGenbyFuel',
        transform=ax.transAxes, ha='right', color='#666', fontsize=7)

ghost_lines = []
fills = []
current_line, = ax.plot([], [], color='#F4C430', lw=3.2, zorder=10)


def update_duck(frame):
    while ghost_lines:
        ghost_lines.pop().remove()
    while fills:
        fills.pop().remove()
    m = frame + 1
    hours = np.arange(24)
    for past in range(1, m):
        l, = ax.plot(hours, monthly_net[past].values,
                     color='#F4C430', alpha=0.16, lw=1.0, zorder=2)
        ghost_lines.append(l)
    cur = monthly_net[m].values
    current_line.set_data(hours, cur)
    fc = ax.fill_between(hours, cur, 25, color='#F4C430', alpha=0.10, zorder=1)
    fills.append(fc)
    belly = cur.min()
    peak = cur.max()
    swing = peak - belly
    title.set_text(f'The Duck Deepens — {month_names[m - 1]} 2025')
    subtitle.set_text(f'belly {belly:.1f} GW · peak {peak:.1f} GW · swing {swing:.1f} GW')
    return [current_line, title, subtitle] + ghost_lines + fills


anim = animation.FuncAnimation(fig, update_duck, frames=12, blit=False)
anim.save(ART / 'duck_deepens.gif', writer=PillowWriter(fps=2))
plt.close(fig)
print('  ->', ART / 'duck_deepens.gif')

# ============================================================
# 2. February peak-week scrubber
# ============================================================
print('Building cold_snap.gif ...')
window = h.loc['2025-02-13':'2025-02-22'].copy()
n = len(window)
x = np.arange(n)

fig, ax = plt.subplots(figsize=(10, 5.6), dpi=90)
fig.patch.set_facecolor(BG)
style_axes(ax)
ax.set_xlim(0, n - 1)
stack_sum = sum(window[f + '_gw'] for f in stack_order)
ax.set_ylim(0, stack_sum.max() * 1.08)

day_starts = [i for i, ts in enumerate(window.index) if ts.hour == 0]
ax.set_xticks(day_starts)
ax.set_xticklabels([window.index[i].strftime('%b %d') for i in day_starts], color=MUTED)
ax.set_ylabel('Generation (GW)')

title = ax.text(0.5, 1.06, "Texas's Peak Week — Feb 13–22, 2025",
                transform=ax.transAxes, ha='center', color=FG, fontsize=14, weight='bold')
subtitle = ax.text(0.5, 0.98, '', transform=ax.transAxes, ha='center',
                   color=MUTED, fontsize=10)
ax.text(0.99, 0.02, 'Hourly fuel mix · Feb 19 was 2025\'s highest-generation day',
        transform=ax.transAxes, ha='right', color='#666', fontsize=7)

handles = [plt.Rectangle((0, 0), 1, 1, color=fuel_colors[f]) for f in stack_order]
ax.legend(handles, [fuel_labels[f] for f in stack_order],
          loc='upper right', frameon=False, ncol=4, fontsize=8, labelcolor=FG)

stacks = []
n_frames = 80
step = max(1, n // n_frames)


def update_cold(frame):
    while stacks:
        stacks.pop().remove()
    end = min((frame + 1) * step, n)
    bottom = np.zeros(end)
    for f in stack_order:
        y = window[f + '_gw'].values[:end]
        col = ax.fill_between(x[:end], bottom, bottom + y,
                              color=fuel_colors[f], alpha=0.92)
        stacks.append(col)
        bottom = bottom + y
    ts = window.index[end - 1]
    total_now = bottom[-1] if end > 0 else 0
    subtitle.set_text(f'{ts.strftime("%a %b %d  %H:%M")}  ·  {total_now:.1f} GW')
    return stacks + [subtitle]


anim = animation.FuncAnimation(fig, update_cold, frames=n_frames + 6, blit=False)
anim.save(ART / 'cold_snap.gif', writer=PillowWriter(fps=12))
plt.close(fig)
print('  ->', ART / 'cold_snap.gif')

# ============================================================
# 3. AI data-center flat-load overlay on August dispatch
# ============================================================
print('Building ai_load_overlay.gif ...')
aug_mask = h.index.month == 8
aug = h[aug_mask].groupby('hour')[[f + '_gw' for f in stack_order]].mean()
aug.columns = stack_order

fig, ax = plt.subplots(figsize=(10, 5.6), dpi=90)
fig.patch.set_facecolor(BG)
style_axes(ax)
hours = np.arange(24)
ax.set_xlim(0, 23)
ax.set_xticks(range(0, 24, 3))
ax.set_xlabel('Hour of day  (CST)')
ax.set_ylabel('Power (GW)')
ax.set_ylim(0, 115)

title = ax.text(0.5, 1.06, '', transform=ax.transAxes, ha='center',
                color=FG, fontsize=14, weight='bold')
subtitle = ax.text(0.5, 0.98, '', transform=ax.transAxes, ha='center',
                   color=MUTED, fontsize=10)
ax.text(0.99, 0.02, 'August 2025 avg dispatch · illustrative AI scenario',
        transform=ax.transAxes, ha='right', color='#666', fontsize=7)

bottom = np.zeros(24)
for f in stack_order:
    y = aug[f].values
    ax.fill_between(hours, bottom, bottom + y, color=fuel_colors[f], alpha=0.92)
    bottom = bottom + y
base_top = bottom.copy()

ai_color = '#3B82F6'
ai_band_artists = [ax.fill_between(hours, base_top, base_top, color=ai_color, alpha=0.85)]
ai_label = ax.text(12, base_top.mean(), '', ha='center', va='center',
                   color='#fff', fontsize=13, weight='bold')

handles = [plt.Rectangle((0, 0), 1, 1, color=fuel_colors[f]) for f in stack_order]
handles.append(plt.Rectangle((0, 0), 1, 1, color=ai_color))
labels = [fuel_labels[f] for f in stack_order] + ['AI data centers (24/7)']
ax.legend(handles, labels, loc='upper left', frameon=False, ncol=2,
          fontsize=8, labelcolor=FG)

target_gw = 25
n_frames = 30


def update_ai(frame):
    while ai_band_artists:
        ai_band_artists.pop().remove()
    gw = (frame / (n_frames - 1)) * target_gw
    new_top = base_top + gw
    band = ax.fill_between(hours, base_top, new_top, color=ai_color, alpha=0.85)
    ai_band_artists.append(band)
    pct = 100 * gw / base_top.mean()
    title.set_text(f'What if AI adds {gw:.0f} GW of always-on load to ERCOT?')
    subtitle.set_text(f'+{gw:.0f} GW flat   ·   ~{pct:.0f}% on top of average August dispatch')
    if gw > 1.5:
        ai_label.set_text(f'+{gw:.0f} GW')
        ai_label.set_position((12, base_top.mean() + gw / 2))
    else:
        ai_label.set_text('')
    return ai_band_artists + [title, subtitle, ai_label]


anim = animation.FuncAnimation(fig, update_ai, frames=n_frames + 6, blit=False)
anim.save(ART / 'ai_load_overlay.gif', writer=PillowWriter(fps=8))
plt.close(fig)
print('  ->', ART / 'ai_load_overlay.gif')

print('Done.')
