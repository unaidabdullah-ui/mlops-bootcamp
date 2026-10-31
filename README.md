# 🚀 MLOps Bootcamp: My Learning Path, From Python to Production ML

This repo is my record of learning **MLOps from scratch**: what I learned, in what order, and where I learned it.
Every folder is hands-on code I wrote along the way.

If you're starting the same journey, follow the stages in order and use the free resources listed under each one. ⭐ Star the repo if it helps you.

---

## 🎓 Where I Learned

All free on YouTube. Huge thanks to these creators:

| Creator | What I learned there |
|---------|----------------------|
| [CampusX](https://www.youtube.com/@campusx-official) | Python, pandas, Machine Learning (100 Days of ML), ML concepts in depth |
| [Krish Naik](https://www.youtube.com/@krishnaik06) | End-to-end ML projects, MLOps, DVC, deployment |
| [CodeWithHarry](https://www.youtube.com/@CodeWithHarry) | Python and Data Science fundamentals |
| [TrainWithShubham](https://www.youtube.com/@TrainWithShubham) | DevOps: Linux, shell scripting, Docker, Kubernetes, CI/CD |

---

## 🗺️ Learning Roadmap

### Stage 1: Python Fundamentals
| Folder | What's inside |
|--------|---------------|
| [`PYHTON_FUNDAMENTALS`](PYHTON_FUNDAMENTALS) | Variables, loops, functions, data structures |
| [`Organizer-python`](Organizer-python) | Mini project: file organizer script |

**Learned from:** CodeWithHarry, CampusX
**Free resources:** [Official Python Tutorial](https://docs.python.org/3/tutorial/) · [Kaggle Learn: Python](https://www.kaggle.com/learn/python)

### Stage 2: Linux & Shell Scripting
| Folder | What's inside |
|--------|---------------|
| [`shell-scripting`](shell-scripting) | Bash basics → dataset scanning → training automation → deploy scripts |

**Learned from:** TrainWithShubham
**Free resources:** [Linux Journey](https://linuxjourney.com/) · [ShellCheck](https://www.shellcheck.net/) (lint your scripts)

### Stage 3: Working With Data
| Folder | What's inside |
|--------|---------------|
| [`machine learning`](machine%20learning) | Loading CSV, JSON and SQL data with pandas |
| [`sql-mlops-pipeline`](sql-mlops-pipeline) | SQL data cleaning and feature engineering |
| [`web-scraping`](web-scraping) | Quote scraper with Requests + BeautifulSoup |
| [`matplotlib_basic`](matplotlib_basic), [`sns_model`](sns_model) | Data visualization with Matplotlib and Seaborn |

**Learned from:** CampusX, CodeWithHarry
**Free resources:** [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [SQLBolt](https://sqlbolt.com/) · [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) · [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Stage 4: Machine Learning
| Folder | What's inside |
|--------|---------------|
| [`Sicket-learn`](Sicket-learn) | scikit-learn Pipelines and SimpleImputer |
| [`titanic-survival-ml-2025`](titanic-survival-ml-2025) | End-to-end classification project |
| [`automated-eda-ml-report`](automated-eda-ml-report) | Automated EDA, training and report generation |

**Learned from:** CampusX, Krish Naik
**Free resources:** [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) · [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) · [Kaggle Learn: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning)

### Stage 5: MLOps
| Folder | What's inside |
|--------|---------------|
| [`dvc-iris-ml-pipeline`](dvc-iris-ml-pipeline) | Reproducible pipeline with DVC (prepare → train → evaluate) |
| [`student-score-dvc`](student-score-dvc) | Data versioning with DVC |
| [`mlops-project`](mlops-project) | Model served with FastAPI, Dockerized, deployed on Kubernetes with Prometheus alert rules |

**Learned from:** Krish Naik, TrainWithShubham
**Free resources:** [DataTalksClub MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) · [Made With ML](https://madewithml.com/) · [DVC Get Started](https://dvc.org/doc/start) · [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [Docker Get Started](https://docs.docker.com/get-started/) · [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## ▶️ How to Use This Repo

```bash
git clone https://github.com/unaidabdullah-ui/mlops-bootcamp.git
cd mlops-bootcamp
```

Then open any stage folder. Projects with their own `README.md` explain how to run them.
Some large datasets aren't committed; check the `DATA.md` in that folder for the download link.

---

## 🔜 Next Up

- CI/CD with GitHub Actions for the MLOps projects
- Experiment tracking with MLflow
- Model drift detection and monitoring dashboards

---

## 👨‍💻 Author

**Unaid Abdullah**: MLOps Engineer | ML Infrastructure | Cloud & DevOps
[GitHub](https://github.com/unaidabdullah-ui) · [Portfolio](https://unaidabdullah-ui.github.io)
