#!/bin/bash

IMAGE_NAME="mlops-unaid-bootcamp"

echo "BUILDING DOCKER IMAGE..."
dcoker build -t $IMAGE_NAME .

echo "Deploying Docker Container..."
docker run -d -p 8000:8000 $IMAGE_NAME