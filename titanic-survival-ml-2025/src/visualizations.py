import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pandas as pd

from .data_loader import load_raw_data
from .features import add_basic_features


FIGURES_DIR = Path(__file__).resolve().parents[1] / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def plot_survival_by_feature(df: pd.DataFrame, feature: str):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=feature, hue="Survived")
    plt.title(f"Survival by {feature}")
    plt.tight_layout()
    out_path = FIGURES_DIR / f"survival_by_{feature.lower()}.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved: {out_path}")


def plot_distributions(df: pd.DataFrame, column: str):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.tight_layout()
    out_path = FIGURES_DIR / f"dist_{column.lower()}.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    df = load_raw_data()
    df = add_basic_features(df)

    # Categorical survival plots
    for col in ["Sex", "Pclass", "Embarked", "Title", "IsAlone", "HasCabin"]:
        plot_survival_by_feature(df, col)

    # Distributions
    for col in ["Age", "Fare", "FamilySize"]:
        plot_distributions(df, col)
