import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import joblib




def train_model(df):
    X = df[["temp_30d_mean", "precip_30d_sum", "humidity_30d_mean"]]
    y = df["fire"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "data/model.pkl")
    joblib.dump(scaler, "data/scaler.pkl")


    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model


if __name__ == "__main__":
    df = pd.read_csv("data/features.csv")
    model = train_model(df)
    print("Model training complete.")
