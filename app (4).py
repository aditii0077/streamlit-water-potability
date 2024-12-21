
import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Water Potability Prediction")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    input_df = pd.read_csv(uploaded_file)
    st.write("Uploaded Dataset:", input_df)

    # Make predictions
    predictions = model.predict(input_df)
    input_df['Potability_Prediction'] = predictions
    st.write("Prediction Results:", input_df)

    # Download predictions
    st.download_button(
        label="Download Predictions",
        data=input_df.to_csv(index=False).encode('utf-8'),
        file_name='predictions.csv',
        mime='text/csv'
    )
