# 🚀 ML Model API (MLOps Project)

A production-ready Machine Learning API built using FastAPI, Docker, Kubernetes, and Scikit-learn.  
This project demonstrates an end-to-end MLOps pipeline — from training to deployment and monitoring.

---

## 📌 Features

- FastAPI-based REST API  
- Machine Learning model (Random Forest)  
- Model training & serialization (joblib)  
- Dockerized application  
- Kubernetes deployment  
- Basic monitoring (latency tracking + Prometheus rules)  
- Clean modular project structure  
- Swagger UI support (/docs)  

---

## 🧠 ML Model

- Algorithm: Random Forest Classifier  
- Dataset: CSV file (data/data.csv)  
- Model saved as: models/model.pkl  

---

## ⚙️ Tech Stack

- Backend: FastAPI  
- ML: Scikit-learn, Pandas, NumPy  
- Model Storage: Joblib  
- Containerization: Docker  
- Orchestration: Kubernetes  
- Monitoring: Prometheus  
- Versioning (optional): DVC, AWS S3 (boto3)  

---

## 📁 Project Structure

```
.
├── data/
│   └── data.csv
├── models/
│   └── model.pkl
├── src/
│   └── utils.py
├── train.py
├── predict.py
├── main.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── prom-rules.yaml
├── requirements.txt
```

---

## 🏗️ Training the Model

Run the training script:

```bash
python train.py
```

---

## 🚀 Running the API Locally

```bash
uvicorn main:app --reload
```

Open in browser:

- http://127.0.0.1:8000  
- http://127.0.0.1:8000/docs  

---

## 🔮 API Endpoints

### GET /

```
{
  "message": "Welcome to the ML Model API"
}
```

### POST /predict

Request:

```
[3.5, 1.2, 0.8]
```

Response:

```
{
  "prediction": 1,
  "latency": 0.0021
}
```

---

## 🧪 Prediction Script

```bash
python predict.py
```

---

## 🐳 Docker Setup

```bash
docker build -t mlapi .
docker run -p 8000:8000 mlapi
```

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 📊 Monitoring

Metric:

```
prediction_latency
```

---

## 📜 Logging

Logs stored in:

```
logs/app.log
```

---

## 💡 Future Improvements

- CI/CD pipeline (GitHub Actions / Jenkins)  
- Model versioning with MLflow  
- Grafana dashboards  
- Auto-retraining pipeline  
- Authentication & rate limiting  

---

## 👨‍💻 Author

Your Name  

GitHub: https://github.com/unaidabdullah-ui 
LinkedIn: https://www.linkedin.com/in/unaid-abdullah/  

---

## ⭐ Give it a Star

If you found this helpful, give it a star on GitHub!
