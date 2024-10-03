import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the prepared dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mthayyibUnp/submission/69e3088043bf5ee1f22d6e3a6a46c80f198f4c0c/Dashboard/dashboard_data.csv"
    data = pd.read_csv(url)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# Load the dataset
dashboard_df = load_data()

# Sidebar for filters
st.sidebar.title('Dashboard Data Bike Sharing')
st.sidebar.markdown('## Filter Data')

# Title
st.title('Dashboard Analisis Bike Sharing')
st.markdown('Dashboard untuk mengeksplorasi dataset bike sharing.')

# Display basic dataset info
if st.sidebar.checkbox('Tampilkan data mentah'):
    st.subheader('Data Mentah')
    st.write(dashboard_df.head())

# Display data description
if st.sidebar.checkbox('Tampilkan deskripsi data'):
    st.subheader('Deskripsi Data')
    st.write(dashboard_df.describe())

# Visualizations
st.sidebar.markdown('## Visualisasi')

# Plot Correlation Matrix
if st.sidebar.checkbox('Tampilkan Matriks Korelasi'):
    st.subheader('Matriks Korelasi')
    # Select only numeric columns for the correlation matrix
    numeric_columns = dashboard_df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = dashboard_df[numeric_columns].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot(fig)

# Scatter plot between Temperature and Total Users
if st.sidebar.checkbox('Tampilkan Scatter Plot Suhu vs Jumlah Pengguna'):
    st.subheader('Suhu vs Jumlah Pengguna')
    fig, ax = plt.subplots()
    sns.scatterplot(x='Temperature', y='Total Users', data=dashboard_df, ax=ax)
    plt.title('Suhu vs Jumlah Pengguna Sepeda')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)

# Histogram for Total Users distribution
if st.sidebar.checkbox('Tampilkan Distribusi Penggunaan Sepeda'):
    st.subheader('Distribusi Penggunaan Sepeda')
    fig, ax = plt.subplots()
    sns.histplot(dashboard_df['Total Users'], kde=True, ax=ax)
    plt.title('Distribusi Penggunaan Sepeda')
    plt.xlabel('Jumlah Pengguna Sepeda')
    plt.ylabel('Frekuensi')
    st.pyplot(fig)

# Line plot for daily bike usage trend
if st.sidebar.checkbox('Tampilkan Tren Harian Penggunaan Sepeda'):
    st.subheader('Tren Harian Penggunaan Sepeda')
    fig, ax = plt.subplots()
    plt.plot(dashboard_df['Date'], dashboard_df['Total Users'])
    plt.title('Tren Harian Penggunaan Sepeda')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Bar plot for average bike usage by season
if st.sidebar.checkbox('Tampilkan Penggunaan Sepeda Berdasarkan Musim'):
    st.subheader('Rata-rata Penggunaan Sepeda Berdasarkan Musim')
    season_impact = dashboard_df.groupby('Season')['Total Users'].mean()
    fig, ax = plt.subplots()
    season_impact.plot(kind='bar', ax=ax)
    plt.title('Rata-rata Penggunaan Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
    st.pyplot(fig)

# Bar plot for usage on working days vs weekends/holidays
if st.sidebar.checkbox('Tampilkan Penggunaan Sepeda: Hari Kerja vs Akhir Pekan'):
    st.subheader('Penggunaan Sepeda: Hari Kerja vs Akhir Pekan')
    workingday_impact = dashboard_df.groupby('Working Day')['Total Users'].mean()
    fig, ax = plt.subplots()
    workingday_impact.plot(kind='bar', ax=ax)
    ax.set_xticklabels(['Akhir Pekan/Libur', 'Hari Kerja'], rotation=0)
    plt.title('Rata-rata Penggunaan Sepeda: Hari Kerja vs Akhir Pekan')
    plt.xlabel('Tipe Hari')
    plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
    st.pyplot(fig)

st.sidebar.markdown('### Akhir dari Dashboard')
