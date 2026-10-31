#!/bin/bash

DATA_DIR="../data"

echo "🔍 Scanning datasets..."

find $DATA_DIR -type f | while read file
do
  echo "Found: $file"
done
