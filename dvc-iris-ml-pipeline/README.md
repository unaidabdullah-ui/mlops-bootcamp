# DVC Iris ML Pipeline

A complete Machine Learning pipeline built with DVC for reproducibility, versioning, 
experiments, and automated workflow management.

## Features
- Data versioning with DVC
- Automated ML pipeline (prepare → train → evaluate)
- Experiment tracking with DVC
- Metrics tracking (accuracy)
- Reproducible and production-ready structure

## Pipeline Stages
1. Prepare data (train/test split)
2. Train RandomForest model
3. Evaluate model and generate metrics.json

## Run the pipeline

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Initialize DVC
dvc init

### Step 3: Track dataset
dvc add data/raw/iris.csv

### Step 4: Create pipeline
dvc repro

### Step 5: View metrics
dvc metrics show

## Folder Structure
```
dvc-iris-ml-pipeline/
│
├── data/
│   └── raw/
│       └── iris.csv
│
├── src/
│   ├── prepare.py
│   ├── train.py
│   └── evaluate.py
│
├── models/
│
├── metrics.json
├── params.yaml
├── requirements.txt
└── README.md
```

