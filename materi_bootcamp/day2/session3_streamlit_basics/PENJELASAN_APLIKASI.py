"""
PENJELASAN INTERAKTIF: Student Performance Analytics Dashboard
Script ini menjelaskan aplikasi Streamlit yang telah dibuat
Bisa dijalankan dengan: streamlit run PENJELASAN_APLIKASI.py
"""

import streamlit as st
from pathlib import Path

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Penjelasan Aplikasi - Streamlit Basics",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# CUSTOM CSS
# ========================================
st.markdown("""
    <style>
    .title-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .feature-box {
        background: #f0f2f6;
        padding: 15px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
        border-radius: 5px;
    }
    .code-box {
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New';
        overflow-x: auto;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR NAVIGATION
# ========================================
st.sidebar.header("📚 Navigasi")
page = st.sidebar.radio(
    "Pilih halaman penjelasan:",
    [
        "🏠 Beranda",
        "📖 Panduan Lengkap",
        "🎨 Struktur Aplikasi",
        "🔧 Fitur-Fitur Widget",
        "📊 Panduan Visualisasi",
        "💡 Tips & Troubleshooting",
        "🚀 Cara Menjalankan"
    ]
)

st.sidebar.divider()
st.sidebar.info("""
    **Student Performance Analytics Dashboard**
    
    Aplikasi Streamlit untuk menganalisis data performa siswa dengan visualisasi interaktif.
    
    **Session:** 3 Streamlit Basics
    **Day:** 2 Bootcamp Data Science
""")

# ========================================
# PAGE: BERANDA
# ========================================
if page == "🏠 Beranda":
    st.markdown("""
        <div class="title-box">
            <h1>🎓 Student Performance Analytics Dashboard</h1>
            <p>Panduan Lengkap Aplikasi Streamlit Session 3</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    ## Selamat Datang! 👋
    
    Dokumentasi ini akan menjelaskan **aplikasi Streamlit yang telah dibuat** 
    untuk menganalisis data performa akademik siswa.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📖 Panduan Lengkap
        Penjelasan mendetail tentang:
        - Tujuan aplikasi
        - Fitur-fitur utama
        - Cara menggunakan
        """)
        if st.button("Baca Selengkapnya →", key="btn1"):
            st.switch_page("pages/panduan.py") if Path("pages").exists() else st.info("Pilih dari sidebar")
    
    with col2:
        st.markdown("""
        ### 🎨 Struktur Aplikasi
        Memahami:
        - Layout dan design
        - Workflow aplikasi
        - Component hierarchy
        """)
    
    with col3:
        st.markdown("""
        ### 📊 Visualisasi Data
        Belajar tentang:
        - Histogram
        - Scatter Plot
        - Heatmap
        - Interpretasi chart
        """)
    
    st.divider()
    
    st.subheader("✨ Fitur Utama Aplikasi")
    
    features = [
        ("🎛️ Sidebar Navigation", "Tab-based filter system dengan multiple options"),
        ("📊 Interactive Metrics", "Real-time metrics display dengan delta calculation"),
        ("📈 Multiple Charts", "Histogram, Scatter, Bar Chart, Heatmap Correlation"),
        ("📋 Data Table", "Dynamic column selection dan CSV export"),
        ("🔍 Smart Filtering", "Range slider, multiselect, checkbox options"),
        ("📚 Built-in Guide", "Panduan visualisasi yang expandable"),
        ("💾 Download Data", "Export filtered data sebagai CSV"),
        ("⚡ Performance", "Data caching dengan @st.cache_data"),
    ]
    
    for feature, description in features:
        st.markdown(f"""
        <div class="feature-box">
            <b>{feature}</b><br/>
            {description}
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("📊 Tech Stack")
    
    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)
    
    with tech_col1:
        st.markdown("""
        **Frontend:**
        - Streamlit
        - HTML/CSS
        """)
    
    with tech_col2:
        st.markdown("""
        **Data Processing:**
        - Pandas
        - NumPy
        """)
    
    with tech_col3:
        st.markdown("""
        **Visualization:**
        - Plotly
        - Chart types
        """)
    
    with tech_col4:
        st.markdown("""
        **Data Source:**
        - CSV file
        - 2000+ records
        - 15+ features
        """)

# ========================================
# PAGE: PANDUAN LENGKAP
# ========================================
elif page == "📖 Panduan Lengkap":
    st.markdown("""
        <div class="title-box">
            <h2>📖 Panduan Lengkap Aplikasi</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎯 Tujuan Aplikasi")
    
    st.write("""
    Aplikasi ini dirancang untuk:
    
    1. **Learning Purpose** - Mengajarkan konsep-konsep Streamlit
    2. **Data Exploration** - Menganalisis data student performance
    3. **Dashboard Example** - Contoh dashboard interaktif yang real-world
    4. **Best Practices** - Mendemonstrasikan practices terbaik
    """)
    
    st.divider()
    
    st.subheader("📋 Struktur Dataset")
    
    st.info("""
    **File:** StudentPerformanceFactors.csv
    **Lokasi:** c:\\itbootcamp\\data-science\\datasets\\
    **Size:** ~2000 records
    **Features:** 15+ numeric dan categorical columns
    """)
    
    with st.expander("📊 Dataset Columns"):
        st.write("""
        Dataset berisi informasi tentang:
        - **Student ID** - Identitas siswa
        - **Hours_Studied** - Jam belajar per minggu
        - **Attendance** - Persentase kehadiran
        - **Previous_Scores** - Nilai ujian sebelumnya
        - **Engagement_Level** - Tingkat engagement (Low/Medium/High)
        - **Sleep_Hours** - Rata-rata jam tidur
        - **Exam_Score** - Skor ujian final
        - **Dan features lainnya...**
        """)
    
    st.divider()
    
    st.subheader("🚀 Cara Menggunakan Aplikasi")
    
    step_col1, step_col2 = st.columns(2)
    
    with step_col1:
        st.markdown("""
        ### Langkah 1: Jalankan Aplikasi
        ```bash
        streamlit run app_part1.py
        ```
        Browser akan terbuka otomatis
        
        ### Langkah 2: Gunakan Sidebar Filters
        - Pilih fitur numerik (multiselect)
        - Atur range filter (slider)
        - Pilih opsi tampilan (checkbox)
        
        ### Langkah 3: Lihat Visualisasi
        - Histogram untuk distribusi
        - Scatter untuk relasi
        - Bar chart untuk perbandingan
        - Heatmap untuk korelasi
        """)
    
    with step_col2:
        st.markdown("""
        ### Langkah 4: Analisis Data
        - Baca penjelasan di setiap chart
        - Lihat statistik yang ditampilkan
        - Perhatikan interpretasi
        
        ### Langkah 5: Download Data
        - Klik tombol "Download CSV"
        - Pilih kolom yang diinginkan
        - Simpan file untuk analisis lanjutan
        
        ### Langkah 6: Reset & Explore
        - Klik "Reset All Filters"
        - Ubah kombinasi filter
        - Lihat data dari sudut pandang berbeda
        """)
    
    st.divider()
    
    st.subheader("📊 Contoh Workflow")
    
    st.markdown("""
    **Skenario:** Analisis relasi antara Jam Belajar dan Nilai Ujian
    
    1. **Select Features**
       - Pilih "Hours_Studied" dan "Exam_Score"
    
    2. **View Distribution**
       - Lihat histogram Hours_Studied
       - Interpretasi: mayoritas siswa belajar berapa jam?
    
    3. **Analyze Relationship**
       - Lihat scatter plot Hours_Studied vs Exam_Score
       - Interpretasi: korelasi positif atau negatif?
    
    4. **Check Correlation**
       - Lihat heatmap correlation
       - Cari nilai korelasi eksak antara kedua variabel
    
    5. **Filter & Compare**
       - Filter hanya siswa dengan Hours_Studied > 5
       - Bandingkan dengan data sebelumnya
       - Lihat perubahan metrik dan visualisasi
    
    6. **Export Results**
       - Download filtered data sebagai CSV
       - Gunakan untuk presentasi atau analisis lebih lanjut
    """)

# ========================================
# PAGE: STRUKTUR APLIKASI
# ========================================
elif page == "🎨 Struktur Aplikasi":
    st.markdown("""
        <div class="title-box">
            <h2>🎨 Struktur & Arsitektur Aplikasi</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📂 File Structure")
    
    st.code("""
session3_streamlit_basics/
├── app_part1.py                    # File utama aplikasi (454 lines)
├── DOKUMENTASI.md                  # Dokumentasi lengkap
├── PENJELASAN_APLIKASI.py          # Script presentasi ini
└── requirements.txt                # Dependencies
    """, language="text")
    
    st.divider()
    
    st.subheader("🔄 Application Flow")
    
    st.markdown("""
    ```
    USER OPENS BROWSER (http://localhost:8502)
        ↓
    STREAMLIT LOADS app_part1.py
        ↓
    ┌─────────────────────────────────────────────┐
    │  PAGE CONFIG                                 │
    │  - Set title, icon, layout                  │
    │  - Define custom CSS                        │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  LOAD DATA (@st.cache_data)                 │
    │  - Read CSV from datasets folder             │
    │  - Cache for performance                     │
    │  - Return DataFrame                          │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  HEADER & INTRODUCTION                       │
    │  - Title & description                       │
    │  - Tips for usage                            │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  SIDEBAR WIDGETS (3 TABS)                    │
    │  ├─ Filter Tab                               │
    │  │  ├─ Multiselect features                 │
    │  │  ├─ Slider range filter                  │
    │  │  └─ Checkbox options                     │
    │  ├─ Visualization Tab                        │
    │  │  ├─ Radio chart type                     │
    │  │  └─ Selectbox color option               │
    │  └─ About Tab                                │
    │     └─ Dataset info                          │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  FILTER DATA (In Memory)                     │
    │  - Apply multiselect filter                  │
    │  - Apply range slider                        │
    │  - Apply checkbox conditions                 │
    │  → Create filtered_df                        │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  METRICS SECTION (4 COLUMNS)                 │
    │  - st.metric() elements                      │
    │  - Real-time calculations                    │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  VISUALIZATION GUIDE (EXPANDER)              │
    │  - Histogram explanation                     │
    │  - Scatter plot guide                        │
    │  - Box plot tutorial                         │
    │  - Heatmap explanation                       │
    │  - Tips & best practices                     │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  CHARTS SECTION (2 ROWS × 2 COLS)            │
    │  Row 1:                                      │
    │  ├─ Histogram (left)                         │
    │  └─ Scatter plot (right)                     │
    │  Row 2:                                      │
    │  ├─ Bar chart (left)                         │
    │  └─ Heatmap (right)                          │
    │  Each with expandable explanation            │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  CONTAINERS & STATISTICS                     │
    │  - Stats container (2 columns)               │
    │  - Insights expander                         │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  DATA TABLE SECTION                          │
    │  - Column multiselect                        │
    │  - Display dataframe                         │
    │  - Data info expander                        │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  INTERACTIVE ACTIONS (3 BUTTONS)             │
    │  ├─ Reset Filters → st.rerun()              │
    │  ├─ Show Summary → st.balloons()            │
    │  └─ Download CSV → st.download_button()     │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  DATA QUALITY INDICATORS                     │
    │  - Data completeness progress bar            │
    │  - Status messages (error/warning/info)      │
    └─────────────────────────────────────────────┘
        ↓
    ┌─────────────────────────────────────────────┐
    │  FOOTER & SIDEBAR INFO                       │
    │  - Credits & info                            │
    │  - Learned features list                     │
    │  - Next session preview                      │
    └─────────────────────────────────────────────┘
    ```
    """)
    
    st.divider()
    
    st.subheader("🔍 Key Components")
    
    components = {
        "Layout Components": [
            "st.columns() - Side-by-side layouts",
            "st.container() - Group elements",
            "st.expander() - Collapsible sections",
            "st.tabs() - Tab navigation",
        ],
        "Widget Components": [
            "st.multiselect() - Multiple selection",
            "st.selectbox() - Single selection",
            "st.slider() - Range input",
            "st.checkbox() - Toggle option",
            "st.radio() - Single choice group",
        ],
        "Display Components": [
            "st.metric() - Key metrics",
            "st.dataframe() - Data tables",
            "st.plotly_chart() - Interactive charts",
            "st.balloons() - Animation",
        ],
        "Data Components": [
            "@st.cache_data - Cache function results",
            "pd.read_csv() - Load CSV data",
            "df.copy() - Create data copy",
            "filtered_df - Filtered dataset",
        ],
    }
    
    for category, items in components.items():
        with st.expander(f"📦 {category}"):
            for item in items:
                st.write(f"• {item}")

# ========================================
# PAGE: FITUR-FITUR WIDGET
# ========================================
elif page == "🔧 Fitur-Fitur Widget":
    st.markdown("""
        <div class="title-box">
            <h2>🔧 Widget Streamlit yang Digunakan</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎛️ Input Widgets")
    
    widgets = [
        {
            "name": "st.multiselect()",
            "purpose": "Memilih multiple items dari list",
            "code": """selected_features = st.multiselect(
    'Pilih fitur numerik untuk analisis:',
    numeric_features,
    default=numeric_features[:3]
)""",
            "result": "List of selected items"
        },
        {
            "name": "st.selectbox()",
            "purpose": "Memilih satu item dari dropdown",
            "code": """feature_to_filter = st.selectbox(
    'Pilih fitur untuk di-filter:',
    numeric_features
)""",
            "result": "Single selected item"
        },
        {
            "name": "st.slider()",
            "purpose": "Memilih range nilai numerik",
            "code": """min_val, max_val = st.slider(
    f'Range {feature_to_filter}:',
    min_value=float(df[feature_to_filter].min()),
    max_value=float(df[feature_to_filter].max()),
    value=(min, max),
    step=0.5
)""",
            "result": "Tuple of (min, max) values"
        },
        {
            "name": "st.checkbox()",
            "purpose": "Toggle on/off option",
            "code": """show_statistics = st.checkbox(
    'Tampilkan Statistik Detail',
    value=True
)""",
            "result": "Boolean (True/False)"
        },
        {
            "name": "st.radio()",
            "purpose": "Pilih satu dari beberapa opsi",
            "code": """chart_type = st.radio(
    "Tipe Chart Utama:",
    ["Distribution", "Scatter Plot", "Box Plot"]
)""",
            "result": "Selected option string"
        },
    ]
    
    for widget in widgets:
        with st.expander(f"📌 {widget['name']}"):
            st.write(f"**Tujuan:** {widget['purpose']}")
            st.markdown("**Contoh Kode:**")
            st.code(widget['code'], language="python")
            st.write(f"**Return Type:** {widget['result']}")
    
    st.divider()
    
    st.subheader("📊 Display Widgets")
    
    display_widgets = [
        {
            "name": "st.metric()",
            "use": "Display KPI atau nilai penting dengan delta",
            "example": "st.metric('Revenue', '$100,000', '+$10,000')"
        },
        {
            "name": "st.dataframe()",
            "use": "Display tabel data dengan pagination",
            "example": "st.dataframe(filtered_df, use_container_width=True)"
        },
        {
            "name": "st.plotly_chart()",
            "use": "Display Plotly interactive charts",
            "example": "st.plotly_chart(fig, use_container_width=True)"
        },
        {
            "name": "st.progress()",
            "use": "Display progress bar",
            "example": "st.progress(0.75)  # 75%"
        },
        {
            "name": "st.balloons()",
            "use": "Show celebration animation",
            "example": "st.balloons()  # Muncul balon"
        },
    ]
    
    for widget in display_widgets:
        st.markdown(f"""
        <div class="feature-box">
            <b>{widget['name']}</b><br/>
            <b>Kegunaan:</b> {widget['use']}<br/>
            <code>{widget['example']}</code>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("🎯 Action Widgets")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### st.button()
        Tombol untuk aksi
        ```python
        if st.button("Click me"):
            st.write("Button clicked!")
        ```
        """)
    
    with col2:
        st.markdown("""
        ### st.download_button()
        Download file
        ```python
        st.download_button(
            label="Download",
            data=csv_data,
            file_name="data.csv",
            mime="text/csv"
        )
        ```
        """)
    
    with col3:
        st.markdown("""
        ### st.form()
        Submit multiple inputs
        ```python
        with st.form("my_form"):
            # Widgets here
            st.form_submit_button("Submit")
        ```
        """)
    
    st.divider()
    
    st.subheader("💬 Message Widgets")
    
    st.success("✅ st.success() - Pesan sukses (hijau)")
    st.info("ℹ️ st.info() - Pesan informasi (biru)")
    st.warning("⚠️ st.warning() - Pesan warning (kuning)")
    st.error("❌ st.error() - Pesan error (merah)")

# ========================================
# PAGE: PANDUAN VISUALISASI
# ========================================
elif page == "📊 Panduan Visualisasi":
    st.markdown("""
        <div class="title-box">
            <h2>📊 Panduan Visualisasi Data</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📈 Tipe-Tipe Visualisasi")
    
    viz_tabs = st.tabs([
        "📊 Histogram",
        "📍 Scatter Plot",
        "📦 Box Plot",
        "🎨 Bar Chart",
        "🔥 Heatmap"
    ])
    
    # HISTOGRAM TAB
    with viz_tabs[0]:
        st.markdown("""
        ### Histogram (Distribution Chart)
        
        **Apa itu?**
        - Menampilkan distribusi frekuensi dari satu variabel numerik
        - Sumbu X: Rentang nilai | Sumbu Y: Jumlah frekuensi
        
        **Cara Membaca:**
        - Bar tinggi = banyak data di rentang itu
        - Bar rendah = sedikit data di rentang itu
        - Bentuk kurva menunjukkan pola distribusi
        
        **Jenis Pola:**
        """)
        
        pat_col1, pat_col2, pat_col3 = st.columns(3)
        with pat_col1:
            st.markdown("🔔 **Normal Distribution**\nBell curve shape")
        with pat_col2:
            st.markdown("➡️ **Right Skewed**\nLong tail ke kanan")
        with pat_col3:
            st.markdown("⬅️ **Left Skewed**\nLong tail ke kiri")
        
        st.markdown("""
        **Digunakan untuk:**
        - Melihat bentuk distribusi
        - Deteksi outlier
        - Memahami penyebaran data
        - Planning data transformation
        
        **Contoh Interpretasi:**
        ```
        IF histogram bell-curve THEN data normally distributed
        IF ada spike terpisah THEN mungkin ada dua kelompok
        IF ada outlier jauh THEN perlu investigasi
        ```
        """)
    
    # SCATTER PLOT TAB
    with viz_tabs[1]:
        st.markdown("""
        ### Scatter Plot (Relasi Antar Variabel)
        
        **Apa itu?**
        - Menampilkan hubungan antara DUA variabel
        - X-axis: Variabel 1 | Y-axis: Variabel 2
        - Setiap titik = satu data point
        
        **Cara Membaca:**
        """)
        
        trend_col1, trend_col2, trend_col3 = st.columns(3)
        with trend_col1:
            st.markdown("📈 **Positive Trend**\nTitik naik ke kanan")
        with trend_col2:
            st.markdown("📉 **Negative Trend**\nTitik turun ke kanan")
        with trend_col3:
            st.markdown("⚪ **No Trend**\nTitik tersebar random")
        
        st.markdown("""
        **Korelasi Kekuatan:**
        ```
        +1.0  = Perfect positive correlation
        +0.7  = Strong positive
        +0.5  = Moderate positive
         0.0  = No correlation
        -0.5  = Moderate negative
        -0.7  = Strong negative
        -1.0  = Perfect negative correlation
        ```
        
        **⚠️ PENTING:**
        Korelasi ≠ Kausalitas
        Dua variabel bisa berkorelasi tanpa saling mempengaruhi!
        
        **Digunakan untuk:**
        - Eksplorasi relasi antar variabel
        - Feature engineering
        - Multicollinearity detection
        """)
    
    # BOX PLOT TAB
    with viz_tabs[2]:
        st.markdown("""
        ### Box Plot (Distribution & Outliers)
        
        **Komponen Box Plot:**
        ```
                Atas Whisker (max normal)
                      ↓
                ┌─────────┐
                │         │
         Q1 (25%)         │ Q3 (75%)
                │ Median  │
                │         │
                └─────────┘
                      ↑
            Bawah Whisker (min normal)
        
        Titik terpisah = Outlier
        ```
        
        **Interpretasi Setiap Bagian:**
        """)
        
        box_col1, box_col2 = st.columns(2)
        with box_col1:
            st.write("""
            **Box (Jantung Data)**
            - 50% data berada di sini
            - Garis di tengah = Median
            - Panjang box = Variabilitas
            """)
        with box_col2:
            st.write("""
            **Whisker (Batas Normal)**
            - 1.5 × IQR dari quartile
            - Titik di luar = Outlier
            - Simetri = Normalitas
            """)
        
        st.markdown("""
        **Digunakan untuk:**
        - Membandingkan distribusi antar grup
        - Deteksi outlier otomatis
        - Analisis symmetry
        - Data quality check
        """)
    
    # BAR CHART TAB
    with viz_tabs[3]:
        st.markdown("""
        ### Bar Chart (Mean ± Std Dev)
        
        **Apa yang ditampilkan:**
        - Bar = Nilai rata-rata (Mean)
        - Error bar = Standar deviasi (Variabilitas)
        
        **Interpretasi:**
        """)
        
        bar_col1, bar_col2 = st.columns(2)
        with bar_col1:
            st.write("""
            **Bar Tinggi**
            + Error bar pendek
            → Nilai tinggi, konsisten
            """)
        with bar_col2:
            st.write("""
            **Bar Rendah**
            + Error bar panjang
            → Nilai rendah, bervariasi
            """)
        
        st.markdown("""
        **Digunakan untuk:**
        - Perbandingan mean antar variabel
        - Visualisasi uncertainty
        - Quick overview multi-variabel
        """)
    
    # HEATMAP TAB
    with viz_tabs[4]:
        st.markdown("""
        ### Heatmap Correlation
        
        **Apa itu?**
        - Menampilkan korelasi SEMUA variabel numerik
        - Warna = kekuatan korelasi
        - Angka = nilai korelasi (-1 hingga +1)
        
        **Skala Warna:**
        """)
        
        st.markdown("""
        | Warna | Korelasi | Arti |
        |-------|----------|------|
        | 🟢 Hijau/Biru | +1 | Korelasi positif sempurna |
        | 🟡 Kuning | 0 | Tidak ada korelasi |
        | 🔴 Ungu/Merah | -1 | Korelasi negatif sempurna |
        """)
        
        st.markdown("""
        **Cara Membaca:**
        - Fokus pada warna gelap (korelasi kuat)
        - Diagonal selalu 1 (var dengan dirinya sendiri)
        - Simetris: X vs Y = Y vs X
        
        **Interpretasi Nilai:**
        - -1 hingga -0.7 = Strong negative
        - -0.7 hingga -0.3 = Moderate negative
        - -0.3 hingga +0.3 = Weak/No correlation
        - +0.3 hingga +0.7 = Moderate positive
        - +0.7 hingga +1.0 = Strong positive
        
        **⚠️ Penting:** Korelasi ≠ Kausalitas!
        
        **Digunakan untuk:**
        - Multi-variabel analysis
        - Feature selection
        - Multicollinearity detection
        """)

# ========================================
# PAGE: TIPS & TROUBLESHOOTING
# ========================================
elif page == "💡 Tips & Troubleshooting":
    st.markdown("""
        <div class="title-box">
            <h2>💡 Tips, Best Practices & Troubleshooting</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✅ Best Practices")
    
    practices = [
        ("📊 Mulai dari Histogram", "Pahami distribusi data terlebih dahulu sebelum analisis lebih lanjut"),
        ("📍 Gunakan Scatter untuk Eksplorasi", "Cari pola dan hubungan antar variabel"),
        ("📦 Box Plot untuk Deteksi Outlier", "Identifikasi dan investigasi nilai ekstrem"),
        ("🔥 Heatmap untuk Overview", "Lihat gambaran besar korelasi semua variabel"),
        ("📋 Perhatikan Ukuran Sampel", "Ukuran sampel besar = interpretasi lebih reliable"),
        ("🔍 Cross-check dengan Statistik", "Jangan hanya mengandalkan visualisasi"),
        ("💾 Dokumentasikan Temuan", "Catat insight dan kesimpulan setiap analisis"),
        ("🎨 Gunakan Warna Konsisten", "Memudahkan pemahaman dan presentasi"),
    ]
    
    for title, description in practices:
        st.markdown(f"""
        <div class="feature-box">
            <b>{title}</b><br/>
            {description}
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("⚠️ Hal yang Perlu Diperhatikan")
    
    warnings = [
        ("Outlier", "Bisa ada karena error atau data unik - periksa konteks sebelum remove"),
        ("Korelasi ≠ Kausalitas", "Hubungan statistik ≠ sebab-akibat - butuh bukti tambahan"),
        ("Missing Values", "Handling NaN affects results - gunakan dropna() atau imputation"),
        ("Skala Berbeda", "Variabel berbeda scale bisa misleading - normalisasi jika perlu"),
        ("Bias Data", "Collection bias bisa influence hasil - understand data source"),
        ("Ukuran Sampel Kecil", "Interpretasi hati-hati - bisa unreliable"),
        ("Overfitting", "Jangan terlalu fokus pada detail kecil dari sample"),
    ]
    
    for issue, solution in warnings:
        st.warning(f"**{issue}:** {solution}")
    
    st.divider()
    
    st.subheader("🔧 Troubleshooting")
    
    troubleshoot_tabs = st.tabs([
        "📁 Data Issues",
        "🎨 Display Issues",
        "⚡ Performance",
        "🐛 Debug Tips"
    ])
    
    with troubleshoot_tabs[0]:
        st.markdown("""
        ### Dataset not found
        ```
        Error: FileNotFoundError
        Solusi:
        1. Periksa path di load_data()
        2. Pastikan file ada di c:\\itbootcamp\\data-science\\datasets\\
        3. Check filename spelling
        ```
        
        ### Empty dataframe after filtering
        ```
        Solusi:
        1. Check filter criteria
        2. Gunakan st.write(filtered_df.shape)
        3. Reset filters dan coba ulang
        ```
        
        ### Missing column error
        ```
        Error: KeyError: 'column_name'
        Solusi:
        1. st.write(df.columns) untuk cek kolom
        2. Periksa spelling
        3. Handle NaN values dengan dropna()
        ```
        """)
    
    with troubleshoot_tabs[1]:
        st.markdown("""
        ### Charts tidak muncul
        ```
        Solusi:
        1. pip install plotly (ensure installed)
        2. Pilih minimal 2 features untuk scatter
        3. Check browser console (F12)
        4. Try st.write(fig) untuk debug
        ```
        
        ### Dropdown kosong
        ```
        Solusi:
        1. st.write(df.dtypes) check data types
        2. Pastikan ada data di kolom
        3. Gunakan df.dropna() untuk remove empty rows
        ```
        
        ### Layout berantakan
        ```
        Solusi:
        1. Clear cache: Ctrl + R
        2. Restart streamlit: Ctrl + C, run ulang
        3. Check screen resolution
        4. Try different browser
        ```
        """)
    
    with troubleshoot_tabs[2]:
        st.markdown("""
        ### Aplikasi lambat
        ```
        Solusi:
        1. @st.cache_data sudah digunakan (cek load_data)
        2. Reduce jumlah rows untuk display
        3. Simplify visualisasi (less complex charts)
        4. Monitor memory usage
        ```
        
        ### Browser crash saat load
        ```
        Solusi:
        1. Check browser resources (Task Manager)
        2. Close other heavy apps
        3. Reduce nbins histogram (dari 30 ke 20)
        4. Filter data terlebih dahulu
        ```
        """)
    
    with troubleshoot_tabs[3]:
        st.markdown("""
        ### Debug Techniques
        ```python
        # Print dataframe shape
        st.write(f"Shape: {df.shape}")
        
        # Print columns
        st.write(df.columns.tolist())
        
        # Print data types
        st.write(df.dtypes)
        
        # Display raw data
        st.dataframe(df.head())
        
        # Check for missing values
        st.write(df.isnull().sum())
        
        # Check statistics
        st.write(df.describe())
        ```
        
        ### Browser Console
        - Tekan F12 untuk buka Developer Tools
        - Cek tab Console untuk error messages
        - Cek Network tab untuk request failures
        """)

# ========================================
# PAGE: CARA MENJALANKAN
# ========================================
elif page == "🚀 Cara Menjalankan":
    st.markdown("""
        <div class="title-box">
            <h2>🚀 Panduan Menjalankan Aplikasi</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Prerequisites")
    
    st.info("""
    Pastikan sudah terinstall:
    - **Python 3.8+** (check dengan: `python --version`)
    - **Streamlit** (check dengan: `pip show streamlit`)
    - **Plotly** (check dengan: `pip show plotly`)
    - **Pandas** (check dengan: `pip show pandas`)
    """)
    
    st.subheader("🛠️ Installation")
    
    st.markdown("""
    ### Opsi 1: Install Individual Packages
    """)
    
    st.code("""
pip install streamlit
pip install plotly
pip install pandas
pip install numpy
    """, language="bash")
    
    st.markdown("""
    ### Opsi 2: Install dari Requirements
    """)
    
    st.code("""
pip install -r requirements.txt
    """, language="bash")
    
    st.divider()
    
    st.subheader("▶️ Running the Application")
    
    st.markdown("""
    ### Step 1: Buka Terminal
    - **Windows:** Tekan `Win + R`, ketik `powershell` atau `cmd`
    - **Mac/Linux:** Buka Terminal
    """)
    
    st.markdown("""
    ### Step 2: Navigate ke Directory
    """)
    
    st.code("""
cd "c:\\itbootcamp\\data-science\\materi_bootcamp\\day2\\session3_streamlit_basics"
    """, language="bash")
    
    st.markdown("""
    ### Step 3: Run Streamlit
    """)
    
    st.code("""
streamlit run app_part1.py
    """, language="bash")
    
    st.info("""
    **Output yang diharapkan:**
    ```
    You can now view your Streamlit app in your browser.
    
    Local URL: http://localhost:8502
    Network URL: http://192.168.50.89:8502
    ```
    Browser akan terbuka otomatis, atau Anda bisa manually buka URL tersebut.
    """)
    
    st.divider()
    
    st.subheader("🎯 Menu Options di Aplikasi")
    
    menu_steps = [
        ("🎛️ Filter Tab", "Pilih features, set range, select options untuk data filtering"),
        ("📈 Visualization Tab", "Pilih tipe chart dan color option untuk visualisasi"),
        ("📚 About Tab", "Lihat informasi tentang dataset"),
        ("📊 Key Metrics", "Lihat 4 metrics utama yang ter-update real-time"),
        ("📖 Panduan Visualisasi", "Expand untuk baca penjelasan setiap jenis chart"),
        ("📋 Charts", "Lihat 4 visualisasi dengan penjelasan interaktif"),
        ("📦 Containers", "Lihat statistik dan insights"),
        ("📋 Data Table", "Pilih kolom dan lihat data lengkap"),
        ("🎯 Buttons", "Reset filters, show summary, atau download CSV"),
        ("⏳ Status", "Lihat data completeness dan status"),
    ]
    
    for menu, description in menu_steps:
        st.markdown(f"**{menu}** - {description}")
    
    st.divider()
    
    st.subheader("🔌 Port Configuration")
    
    st.markdown("""
    Jika port 8502 sudah digunakan, gunakan port berbeda:
    """)
    
    st.code("""
streamlit run app_part1.py --server.port 8503
streamlit run app_part1.py --server.port 8504
streamlit run app_part1.py --server.port 9000
    """, language="bash")
    
    st.divider()
    
    st.subheader("🛑 Menghentikan Aplikasi")
    
    st.code("""
Tekan: Ctrl + C  (di terminal tempat streamlit running)
    """, language="bash")
    
    st.divider()
    
    st.subheader("💻 Quick Start Checklist")
    
    with st.form("checklist"):
        st.checkbox("✅ Python 3.8+ terinstall")
        st.checkbox("✅ Streamlit terinstall (pip install streamlit)")
        st.checkbox("✅ Navigate ke directory session3_streamlit_basics")
        st.checkbox("✅ Dataset ada di datasets/ folder")
        st.checkbox("✅ Run: streamlit run app_part1.py")
        st.checkbox("✅ Buka browser: http://localhost:8502")
        st.form_submit_button("✅ All Ready!")
    
    st.success("""
    🎉 Selamat! Aplikasi siap dijalankan!
    
    Jika ada masalah, silakan:
    1. Check troubleshooting di halaman Tips & Troubleshooting
    2. Baca dokumentasi DOKUMENTASI.md
    3. Lihat error messages di console
    """)

# ========================================
# FOOTER
# ========================================
st.divider()
st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><strong>📚 Penjelasan Interaktif - Student Performance Analytics Dashboard</strong></p>
        <p>Session 3: Streamlit Basics | Bootcamp Data Science | Day 2</p>
        <p style='font-size: 12px;'>Dibuat untuk membantu Anda memahami aplikasi Streamlit yang telah dibuat</p>
    </div>
""", unsafe_allow_html=True)
