# Titanic Survival Prediction – End-to-End Data Science Project (2025)

This project demonstrates a modern data science workflow using the Titanic dataset.

## Tech Stack

- Python
- NumPy, Pandas
- Seaborn, Matplotlib
- Scikit-learn
- Joblib

## What I Did

- Performed EDA (distributions, survival rates by features).
- Engineered features: Title, FamilySize, IsAlone, HasCabin, TicketPrefix.
- Built a preprocessing pipeline using ColumnTransformer.
- Trained and compared models (Logistic Regression, Random Forest).
- Evaluated with cross-validation, Accuracy, F1, ROC-AUC.
- Saved the best model to `models/best_model.joblib`.
- Organized the project into reusable modules and scripts.

## How to Run

```bash
git clone https://github.com/unaidabdullah-ui/mlops-bootcamp/tree/4ffe250ef4dd4e32e7af967d5a7a330423fe5ef2/titanic-survival-ml-2025
cd titanic-survival-ml-2025
pip install -r requirements.txt

# Generate plots
python -m src.visualizations

# Train models
python -m src.train_model

# Evaluate saved model
python -m src.evaluate_model

