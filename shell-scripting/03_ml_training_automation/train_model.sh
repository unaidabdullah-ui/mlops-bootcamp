#!/bin/bash

echo "Training Model..."
source /env/bin/activate

python train.py

if [$? -eq 0]
echo "Model Trained Successfully"
else
echo "Model Training Failed"
exit 1
fi