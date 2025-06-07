import os

os.makedirs("data/raw", exist_ok=True)
os.system("kaggle datasets download -d emmarex/plantdisease -p data/raw --unzip")
