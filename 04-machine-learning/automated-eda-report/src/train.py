import os
from utils import load_data, save_model
from eda import generate_eda
from modeling import train_models
from report import create_pdf_report

def main():
    df = load_data("data/sample.csv")

    print("Generating EDA...")
    summary = generate_eda(df)

    print("Training models...")
    model, model_results = train_models(df, target=df.columns[-1])

    print("Saving best model...")
    os.makedirs("models", exist_ok=True)
    save_model(model)

    print("Preparing PDF Report...")
    create_pdf_report(summary, model_results)

    print("Pipeline Complete! Report saved in reports/")

if __name__ == "__main__":
    main()
