import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

def create_season(df):
    season_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_df

def create_holiday(df):
    holiday_df = df.groupby(by='holiday').sum().reset_index()
    return holiday_df
    
def create_workingday(df):
    on_workingday = df[(df["workingday"]) == 1]
    workingday_df = on_workingday.groupby(by='hour').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_df

def create_rfm(df):
    rfm_df = df.groupby(by="hour", as_index=False).agg({
        "dateday": "max", # mengambil tanggal penyewaan sepeda terakhir
        "instant": "nunique", # menghitung jumlah penyewaan sepeda
        "count": "sum" # menghitung jumlah revenue yang dihasilkan
    })

    rfm_df.columns = ["hour", "last_order_date", "frequency", "monetary"]

    # menghitung kapan terakhir pelanggan melakukan transaksi (hari)
    rfm_df["last_order_date"] = rfm_df["last_order_date"].dt.date
    recent_date = df["dateday"].dt.date.max()
    rfm_df["recency"] = rfm_df["last_order_date"].apply(lambda x: (recent_date - x).days)

    rfm_df.drop("last_order_date", axis=1, inplace=True)
    
    return rfm_df

# masukkan dataset
all_df = pd.read_csv("https://raw.githubusercontent.com/audyfebryantii/submission-dicoding/main/dashboard/main_data.csv")

datetime_columns = ["dateday"]
all_df.sort_values(by="dateday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
   
min_date = all_df["dateday"].min()
max_date = all_df["dateday"].max()

# sidebar
with st.sidebar:
    # menambahkan logo
    st.image("https://raw.githubusercontent.com/audyfebryantii/submission-dicoding/961059c30f9cbe0f2bfc9f528e30c5200fd4f4aa/dashboard/8960285.jpg")
    # mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Time Period',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = all_df[(all_df['dateday'] >= str(start_date)) & (all_df['dateday'] <= str(end_date))]

season_df = create_season(main_df)
holiday_df = create_holiday(main_df)
workingday_df = create_workingday(main_df)
rfm_df = create_rfm(main_df)

# Tampilan Utama
st.header('Bike Rentals Analytics Dashboard 🚴🏼')

# Subheader penyewaan sepeda berdasarkan musim
st.subheader('Bike Rentals based on Season')
fig, ax = plt.subplots(figsize=(20, 10))
 
sns.barplot(
    y="registered",
    x="season",
    data=season_df,
    color='tab:blue',
    label='Registered'
)

sns.barplot(
    y="casual",
    x="season",
    data=season_df,
    color='tab:orange',
    label='Casual'
)

ax.set_title("Number of Bike Rentals by Season", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Subheader penyewaan sepeda berdasarkan holidays(hari libur/tidak)
st.subheader('Bike Rental based on Holidays')
fig, ax = plt.subplots(figsize=(20,10))

colors_ = ["#72BCD4", "#D3D3D3"]

sns.barplot(
    y="holiday",
    x="count",
    data=holiday_df,
    palette=colors_,
    order=holiday_df.sort_values(by=["count"], ascending=False)["holiday"],
    ax=ax
)

ax.set_title("Number of Bike Rentals Based on Holidays", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

# Subheader penyewaan sepeda pada hari kerja
st.subheader('Bike Rental Time Distribution on Workingday')
fig, ax = plt.subplots(figsize=(10, 5))

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    data=workingday_df, 
    x='hour', 
    y='count',
    palette=colors
)

ax.set_title("Bike Rental Time Distribution on Workingday")
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.legend()
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Subheader penyewaan sepeda terbaik berdasarkan  RFM
st.subheader("Best Rental Hours Based on RFM Parameters")
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))
 
colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]
 
sns.barplot(y="recency", x="hour", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis ='x', labelsize=15)
 
sns.barplot(y="frequency", x="hour", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)
 
sns.barplot(y="monetary", x="hour", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)
 
plt.suptitle("Best Rental Hours Based on RFM Parameters", fontsize=20)

st.pyplot(fig)

st.caption('Copyright (c) 2024')