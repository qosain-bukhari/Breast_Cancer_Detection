import streamlit as st
import joblib 
import numpy as np

model=joblib.load('svm_model.pkl')

st.title("Breast Cancer Detection web App")
st.markdown("This app predicts whether a tumor is **Malignant** or **Benign** using 5 key features.")

#inputfields
radius_mean = st.number_input("Radius Mean", min_value=0.0, format="%.2f")
texture_mean = st.number_input("Texture Mean", min_value=0.0, format="%.2f")
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, format="%.2f")
area_mean = st.number_input("Area Mean", min_value=0.0, format="%.2f")
concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, format="%.5f")

if st.button("Predict Diagnosis"):
      input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, concave_points_mean]])
      prediction = model.predict(input_data)[0]
      probability = model.predict_proba(input_data)[0][prediction]

      
      if prediction == 1:
        st.error(f"⚠️ **Malignant Tumor Detected**\n\nConfidence: {probability:.2%}")
      else:
        st.success(f"✅ **Benign Tumor Detected**\n\nConfidence: {probability:.2%}")
