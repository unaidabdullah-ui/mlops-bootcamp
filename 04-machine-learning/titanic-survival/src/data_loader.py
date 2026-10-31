import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "train.csv"


def load_raw_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the raw Titanic training data."""
    df = pd.read_csv(path)
    return df


def train_val_test_split(
    df: pd.DataFrame,
    target_col: str = "Survived",
    test_size: float = 0.2,
    val_size: float = 0.2,
    random_state: int = 42,
):
    """
    Split full DF (including target) into train/val/test.
    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test
    """

    # First split: train+val vs test
    train_val_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df[target_col]
    )

    # Second split: train vs val
    val_ratio = val_size / (1 - test_size)

    train_df, val_df = train_test_split(
        train_val_df,
        test_size=val_ratio,
        random_state=random_state,
        stratify=train_val_df[target_col],
    )

    # Separate X and y
    X_train = train_df.drop(columns=[target_col])
    y_train = train_df[target_col]

    X_val = val_df.drop(columns=[target_col])
    y_val = val_df[target_col]

    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col]

    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == "__main__":
    df = load_raw_data()
    print(df.head())
    splits = train_val_test_split(df)
    print("Train shape:", splits[0].shape)
