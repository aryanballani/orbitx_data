import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib


def predict_risk(model, scaler, new_data_df):
    X = new_data_df[["temp_30d_mean", "precip_30d_sum", "humidity_30d_mean"]]
    X_scaled = scaler.transform(X)
    predictions = model.predict_proba(X_scaled)[:, 1]  # Probability of class 1 (fire)
    new_data_df["fire_risk"] = predictions
    return new_data_df[["lat", "lon", "date", "fire_risk"]]


if __name__ == "__main__":
    # Example usage with saved model + scaler (optional to save from training)
    model = joblib.load("data/model.pkl")
    scaler = joblib.load("data/scaler.pkl")

    new_data = pd.read_csv("data/new_features.csv")  # Features for unseen data
    result_df = predict_risk(model, scaler, new_data)
    print(result_df.head())
