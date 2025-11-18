#!/bin/bash
# Build script to preload rembg models

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Preloading rembg models..."
python preload_models.py || echo "Model preload failed, will download on first request"

echo "Build complete"

