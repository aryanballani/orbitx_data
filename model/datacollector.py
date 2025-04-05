import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from shapely.geometry import Point
import time
from geopy.distance import geodesic

NASA_POWER_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

JASPER_DATA_PATH = "data/fires_within_jasper.csv"


def fetch_climate_data(lat, lon, start_date, end_date):
    params = {
        "start": start_date.strftime("%Y%m%d"),
        "end": end_date.strftime("%Y%m%d"),
        "latitude": lat,
        "longitude": lon,
        "parameters": "T2M,PRECTOTCORR,RH2M",
        "community": "RE",
        "format": "JSON"
    }
    try:
        r = requests.get(NASA_POWER_URL, params=params)
        data = r.json()["properties"]["parameter"]
        df = pd.DataFrame({
            "date": list(data["T2M"].keys()),
            "temp": list(data["T2M"].values()),
            "humidity": list(data["RH2M"].values()),
            "precip": list(data["PRECTOTCORR"].values())
        })
        df["lat"] = lat
        df["lon"] = lon
        return df
    except Exception as e:
        print(f"Failed to fetch data for ({lat}, {lon}): {e}")
        return pd.DataFrame()


def label_fire_occurrence(lat, lon, date_range):
    jasper_data = pd.read_csv(JASPER_DATA_PATH)
    jasper_data['date'] = pd.to_datetime(jasper_data['acq_date'], format='%Y-%m-%d').dt.date

    fire_dates = jasper_data[
        jasper_data.apply(
            lambda row: geodesic((row['latitude'], row['longitude']), (lat, lon)).km <= 10,
            axis=1
        )
    ]['date'].unique()
    date_range = pd.to_datetime(date_range, format='%Y-%m-%d').date
    if len(fire_dates) == 0:
        print(f"No fire occurrences found for point ({lat}, {lon})")
        return pd.DataFrame({
            "date": date_range,
            "fire": [0] * len(date_range)
        })
    else:
        print(f"Found {len(fire_dates)} fire occurrences for point ({lat}, {lon})")
        print(f"Fire dates: {fire_dates}")
        return pd.DataFrame({
            "date": date_range,
            "fire": [1 if date in fire_dates else 0 for date in date_range]
        })



def collect_data_for_point(lat, lon, start_date, end_date):
    climate_df = fetch_climate_data(lat, lon, start_date, end_date)
    if climate_df.empty:
        return pd.DataFrame()
    # date_range = pd.to_datetime(climate_df["date"])
    date_range = pd.date_range(start=start_date, end=end_date)
    fire_df = label_fire_occurrence(lat, lon, date_range)
    climate_df['date'] = pd.to_datetime(climate_df['date'])
    fire_df['date'] = pd.to_datetime(fire_df['date'])
    # Merge climate and fire data
    full_df = climate_df.merge(fire_df, on="date")
    return full_df


def collect_dataset(points, start_date, end_date, delay=1):
    all_data = []
    for i, pt in enumerate(points):
        lat, lon = pt.y, pt.x
        print(f"[{i+1}/{len(points)}] Collecting data for point ({lat:.3f}, {lon:.3f})")
        df = collect_data_for_point(lat, lon, start_date, end_date)
        if not df.empty:
            all_data.append(df)
        time.sleep(delay)  # be nice to the API
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame()


if __name__ == "__main__":
    from geoutils import load_shapefile, buffer_geometry, generate_grid_points

    shape_path = "data/POLYGON.shp"
    gdf = load_shapefile(shape_path)
    buffered = buffer_geometry(gdf, buffer_km=5)
    points = generate_grid_points(buffered.geometry.iloc[0], spacing_km=10)

    start = datetime.now() - timedelta(days=2500)
    end = datetime.now() - timedelta(days=1)

    # df = collect_dataset(points[:5], start, end)  # Use first 5 points for testing
    label_fire_occurrence(52.5246,-115.22038, pd.date_range(start, end)).to_csv("data/fire_occurrence.csv", index=False)
    # df.to_csv("data/training_data.csv", index=False)
    print("Saved training data to data/training_data.csv")
