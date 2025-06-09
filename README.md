# Plant-diseases

Sistema para detectar enfermedades en hojas de plantas usando modelos de deep learning.

## 📄 Descripción

Clasifica imágenes de hojas (por ahora tomate y papa) para identificar enfermedades comunes, usando una CNN entrenada sobre el dataset PlantVillage. Ideal para prevenir brotes tempranos.

## 🛠 Instalación

```bash
git clone https://github.com/Estani94/Plant-diseases.git
cd Plant-diseases
pip install -r requirements.txt
```

## 🚀 Uso

Ejecutá la app con:
```bash
streamlit run app/main.py --server.runOnSave=false
```
Se abre una interfaz web donde se puede cargar una imagen y obtener la predicción del modelo con la probabilidad correspondiente.

## 🧠 Modelo

* CNN construida en PyTorch/TensorFlow.
* Entrenamiento con augmentación de imágenes.
* Clasifica enfermedades específicas de tomate y papa.

## ♻️ Expandir

Para otros cultivos: agregá imágenes del nuevo dataset, actualizá clases y entrená de nuevo.
