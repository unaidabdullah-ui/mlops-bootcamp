#!/bin/bash

echo "Training Model..."
[ -f venv/bin/activate ] && source venv/bin/activate

if python train.py
then
  echo "Model Trained Successfully"
else
  echo "Model Training Failed"
  exit 1
fi
