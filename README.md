# 🚀 MLOps Bootcamp: From Python to Production ML

[![CI](https://github.com/unaidabdullah-ui/mlops-bootcamp/actions/workflows/ci.yml/badge.svg)](https://github.com/unaidabdullah-ui/mlops-bootcamp/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A free, self-paced **MLOps bootcamp** built from my own learning journey. It has 5 stages, from your first Python script to a monitored ML API on Kubernetes.
Every stage has goals, hands-on code, practice exercises, free resources and a checklist.

⭐ Star the repo if it helps you, and fork it to track your own progress.

---

## 🗺️ Roadmap

| # | Stage | You'll learn | Time | Key project |
|---|-------|--------------|------|-------------|
| 1 | [Python Fundamentals](01-python) | Python, OOP, NumPy, pandas, CLI tools | 2–3 wks | File organizer CLI |
| 2 | [Linux & Shell](02-linux-shell) | Bash, Linux commands, automation scripts | 1–2 wks | Training & deploy scripts |
| 3 | [Working With Data](03-data-handling) | pandas I/O, SQL, web scraping, visualization | 3–4 wks | SQL feature-engineering pipeline |
| 4 | [Machine Learning](04-machine-learning) | scikit-learn, pipelines, feature engineering | 4–6 wks | Titanic end-to-end project |
| 5 | [MLOps](05-mlops) | DVC, FastAPI, Docker, Kubernetes, Prometheus, CI | 6–8 wks | ⭐ [ML API on Kubernetes](05-mlops/ml-api-docker-kubernetes) |

**Total: about 4–6 months** at 1–2 hours a day.

---

## 🧭 How to Follow This Bootcamp

1. **Fork** this repo, then clone your fork:
   ```bash
   git clone https://github.com/<your-username>/mlops-bootcamp.git
   ```
2. Go **stage by stage**. Open the stage's `README.md`, read the goals, and run the code.
3. Do the **🏋️ Practice** exercises yourself. That's where the learning happens.
4. Tick the **✅ Checklist** in your fork before moving on.

**Prerequisites:** a laptop, Python 3.10+, Git, and (for Stage 5) Docker. No prior coding experience needed.

---

## 🎓 Where I Learned

Everything here is learned from free YouTube content. Huge thanks to these creators:

| Creator | What I learned there |
|---------|----------------------|
| [CampusX](https://www.youtube.com/@campusx-official) | Python, pandas, Machine Learning (100 Days of ML) |
| [Krish Naik](https://www.youtube.com/@krishnaik06) | End-to-end ML projects, MLOps, DVC, deployment |
| [CodeWithHarry](https://www.youtube.com/@CodeWithHarry) | Python and Data Science fundamentals |
| [TrainWithShubham](https://www.youtube.com/@TrainWithShubham) | DevOps: Linux, shell scripting, Docker, Kubernetes, CI/CD |

Each stage's README also lists free docs and courses for going deeper.

---

## 🧱 Repo Structure

```
mlops-bootcamp/
├── 01-python/             # Python basics + file organizer CLI
├── 02-linux-shell/        # Bash scripting → training & deploy automation
├── 03-data-handling/      # pandas, SQL, web scraping, visualization
├── 04-machine-learning/   # scikit-learn pipelines, Titanic, automated EDA
├── 05-mlops/              # DVC pipelines, FastAPI + Docker + Kubernetes + Prometheus
└── .github/workflows/     # CI: ShellCheck, Ruff, DVC pipelines, Docker smoke test
```

---

## ✅ What CI Checks on Every Push

- All shell scripts pass **ShellCheck**
- Python has no syntax errors or undefined names (**Ruff**)
- Both **DVC pipelines** run end to end
- The **ML API Docker image** builds and answers `/health`, `/predict` and `/metrics`

---

## 🔜 Coming Next

- Experiment tracking with MLflow
- Grafana dashboard for the model API
- Model drift detection

---

## 👨‍💻 Author

**Unaid Abdullah**: MLOps Engineer | ML Infrastructure | Cloud & DevOps
[GitHub](https://github.com/unaidabdullah-ui) · [LinkedIn](https://www.linkedin.com/in/unaid-abdullah/) · [Portfolio](https://unaidabdullah-ui.github.io)

Licensed under [MIT](LICENSE).
