import pandas as pd
import numpy as np


def generate_features(df):
    """
    Input: Raw dataframe with daily climate data + fire labels
    Output: Aggregated features per point (lat/lon)
    """
    df["date"] = pd.to_datetime(df["date"])
    df_grouped = df.groupby(["lat", "lon"])

    features = []
    for (lat, lon), group in df_grouped:
        group = group.sort_values("date")

        # 30-day rolling means as a sample feature set
        group["temp_30d_mean"] = group["temp"].rolling(window=30).mean()
        group["precip_30d_sum"] = group["precip"].rolling(window=30).sum()
        group["humidity_30d_mean"] = group["humidity"].rolling(window=30).mean()

        # Drop first 29 days (NaNs)
        group = group.dropna()

        # Extract features per day
        for _, row in group.iterrows():
            features.append({
                "lat": lat,
                "lon": lon,
                "date": row["date"],
                "temp_30d_mean": row["temp_30d_mean"],
                "precip_30d_sum": row["precip_30d_sum"],
                "humidity_30d_mean": row["humidity_30d_mean"],
                "fire": row["fire"]
            })

    return pd.DataFrame(features)


if __name__ == "__main__":
    df = pd.read_csv("data/training_data.csv")
    features_df = generate_features(df)
    features_df.to_csv("data/features.csv", index=False)
    print("Saved engineered features to data/features.csv")
