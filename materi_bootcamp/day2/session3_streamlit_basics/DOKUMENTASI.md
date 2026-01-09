# 📊 Student Performance Analytics Dashboard
## Dokumentasi Lengkap Aplikasi Streamlit

---

## 📋 Daftar Isi
1. [Pengenalan Aplikasi](#pengenalan-aplikasi)
2. [Struktur File](#struktur-file)
3. [Cara Menjalankan](#cara-menjalankan)
4. [Fitur-Fitur Utama](#fitur-fitur-utama)
5. [Penjelasan Setiap Section](#penjelasan-setiap-section)
6. [Panduan Visualisasi Data](#panduan-visualisasi-data)
7. [Tips & Troubleshooting](#tips--troubleshooting)

---

## 🎯 Pengenalan Aplikasi

### Apa itu Aplikasi Ini?
Aplikasi **Student Performance Analytics Dashboard** adalah dashboard interaktif yang dibangun menggunakan **Streamlit** untuk menganalisis data performa akademik siswa dari dataset `StudentPerformanceFactors.csv`.

### Tujuan Aplikasi:
- ✅ Memberikan pengalaman belajar Streamlit yang hands-on
- ✅ Menampilkan berbagai widget dan layout options
- ✅ Mendemonstrasikan visualisasi data yang interaktif
- ✅ Membantu user memahami analisis data dengan penjelasan lengkap

### Target User:
- Peserta bootcamp data science
- Pemula yang ingin belajar Streamlit
- Analyst yang ingin membuat dashboard cepat

---

## 📁 Struktur File

```
session3_streamlit_basics/
├── app_part1.py                    # File utama aplikasi
├── DOKUMENTASI.md                  # File ini
├── PENJELASAN_APLIKASI.py          # Script presentasi interaktif
└── requirements.txt                # Dependencies (optional)
```

---

## 🚀 Cara Menjalankan

### Prerequisite:
```bash
# Pastikan Python 3.8+ sudah terinstall
python --version

# Install dependencies (jika belum)
pip install streamlit plotly pandas numpy
```

### Menjalankan Aplikasi:

#### Opsi 1: Dari Terminal PowerShell
```powershell
cd "c:\itbootcamp\data-science\materi_bootcamp\day2\session3_streamlit_basics"
streamlit run app_part1.py
```

#### Opsi 2: Dari Command Prompt
```cmd
cd c:\itbootcamp\data-science\materi_bootcamp\day2\session3_streamlit_basics
streamlit run app_part1.py
```

#### Opsi 3: Dengan Konfigurasi Port Custom
```bash
streamlit run app_part1.py --server.port 8503
```

### Akses Aplikasi:
- **Local:** http://localhost:8502
- **Network:** http://192.168.50.89:8502 (atau IP Anda)

### Menghentikan Aplikasi:
- Tekan `Ctrl + C` di terminal
- Atau tutup terminal

---

## 🎨 Fitur-Fitur Utama

### 1. **Smart Sidebar Navigation**
```
🎛️ SIDEBAR FILTERS
├── Filter Tab
│   ├── Multi-select Features
│   ├── Range Slider
│   └── Data Filter Options
├── Visualization Tab
│   ├── Chart Type Selector
│   └── Color Customization
└── About Tab
    └── Dataset Information
```

### 2. **Interactive Metrics Display**
- Menampilkan 4 metrik utama secara real-time
- Metric 1: Rata-rata fitur pertama
- Metric 2: Maksimum fitur kedua
- Metric 3: Minimum fitur ketiga
- Metric 4: Total records

### 3. **Multiple Visualizations**
| Tipe Visualisasi | Kegunaan | Lokasi |
|---|---|---|
| Histogram | Distribusi data | Top-left |
| Scatter Plot | Relasi 2 variabel | Top-right |
| Bar Chart | Perbandingan mean | Bottom-left |
| Heatmap | Korelasi matrix | Bottom-right |

### 4. **Statistical Insights**
- Statistik deskriptif otomatis
- Data type summary
- Detail statistik dalam expander
- Range/quartile information

### 5. **Interactive Features**
- 🔄 Reset Filters Button
- 📊 Show Summary (dengan animasi balloons)
- 📥 Download CSV Button
- 📚 Data completeness indicator

---

## 📖 Penjelasan Setiap Section

### **SECTION 1: Header & Introduction**
```python
st.title("🎓 Student Performance Analytics Dashboard")
st.markdown("Analisis komprehensif performa akademik siswa...")
st.info("💡 **Tips:** Gunakan sidebar...")
```

**Fungsi:**
- Memberikan judul dan deskripsi aplikasi
- Menampilkan tips penggunaan

**Interaksi User:** Informasi saja (non-interactive)

---

### **SECTION 2: Sidebar Navigation**

#### Tab 1: Filter
```python
# Multi-select untuk pilih fitur
selected_features = st.multiselect(
    'Pilih fitur numerik untuk analisis:',
    numeric_features,
    default=numeric_features[:3]
)

# Slider untuk range filter
min_val, max_val = st.slider(
    f'Range {feature_to_filter}:',
    ...
)
```

**Widget Digunakan:**
- `st.multiselect()` - Pilih multiple items
- `st.selectbox()` - Pilih single item
- `st.slider()` - Pilih range values
- `st.checkbox()` - Toggle on/off

#### Tab 2: Visualization
```python
# Radio untuk pilih tipe chart
chart_type = st.radio(
    "Tipe Chart Utama:",
    ["Distribution (Histogram)", "Scatter Plot", ...]
)

# Selectbox untuk color
color_by = st.selectbox(
    'Warna berdasarkan:',
    ...
)
```

#### Tab 3: About
Menampilkan informasi dataset:
- Total Records
- Total Features
- Numeric Features

---

### **SECTION 3: Key Metrics**

Menampilkan 4 metric boxes dengan layout columns:

```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="...", value=..., delta=...)
with col2:
    st.metric(label="...", value=...)
# dst
```

**Interpretasi Metric:**
- Nilai = hasil kalkulasi statistik
- Delta = perubahan dibanding data keseluruhan

---

### **SECTION 4: Panduan Visualisasi**

Expandable section yang berisi:
- Penjelasan Histogram
- Penjelasan Scatter Plot
- Penjelasan Box Plot
- Penjelasan Heatmap Correlation
- Tips analisis data
- Best practices

**Mengapa penting?** Membantu user memahami apa yang mereka lihat

---

### **SECTION 5: Visualisasi Data**

#### Row 1: Distribution & Scatter
```
┌─────────────────────┬──────────────────────┐
│  Distribution       │  Scatter Plot        │
│  (Histogram)        │  (2 variabel)        │
│  + Explanation      │  + Correlation Info  │
└─────────────────────┴──────────────────────┘
```

#### Row 2: Comparison & Correlation
```
┌─────────────────────┬──────────────────────┐
│  Bar Chart          │  Heatmap             │
│  (Mean ± Std)       │  (Correlation)       │
│  + Explanation      │  + Explanation       │
└─────────────────────┴──────────────────────┘
```

**Setiap Chart Include:**
- Visualization
- Expandable explanation
- Interpretasi hasil
- Statistik terkait

---

### **SECTION 6: Containers & Analytics**

#### Container 1: Statistics
Dua kolom:
- Statistik deskriptif (mean, median, std dev)
- Data type summary

#### Container 2: Insights (Expander)
Detail insights termasuk:
- Min, Max, Range
- Ukuran pemusatan
- Variabilitas

---

### **SECTION 7: Data Table**

```python
# Column selector
display_cols = st.multiselect(
    'Pilih kolom untuk ditampilkan:',
    available_cols,
    default=available_cols[:5]
)

# Display dataframe
st.dataframe(filtered_df[display_cols], ...)
```

**Fitur:**
- Dinamis column selection
- Pagination otomatis
- Scrollable
- Sortable columns
- Data info dalam expander

---

### **SECTION 8: Interactive Actions**

Tiga button dalam layout columns:

1. **Reset Filters Button**
   ```python
   if st.button("🔄 Reset All Filters", type="primary"):
       st.rerun()
   ```
   Fungsi: Refresh halaman & reset semua filter

2. **Show Summary Button**
   ```python
   if st.button("📊 Show Data Summary"):
       st.balloons()  # Animasi
       st.success(...)  # Tampilkan summary
   ```
   Fungsi: Tampilkan ringkasan dengan animasi

3. **Download CSV Button**
   ```python
   st.download_button(
       label="📥 Download CSV",
       data=csv,
       file_name="...",
       mime="text/csv"
   )
   ```
   Fungsi: Download filtered data sebagai CSV

---

### **SECTION 9: Data Quality Indicators**

```
┌──────────────────────┬──────────────────────┐
│ Data Completeness    │ Data Status          │
│ Progress Bar         │ Status Messages      │
│ (0-100%)             │ (Error/Warning/Info) │
└──────────────────────┴──────────────────────┘
```

Menampilkan:
- Persentase kelengkapan data
- Status indicators dengan warna
- Conditional messages

---

### **SECTION 10: Footer**

Menampilkan:
- Judul aplikasi
- Info bootcamp
- Dataset info
- Sidebar summary of learned features
- Next session preview

---

## 📊 Panduan Visualisasi Data

### 1. Histogram (Distribution Chart)

**Apa itu?**
- Menampilkan distribusi frekuensi dari satu variabel numerik
- Sumbu X: Rentang nilai | Sumbu Y: Jumlah frekuensi

**Cara Membaca:**
```
Tinggi bar = banyak data di rentang itu
Rendah bar = sedikit data di rentang itu
Bentuk kurva = pattern distribusi
```

**Interpretasi Pola:**
- 🔔 Bell curve (normal) = distribusi normal
- ➡️ Skewed right = sebagian besar nilai rendah
- ⬅️ Skewed left = sebagian besar nilai tinggi
- 👥 Bimodal = dua puncak (dua kelompok)

**Digunakan untuk:**
- Melihat bentuk distribusi
- Deteksi outlier
- Memahami penyebaran data
- Transformasi data planning

---

### 2. Scatter Plot (Relasi Antar Variabel)

**Apa itu?**
- Menampilkan hubungan antara DUA variabel numerik
- X-axis: Variabel 1 | Y-axis: Variabel 2
- Setiap titik = satu data point

**Cara Membaca:**
```
Titik rapat naik ke kanan = korelasi positif kuat
Titik rapat turun ke kanan = korelasi negatif kuat
Titik tersebar = korelasi lemah
```

**Trendline (Garis Merah):**
- Menunjukkan arah umum hubungan
- Dihitung dengan metode Ordinary Least Squares (OLS)

**Korelasi Interpretasi:**
```
+1.0  ──────► Perfect Positive (ideal naik)
+0.7  ──────► Strong Positive
+0.5  ──────► Moderate Positive
 0.0  ──────► No Correlation
-0.5  ──────► Moderate Negative
-0.7  ──────► Strong Negative
-1.0  ──────► Perfect Negative (ideal turun)
```

**Digunakan untuk:**
- Mengeksplorasi hubungan antar variabel
- Feature engineering
- Deteksi non-linear relationships
- Multicollinearity check

---

### 3. Box Plot (Distribution & Outliers)

**Komponen Box Plot:**
```
      Atas Whisker ─────┐
                         │
         Q3 (75%)  ┌─────┤
         Median    │     │
         Q1 (25%)  └─────┤
                         │
      Bawah Whisker──────┘
      
      Titik terpisah = Outlier
```

**Interpretasi:**
- **Box** = 50% data tengah (interquartile range)
- **Garis di tengah** = Median (nilai tengah)
- **Whisker** = Batas data normal (1.5 × IQR)
- **Titik** = Outlier (nilai ekstrem)

**Digunakan untuk:**
- Membandingkan distribusi antar grup
- Deteksi outlier otomatis
- Melihat simetri data
- Analisis data quality

---

### 4. Bar Chart (Mean ± Std Dev)

**Apa itu?**
- Bar = Nilai rata-rata (mean) variabel
- Error bar = Standar deviasi (variabilitas)

**Interpretasi:**
```
Bar tinggi + error bar pendek   = Nilai tinggi, konsisten
Bar tinggi + error bar panjang  = Nilai tinggi, bervariasi
Bar pendek + error bar pendek   = Nilai rendah, konsisten
Bar pendek + error bar panjang  = Nilai rendah, bervariasi
```

**Digunakan untuk:**
- Perbandingan mean antar variabel
- Melihat variabilitas relatif
- Visualisasi uncertainty
- Quick overview multi-variabel

---

### 5. Heatmap Correlation

**Apa itu?**
- Menampilkan korelasi SEMUA pasangan variabel numerik
- Warna = kekuatan korelasi
- Angka = nilai korelasi eksak

**Skala Warna:**
```
🟢 Hijau/Biru (1)    = Korelasi positif kuat
🟡 Kuning (0)        = Tidak ada korelasi
🔴 Ungu/Merah (-1)   = Korelasi negatif kuat
```

**Membaca Heatmap:**
- Fokus pada warna gelap (korelasi kuat)
- Diagonal selalu 1 (variabel dengan dirinya sendiri)
- Matriks simetris (X vs Y = Y vs X)

**⚠️ Penting: Korelasi ≠ Kausalitas**
- Korelasi hanya menunjukkan hubungan
- Tidak menunjukkan sebab-akibat
- Perlu domain expertise untuk interpretasi

**Digunakan untuk:**
- Analisis multi-variabel
- Deteksi multicollinearity
- Feature selection
- Correlation-based clustering

---

## 💡 Tips & Best Practices

### Tips Analisis Data:
1. ✅ **Mulai dari Histogram** - Pahami distribusi dulu
2. ✅ **Gunakan Scatter untuk Eksplorasi** - Cari hubungan
3. ✅ **Box Plot untuk Outlier** - Deteksi anomali
4. ✅ **Heatmap untuk Overview** - Lihat gambar besar
5. ✅ **Perhatikan Ukuran Sampel** - Besar sampel = lebih reliable
6. ✅ **Cross-check dengan Statistik** - Jangan hanya visual

### Hal yang Perlu Diperhatikan:
- ⚠️ Outlier bisa ada karena error atau data unik - periksa konteks
- ⚠️ Korelasi ≠ Kausalitas - jangan buat kesimpulan causal
- ⚠️ Skala berbeda bisa misleading - normalisasi jika perlu
- ⚠️ Missing values mempengaruhi hasil - handle dengan baik
- ⚠️ Ukuran sampel kecil = interpretasi hati-hati
- ⚠️ Bias dalam data collection bisa misleading

### Best Practices Visualization:
1. Judul yang deskriptif
2. Label axis yang jelas
3. Skala yang appropriate
4. Color scheme yang konsisten
5. Menghindari chart junk
6. Storytelling yang baik

---

## 🔧 Troubleshooting

### Problem: "Dataset not found"
```
Solusi:
- Pastikan StudentPerformanceFactors.csv ada di: 
  c:\itbootcamp\data-science\datasets\
- Periksa path di fungsi load_data()
```

### Problem: Aplikasi lambat
```
Solusi:
- Gunakan @st.cache_data untuk mempercepat
- Reduce jumlah rows yang ditampilkan
- Gunakan session state untuk penyimpanan state
```

### Problem: Chart tidak muncul
```
Solusi:
- Pastikan plotly installed: pip install plotly
- Pilih minimal 2 features untuk scatter plot
- Check browser console untuk error messages
```

### Problem: Dropdown kosong
```
Solusi:
- Periksa data types di dataset
- Gunakan .dropna() untuk remove missing values
- Debug dengan st.write(df.columns)
```

### Problem: Download button error
```
Solusi:
- Pastikan data tidak kosong
- Check encoding (gunakan utf-8)
- Periksa ukuran file (jika terlalu besar)
```

---

## 📚 Referensi & Resources

### Dokumentasi Resmi:
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Streamlit Features yang Digunakan:
- `st.set_page_config()` - Konfigurasi halaman
- `st.title()`, `st.header()`, `st.subheader()` - Text elements
- `st.sidebar` - Sidebar navigation
- `st.tabs()` - Tab navigation
- `st.columns()` - Layout columns
- `st.expander()` - Collapsible sections
- `st.metric()` - Metric display
- `st.dataframe()` - Data table
- `st.plotly_chart()` - Plotly integration
- `st.slider()`, `st.selectbox()`, `st.multiselect()` - Input widgets
- `st.button()`, `st.download_button()` - Action buttons
- `st.progress()` - Progress bar
- `st.success()`, `st.info()`, `st.warning()`, `st.error()` - Messages
- `st.balloons()` - Animation

### Dataset Features:
Dataset `StudentPerformanceFactors.csv` mencakup:
- Student ID
- Waktu belajar
- Kehadiran
- Nilai ujian
- Engagement level
- Dan features lainnya

---

## 🎓 Learning Outcomes

Setelah menggunakan aplikasi ini, Anda akan mengerti:

✅ Cara membangun dashboard interaktif dengan Streamlit
✅ Widget-widget Streamlit dan cara menggunakannya
✅ Layout design dengan columns, containers, expanders
✅ Cara membuat visualisasi dengan Plotly
✅ Interpretasi berbagai jenis chart
✅ Data filtering dan manipulation di Streamlit
✅ File download functionality
✅ UI/UX best practices

---

## 📞 Support & Questions

Jika ada pertanyaan atau issues:
1. Check dokumentasi ini terlebih dahulu
2. Lihat error messages di console
3. Check browser console (F12)
4. Consult dengan instructor
5. Cek Streamlit documentation

---

**Dibuat untuk:** Bootcamp Data Science - Session 3
**Tanggal:** December 2025
**Status:** Complete ✅
