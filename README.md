## Cara Menjalankan Dashboard

### 1. Clone Repository
Clone repository ini ke local machine Anda:
```bash
git clone https://github.com/mthayyibUnp/submission.git
cd submission/dashboard
```

### 2. Instal Dependensi
Pastikan Anda memiliki Python dan pip terinstal di komputer Anda. Instal semua dependensi yang diperlukan dengan menjalankan perintah berikut:
```bash
pip install -r ../requirements.txt
```

### 3. Jalankan Streamlit
Setelah semua dependensi terinstal, Anda dapat menjalankan dashboard dengan menggunakan perintah:
```bash
streamlit run dashboard.py
```

Dashboard kemudian akan terbuka di browser default Anda, atau Anda dapat mengaksesnya melalui URL yang disediakan di terminal, biasanya pada `http://localhost:8501`.

### 4. Dataset yang Digunakan
- `dashboard_data.csv`: Dataset yang digunakan untuk dashboard dan diletakkan di folder `dashboard/`.
- Dataset tambahan seperti `day.csv` dan `hour.csv` berada di folder `data/` dan digunakan dalam notebook `Proyek_Analisis_Data.ipynb`.
