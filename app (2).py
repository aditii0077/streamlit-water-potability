
import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model (ensure model.pkl is available in Colab's runtime)
model = pickle.load(open('model.pkl', 'rb'))

st.title("Water Potability Prediction")

# Input fields
ph = st.number_input("Enter pH Level", min_value=0.0, max_value=14.0)
hardness = st.number_input("Enter Hardness")
solids = st.number_input("Enter Solids")
chloramines = st.number_input("Enter Chloramines")
sulfate = st.number_input("Enter Sulfate")
conductivity = st.number_input("Enter Conductivity")
organic_carbon = st.number_input("Enter Organic Carbon")
chlorine = st.number_input("Enter Chlorine")
turbidity = st.number_input("Enter Turbidity")

if st.button('Predict'):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, chlorine, turbidity]])
    prediction = model.predict(features)
    
    if prediction == 1:
        st.success("The water is potable!")
    else:
        st.error("The water is not potable.")
