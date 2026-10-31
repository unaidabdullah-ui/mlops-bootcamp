# Stage 4: Machine Learning

⏱️ Suggested time: 4–6 weeks · 🎓 Learned from: CampusX, Krish Naik

## 🎯 Goals

By the end of this stage you can:
- Handle missing values and build scikit-learn `Pipeline`s
- Engineer features and compare models with cross-validation
- Structure an ML project as reusable modules instead of one notebook
- Automate EDA, training and reporting end to end

## 📂 What's Inside

| Folder | Topic |
|--------|-------|
| [`sklearn-pipelines`](sklearn-pipelines) | `SimpleImputer`, `ColumnTransformer` and `Pipeline` notebooks |
| [`titanic-survival`](titanic-survival) | Feature engineering, model comparison, saved best model, plots |
| [`automated-eda-report`](automated-eda-report) | One command: EDA plots → model training → PDF report (also Dockerized) |

## ▶️ Run It

```bash
cd titanic-survival
pip install -r requirements.txt
python -m src.visualizations
python -m src.train_model
python -m src.evaluate_model

cd ../automated-eda-report
pip install -r requirements.txt
python src/train.py        # writes reports/ and models/model.pkl
```

## 🏋️ Practice

1. Add a `GradientBoostingClassifier` to the Titanic model comparison. Does it beat Random Forest?
2. Add a confusion matrix image to the automated EDA PDF report.
3. Replace manual preprocessing in the Titanic project with a single `Pipeline` and save that instead.

## 📚 Free Resources

- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Kaggle Learn: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning) · [Feature Engineering](https://www.kaggle.com/learn/feature-engineering)

## ✅ Checklist

- [ ] I can explain train/validation/test splits and why leakage matters
- [ ] I can build and save a full preprocessing + model `Pipeline`
- [ ] I turned a notebook into a project with `src/` modules

**← Previous** [Stage 3: Data Handling](../03-data-handling) · **Next →** [Stage 5: MLOps](../05-mlops)
