#!/bin/bash

# Install required tools
sudo apt-get update && sudo apt-get install -y git-lfs

# Create model directory
MODEL_DIR="${HOME}/huggingface_models/Qwen-Qwen2.5-7B-Instruct"
mkdir -p "${MODEL_DIR}"

# Download model with all components
cd "${MODEL_DIR}" || exit 1
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-7B-Instruct .

# Explicitly download smaller config/tokenizer files (in case LFS missed them)
git lfs pull --include="*.json,*.py,*.md,*.txt"
git lfs fetch --include="*.bin"