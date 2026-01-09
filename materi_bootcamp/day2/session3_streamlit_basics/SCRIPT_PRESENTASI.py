"""
SCRIPT PRESENTASI: Menjelaskan Halaman Student Performance Analytics Dashboard
Script ini bisa digunakan untuk presentasi dan menjelaskan setiap bagian halaman aplikasi

Usage:
1. Run: streamlit run SCRIPT_PRESENTASI.py
2. Navigasi untuk melihat penjelasan setiap section halaman
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Presentasi - Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ========================================
# CUSTOM CSS
# ========================================
st.markdown("""
    <style>
    .slide-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
        font-weight: bold;
    }
    .section-box {
        background: #f0f2f6;
        padding: 20px;
        border-left: 5px solid #667eea;
        margin: 15px 0;
        border-radius: 5px;
    }
    .feature-item {
        background: white;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #764ba2;
        border-radius: 3px;
    }
    .code-demo {
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New';
        font-size: 12px;
        overflow-x: auto;
    }
    .screenshot-label {
        color: #666;
        font-style: italic;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR NAVIGATION
# ========================================
st.sidebar.title("📊 PRESENTASI HALAMAN")
st.sidebar.divider()

presentation_page = st.sidebar.radio(
    "Pilih Slide Presentasi:",
    [
        "🎬 Intro",
        "📄 Halaman Lengkap",
        "📍 Section 1: Header",
        "🎛️ Section 2: Sidebar",
        "📊 Section 3: Metrics",
        "📚 Section 4: Visualization Guide",
        "📈 Section 5: Charts",
        "📦 Section 6: Containers",
        "📋 Section 7: Data Table",
        "🎯 Section 8: Actions",
        "⏳ Section 9: Status",
        "👣 Section 10: Footer",
        "🔄 Full Flow"
    ]
)

st.sidebar.divider()
st.sidebar.info("""
**Presentasi Halaman Aplikasi**

Student Performance Analytics Dashboard
Session 3 - Streamlit Basics
""")

# ========================================
# SLIDE: INTRO
# ========================================
if presentation_page == "🎬 Intro":
    st.markdown('<div class="slide-title">🎓 Student Performance Analytics Dashboard</div>', unsafe_allow_html=True)
    
    st.write("## Presentasi Halaman Aplikasi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📌 Tujuan Presentasi
        
        Menjelaskan secara detail tentang:
        - ✅ Struktur halaman aplikasi
        - ✅ Setiap section dan fungsinya
        - ✅ Widget dan interaksi yang digunakan
        - ✅ Cara user berinteraksi
        - ✅ Flow data dan processing
        - ✅ Design decisions
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Apa yang akan dipelajari
        
        Setelah presentasi ini, Anda akan mengerti:
        - 🏗️ Arsitektur halaman
        - 🎨 Layout dan design
        - 🔄 User interaction flow
        - 📊 Data visualization
        - 💡 Best practices
        - 🚀 Deployment considerations
        """)
    
    st.divider()
    
    st.markdown("""
    ### 📖 Struktur Presentasi
    
    Presentasi ini dibagi menjadi **10 sections**:
    
    1. **Header** - Title dan informasi
    2. **Sidebar** - Navigation dan filters
    3. **Metrics** - Key metrics display
    4. **Visualization Guide** - Panduan membaca chart
    5. **Charts** - Visualisasi data interaktif
    6. **Containers** - Statistik dan insights
    7. **Data Table** - Display data lengkap
    8. **Actions** - Interactive buttons
    9. **Status** - Data quality indicators
    10. **Footer** - Credits dan info
    
    **Bonus:** Full Flow - Menunjukkan keseluruhan halaman
    """)
    
    st.info("💡 Pilih section di sidebar untuk melihat detail setiap bagian halaman")

# ========================================
# SLIDE: HALAMAN LENGKAP
# ========================================
elif presentation_page == "📄 Halaman Lengkap":
    st.markdown('<div class="slide-title">📄 Struktur Halaman Aplikasi</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Gambaran Lengkap Halaman
    
    Halaman aplikasi terdiri dari beberapa bagian utama yang tersusun dari atas ke bawah:
    """)
    
    st.code("""
    ┌─────────────────────────────────────────────────┐
    │ HEADER                                          │
    │ 🎓 Student Performance Analytics Dashboard      │
    │ Deskripsi dan tips                              │
    └─────────────────────────────────────────────────┘
    
    ┌──────────────────┬────────────────────────────┐
    │                  │ SIDEBAR (3 TABS)           │
    │    MAIN CONTENT  │ • Filter Tab               │
    │                  │ • Visualization Tab        │
    │                  │ • About Tab                │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ METRICS (4 COLUMNS)  │   │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ VISUALIZATION GUIDE  │   │
    │                  │ │ (Expandable)         │   │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ CHARTS (2 ROWS)      │   │
    │                  │ │ • Histogram + Scatter│   │
    │                  │ │ • Bar + Heatmap      │   │
    │                  │ │ (Each with explanation)  │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ CONTAINERS           │   │
    │                  │ │ & STATISTICS         │   │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ DATA TABLE           │   │
    │                  │ │ (scrollable)         │   │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ ACTION BUTTONS       │   │
    │                  │ │ (3 tombol)           │   │
    │                  │ └──────────────────────┘   │
    │                  │                            │
    │                  │ ┌──────────────────────┐   │
    │                  │ │ STATUS INDICATORS    │   │
    │                  │ └──────────────────────┘   │
    └──────────────────┴────────────────────────────┘
    
    ┌─────────────────────────────────────────────────┐
    │ FOOTER                                          │
    │ Credits dan informasi tambahan                  │
    └─────────────────────────────────────────────────┘
    """, language="text")
    
    st.divider()
    
    st.subheader("⚡ Key Characteristics")
    
    characteristics = [
        ("Layout", "Wide layout dengan sidebar navigation (st.set_page_config)"),
        ("Responsiveness", "Columns yang adaptif sesuai screen size"),
        ("Interactivity", "Real-time update saat user mengubah filter"),
        ("Visual", "Plotly charts + custom CSS styling"),
        ("User Experience", "Expandable sections, clear labeling, helpful messages"),
        ("Performance", "Data caching dengan @st.cache_data"),
        ("Accessibility", "Clear color scheme, emoji icons, informative text"),
    ]
    
    for char, description in characteristics:
        st.markdown(f"""
        <div class="feature-item">
            <b>{char}:</b> {description}
        </div>
        """, unsafe_allow_html=True)

# ========================================
# SLIDE: SECTION 1 - HEADER
# ========================================
elif presentation_page == "📍 Section 1: Header":
    st.markdown('<div class="slide-title">📍 Section 1: Header & Introduction</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Header?
    
    Section ini adalah bagian paling atas halaman yang berfungsi sebagai **entry point** untuk user.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Komponen Header")
        st.markdown("""
        **Elemen yang ditampilkan:**
        
        1. **Title**
           - `st.title("🎓 Student Performance...")`
           - Emoji 🎓 untuk visual appeal
           - Font besar dan bold
        
        2. **Description**
           - `st.markdown("Analisis komprehensif...")`
           - Penjelasan singkat tentang aplikasi
        
        3. **Info Box**
           - `st.info("💡 Tips: Gunakan sidebar...")`
           - Memberikan hint kepada user
        
        4. **Divider**
           - `st.markdown("---")`
           - Pemisah visual
        """)
    
    with col2:
        st.subheader("💻 Kode Section Header")
        st.markdown("""
        ```python
        st.title("🎓 Student Performance Analytics Dashboard")
        st.markdown("Analisis komprehensif performa akademik siswa...")
        
        st.info("💡 **Tips:** Gunakan sidebar di sebelah kiri...")
        
        st.markdown("---")
        ```
        """)
    
    st.divider()
    
    st.subheader("🎯 Fungsi Section Header")
    
    functions = [
        ("Brand Identity", "Menampilkan judul dan identitas aplikasi"),
        ("User Guidance", "Memberikan tips tentang cara menggunakan aplikasi"),
        ("Visual Separation", "Memisahkan header dari section berikutnya"),
        ("First Impression", "User langsung tahu apa aplikasi ini"),
        ("Hierarchy", "Menunjukkan informasi paling penting di atas"),
    ]
    
    for func, description in functions:
        st.markdown(f"**{func}** - {description}")

# ========================================
# SLIDE: SECTION 2 - SIDEBAR
# ========================================
elif presentation_page == "🎛️ Section 2: Sidebar":
    st.markdown('<div class="slide-title">🎛️ Section 2: Sidebar Navigation & Filters</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Sidebar?
    
    Sidebar adalah panel di kiri yang berisi **filter controls** dan navigasi aplikasi.
    """)
    
    st.subheader("📐 Struktur Sidebar")
    
    st.code("""
    SIDEBAR
    ├── Header: 🎛️ Filter & Kontrol
    │
    ├── FILTER TAB
    │   ├── 1️⃣ Multi-select Features
    │   │   └── Pilih fitur numerik untuk analisis
    │   │
    │   ├── 2️⃣ Range Filter
    │   │   └── Slider untuk set min-max value
    │   │
    │   └── 3️⃣ Opsi Tampilan
    │       ├── Checkbox: Show Statistics
    │       ├── Checkbox: Highlight Outliers
    │       └── Checkbox: Show Correlation
    │
    ├── VISUALIZATION TAB
    │   ├── Chart Type Selector (Radio)
    │   │   ├── Distribution (Histogram)
    │   │   ├── Scatter Plot
    │   │   ├── Box Plot
    │   │   └── Bar Chart
    │   │
    │   └── Color By (Selectbox)
    │
    └── ABOUT TAB
        └── Dataset Information
    """, language="text")
    
    st.divider()
    
    st.subheader("🔧 Widget yang Digunakan")
    
    widgets_used = {
        "st.multiselect()": {
            "purpose": "Pilih multiple features",
            "example": "selected_features = st.multiselect('Pilih fitur...', numeric_features)",
            "return": "List of selected items"
        },
        "st.selectbox()": {
            "purpose": "Pilih single feature dari dropdown",
            "example": "feature_to_filter = st.selectbox('Pilih fitur...', numeric_features)",
            "return": "Single selected string"
        },
        "st.slider()": {
            "purpose": "Set range value untuk filter",
            "example": "min_val, max_val = st.slider('Range...', min_value=0, max_value=100)",
            "return": "Tuple (min, max)"
        },
        "st.checkbox()": {
            "purpose": "Toggle options on/off",
            "example": "show_stats = st.checkbox('Tampilkan Statistik', value=True)",
            "return": "Boolean True/False"
        },
        "st.radio()": {
            "purpose": "Pilih satu dari beberapa opsi",
            "example": "chart_type = st.radio('Tipe Chart:', ['Histogram', 'Scatter'])",
            "return": "Selected option string"
        },
        "st.tabs()": {
            "purpose": "Organize widgets dalam tabs",
            "example": "tab1, tab2, tab3 = st.sidebar.tabs(['Filter', 'Viz', 'About'])",
            "return": "Tab context managers"
        }
    }
    
    for widget_name, info in widgets_used.items():
        with st.expander(f"📌 {widget_name}"):
            st.write(f"**Purpose:** {info['purpose']}")
            st.write(f"**Example:** `{info['example']}`")
            st.write(f"**Return:** {info['return']}")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Sidebar")
    
    sidebar_functions = [
        ("User Input", "Mengumpulkan input dari user untuk filtering"),
        ("Data Control", "User bisa mengontrol data yang ditampilkan"),
        ("Space Efficiency", "Menu tidak mengambil space dari main content"),
        ("Organized UI", "Widget diorganisir dalam tabs untuk clarity"),
        ("Interactivity", "Setiap perubahan trigger data update otomatis"),
    ]
    
    for func, desc in sidebar_functions:
        st.markdown(f"- **{func}:** {desc}")

# ========================================
# SLIDE: SECTION 3 - METRICS
# ========================================
elif presentation_page == "📊 Section 3: Metrics":
    st.markdown('<div class="slide-title">📊 Section 3: Key Metrics Display</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Metrics?
    
    Section ini menampilkan **4 key metrics** dalam layout horizontal (columns).
    Metrics ter-update real-time saat user mengubah filter.
    """)
    
    st.subheader("📐 Struktur Metrics Section")
    
    st.code("""
    METRICS SECTION
    ├── Header: 📊 Key Metrics
    │
    └── 4 COLUMNS LAYOUT
        ├── Col 1: Metric 1
        │   ├── Label: Rata-rata [Feature 1]
        │   ├── Value: [calculated mean]
        │   └── Delta: [difference from original]
        │
        ├── Col 2: Metric 2
        │   ├── Label: Maksimum [Feature 2]
        │   └── Value: [calculated max]
        │
        ├── Col 3: Metric 3
        │   ├── Label: Minimum [Feature 3]
        │   └── Value: [calculated min]
        │
        └── Col 4: Metric 4
            ├── Label: Total Records
            ├── Value: [record count]
            └── Delta: [comparison with original]
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Implementation")
    
    st.code("""
# Buat 4 columns
col1, col2, col3, col4 = st.columns(4)

# Column 1: Mean
with col1:
    avg_val = filtered_df[numeric_cols[0]].mean()
    st.metric(
        label=f"Rata-rata {numeric_cols[0]}",
        value=f"{avg_val:.2f}",
        delta=f"{avg_val - df[numeric_cols[0]].mean():.2f}"
    )

# Column 2: Max
with col2:
    max_val = filtered_df[numeric_cols[1]].max()
    st.metric(label=f"Maksimum {numeric_cols[1]}", value=f"{max_val:.2f}")

# Column 3: Min
with col3:
    min_val = filtered_df[numeric_cols[2]].min()
    st.metric(label=f"Minimum {numeric_cols[2]}", value=f"{min_val:.2f}")

# Column 4: Count
with col4:
    total_records = len(filtered_df)
    st.metric(
        label="Total Records",
        value=f"{total_records:,}",
        delta=f"{total_records} dari {len(df)}"
    )
    """, language="python")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Metrics Section")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Visual Function:**
        - Quick view dari KPI utama
        - Eye-catching dengan layout columns
        - Clear labeling dengan emoji
        """)
    
    with col2:
        st.markdown("""
        **Data Function:**
        - Show summary statistics
        - Delta untuk compare filtered vs original
        - Real-time update saat filter berubah
        """)
    
    st.info("💡 Metrics adalah cara cepat user melihat impact dari filtering yang mereka lakukan")

# ========================================
# SLIDE: SECTION 4 - VISUALIZATION GUIDE
# ========================================
elif presentation_page == "📚 Section 4: Visualization Guide":
    st.markdown('<div class="slide-title">📚 Section 4: Panduan Membaca Visualisasi</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Visualization Guide?
    
    Section ini adalah **educational content** yang menjelaskan setiap jenis visualisasi
    agar user mengerti cara membaca chart dan apa artinya.
    """)
    
    st.subheader("📐 Struktur Visualization Guide")
    
    st.code("""
    VISUALIZATION GUIDE
    ├── st.expander("📚 Panduan Membaca...")
    │
    ├── COLUMN 1 & 2
    │   ├── 📊 Histogram Explanation
    │   │   ├── Apa itu?
    │   │   ├── Cara membaca
    │   │   ├── Interpretasi pola
    │   │   └── Digunakan untuk
    │   │
    │   └── 📍 Scatter Plot Explanation
    │       ├── Apa itu?
    │       ├── Cara membaca
    │       ├── Interpretasi korelasi
    │       └── Digunakan untuk
    │
    ├── COLUMN 3 & 4
    │   ├── 📦 Box Plot Explanation
    │   └── 🔥 Heatmap Explanation
    │
    ├── DIVIDER
    │
    └── TIPS SECTION
        ├── Best Practices (5 tips)
        └── Hal yang Perlu Diperhatikan (7 warnings)
    """, language="text")
    
    st.divider()
    
    st.subheader("📝 Konten Setiap Penjelasan")
    
    explanation_structure = {
        "Histogram": [
            "Apa itu - Menampilkan distribusi frekuensi",
            "Cara Membaca - Bar tinggi = banyak data",
            "Interpretasi Pola - Normal, skewed, bimodal",
            "Digunakan untuk - Deteksi outlier, pola distribusi",
        ],
        "Scatter Plot": [
            "Apa itu - Relasi antar 2 variabel",
            "Cara Membaca - Titik rapat = korelasi kuat",
            "Trendline - Menunjukkan arah hubungan",
            "Korelasi Values - Dari -1 hingga +1",
        ],
        "Box Plot": [
            "Komponen - Q1, Median, Q3, Whisker, Outlier",
            "Interpretasi - Box = 50% data tengah",
            "Digunakan untuk - Deteksi outlier, perbandingan grup",
        ],
        "Heatmap": [
            "Skala Warna - Hijau (positif) hingga Merah (negatif)",
            "Interpretasi - Warna gelap = korelasi kuat",
            "Penting - Korelasi ≠ Kausalitas",
        ]
    }
    
    for chart_type, contents in explanation_structure.items():
        with st.expander(f"📌 {chart_type}"):
            for content in contents:
                st.write(f"• {content}")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Section Ini")
    
    st.markdown("""
    **Educational:**
    - Mengajar user cara membaca chart
    - Memberikan konteks untuk interpretasi
    - Prevent misinterpretation
    
    **User Experience:**
    - Expandable = user bisa buka/tutup sesuai kebutuhan
    - Clear dan comprehensive explanations
    - Tips & warnings untuk best practices
    
    **Value Add:**
    - Membuat dashboard lebih dari sekedar data display
    - Menjadi learning tool yang edukatif
    - Meningkatkan trust kepada analisis
    """)

# ========================================
# SLIDE: SECTION 5 - CHARTS
# ========================================
elif presentation_page == "📈 Section 5: Charts & Visualizations":
    st.markdown('<div class="slide-title">📈 Section 5: Visualisasi Data Interaktif</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Charts?
    
    Section ini menampilkan **4 visualisasi interaktif** dalam layout 2 rows × 2 columns.
    Setiap chart dilengkapi dengan expandable explanation.
    """)
    
    st.subheader("📐 Struktur Charts Section")
    
    st.code("""
    CHARTS SECTION
    ├── Row 1: Distribution & Relationship
    │   ├── COL 1: Histogram/Distribution
    │   │   ├── st.plotly_chart()
    │   │   ├── Expandable Explanation
    │   │   ├── Statistics (mean, median, std dev)
    │   │   └── Interpretation Guide
    │   │
    │   └── COL 2: Scatter Plot
    │       ├── st.plotly_chart()
    │       ├── Expandable Explanation
    │       ├── Correlation Value
    │       └── Automatic Interpretation
    │
    └── Row 2: Comparison & Correlation
        ├── COL 3: Bar Chart (Mean ± Std Dev)
        │   ├── st.plotly_chart()
        │   ├── Expandable Explanation
        │   └── Mean Comparison
        │
        └── COL 4: Heatmap Correlation
            ├── st.plotly_chart()
            ├── Expandable Explanation
            ├── Color Scale Guide
            └── Correlation Matrix
    """, language="text")
    
    st.divider()
    
    st.subheader("📊 4 Tipe Visualisasi")
    
    tab_viz = st.tabs(["Histogram", "Scatter", "Bar Chart", "Heatmap"])
    
    with tab_viz[0]:
        st.markdown("""
        ### 📊 Histogram (Distribution)
        
        **Code:**
        ```python
        fig1 = px.histogram(
            filtered_df,
            x=feature1,
            nbins=30,
            title=f"Distribution of {feature1}",
            color_discrete_sequence=['#667eea']
        )
        st.plotly_chart(fig1, use_container_width=True)
        ```
        
        **Keunggulan Plotly:**
        - Interactive (hover untuk melihat value)
        - Zoom dan pan capability
        - Download chart sebagai PNG
        - Responsive dan smooth
        """)
    
    with tab_viz[1]:
        st.markdown("""
        ### 📍 Scatter Plot (Relationship)
        
        **Code:**
        ```python
        fig2 = px.scatter(
            filtered_df,
            x=feature1,
            y=feature2,
            title=f"Scatter: {feature1} vs {feature2}",
            trendline="ols",  # Ordinary Least Squares
            color_discrete_sequence=['#764ba2']
        )
        st.plotly_chart(fig2, use_container_width=True)
        ```
        
        **Special Feature:**
        - Trendline dengan OLS regression
        - Menunjukkan arah hubungan dengan garis merah
        - User bisa hover untuk melihat koordinat titik
        """)
    
    with tab_viz[2]:
        st.markdown("""
        ### 📊 Bar Chart (Comparison)
        
        **Code:**
        ```python
        comparison_df = filtered_df[selected_features].describe().T
        fig3 = px.bar(
            comparison_df.reset_index(),
            x='index',
            y='mean',
            error_y='std',
            title="Mean ± Std Dev"
        )
        st.plotly_chart(fig3, use_container_width=True)
        ```
        
        **Feature Penting:**
        - Error bar menunjukkan standard deviation
        - Bar membandingkan mean antar variabel
        - Visual untuk uncertainty quantification
        """)
    
    with tab_viz[3]:
        st.markdown("""
        ### 🔥 Heatmap (Correlation Matrix)
        
        **Code:**
        ```python
        corr_matrix = filtered_df[selected_features].corr()
        fig4 = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='Viridis',
            text=corr_matrix.values.round(2),
            texttemplate='%{text}'
        ))
        st.plotly_chart(fig4, use_container_width=True)
        ```
        
        **Feature Penting:**
        - Menampilkan semua korelasi sekaligus
        - Angka di tengah cell untuk presisi
        - Color scale intuitif (hijau=positif, merah=negatif)
        """)
    
    st.divider()
    
    st.subheader("💡 Expandable Explanations")
    
    st.markdown("""
    Setiap chart memiliki expandable explanation yang berisi:
    
    ✅ **Variabel yang ditampilkan** - Clear labeling
    ✅ **Apa yang dilihat** - User bisa melihat apa di chart
    ✅ **Statistik relevant** - Mean, median, std dev, etc
    ✅ **Interpretasi** - Penjelasan tentang hasil
    ✅ **Context** - Kapan digunakan, apa artinya
    
    Ini membuat chart menjadi **self-explanatory** dan educational!
    """)

# ========================================
# SLIDE: SECTION 6 - CONTAINERS
# ========================================
elif presentation_page == "📦 Section 6: Containers & Statistics":
    st.markdown('<div class="slide-title">📦 Section 6: Containers & Advanced Statistics</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Containers?
    
    Section ini menggunakan **Streamlit containers** untuk menampilkan statistik
    dan insights dengan layout yang rapi.
    """)
    
    st.subheader("📐 Struktur Section")
    
    st.code("""
    CONTAINERS & STATISTICS
    ├── Header: 📦 Advanced Layouts
    │
    ├── CONTAINER 1: Statistics
    │   ├── Description: "Container digunakan untuk mengelompokkan elemen"
    │   │
    │   └── 2 COLUMNS
    │       ├── COL 1: Statistik Deskriptif
    │       │   ├── Mean, Median, Std Dev
    │       │   ├── Min, Max, 25%, 50%, 75%
    │       │   └── Displayed sebagai DataFrame
    │       │
    │       └── COL 2: Data Type Summary
    │           ├── Count per data type
    │           ├── Object, Float, Integer, etc
    │           └── Quick overview struktur data
    │
    └── EXPANDER: Insights Detail
        ├── Ukuran Pemusatan & Penyebaran
        │   └── Mean, Median, Std Dev per feature
        │
        └── Nilai Ekstrem
            └── Min, Max, Range per feature
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Implementation")
    
    code_col1, code_col2 = st.columns(2)
    
    with code_col1:
        st.markdown("**Container Syntax:**")
        st.code("""
with st.container():
    st.subheader("Container Example")
    st.write("Ini dalam container")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Left column")
    with col2:
        st.write("Right column")
        """, language="python")
    
    with code_col2:
        st.markdown("**Expander Syntax:**")
        st.code("""
with st.expander("Click to expand"):
    st.write("Hidden content")
    st.dataframe(df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Content 1")
    with col2:
        st.write("Content 2")
        """, language="python")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Section Containers")
    
    st.markdown("""
    **Organizational:**
    - Mengelompokkan elemen yang related
    - Visual grouping dengan background color
    - Clear hierarchy
    
    **Space Efficiency:**
    - Expandable untuk save screen real estate
    - User bisa buka hanya yang mereka butuhkan
    - Prevent information overload
    
    **User Experience:**
    - Organized layout yang mudah dipahami
    - Progressive disclosure (detail di expander)
    - Easy to scan
    """)

# ========================================
# SLIDE: SECTION 7 - DATA TABLE
# ========================================
elif presentation_page == "📋 Section 7: Data Table":
    st.markdown('<div class="slide-title">📋 Section 7: Data Table & Column Selection</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Data Table?
    
    Section ini menampilkan **data lengkap dalam format tabel** dengan
    dynamic column selection dan pagination.
    """)
    
    st.subheader("📐 Struktur Section")
    
    st.code("""
    DATA TABLE
    ├── Header: 📋 Data Table & Export
    │   └── Menampilkan: X records dari Y total
    │
    ├── Column Selection
    │   └── st.multiselect() - User pilih kolom mana saja
    │
    ├── Data Table
    │   ├── st.dataframe()
    │   ├── Pagination otomatis (50 rows per page)
    │   ├── Sortable columns
    │   ├── Copy functionality
    │   └── Height: 400px
    │
    └── Data Info Expander
        ├── Shape (rows, columns)
        └── Memory usage (KB)
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Implementation")
    
    st.code("""
# Column Selector
available_cols = filtered_df.columns.tolist()
display_cols = st.multiselect(
    'Pilih kolom untuk ditampilkan:',
    available_cols,
    default=available_cols[:5]  # Default 5 kolom pertama
)

# Display DataFrame
if display_cols:
    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True,
        height=400  # Scrollable
    )
    
    # Data Info Expander
    with st.expander("ℹ️ Data Info"):
        st.write(f"Shape: {filtered_df[display_cols].shape}")
        st.write(f"Memory usage: {filtered_df[display_cols].memory_usage(deep=True).sum() / 1024:.2f} KB")
    """, language="python")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Data Table Section")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **User Control:**
        - User bisa pilih kolom yang mau dilihat
        - Reduce visual clutter
        - Focus pada data yang relevant
        """)
    
    with col2:
        st.markdown("""
        **Data Exploration:**
        - Raw data viewing capability
        - Scrollable dan sortable
        - Easy inspection
        
        **Download:**
        - Foundation untuk export functionality
        """)

# ========================================
# SLIDE: SECTION 8 - ACTIONS
# ========================================
elif presentation_page == "🎯 Section 8: Interactive Actions":
    st.markdown('<div class="slide-title">🎯 Section 8: Interactive Buttons & Actions</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Actions?
    
    Section ini berisi **3 interactive buttons** yang memungkinkan user
    untuk melakukan aksi terhadap data.
    """)
    
    st.subheader("📐 Struktur Section")
    
    st.code("""
    INTERACTIVE ACTIONS
    ├── Header: 🎯 Interactive Features
    │
    └── 3 COLUMNS LAYOUT
        ├── COL 1: Reset Filters Button
        │   ├── Label: 🔄 Reset All Filters
        │   ├── Type: primary (blue)
        │   └── Action: st.rerun() → refresh halaman
        │
        ├── COL 2: Show Summary Button
        │   ├── Label: 📊 Show Data Summary
        │   ├── Type: secondary
        │   ├── Action 1: st.balloons() → animation
        │   └── Action 2: st.success() → show summary
        │
        └── COL 3: Download Button
            ├── Label: 📥 Download CSV
            ├── Type: secondary
            ├── Data: filtered_df as CSV
            └── Action: Browser download
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Setiap Button")
    
    button_tabs = st.tabs(["Reset Button", "Summary Button", "Download Button"])
    
    with button_tabs[0]:
        st.markdown("""
        ### 🔄 Reset Filters Button
        
        ```python
        if st.button("🔄 Reset All Filters", type="primary"):
            st.rerun()
        ```
        
        **Fungsi:**
        - Reset semua filter ke default
        - Refresh page state
        - Return ke view original
        
        **User Benefit:**
        - Quick reset tanpa manual
        - Eksplorasi dari awal lagi
        - Convenient untuk banyak iterasi
        """)
    
    with button_tabs[1]:
        st.markdown("""
        ### 📊 Show Summary Button
        
        ```python
        if st.button("📊 Show Data Summary"):
            st.balloons()  # Animation
            st.success(f'''
            **Summary Statistics:**
            - Total Records: {len(filtered_df):,}
            - Numeric Features: {len(numeric_cols)}
            - Memory Usage: {memory_usage} KB
            ''')
        ```
        
        **Fungsi:**
        - Display quick summary
        - Show celebration animation
        - Provide key statistics
        
        **User Experience:**
        - Fun dengan balloons
        - Quick overview dari filtered data
        - Motivational feedback
        """)
    
    with button_tabs[2]:
        st.markdown("""
        ### 📥 Download CSV Button
        
        ```python
        if display_cols:
            csv = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="student_performance_filtered.csv",
                mime="text/csv"
            )
        ```
        
        **Fungsi:**
        - Export filtered data
        - Download sebagai CSV
        - Untuk analisis lebih lanjut
        
        **User Benefit:**
        - Take data dengan mereka
        - Use di Excel, Python, dll
        - Preserve filtered view
        """)
    
    st.divider()
    
    st.subheader("🎯 Fungsi Section Actions")
    
    st.markdown("""
    **Interactivity:**
    - Buttons membuat dashboard interactive
    - User bisa control data flow
    - Responsive to user intent
    
    **Utility:**
    - Reset: Explore dari awal
    - Summary: Quick insight
    - Download: Data export
    
    **User Engagement:**
    - Actionable elements
    - Clear purpose untuk setiap button
    - Emojis untuk visual clarity
    """)

# ========================================
# SLIDE: SECTION 9 - STATUS
# ========================================
elif presentation_page == "⏳ Section 9: Status & Indicators":
    st.markdown('<div class="slide-title">⏳ Section 9: Data Quality Indicators</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Status?
    
    Section ini menampilkan **data quality indicators** dan status messages
    untuk inform user tentang kondisi data mereka.
    """)
    
    st.subheader("📐 Struktur Section")
    
    st.code("""
    DATA QUALITY & STATUS
    ├── Header: ⏳ Data Quality & Status
    │
    └── 2 COLUMNS
        ├── COL 1: Data Completeness
        │   ├── Label: "Data Completeness"
        │   ├── st.progress() - Visual bar (0-100%)
        │   └── Text: "X.X% completeness"
        │
        └── COL 2: Data Status
            └── Conditional Messages
                ├── IF len(filtered_df) == 0:
                │   └── st.error("Tidak ada data...")
                │
                ├── ELIF len(filtered_df) < 10:
                │   └── st.warning("Data sangat sedikit...")
                │
                ├── ELIF len(filtered_df) / len(df) < 0.5:
                │   └── st.info("Menampilkan X records...")
                │
                └── ELSE:
                    └── st.success("Menampilkan X records")
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Implementation")
    
    code_col1, code_col2 = st.columns(2)
    
    with code_col1:
        st.markdown("**Completeness Calculation:**")
        st.code("""
completeness = (1 - (
    filtered_df.isnull().sum().sum() / 
    (filtered_df.shape[0] * filtered_df.shape[1])
)) * 100

st.subheader("Data Completeness")
st.progress(completeness / 100)
st.write(f"Completeness: {completeness:.1f}%")
        """, language="python")
    
    with code_col2:
        st.markdown("**Status Messages:**")
        st.code("""
if len(filtered_df) == 0:
    st.error("⚠️ No data matches filter")
elif len(filtered_df) < 10:
    st.warning("⚡ Very few records")
elif len(filtered_df) / len(df) < 0.5:
    st.info(f"📊 Showing {len(filtered_df):,}")
else:
    st.success(f"✅ Showing {len(filtered_df):,}")
        """, language="python")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Status Section")
    
    st.markdown("""
    **Data Quality Awareness:**
    - User tahu data completeness
    - Progress bar visual
    - Conditional warnings jika ada masalah
    
    **User Guidance:**
    - Error: Tahu saat tidak ada data
    - Warning: Alert saat data terlalu sedikit
    - Info: Neutral info
    - Success: Positive confirmation
    
    **Trust Building:**
    - Transparency tentang data state
    - Clear status messages
    - Prevent misleading analysis
    """)

# ========================================
# SLIDE: SECTION 10 - FOOTER
# ========================================
elif presentation_page == "👣 Section 10: Footer & Info":
    st.markdown('<div class="slide-title">👣 Section 10: Footer & Sidebar Info</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Apa itu Section Footer?
    
    Section ini adalah **closing section** yang berisi credits, info, dan
    next steps untuk user.
    """)
    
    st.subheader("📐 Struktur Section")
    
    st.code("""
    FOOTER
    ├── Divider: st.markdown("---")
    │
    ├── HTML Footer
    │   ├── Title: 🎓 Student Performance Analytics Dashboard
    │   ├── Subtitle: Session 3 | Bootcamp | Day 2
    │   └── Dataset info: StudentPerformanceFactors.csv
    │
    └── SIDEBAR: Learned Features
        ├── Divider
        ├── Header: 📚 Fitur Yang Sudah Dipelajari
        ├── Checklist (13 items):
        │   ├── ✅ Text Input & Multiselect
        │   ├── ✅ Slider & Range Filter
        │   ├── ✅ Checkbox & Radio Button
        │   ├── ... (13 items total)
        │   └── ✅ Custom CSS Styling
        │
        └── Next Section Info
            └── Preview untuk Session 4
    """, language="text")
    
    st.divider()
    
    st.subheader("💻 Kode Implementation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Footer HTML:**")
        st.code("""
st.markdown('''
<div style='text-align: center; color: #888; 
            padding: 20px;'>
    <p><strong>
    🎓 Student Performance Analytics
    </strong></p>
    <p>Session 3: Streamlit Basics
    Bootcamp Data Science | Day 2
    </p>
    <p style='font-size: 12px;'>
    Dataset: StudentPerformanceFactors.csv
    </p>
</div>
''', unsafe_allow_html=True)
        """, language="python")
    
    with col2:
        st.markdown("**Sidebar Info:**")
        st.code("""
with st.sidebar:
    st.markdown("---")
    st.subheader("📚 Fitur Dipelajari")
    st.write('''
    ✅ Text Input & Multiselect
    ✅ Slider & Range Filter
    ✅ Checkbox & Radio Button
    ✅ Sidebar Tabs
    ... (13 items)
    ''')
    
    st.info("💡 Next: Session 4...")
        """, language="python")
    
    st.divider()
    
    st.subheader("🎯 Fungsi Footer Section")
    
    st.markdown("""
    **Information:**
    - Memberikan context (program, session, dataset)
    - Credit dan attribution
    - Professional appearance
    
    **Learning Summary:**
    - Menunjukkan apa yang sudah dipelajari
    - Validation untuk user
    - Progress tracking
    
    **Next Steps:**
    - Preview untuk session berikutnya
    - Keep user engaged
    - Clear learning path
    """)

# ========================================
# SLIDE: FULL FLOW
# ========================================
elif presentation_page == "🔄 Full Flow":
    st.markdown('<div class="slide-title">🔄 Full Page Flow & Interaction</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Keseluruhan Flow Halaman
    
    Ini adalah diagram lengkap tentang bagaimana user berinteraksi dengan halaman
    dan bagaimana data mengalir dari top ke bottom.
    """)
    
    st.subheader("📊 User Interaction Flow")
    
    st.code("""
USER BUKA APLIKASI
        ↓
   LIHAT HEADER
   (Title + Tips)
        ↓
USER UBAH FILTER DI SIDEBAR
   • Pilih features (multiselect)
   • Set range (slider)
   • Toggle options (checkbox)
        ↓
DATA DIFILTER (REAL-TIME)
   • filtered_df = df.copy()
   • Apply multiselect filter
   • Apply range filter
   • Apply checkbox conditions
        ↓
METRICS TERUPDATE (AUTO)
   • Calculate mean, max, min
   • Display dalam 4 columns
   • Show delta from original
        ↓
USER LIHAT VISUALIZATION GUIDE
   • Expand untuk baca penjelasan
   • Understand chart types
        ↓
USER LIHAT 4 CHARTS
   • Histogram (distribusi)
   • Scatter (relasi)
   • Bar (perbandingan)
   • Heatmap (korelasi)
   • Setiap chart expandable
        ↓
USER LIHAT STATISTICS
   • Container dengan stats
   • Expandable insights
        ↓
USER LIHAT DATA TABLE
   • Select kolom (multiselect)
   • Lihat raw data
   • Scrollable & sortable
        ↓
USER CLICK BUTTON
   ├─ Reset → st.rerun()
   ├─ Summary → st.balloons() + info
   └─ Download → Save CSV
        ↓
USER LIHAT STATUS
   • Progress bar (completeness)
   • Status message (success/warn)
        ↓
USER LIHAT FOOTER
   • Credits & info
   • Learned features
   • Next session
        ↓
USER UBAH FILTER LAGI
   • Kembali ke sidebar
   • Semua update otomatis
   • Loop terus...
    """, language="text")
    
    st.divider()
    
    st.subheader("💾 Data Processing Pipeline")
    
    st.code("""
LOAD DATA (@st.cache_data)
        ↓
    df (Original)
        ↓
COPY DATA
        ↓
    filtered_df = df.copy()
        ↓
APPLY FILTERS
   ├─ Multiselect features
   ├─ Range slider
   └─ Checkbox options
        ↓
    filtered_df (Filtered)
        ↓
PROCESS FOR DISPLAY
   ├─ Calculate metrics
   ├─ Create visualizations
   ├─ Generate statistics
   └─ Format for table
        ↓
DISPLAY TO USER
   ├─ Metrics
   ├─ Charts
   ├─ Table
   └─ Status
        ↓
USER INTERACTION
   └─ Back to sidebar
    """, language="text")
    
    st.divider()
    
    st.subheader("🎨 Visual Layout Hierarchy")
    
    st.markdown("""
    ```
    FULL WIDTH
    ┌───────────────────────────────────────┐
    │ HEADER (Title + Intro)                │
    └───────────────────────────────────────┘
    
    SIDEBAR (Left 20%)  +  MAIN (Right 80%)
    ┌──────────────────┬──────────────────┐
    │ FILTERS          │ METRICS (4 cols) │
    │ • Multiselect    │                  │
    │ • Slider         │ ┌──┬──┬──┬──┐   │
    │ • Checkbox       │ │M1│M2│M3│M4│   │
    │                  │ └──┴──┴──┴──┘   │
    │ VIZ OPTIONS      │                  │
    │ • Radio          │ VIZ GUIDE        │
    │ • Selectbox      │ (Expandable)     │
    │                  │                  │
    │ ABOUT            │ CHARTS (2×2)     │
    │ • Info           │ ┌──────┬──────┐  │
    │                  │ │ Hist │Scatter│ │
    │                  │ ├──────┼──────┤  │
    │                  │ │ Bar  │Heatmap│ │
    │                  │ └──────┴──────┘  │
    │                  │                  │
    │                  │ CONTAINERS       │
    │                  │                  │
    │                  │ DATA TABLE       │
    │                  │                  │
    │                  │ BUTTONS (3)      │
    │                  │                  │
    │                  │ STATUS           │
    └──────────────────┴──────────────────┘
    
    FULL WIDTH
    ┌───────────────────────────────────────┐
    │ FOOTER (Credits)                      │
    └───────────────────────────────────────┘
    ```
    """)
    
    st.divider()
    
    st.subheader("🎯 Key Points dari Full Flow")
    
    points = [
        ("Real-time Updates", "Setiap perubahan filter langsung ter-reflect di semua chart dan metrics"),
        ("Responsive Design", "Layout adaptif (sidebar + main, columns, containers)"),
        ("Progressive Disclosure", "Expandables untuk detail, main content always visible"),
        ("User Control", "User bisa filter, select columns, download, reset sesuai kebutuhan"),
        ("Educational", "Built-in explanations dan guides untuk setiap chart"),
        ("Data Caching", "@st.cache_data untuk performance optimization"),
        ("Accessibility", "Clear labeling, emoji icons, color-coded messages"),
        ("Feedback", "Status messages, progress bars, balloons animation"),
    ]
    
    for i, (point, description) in enumerate(points, 1):
        st.markdown(f"**{i}. {point}** - {description}")

st.divider()
st.markdown("""
<div style='text-align: center; color: #888; padding: 20px;'>
    <p><strong>Presentasi Halaman - Student Performance Analytics Dashboard</strong></p>
    <p>Session 3: Streamlit Basics | Bootcamp Data Science | Day 2</p>
</div>
""", unsafe_allow_html=True)
