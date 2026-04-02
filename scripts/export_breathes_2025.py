#!/usr/bin/env python3
"""
Export 2025 data for the "India Breathes" interactive web page.

Reads existing CSVs, derives CO2/clean-share columns, fetches temperature
from Open-Meteo, computes regional map data, and exports:
  - data/processed/india_2025_derived.csv
  - data/processed/india_2025_temperature.csv
  - web/data/breathes_2025.json
  - web/data/india_topo.json  (simplified GeoJSON, not true TopoJSON)
"""

import json
import math
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"
WEB_DATA = ROOT / "web" / "data"

# Emission factors (tCO2/GWh) — from NB03, IPCC + CEA India-specific
EF_COAL = 950
EF_LIGNITE = 1100
EF_GAS = 400

# POSOCO grid regions → GeoJSON ST_NM state names
STATE_TO_REGION = {
    # Northern Region
    "Delhi": "NR", "Uttar Pradesh": "NR", "Punjab": "NR",
    "Haryana": "NR", "Rajasthan": "NR", "Himachal Pradesh": "NR",
    "Uttarakhand": "NR", "Jammu & Kashmir": "NR", "Ladakh": "NR",
    "Chandigarh": "NR",
    # Western Region
    "Maharashtra": "WR", "Gujarat": "WR", "Madhya Pradesh": "WR",
    "Chhattisgarh": "WR", "Goa": "WR",
    "Dadra and Nagar Haveli and Daman and Diu": "WR",
    # Southern Region
    "Tamil Nadu": "SR", "Karnataka": "SR", "Kerala": "SR",
    "Andhra Pradesh": "SR", "Telangana": "SR", "Puducherry": "SR",
    "Lakshadweep": "SR",
    # Eastern Region
    "West Bengal": "ER", "Bihar": "ER", "Jharkhand": "ER",
    "Odisha": "ER", "Sikkim": "ER",
    "Andaman & Nicobar": "ER",
    # North-Eastern Region
    "Assam": "NER", "Arunachal Pradesh": "NER", "Meghalaya": "NER",
    "Manipur": "NER", "Mizoram": "NER", "Nagaland": "NER",
    "Tripura": "NER",
}

REGIONS = ["NR", "WR", "SR", "ER", "NER"]
MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 5 cities for temperature (same as NB15)
CITIES = {
    "Delhi":     {"lat": 28.6139, "lon": 77.2090},
    "Mumbai":    {"lat": 19.0760, "lon": 72.8777},
    "Chennai":   {"lat": 13.0827, "lon": 80.2707},
    "Kolkata":   {"lat": 22.5726, "lon": 88.3639},
    "Bengaluru": {"lat": 12.9716, "lon": 77.5946},
}


def load_and_derive_2025():
    """Load india_all_years.csv, filter to 2025, derive CO2/share columns."""
    print("Loading india_all_years.csv ...")
    df = pd.read_csv(DATA_PROC / "india_all_years.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df[(df["date"].dt.year == 2025)].copy().reset_index(drop=True)
    print(f"  2025 rows: {len(df)}")

    # Forward-fill null wind values
    nulls = df["wind"].isna().sum()
    if nulls > 0:
        print(f"  Forward-filling {nulls} null wind values")
        df["wind"] = df["wind"].ffill()

    # CO2 emissions (kt/day)
    df["co2_coal"] = df["coal"] * EF_COAL / 1000
    df["co2_lignite"] = df["lignite"] * EF_LIGNITE / 1000
    df["co2_gas"] = df["gas"] * EF_GAS / 1000
    df["co2_total"] = df["co2_coal"] + df["co2_lignite"] + df["co2_gas"]

    # Emissions intensity (tCO2/GWh; total is in MU = GWh)
    df["emissions_intensity"] = df["co2_total"] / (df["total"] / 1000)

    # Shares (%)
    df["re_share"] = (df["wind"] + df["solar"] + df["other_re"]) / df["total"] * 100
    df["clean_share"] = (df["nuclear"] + df["hydro"] + df["wind"] + df["solar"] + df["other_re"]) / df["total"] * 100
    df["fossil_share"] = (df["coal"] + df["lignite"] + df["gas"] + df["diesel"]) / df["total"] * 100
    df["wind_solar"] = df["wind"] + df["solar"]
    df["wind_solar_share"] = df["wind_solar"] / df["total"] * 100

    # Month
    df["month"] = df["date"].dt.month

    # Cumulative
    fossil_daily = df["coal"] + df["lignite"] + df["gas"] + df.get("diesel", 0)
    clean_daily = df["nuclear"] + df["hydro"] + df["wind"] + df["solar"] + df["other_re"]
    df["cum_fossil"] = fossil_daily.cumsum()
    df["cum_clean"] = clean_daily.cumsum()
    df["cum_total"] = df["total"].cumsum()
    df["cum_clean_pct"] = df["cum_clean"] / df["cum_total"] * 100

    # Save derived CSV
    out = DATA_PROC / "india_2025_derived.csv"
    df.to_csv(out, index=False)
    print(f"  Saved {out}")

    return df


def fetch_temperature_2025():
    """Fetch 2025 daily temperature from Open-Meteo for 5 cities."""
    out_path = DATA_PROC / "india_2025_temperature.csv"

    # Check if already cached
    if out_path.exists():
        print(f"Temperature file exists, loading from cache: {out_path}")
        return pd.read_csv(out_path, parse_dates=["date"])

    print("Fetching 2025 temperature from Open-Meteo ...")
    all_city_data = {}

    for city, coords in CITIES.items():
        print(f"  Fetching {city} ...")
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "daily": "temperature_2m_mean,temperature_2m_max,temperature_2m_min",
            "timezone": "Asia/Kolkata",
        }
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()["daily"]

        all_city_data[f"{city}_mean"] = data["temperature_2m_mean"]
        all_city_data[f"{city}_max"] = data["temperature_2m_max"]
        all_city_data[f"{city}_min"] = data["temperature_2m_min"]

        if "date" not in all_city_data:
            all_city_data["date"] = data["time"]

    df_temp = pd.DataFrame(all_city_data)
    df_temp["date"] = pd.to_datetime(df_temp["date"])

    # Compute 5-city averages
    mean_cols = [f"{c}_mean" for c in CITIES]
    max_cols = [f"{c}_max" for c in CITIES]
    min_cols = [f"{c}_min" for c in CITIES]
    df_temp["india_mean"] = df_temp[mean_cols].mean(axis=1)
    df_temp["india_max"] = df_temp[max_cols].mean(axis=1)
    df_temp["india_min"] = df_temp[min_cols].mean(axis=1)

    df_temp.to_csv(out_path, index=False)
    print(f"  Saved {out_path} ({len(df_temp)} days)")
    return df_temp


def compute_regional_map_data():
    """Compute monthly clean energy share per POSOCO region for 2025."""
    print("Computing regional map data from POSOCO ...")
    df = pd.read_csv(DATA_RAW / "POSOCO_data.csv")
    df = df[(df["yyyymmdd"] >= 20250101) & (df["yyyymmdd"] <= 20251231)].copy()
    df["date"] = pd.to_datetime(df["yyyymmdd"], format="%Y%m%d")
    df["month"] = df["date"].dt.month
    print(f"  POSOCO 2025 rows: {len(df)}")

    monthly_clean = {}
    for region in REGIONS:
        monthly_vals = []
        for m in range(1, 13):
            mdf = df[df["month"] == m]
            total = mdf[f"{region}: Total"].sum()
            coal = mdf[f"{region}: Coal"].sum()
            hydro = mdf[f"{region}: Hydro"].sum()
            nuclear = mdf[f"{region}: Nuclear"].sum()
            res = mdf[f"{region}: RES"].sum()
            clean = hydro + nuclear + res
            clean_pct = 100 * clean / total if total > 0 else 0
            monthly_vals.append(round(clean_pct, 1))
        monthly_clean[region] = monthly_vals

    return monthly_clean


def simplify_geojson():
    """Load GeoJSON and output a simplified version for web use."""
    print("Processing GeoJSON ...")
    geo_path = DATA_RAW / "india_states.geojson"
    out_path = WEB_DATA / "india_topo.json"

    with open(geo_path) as f:
        geo = json.load(f)

    # Reduce coordinate precision to shrink file size (~60% reduction)
    def round_coords(coords, precision=3):
        if isinstance(coords[0], (int, float)):
            return [round(c, precision) for c in coords]
        return [round_coords(c, precision) for c in coords]

    for feature in geo["features"]:
        feature["geometry"]["coordinates"] = round_coords(
            feature["geometry"]["coordinates"]
        )
        # Keep only ST_NM property
        feature["properties"] = {"ST_NM": feature["properties"]["ST_NM"]}

    with open(out_path, "w") as f:
        json.dump(geo, f, separators=(",", ":"))

    size_kb = os.path.getsize(out_path) / 1024
    print(f"  Saved {out_path} ({size_kb:.0f} KB)")
    return geo


def build_json(df, df_temp, monthly_clean):
    """Build the master breathes_2025.json for all 6 panels."""
    print("Building breathes_2025.json ...")
    n_days = len(df)
    dates = df["date"].dt.strftime("%Y-%m-%d").tolist()

    # --- Bloom data ---
    max_total = df["total"].max()
    bloom = {
        "total": [round(v, 1) for v in df["total"].tolist()],
        "clean_pct": [round(v, 2) for v in df["clean_share"].tolist()],
        "max_total": round(max_total, 1),
    }

    # --- Week/DOW columns (used by temp heatmap + day_to_week) ---
    df["dow"] = df["date"].dt.dayofweek  # 0=Mon, 6=Sun
    df["week"] = df["date"].dt.isocalendar().week.astype(int)
    # Fix: week 1 of next year for late Dec days
    df.loc[(df["month"] == 12) & (df["week"] == 1), "week"] = 53

    # --- Map data ---
    map_data = {
        "monthly_clean": monthly_clean,
        "state_to_region": STATE_TO_REGION,
    }

    # --- Heartbeat data ---
    heartbeat = {
        "fossil": {
            "coal": [round(v, 1) for v in df["coal"].tolist()],
            "lignite": [round(v, 1) for v in df["lignite"].tolist()],
            "gas": [round(v, 1) for v in df["gas"].tolist()],
        },
        "clean": {
            "nuclear": [round(v, 1) for v in df["nuclear"].tolist()],
            "hydro": [round(v, 1) for v in df["hydro"].tolist()],
            "wind": [round(v, 1) for v in df["wind"].tolist()],
            "solar": [round(v, 1) for v in df["solar"].tolist()],
            "other_re": [round(v, 1) for v in df["other_re"].tolist()],
        },
    }

    # --- CO2 data ---
    cum_co2 = (df["co2_total"].cumsum() / 1000).tolist()  # Mt
    co2 = {
        "daily_kt": [round(v, 1) for v in df["co2_total"].tolist()],
        "cumulative_mt": [round(v, 2) for v in cum_co2],
        "intensity": [round(v, 1) for v in df["emissions_intensity"].tolist()],
    }

    # --- Temperature data ---
    # Align temperature df with main df by date
    temp_merged = df[["date"]].merge(df_temp[["date", "india_mean"]], on="date", how="left")
    # Fill any missing temp days
    temp_merged["india_mean"] = temp_merged["india_mean"].ffill().bfill()

    temperature = {
        "india_mean": [round(v, 1) for v in temp_merged["india_mean"].tolist()],
    }

    # --- Temperature heatmap (52x7 grid) ---
    # Merge temp into main df for pivoting
    df["temp_mean"] = temp_merged["india_mean"].values

    temp_pivot = df.pivot_table(
        values="temp_mean", index="week", columns="dow", aggfunc="mean"
    )
    for d in range(7):
        if d not in temp_pivot.columns:
            temp_pivot[d] = float("nan")
    temp_pivot = temp_pivot.sort_index()

    temp_heatmap = {
        "weeks": len(temp_pivot),
        "dow": 7,
        "z": [[round(v, 1) if not math.isnan(v) else None
               for v in row] for row in temp_pivot.values.tolist()],
        "z_min": round(temp_pivot.min().min(), 1),
        "z_max": round(temp_pivot.max().max(), 1),
        "week_indices": temp_pivot.index.tolist(),
    }

    # --- Meta & stats ---
    meta = {
        "year": 2025,
        "n_days": n_days,
        "dates": dates,
        "month_names": MONTH_NAMES,
    }

    stats = {
        "total_twh": round(df["total"].sum() / 1000, 1),
        "clean_share_avg": round(df["clean_share"].mean(), 1),
        "peak_demand_mu": round(df["total"].max(), 1),
        "co2_total_mt": round(cum_co2[-1], 1),
        "min_clean_pct": round(df["clean_share"].min(), 1),
        "max_clean_pct": round(df["clean_share"].max(), 1),
    }

    # --- Day-to-week mapping for heatmap reveal ---
    day_to_week = []
    week_list = temp_pivot.index.tolist()
    for _, row in df.iterrows():
        w = row["week"]
        if w in week_list:
            day_to_week.append(week_list.index(w))
        else:
            day_to_week.append(len(week_list) - 1)

    output = {
        "meta": meta,
        "stats": stats,
        "bloom": bloom,
        "temp_heatmap": temp_heatmap,
        "map": map_data,
        "heartbeat": heartbeat,
        "co2": co2,
        "temperature": temperature,
        "day_to_week": day_to_week,
    }

    out_path = WEB_DATA / "breathes_2025.json"
    with open(out_path, "w") as f:
        json.dump(output, f, separators=(",", ":"))

    size_kb = os.path.getsize(out_path) / 1024
    print(f"  Saved {out_path} ({size_kb:.0f} KB)")
    return output


def main():
    os.makedirs(WEB_DATA, exist_ok=True)
    os.makedirs(DATA_PROC, exist_ok=True)

    df = load_and_derive_2025()
    df_temp = fetch_temperature_2025()
    monthly_clean = compute_regional_map_data()
    simplify_geojson()
    data = build_json(df, df_temp, monthly_clean)

    print("\n--- Summary ---")
    print(f"Days: {data['meta']['n_days']}")
    print(f"Total generation: {data['stats']['total_twh']} TWh")
    print(f"Avg clean share: {data['stats']['clean_share_avg']}%")
    print(f"Peak demand: {data['stats']['peak_demand_mu']} MU/day")
    print(f"Total CO2: {data['stats']['co2_total_mt']} Mt")
    print("\nDone!")


if __name__ == "__main__":
    main()
