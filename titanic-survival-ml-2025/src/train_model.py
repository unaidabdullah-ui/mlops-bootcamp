from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .data_loader import load_raw_data, train_val_test_split
from .features import add_basic_features, select_features


MODELS_DIR = Path(__file__).resolve().parents[1] / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)


def build_preprocessing_pipeline(X: pd.DataFrame) -> ColumnTransformer:
    """Build a ColumnTransformer for numeric + categorical preprocessing."""
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    return preprocessor


def train_and_evaluate():
    # Load & feature engineer
    df = load_raw_data()
    df = add_basic_features(df)

    # Target
    y = df["Survived"]
    X = select_features(df)

    # Split
    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(
        df=pd.concat([X, y], axis=1), target_col="Survived"
    )

    

    # Preprocessing
    preprocessor = build_preprocessing_pipeline(X_train)

    # Two models: Logistic Regression & Random Forest
    log_reg = LogisticRegression(max_iter=1000)
    rf_clf = RandomForestClassifier(
        n_estimators=200, max_depth=5, random_state=42
    )

    models = {
        "log_reg": log_reg,
        "random_forest": rf_clf,
    }

    best_model_name = None
    best_val_score = -np.inf
    best_pipeline = None

    for name, model in models.items():
        clf = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        # Cross-validation on training data
        cv_scores = cross_val_score(clf, X_train, y_train, cv=5, scoring="accuracy")
        print(f"{name} CV accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

        # Fit on train and evaluate on validation
        clf.fit(X_train, y_train)
        y_val_pred = clf.predict(X_val)
        y_val_proba = clf.predict_proba(X_val)[:, 1]

        acc = accuracy_score(y_val, y_val_pred)
        f1 = f1_score(y_val, y_val_pred)
        auc = roc_auc_score(y_val, y_val_proba)

        print(f"{name} Val Accuracy: {acc:.4f}, F1: {f1:.4f}, AUC: {auc:.4f}\n")

        if acc > best_val_score:
            best_val_score = acc
            best_model_name = name
            best_pipeline = clf

    print(f"Best model on validation: {best_model_name} (Acc = {best_val_score:.4f})")

    # Final evaluation on test set
    y_test_pred = best_pipeline.predict(X_test)
    y_test_proba = best_pipeline.predict_proba(X_test)[:, 1]

    test_acc = accuracy_score(y_test, y_test_pred)
    test_f1 = f1_score(y_test, y_test_pred)
    test_auc = roc_auc_score(y_test, y_test_proba)

    print(f"Test Accuracy: {test_acc:.4f}")
    print(f"Test F1: {test_f1:.4f}")
    print(f"Test AUC: {test_auc:.4f}")

    # Save best model
    model_path = MODELS_DIR / "best_model.joblib"
    joblib.dump(best_pipeline, model_path)
    print(f"Saved best model to: {model_path}")


if __name__ == "__main__":
    train_and_evaluate()
