import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_eda(df, output_folder="reports/"):
    plt.figure(figsize=(10,5))
    df.hist(figsize=(12,8))
    plt.savefig(f"{output_folder}/histograms.png")

    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(), annot=False)
    plt.savefig(f"{output_folder}/correlation.png")

    summary = df.describe().to_string()
    with open(f"{output_folder}/summary.txt", "w") as f:
        f.write(summary)

    return summary
