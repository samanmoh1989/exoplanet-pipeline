"""
train_model.py
---------------
Trains a simple machine learning model (RandomForest)
to classify transit-like signals using extracted BLS features.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
from pathlib import Path

def train_model(features_csv: str = "../data/processed/all_bls_features.csv", model_dir: str = "../models"):
    df = pd.read_csv(features_csv)
    X = df[["period_days", "duration_days", "depth_ppm", "snr"]]
    y = df["label"]  # 0 = false positive, 1 = real transit

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    model_dir = Path(model_dir)
    model_dir.mkdir(parents=True, exist_ok=True)
    dump(model, model_dir / "rf_transit_classifier.joblib")
    print(f"[✓] Model saved to {model_dir}/rf_transit_classifier.joblib")

if __name__ == "__main__":
    train_model()
