import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load model with error handling
try:
    with open('prediksi_CO2.pkl', 'rb') as file:
        model = pickle.load(file)
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Load dataset with error handling
try:
    df = pd.read_excel("CO2 dataset.xlsx")
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df.set_index(['Year'], inplace=True)
    st.success("Dataset loaded successfully")
except Exception as e:
    st.error(f"Error loading dataset: {e}")

# Streamlit app
st.title('Forecast Kualitas Udara')

# User input
year = st.slider("Tentukan Tahun", 1, 50, step=1)

# Predict
try:
    pred = model.forecast(year)
    pred = pd.DataFrame(pred, columns=['CO2'])
except Exception as e:
    st.error(f"Error during prediction: {e}")

# Display prediction
if st.button("Prediksi"):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['CO2'].plot(style='--', color='gray', legend=True, label='known', ax=ax)
        pred['CO2'].plot(color='b', legend=True, label='Predictions', ax=ax)
        st.pyplot(fig)
