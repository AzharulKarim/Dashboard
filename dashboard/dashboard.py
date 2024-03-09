import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#dashboard/
hours_dataset = pd.read_csv("dashboard/hour.csv")
days_dataset = pd.read_csv("dashboard/day.csv")
data_dashboard = pd.read_csv("dashboard/all_data.csv")

season_cnt = days_dataset.groupby('season')['cnt'].sum().reset_index()
weather_cnt = hours_dataset.groupby('weathersit')['cnt'].sum().reset_index()

def create_daily_orders_df(df):
    # Resample data harian dan hitung jumlah pesanan serta total pendapatan harian
    daily_orders_df = df.resample(rule='D', on='dteday').agg({
        "cnt": "sum",
        "casual": "sum",
        "registered": "sum"
    })
    daily_orders_df.reset_index(inplace=True)
    daily_orders_df.rename(columns={"cnt": "order_count"}, inplace=True)
    return daily_orders_df



st.title('Proyek Analisis Data dengan Bike Sharing Dataset')

datetime_columns = ["dteday"]
data_dashboard.sort_values(by="dteday", inplace=True)
data_dashboard.reset_index(inplace=True)
 
for column in datetime_columns:
    data_dashboard[column] = pd.to_datetime(data_dashboard[column])

min_date = data_dashboard["dteday"].min()
max_date = data_dashboard["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = data_dashboard[(data_dashboard["dteday"] >= str(start_date)) & 
                (data_dashboard["dteday"] <= str(end_date))]

daily_orders_df = create_daily_orders_df(main_df)

st.subheader('Daily Orders')
 
col1 = st.columns(2)
 
total_orders = daily_orders_df.order_count.sum()
st.metric("Total orders", value=total_orders)
 

 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_orders_df["dteday"], 
    daily_orders_df["order_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xlabel("Date", fontsize=15)
ax.set_ylabel("Order Count", fontsize=15)
ax.set_title("Daily Orders", fontsize=20)
ax.grid(True)
 
st.pyplot(fig)

st.subheader('')
st.subheader('Hasil 1')
#Pertanyaan 1
fig1, ax1= plt.subplots(figsize=(10, 6))
st.subheader("Bagaimana tren penyewaan sepeda berdasarkan musim ?")
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


st.subheader('')
st.subheader('Hasil 2')

#Pertanyaan 2
fig2, ax2= plt.subplots(figsize=(10, 6))
st.subheader("Bagaimana pengaruh kondisi cuaca terhadap tingkat penyewaan sepeda ?")
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

