#!/bin/bash

echo "Installing Python dependencies"
pip install -r requirements.txt

echo "Running tests (if any)"
pytest tests/

echo "Build completed"
