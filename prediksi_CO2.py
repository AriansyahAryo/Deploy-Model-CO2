import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('prediksi_CO2.sav','rb'))

df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

st.title('Forecast Kualitas Udara')
year = st.slider("Tentukan Tahun",1,50,step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if st.button("Prediksi"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['CO2'].plot(style='--', color='gray', legend=True, label='known')
        pred['CO2'].plot(color='b', legend=True, label='Predictions')
        st.pyplot(fig)

