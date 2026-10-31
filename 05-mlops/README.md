# Stage 5: MLOps

⏱️ Suggested time: 6–8 weeks · 🎓 Learned from: Krish Naik, TrainWithShubham

## 🎯 Goals

By the end of this stage you can:
- Version data and build reproducible pipelines with DVC
- Serve a model as a REST API with FastAPI
- Containerize it with Docker and deploy it on Kubernetes
- Monitor it with Prometheus metrics and alerts
- Test all of it automatically with CI (GitHub Actions)

## 📂 What's Inside

| Folder | Topic |
|--------|-------|
| [`dvc-iris-pipeline`](dvc-iris-pipeline) | DVC pipeline `prepare → train → evaluate` with `params.yaml` and tracked metrics |
| [`dvc-student-score`](dvc-student-score) | Smaller DVC pipeline: regression of score on study hours |
| [`ml-api-docker-kubernetes`](ml-api-docker-kubernetes) | ⭐ FastAPI model API, Docker image, Kubernetes manifests with probes, Prometheus rules |

## ▶️ Run It

```bash
# DVC pipeline
cd dvc-iris-pipeline
pip install -r requirements.txt
python src/prepare.py && python src/train.py && python src/evaluate.py
# or, inside a DVC repo: dvc repro && dvc metrics show

# Model API
cd ../ml-api-docker-kubernetes
docker build -t mlapi .
docker run -p 8000:8000 mlapi
# open http://127.0.0.1:8000/docs
```

Every push runs both pipelines and smoke-tests the Docker image in [CI](../.github/workflows/ci.yml).

## 🏋️ Practice

1. Change `max_depth` in `dvc-iris-pipeline/params.yaml`, re-run, and compare `metrics.json`.
2. Add input validation to `/predict` so it rejects requests without exactly 3 features (HTTP 422).
3. Deploy the API to a local cluster with [kind](https://kind.sigs.k8s.io/) or minikube and scrape `/metrics` with Prometheus.
4. Track experiments with MLflow: log params, metrics and the model from `src/train.py`.

## 📚 Free Resources

- [DataTalksClub MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp): free full course
- [Made With ML](https://madewithml.com/)
- [DVC Get Started](https://dvc.org/doc/start) · [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Docker Get Started](https://docs.docker.com/get-started/) · [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Prometheus Getting Started](https://prometheus.io/docs/prometheus/latest/getting_started/) · [GitHub Actions Docs](https://docs.github.com/en/actions)

## ✅ Checklist

- [ ] I can reproduce a pipeline from raw data to metrics with one command
- [ ] I served a model behind an API and documented it
- [ ] I deployed a container to Kubernetes with health checks
- [ ] My repo has CI that fails when something breaks

**← Previous** [Stage 4: Machine Learning](../04-machine-learning) · 🎉 **You finished the bootcamp!**
