import pandas as pd
import numpy as np


def extract_title(name: str) -> str:
    """Extract title from passenger name."""
    if pd.isna(name):
        return "Unknown"
    return name.split(",")[1].split(".")[0].strip()


def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add handcrafted features commonly used in Titanic problems."""
    df = df.copy()

    # Title from name
    df["Title"] = df["Name"].apply(extract_title)

    # Family size
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # Is alone
    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    # Cabin known or not
    df["HasCabin"] = df["Cabin"].notna().astype(int)

    # Ticket prefix (e.g., 'PC', 'A/5')
    df["TicketPrefix"] = (
        df["Ticket"]
        .apply(lambda x: "".join([c for c in str(x) if not c.isdigit()]).strip() or "None")
    )

    # Fill missing embarked with mode
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Age & Fare: simple imputation with median
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    return df


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """Select final set of features to feed into ML model."""
    feature_cols = [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Embarked",
        "Title",
        "FamilySize",
        "IsAlone",
        "HasCabin",
        "TicketPrefix",
    ]
    return df[feature_cols]


if __name__ == "__main__":
    from data_loader import load_raw_data

    df = load_raw_data()
    df_feat = add_basic_features(df)
    print(df_feat.head())
    print(select_features(df_feat).head())
