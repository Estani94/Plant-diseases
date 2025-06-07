import os
from pathlib import Path
from PIL import Image
import numpy as np

input_path = Path("../data/raw/PlantVillage")
output_path = Path("../data/processed")
output_path.mkdir(parents=True, exist_ok=True)

image_size = (224, 224)
images = []
labels = []
class_names = sorted([d.name for d in input_path.iterdir() if d.is_dir()])
class_to_idx = {cls: idx for idx, cls in enumerate(class_names)}

for cls in class_names:
    cls_folder = input_path / cls
    for img_path in cls_folder.rglob("*.*"):
        img = Image.open(img_path).convert("RGB")
        img = img.resize(image_size)
        img_array = np.array(img) / 255.0
        images.append(img_array)
        labels.append(class_to_idx[cls])

images = np.array(images, dtype=np.float32)
labels = np.array(labels, dtype=np.int64)

np.save(output_path / "images.npy", images)
np.save(output_path / "labels.npy", labels)
np.save(output_path / "class_names.npy", np.array(class_names))