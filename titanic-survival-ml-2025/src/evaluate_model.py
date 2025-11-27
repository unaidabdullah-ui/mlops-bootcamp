from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

from .data_loader import load_raw_data, train_val_test_split
from .features import add_basic_features, select_features


MODELS_DIR = Path(__file__).resolve().parents[1] / "models"


def evaluate_saved_model(model_filename: str = "best_model.joblib"):
    # Load model
    model_path = MODELS_DIR / model_filename
    model = joblib.load(model_path)

    # Load & preprocess data
    df = load_raw_data()
    df = add_basic_features(df)

    X = select_features(df)
    y = df["Survived"]

    df_for_split = pd.concat([X, y], axis=1)

    # Split data
    _, _, X_test, _, _, y_test = train_val_test_split(
        df_for_split,
        target_col="Survived"
    )

    # ❗ DO NOT DROP 'Survived' — it’s already removed in the split

    # Predictions
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    print("Loaded model:", model_filename)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("F1:", f1_score(y_test, y_pred))
    print("AUC:", roc_auc_score(y_test, y_proba))


if __name__ == "__main__":
    evaluate_saved_model()
