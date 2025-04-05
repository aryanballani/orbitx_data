import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, precision_recall_curve
import xgboost as xgb
import joblib
import matplotlib.pyplot as plt


def train_model(df):
    # Features and target
    X = df[["temp_30d_mean", "precip_30d_sum", "humidity_30d_mean"]]
    y = df["fire"]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Handle class imbalance with scale_pos_weight
    pos_weight = (y == 0).sum() / (y == 1).sum()

    # Small XGBoost model
    model = xgb.XGBClassifier(
        n_estimators=50,
        max_depth=3,
        learning_rate=0.1,
        scale_pos_weight=pos_weight,
        use_label_encoder=False,
        eval_metric="logloss",
        random_state=42
    )
    model.fit(X_train, y_train)

    # Save model + scaler
    joblib.dump(model, "data/xgb_model.pkl")
    joblib.dump(scaler, "data/xgb_scaler.pkl")

    # Predict probabilities
    y_probs = model.predict_proba(X_test)[:, 1]

    # Precision-recall curve
    precision, recall, thresholds = precision_recall_curve(y_test, y_probs)

    # Plot precision-recall vs threshold
    plt.figure(figsize=(10, 6))
    plt.plot(thresholds, precision[:-1], label="Precision", color="b")
    plt.plot(thresholds, recall[:-1], label="Recall", color="g")
    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.title("Precision and Recall vs Threshold")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Select a custom threshold (e.g., 0.2)
    threshold = 0.6
    y_pred = (y_probs >= threshold).astype(int)

    # Show classification report
    print(f"\nClassification Report (Threshold = {threshold}):")
    print(classification_report(y_test, y_pred, digits=4))

    return model


if __name__ == "__main__":
    df = pd.read_csv("data/features.csv")
    model = train_model(df)
    print("Model training complete.")
