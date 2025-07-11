import os
import sys
from PIL import Image

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "./../.."))
sys.path.insert(0, project_root)
from AI.Real_Time_Analysis.predict import run_prediction

IMAGE_DIR = os.path.join(project_root, "gallery_images")

# Load sample images
image_paths = [
    os.path.join(IMAGE_DIR, "Samsung_galaxy_s21_ultra_1.jpg"),
    os.path.join(IMAGE_DIR, "Samsung_galaxy_s21_ultra_2.jpg")
]

images = [Image.open(path).convert("RGB") for path in image_paths]

# Sample title and description
title = "Stylish T-Shirt"
desc = "A comfortable and trendy cotton t-shirt suitable for all seasons."

# Run prediction
result = run_prediction(images, title, desc)

# Print the results
print("🔍 Prediction Output:")
for key, value in result.items():
    print(f"{key}: {value}")
