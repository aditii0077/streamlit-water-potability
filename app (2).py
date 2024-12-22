
import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('water_potability_model.pkl', 'rb'))

# Title and introduction with an emoji
st.title("💧 Water Potability Prediction Tool 🌍")
st.markdown('''
    Welcome to the **Water Potability Prediction Tool**! 🌊
    This tool can help you determine whether the water is potable or not based on various parameters.
    
    **Features:**
    * Enter key parameters related to water quality
    * Get a prediction on whether the water is potable or not
    * View the percentage of purity for better understanding
    
    🌟 Give it a try and see the result! 🌟
''')

# Input fields with descriptions and emojis
st.subheader("🔍 Enter Water Quality Parameters:")
ph = st.number_input("💧 Enter pH Level", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("💦 Enter Hardness")
solids = st.number_input("💧 Enter Solids")
chloramines = st.number_input("🧴 Enter Chloramines")
sulfate = st.number_input("🧪 Enter Sulfate")
conductivity = st.number_input("⚡ Enter Conductivity")
organic_carbon = st.number_input("🌱 Enter Organic Carbon")
trihalomethanes = st.number_input("🧫 Enter Trihalomethanes", min_value=0.0, step=0.1)
turbidity = st.number_input("🌫️ Enter Turbidity")

# Prediction logic and displaying results
if st.button("🔮 Predict"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    # Get the probability for the water being potable
    probability = model.predict_proba(features)[0][1]  # Probability for 'Potable' class (1)
    
    # Convert to percentage
    percentage = round(probability * 100, 2)
    
    if probability > 0.5:  # More than 50% probability indicates potable
        st.success(f"🌟 The water is potable with {percentage}% probability! 🌟")
    else:
        st.error(f"🚫 The water is not potable with {percentage}% probability. 🚫")

# Encourage feedback or next steps
st.markdown('''
    📝 If you found this tool helpful, feel free to share it with others!
    💡 You can also input different values to see how various water quality parameters affect potability.
    🔗 **Stay hydrated and safe!** 💦
''')

# Formal closing message with your name
st.markdown('''
    Created by Aditi Kalbhor.
    Connect with Aditi on [GitHub](https://github.com/aditii0077) or [LinkedIn](https://www.linkedin.com/in/aditi-kalbhor/) for more exciting projects and updates.
    **Thank you for using the Water Potability Prediction Tool.** 🙏
''')
