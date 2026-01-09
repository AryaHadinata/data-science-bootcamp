# 🎓 Student Performance Analytics Dashboard
## Quick Reference Guide

---

## 📂 File-File yang Ada

| File | Deskripsi |
|------|-----------|
| `app_part1.py` | Aplikasi utama Streamlit (454 lines) |
| `DOKUMENTASI.md` | Dokumentasi lengkap dalam format Markdown |
| `PENJELASAN_APLIKASI.py` | Script presentasi interaktif (bisa di-run dengan Streamlit) |
| `README.md` | File ini - Quick reference |

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install streamlit plotly pandas numpy
```

### 2. Navigate ke Folder
```bash
cd "c:\itbootcamp\data-science\materi_bootcamp\day2\session3_streamlit_basics"
```

### 3. Run Aplikasi Utama
```bash
streamlit run app_part1.py
```

### 4. Run Penjelasan Interaktif (Optional)
```bash
streamlit run PENJELASAN_APLIKASI.py
```

### 5. Buka di Browser
- **Aplikasi:** http://localhost:8502
- **Penjelasan:** http://localhost:8503 (jika port berbeda)

---

## 📊 Aplikasi Utama (app_part1.py)

### Fitur Utama:
✅ Sidebar navigation dengan 3 tabs (Filter, Visualisasi, About)
✅ Interactive widgets (multiselect, slider, checkbox, radio)
✅ 4 Key Metrics real-time
✅ 4 Visualisasi interaktif (Histogram, Scatter, Bar, Heatmap)
✅ Panduan visualisasi yang expandable
✅ Statistik deskriptif dan insights
✅ Data table dengan column selection
✅ Download CSV functionality
✅ Status indicators dan progress bar
✅ Custom CSS styling

### Data Source:
**File:** `StudentPerformanceFactors.csv`
**Lokasi:** `c:\itbootcamp\data-science\datasets\`
**Records:** ~2000
**Features:** 15+ columns (numeric & categorical)

### Workflow:
```
1. Pilih features dari sidebar (multiselect)
2. Set range filter (slider)
3. Toggle options (checkbox)
4. Lihat data ter-filter di 4 visualisasi
5. Expand penjelasan untuk interpretasi
6. Analisis statistik dan insights
7. Download data jika diperlukan
```

---

## 📚 Penjelasan Interaktif (PENJELASAN_APLIKASI.py)

### Menu Navigasi:
1. **🏠 Beranda** - Overview aplikasi & fitur utama
2. **📖 Panduan Lengkap** - Cara menggunakan aplikasi
3. **🎨 Struktur Aplikasi** - Layout, flow, components
4. **🔧 Fitur-Fitur Widget** - Widget yang digunakan & cara kerjanya
5. **📊 Panduan Visualisasi** - Interpretasi setiap jenis chart
6. **💡 Tips & Troubleshooting** - Best practices & troubleshooting
7. **🚀 Cara Menjalankan** - Setup & running instructions

### Fokus Utama:
- Pemahaman setiap widget Streamlit
- Interpretasi visualisasi data
- Best practices analisis data
- Troubleshooting issues

---

## 📖 Dokumentasi (DOKUMENTASI.md)

### Isi Lengkap:
1. Pengenalan aplikasi & tujuan
2. Struktur file dan direktori
3. Cara menjalankan aplikasi
4. Fitur-fitur utama dan deskripsi
5. Penjelasan detail setiap section
6. Panduan membaca visualisasi (5 tipe chart)
7. Tips, best practices, dan warnings
8. Troubleshooting & solutions
9. Referensi dan resources
10. Learning outcomes

### Format:
- Markdown dengan table of contents
- Detailed explanations
- Code examples
- Troubleshooting guide

---

## 🎨 Visualisasi Data yang Tersedia

| Chart | Tujuan | Lokasi |
|-------|--------|--------|
| **Histogram** | Distribusi frekuensi | Top-left |
| **Scatter Plot** | Relasi 2 variabel | Top-right |
| **Bar Chart** | Perbandingan mean | Bottom-left |
| **Heatmap** | Korelasi matrix | Bottom-right |

### Setiap Chart Include:
- Visualisasi interaktif (Plotly)
- Expandable explanation
- Interpretasi hasil
- Statistik terkait

---

## 🔧 Widget yang Digunakan

### Input Widgets:
- `st.multiselect()` - Pilih multiple features
- `st.selectbox()` - Pilih single feature
- `st.slider()` - Set range value
- `st.checkbox()` - Toggle options
- `st.radio()` - Pilih single choice

### Display Widgets:
- `st.metric()` - Key metrics
- `st.dataframe()` - Data table
- `st.plotly_chart()` - Interactive charts
- `st.progress()` - Progress bar
- `st.balloons()` - Animation

### Action Widgets:
- `st.button()` - Reset filters
- `st.download_button()` - Download CSV

### Message Widgets:
- `st.success()`, `st.info()`, `st.warning()`, `st.error()`

### Layout Widgets:
- `st.columns()` - Side-by-side layouts
- `st.container()` - Group elements
- `st.expander()` - Collapsible sections
- `st.tabs()` - Tab navigation

---

## 💡 Key Features Explained

### Sidebar Navigation
```
🎛️ SIDEBAR (3 TABS)
├─ FILTER TAB
│  ├─ Multi-select features (minimal 2)
│  ├─ Range slider (dynamic range)
│  └─ Checkbox options (stats, outliers, correlation)
├─ VISUALIZATION TAB
│  ├─ Chart type selector (4 options)
│  └─ Color customization
└─ ABOUT TAB
   └─ Dataset information
```

### Metrics Section
- 4 Key Metrics dalam layout columns
- Real-time calculation
- Delta menunjukkan perubahan dari data asli

### Visualizations
- Histogram: Distribusi satu variabel
- Scatter: Relasi 2 variabel dengan trendline
- Bar: Perbandingan mean ± std dev
- Heatmap: Korelasi semua variabel

### Interactive Actions
- 🔄 Reset Filters → st.rerun()
- 📊 Show Summary → st.balloons()
- 📥 Download CSV → Export filtered data

---

## 📊 Data Flow Diagram

```
START
  ↓
Load CSV (@st.cache_data)
  ↓
Display Header & Info
  ↓
Sidebar Widgets Input
  ↓
Apply Filters to Data
  ↓
Calculate Metrics
  ↓
Generate Visualizations
  ↓
Display Statistics
  ↓
Show Data Table
  ↓
Action Buttons (Reset/Download)
  ↓
Status Indicators
  ↓
Footer
  ↓
END (User interacts → Re-run from Sidebar)
```

---

## 🎯 Cara Menggunakan Aplikasi

### Scenario 1: Analisis Distribusi
```
1. Open app_part1.py
2. Sidebar → Select 1 feature
3. Lihat histogram untuk bentuk distribusi
4. Check mean, median, std dev
5. Baca interpretasi di expander
```

### Scenario 2: Analisis Relasi
```
1. Sidebar → Select 2+ features
2. Lihat scatter plot
3. Check correlation value
4. Baca interpretasi otomatis
5. Lihat heatmap untuk overview
```

### Scenario 3: Filter & Compare
```
1. Set range slider untuk filter
2. Lihat metrik ter-update
3. Compare dengan data original
4. Check status indicators
5. Download filtered data
```

---

## ⚙️ Technical Details

### Performance:
- `@st.cache_data` digunakan untuk caching
- Reduce computational overhead
- Fast data loading & filtering

### Data Processing:
- `df.dropna()` untuk remove missing values
- Dynamic column detection
- Auto numeric column identification

### Visualizations:
- Plotly Express untuk interactive charts
- Trendline dengan OLS regression
- Custom color schemes

### UI/UX:
- Responsive layout dengan columns
- Tabs untuk organize controls
- Expanders untuk progressive disclosure
- Status messages untuk user feedback

---

## 🔍 Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Dataset not found | Check path: `datasets/StudentPerformanceFactors.csv` |
| Dropdown kosong | Use `df.dropna()` or check data types |
| Slow performance | Reduce nbins or filter data first |
| Charts tidak muncul | pip install plotly / select 2+ features |
| Port sudah pakai | `streamlit run app.py --server.port 8503` |

---

## 📚 Learning Resources

### Dokumentasi:
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)

### Files dalam Project:
- `DOKUMENTASI.md` - Comprehensive guide (semua detail)
- `PENJELASAN_APLIKASI.py` - Interactive presentation
- `README.md` - Quick reference (file ini)
- `app_part1.py` - Actual application

---

## 📝 File Organization

```
session3_streamlit_basics/
├── app_part1.py                  ← MAIN APPLICATION
├── DOKUMENTASI.md                ← COMPREHENSIVE GUIDE
├── PENJELASAN_APLIKASI.py        ← INTERACTIVE PRESENTATION
├── README.md                      ← QUICK REFERENCE (INI)
└── requirements.txt               ← DEPENDENCIES
```

---

## ✅ Checklist Sebelum Running

- [ ] Python 3.8+ installed
- [ ] Streamlit installed (`pip install streamlit`)
- [ ] Plotly installed (`pip install plotly`)
- [ ] Pandas installed (`pip install pandas`)
- [ ] Navigate ke directory session3_streamlit_basics
- [ ] StudentPerformanceFactors.csv ada di datasets/
- [ ] No port conflicts (8502 free)

---

## 🎓 Learning Outcomes

Setelah menggunakan aplikasi ini, Anda akan mengerti:

✅ Cara membangun dashboard dengan Streamlit
✅ Input/Output widgets dan cara kerjanya
✅ Layout design (columns, containers, tabs)
✅ Interactive visualizations dengan Plotly
✅ Data filtering & manipulation
✅ File download functionality
✅ UI/UX best practices
✅ Interpretasi visualisasi data
✅ Data analysis workflow
✅ Streamlit performance optimization

---

## 🆘 Need Help?

1. **Read DOKUMENTASI.md** untuk penjelasan lengkap
2. **Run PENJELASAN_APLIKASI.py** untuk tutorial interaktif
3. **Check troubleshooting section** untuk common issues
4. **Review code comments** di app_part1.py
5. **Check console output** untuk error messages

---

## 📞 Contact & Support

Jika ada pertanyaan:
1. Check documentation terlebih dahulu
2. Review error messages dengan hati-hati
3. Try reproduction steps
4. Consult with instructor/peers
5. Check Streamlit documentation

---

**Status:** ✅ Complete & Ready
**Last Updated:** December 2025
**Version:** 1.0

---

Selamat belajar! 🚀
