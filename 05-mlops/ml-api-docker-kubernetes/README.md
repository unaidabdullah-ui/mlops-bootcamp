# 🚀 ML Model API: FastAPI + Docker + Kubernetes + Prometheus

A scikit-learn model served as a REST API, containerized with Docker, deployed to Kubernetes with health probes, and monitored with Prometheus.

---

## 📌 Features

- FastAPI REST API with Swagger UI at `/docs`
- Random Forest classifier trained with scikit-learn, saved with joblib
- Docker image that trains the model at build time, so it always matches the installed library versions
- Kubernetes Deployment (2 replicas, readiness/liveness probes, resource limits) + LoadBalancer Service
- Prometheus metrics at `/metrics`, with a p95 latency recording rule and an alert

---

## ⚙️ Tech Stack

FastAPI · scikit-learn · pandas · joblib · Docker · Kubernetes · Prometheus

---

## 📁 Project Structure

```
ml-api-docker-kubernetes/
├── api/main.py          # FastAPI app: /, /health, /predict, /metrics
├── src/
│   ├── train.py         # trains the model → models/model.pkl
│   ├── predict.py       # predict from Python
│   └── utils.py
├── data/data.csv        # training data (feature1, feature2, feature3, label)
├── models/model.pkl
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── prom-rules.yaml  # Prometheus recording rule + alert
├── Dockerfile
└── requirements.txt
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python src/train.py
uvicorn api.main:app --reload
```

Open http://127.0.0.1:8000/docs

---

## 🔮 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check (used by Kubernetes probes) |
| POST | `/predict` | Body: `[3.5, 1.2, 0.8]` → `{"prediction": 1}` |
| GET | `/metrics` | Prometheus metrics |

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "[3.5, 1.2, 0.8]"
```

---

## 🐳 Docker

```bash
docker build -t mlapi .
docker run -p 8000:8000 mlapi
```

---

## ☸️ Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -l app=mlapi
```

Using a local cluster (minikube/kind)? Build the image there and change `image:` in `deployment.yaml`.

---

## 📊 Monitoring

| Metric | Type | Meaning |
|--------|------|---------|
| `predictions_total` | Counter | Predictions served |
| `prediction_latency_seconds` | Histogram | Time spent in `model.predict` |

Pods are annotated for Prometheus scraping. `k8s/prom-rules.yaml` records p95 latency and fires `MLApiHighLatency` when it stays above 500 ms for 5 minutes.

---

## 💡 Next Steps

- Model versioning with MLflow
- Grafana dashboard for the metrics above
- Auto-retraining pipeline
