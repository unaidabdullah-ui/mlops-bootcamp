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

## 🧱 Repo Structure

```
mlops-bootcamp/
├── 01-python/             # Python basics + file organizer project
├── 02-linux-shell/        # Bash scripting → ML training & deploy automation
├── 03-data-handling/      # pandas, SQL, web scraping, visualization
├── 04-machine-learning/   # scikit-learn pipelines, Titanic, automated EDA
└── 05-mlops/              # DVC pipelines, FastAPI + Docker + Kubernetes
```

⭐ **Highlight project:** [`05-mlops/ml-api-docker-kubernetes`](05-mlops/ml-api-docker-kubernetes): a scikit-learn model served with FastAPI, containerized with Docker, deployed on Kubernetes, with Prometheus alert rules.

---

## 🗺️ Learning Roadmap

### Stage 1: Python Fundamentals
| Folder | What's inside |
|--------|---------------|
| [`python-basics`](01-python/python-basics) | Variables, loops, functions, data structures |
| [`file-organizer`](01-python/file-organizer) | Mini project: file organizer script |

**Learned from:** CodeWithHarry, CampusX
**Free resources:** [Official Python Tutorial](https://docs.python.org/3/tutorial/) · [Kaggle Learn: Python](https://www.kaggle.com/learn/python)

### Stage 2: Linux & Shell Scripting
| Folder | What's inside |
|--------|---------------|
| [`02-linux-shell`](02-linux-shell) | Bash basics → dataset scanning → training automation → deploy scripts |

**Learned from:** TrainWithShubham
**Free resources:** [Linux Journey](https://linuxjourney.com/) · [ShellCheck](https://www.shellcheck.net/) (lint your scripts)

### Stage 3: Working With Data
| Folder | What's inside |
|--------|---------------|
| [`pandas-data-loading`](03-data-handling/pandas-data-loading) | Loading CSV, JSON and SQL data with pandas |
| [`sql-feature-engineering`](03-data-handling/sql-feature-engineering) | SQL data cleaning and feature engineering |
| [`web-scraping`](03-data-handling/web-scraping) | Quote scraper with Requests + BeautifulSoup |
| [`matplotlib-basics`](03-data-handling/matplotlib-basics), [`seaborn-eda`](03-data-handling/seaborn-eda) | Data visualization with Matplotlib and Seaborn |

**Learned from:** CampusX, CodeWithHarry
**Free resources:** [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · [SQLBolt](https://sqlbolt.com/) · [Kaggle Learn: Pandas](https://www.kaggle.com/learn/pandas) · [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Stage 4: Machine Learning
| Folder | What's inside |
|--------|---------------|
| [`sklearn-pipelines`](04-machine-learning/sklearn-pipelines) | scikit-learn Pipelines and SimpleImputer |
| [`titanic-survival`](04-machine-learning/titanic-survival) | End-to-end classification project |
| [`automated-eda-report`](04-machine-learning/automated-eda-report) | Automated EDA, training and report generation |

**Learned from:** CampusX, Krish Naik
**Free resources:** [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) · [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) · [Kaggle Learn: Intro to ML](https://www.kaggle.com/learn/intro-to-machine-learning)

### Stage 5: MLOps
| Folder | What's inside |
|--------|---------------|
| [`dvc-iris-pipeline`](05-mlops/dvc-iris-pipeline) | Reproducible pipeline with DVC (prepare → train → evaluate) |
| [`dvc-student-score`](05-mlops/dvc-student-score) | Data versioning with DVC |
| [`ml-api-docker-kubernetes`](05-mlops/ml-api-docker-kubernetes) | Model served with FastAPI, Dockerized, deployed on Kubernetes with Prometheus alert rules |

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
