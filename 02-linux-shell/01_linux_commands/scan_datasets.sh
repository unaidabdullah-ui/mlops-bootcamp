#!/bin/bash

DATA_DIR="${1:-../data}"

echo "🔍 Scanning datasets..."

find "$DATA_DIR" -type f | while read -r file
do
  echo "Found: $file"
done
