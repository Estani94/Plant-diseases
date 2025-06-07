import os
import numpy as np
from PIL import Image
from pathlib import Path
from tqdm import tqdm
import torchvision.transforms as transforms

data_dir = Path("data/raw/PlantVillage")
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

transform = transforms.Compose([
    transforms.Resize((224, 224))
])

images = []
labels = []
class_names = sorted([d.name for d in data_dir.iterdir() if d.is_dir()])
class_to_idx = {name: idx for idx, name in enumerate(class_names)}

for class_name in class_names:
    class_path = data_dir / class_name
    for img_path in tqdm(list(class_path.glob("*")), desc=class_name):
        try:
            img = Image.open(img_path).convert("RGB")
            img = transform(img)
            images.append(np.array(img))
            labels.append(class_to_idx[class_name])
        except:
            continue

images = np.array(images)
labels = np.array(labels)

np.save(output_dir / "images.npy", images)
np.save(output_dir / "labels.npy", labels)
np.save(output_dir / "class_names.npy", class_names)