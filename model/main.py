from datetime import datetime, timedelta
from geoutils import load_shapefile, buffer_geometry, generate_grid_points
from datacollector import collect_dataset
from featureeng import generate_features
from model import train_model
import pandas as pd
import os


def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")


def main():
    ensure_data_dir()

    print("Step 1: Load and buffer shapefile...")
    gdf = load_shapefile("data/POLYGON.shp")
    buffered = buffer_geometry(gdf, buffer_km=5)

    print("Step 2: Generate grid points...")
    points = generate_grid_points(buffered.geometry.iloc[0], spacing_km=10)

    print("Step 3: Collect climate + fire data for 5 years...")
    start = datetime.now() - timedelta(days=2500)
    end = datetime.now() - timedelta(days=1)
    df_raw = collect_dataset(points, start, end)
    df_raw.to_csv("data/training_data.csv", index=False)

    print("Step 4: Feature engineering...")
    df_features = generate_features(df_raw)
    df_features.to_csv("data/features.csv", index=False)

    print("Step 5: Model training...")
    model = train_model(df_features)
    print("Pipeline complete.")


if __name__ == "__main__":
    main()