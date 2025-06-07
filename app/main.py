import os
os.environ["STREAMLIT_DEV_MODE"] = "false"
os.environ["STREAMLIT_WATCH_SUPPORT"] = "false"

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import streamlit as st
from PIL import Image
from inference import predict

st.title("Plant Disease Detector")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.write("Predicting...")
    label = predict(uploaded_file)
    st.write(f"Prediction: **{label}**")
