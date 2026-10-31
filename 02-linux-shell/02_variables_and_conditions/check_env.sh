#!/bin/bash

if command -v python3 >/dev/null 2>&1
then
  echo "✅ Python Installed"
else
  echo "❌ Python Not Found"
  exit 1
fi

if command -v docker >/dev/null 2>&1
then
  echo "✅ Docker Installed"
else
  echo "❌ Docker Not Found"
fi
