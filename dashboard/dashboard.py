import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

try:
    hours_dataset = pd.read_csv("dashboard/hour.csv")
    st.write("File 'hour.csv' berhasil dimuat.")
except FileNotFoundError:
    st.error("File 'hour.csv' tidak ditemukan. Pastikan file ada di direktori yang benar.")
try:
    days_dataset = pd.read_csv("dashboard/day.csv")
    st.write("File 'day.csv' berhasil dimuat.")
except FileNotFoundError:
    st.error("File 'day.csv' tidak ditemukan. Pastikan file ada di direktori yang benar.")    
days_dataset = pd.read_csv("day.csv")

season_cnt = days_dataset.groupby('season')['cnt'].sum().reset_index()
weather_cnt = hours_dataset.groupby('weathersit')['cnt'].sum().reset_index()

def start():
    st.title('Proyek Analisis Data dengan Bike Sharing Dataset')

    #Pertanyaan 1
    fig1, ax1= plt.subplots(figsize=(10, 6))
    st.subheader(" Pertanyaan 1 : Bagaimana tren penyewaan sepeda berdasarkan musim ?")
    sns.barplot(x='season', y='cnt', data=season_cnt, palette='viridis', ax=ax1)
    ax1.set_xlabel("Musim")
    ax1.set_ylabel("Jumlah Penyewaan")
    plt.xticks(ticks=range(4), labels=['spring', 'summer', 'fall', 'winter'])
    plt.ylim(0, 1100000)
    st.pyplot(fig1)

    st.write(
    """
    Dari hasil terlihat bahwa jumlah penyewaan sepeda cenderung meningkat dari musim semi, musim panas, dan musim gugur, yang kemudian turun sedikit pada musim dingin (musim 4). Oleh karena itu, tren penyewaan sepeda cenderung menunjukkan pola peningkatan seiring dengan berjalannya musim dari musim semi hingga musim gugur, dengan penurunan yang sedikit terlihat pada musim dingin.
    """
    )

    #Pertanyaan 2
    fig2, ax2= plt.subplots(figsize=(10, 6))
    st.subheader(" Pertanyaan 2 : Bagaimana pengaruh kondisi cuaca terhadap tingkat penyewaan sepeda ?")
    sns.barplot(x='weathersit', y='cnt', data=weather_cnt, palette='viridis', ax=ax2)
    ax2.set_xlabel("Kondisi Cuaca")
    ax2.set_ylabel("Jumlah Penyewaan")
    plt.xticks(ticks=range(len(weather_cnt['weathersit'])), labels=['Clear', 'Mist', 'Light Rain', 'Heavy Rain'], rotation=45)
    st.pyplot(fig2)


    st.write(
    """
    Dari hasil terlihat bahwa kondisi cuaca mempengaruhi tingkat penyewaan sepeda, dengan cuaca cerah atau sedikit berawan cenderung meningkatkan minat orang untuk menyewa sepeda, sedangkan cuaca buruk seperti hujan cenderung menguranginya.
    """
    )

if __name__ == "__main__":
    start()

