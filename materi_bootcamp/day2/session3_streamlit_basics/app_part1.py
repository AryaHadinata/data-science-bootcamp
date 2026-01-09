"""
Session 3: Streamlit Basics - Part 1
Dashboard Analisis Performa Siswa

Fokus: Layout, Widgets, Metrics, Visualisasi Chart
Durasi: 120 menit
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np

# ========================================
# PAGE CONFIG
# ========================================
st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ========================================
# LOAD DATA
# ========================================
@st.cache_data
def load_data():
    """Load Student Performance data"""
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    data_path = project_root / 'datasets' / 'StudentPerformanceFactors.csv'

    if not data_path.exists():
        st.error(f"Dataset not found at {data_path}")
        st.stop()

    df = pd.read_csv(data_path)
    return df

df = load_data()

# Data cleaning
df = df.dropna()
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# ========================================
# HEADER
# ========================================
st.title("🎓 Student Performance Analytics Dashboard")
st.markdown("Analisis komprehensif performa akademik siswa dengan interaktivitas penuh")

# Info message
st.info("💡 **Tips:** Gunakan sidebar di sebelah kiri untuk mengatur filter dan visualisasi")

st.markdown("---")

# ========================================
# SIDEBAR WIDGETS
# ========================================
st.sidebar.header("🎛️ Filter & Kontrol")

# Tab untuk organisir widget
tab1, tab2, tab3 = st.sidebar.tabs(["Filter", "Visualisasi", "Tentang"])

with tab1:
    st.subheader("1️⃣ Filter Data")
    
    # Get numeric columns untuk slider
    numeric_features = [col for col in numeric_cols if col not in ['StudentID']]
    
    # Multi-select for numeric columns
    selected_features = st.multiselect(
        'Pilih fitur numerik untuk analisis:',
        numeric_features,
        default=numeric_features[:3]
    )
    
    # Slider untuk filter nilai
    if numeric_features:
        st.subheader("2️⃣ Range Filter")
        feature_to_filter = st.selectbox(
            'Pilih fitur untuk di-filter:',
            numeric_features
        )
        
        min_val, max_val = st.slider(
            f'Range {feature_to_filter}:',
            min_value=float(df[feature_to_filter].min()),
            max_value=float(df[feature_to_filter].max()),
            value=(float(df[feature_to_filter].min()), float(df[feature_to_filter].max())),
            step=0.5
        )
    
    # Checkbox
    st.subheader("3️⃣ Opsi Tampilan")
    show_statistics = st.checkbox('Tampilkan Statistik Detail', value=True)
    show_outliers = st.checkbox('Highlight Outliers', value=False)
    show_correlation = st.checkbox('Tampilkan Correlation Matrix', value=True)

with tab2:
    st.subheader("📈 Pilihan Visualisasi")
    
    chart_type = st.radio(
        "Tipe Chart Utama:",
        ["Distribution (Histogram)", "Scatter Plot", "Box Plot", "Bar Chart"]
    )
    
    color_by = st.selectbox(
        'Warna berdasarkan:',
        [col for col in df.columns if df[col].dtype == 'object']
    )

with tab3:
    st.write("**Tentang Dataset:**")
    st.info(f"""
    📊 **Student Performance Factors**
    - Total Records: {len(df):,}
    - Total Features: {len(df.columns)}
    - Numeric Features: {len(numeric_cols)}
    """)

# ========================================
# APPLY FILTERS
# ========================================
filtered_df = df.copy()

if 'feature_to_filter' in locals() and 'min_val' in locals():
    filtered_df = filtered_df[
        (filtered_df[feature_to_filter] >= min_val) &
        (filtered_df[feature_to_filter] <= max_val)
    ]

# ========================================
# LAYOUT: METRICS
# ========================================
st.header("📊 Key Metrics")
st.write("**Contoh penggunaan `st.columns()` untuk layout horizontal**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_val = filtered_df[numeric_cols[0]].mean()
    st.metric(
        label=f"Rata-rata {numeric_cols[0]}",
        value=f"{avg_val:.2f}",
        delta=f"{avg_val - df[numeric_cols[0]].mean():.2f}"
    )

with col2:
    max_val = filtered_df[numeric_cols[1]].max()
    st.metric(
        label=f"Maksimum {numeric_cols[1]}",
        value=f"{max_val:.2f}"
    )

with col3:
    min_val = filtered_df[numeric_cols[2]].min()
    st.metric(
        label=f"Minimum {numeric_cols[2]}",
        value=f"{min_val:.2f}"
    )

with col4:
    total_records = len(filtered_df)
    st.metric(
        label="Total Records",
        value=f"{total_records:,}",
        delta=f"{total_records} dari {len(df)}"
    )

st.markdown("---")

# ========================================
# VISUALIZATIONS & GUIDE
# ========================================
st.header("📈 Visualisasi Data")

# Visualization Guide
with st.expander("📚 Panduan Membaca Visualisasi Data", expanded=False):
    st.subheader("🎯 Jenis-jenis Visualisasi Data")
    
    guide_col1, guide_col2 = st.columns(2)
    
    with guide_col1:
        st.markdown("""
        ### 📊 Histogram (Distribution)
        **Apa itu?**
        - Menampilkan distribusi frekuensi dari satu variabel numerik
        - Sumbu X: Rentang nilai | Sumbu Y: Jumlah frekuensi
        
        **Cara membaca:**
        - Bar tinggi = banyak data di rentang tersebut
        - Bar rendah = sedikit data di rentang tersebut
        - Puncak = nilai yang paling sering muncul (mode)
        
        **Apa yang bisa diketahui?**
        ✓ Bentuk distribusi (normal, skewed, bimodal)
        ✓ Nilai paling umum
        ✓ Penyebaran data
        ✓ Keberadaan outlier
        
        **Contoh penggunaan:**
        - Analisis distribusi nilai ujian siswa
        - Melihat pola umum dari satu variabel
        """)
    
    with guide_col2:
        st.markdown("""
        ### 📍 Scatter Plot
        **Apa itu?**
        - Menampilkan relasi antara DUA variabel numerik
        - Setiap titik = satu data point
        - Sumbu X & Y = dua variabel berbeda
        
        **Cara membaca:**
        - Titik berkumpul rapat = korelasi kuat
        - Titik tersebar = korelasi lemah
        - Pola naik = korelasi positif
        - Pola turun = korelasi negatif
        
        **Apa yang bisa diketahui?**
        ✓ Hubungan antar variabel
        ✓ Kekuatan korelasi
        ✓ Outlier atau anomali
        ✓ Trend atau pola
        
        **Contoh penggunaan:**
        - Hubungan waktu belajar vs nilai ujian
        - Relasi umur vs performa
        """)
    
    guide_col3, guide_col4 = st.columns(2)
    
    with guide_col3:
        st.markdown("""
        ### 📦 Box Plot
        **Apa itu?**
        - Menampilkan distribusi & outlier dari data
        - Box = 50% data tengah (Q1-Q3)
        - Garis di tengah = median (Q2)
        - Whisker = batas data normal
        - Titik terpisah = outlier
        
        **Komponen:**
        - Bawah whisker = minimum data normal
        - Q1 (bawah box) = 25% data
        - Median (garis) = 50% data
        - Q3 (atas box) = 75% data
        - Atas whisker = maksimum data normal
        - Titik = nilai ekstrem (outlier)
        
        **Apa yang bisa diketahui?**
        ✓ Median & kuartil
        ✓ Penyebaran data
        ✓ Kehadiran outlier
        ✓ Simetri distribusi
        
        **Contoh penggunaan:**
        - Membandingkan performa antar grup
        - Deteksi outlier otomatis
        """)
    
    with guide_col4:
        st.markdown("""
        ### 🔥 Heatmap Correlation
        **Apa itu?**
        - Menampilkan korelasi antara SEMUA variabel numerik
        - Warna = kekuatan korelasi
        - Angka = nilai korelasi (-1 sampai +1)
        
        **Interpretasi warna:**
        - 🟢 Hijau/biru terang = korelasi positif kuat (+1)
        - 🟡 Kuning = korelasi lemah (~0)
        - 🔴 Ungu/merah = korelasi negatif kuat (-1)
        
        **Nilai korelasi:**
        - +1 = hubungan positif sempurna
        - +0.5 = hubungan positif sedang
        - 0 = tidak ada hubungan
        - -0.5 = hubungan negatif sedang
        - -1 = hubungan negatif sempurna
        
        **Apa yang bisa diketahui?**
        ✓ Variabel yang saling berkaitan
        ✓ Multikolinearitas (variabel sangat mirip)
        ✓ Feature engineering opportunities
        
        **Contoh penggunaan:**
        - Analisis multi-variabel
        - Feature selection
        """)
    
    st.divider()
    
    st.subheader("💡 Tips Analisis Data")
    
    tips_col1, tips_col2 = st.columns(2)
    
    with tips_col1:
        st.info("""
        **Best Practices:**
        1. Selalu lihat histogram terlebih dahulu
        2. Gunakan scatter untuk eksplorasi hubungan
        3. Box plot untuk deteksi outlier
        4. Heatmap untuk multi-variabel analysis
        5. Perhatikan ukuran sampel data
        6. Cross-check dengan statistik deskriptif
        """)
    
    with tips_col2:
        st.warning("""
        **Hal yang Perlu Diperhatikan:**
        ⚠️ Outlier bisa ada karena error atau data unik
        ⚠️ Korelasi ≠ Kausalitas
        ⚠️ Ukuran sampel mempengaruhi interpretasi
        ⚠️ Skala berbeda bisa misleading
        ⚠️ Perlu context domain expertise
        ⚠️ Visualisasi statis vs dinamis
        """)

st.markdown("---")

if 'selected_features' in locals() and selected_features:
    # Row 1: Distribution charts
    viz_col1, viz_col2 = st.columns(2)
    
    with viz_col1:
        st.subheader("📊 Distribution Chart (Histogram)")
        feature1 = selected_features[0]
        
        if chart_type == "Distribution (Histogram)":
            fig1 = px.histogram(
                filtered_df,
                x=feature1,
                nbins=30,
                title=f"Distribution of {feature1}",
                color_discrete_sequence=['#667eea']
            )
        elif chart_type == "Box Plot":
            fig1 = px.box(
                filtered_df,
                y=feature1,
                title=f"Box Plot - {feature1}",
                color_discrete_sequence=['#667eea']
            )
        else:
            fig1 = px.histogram(
                filtered_df,
                x=feature1,
                nbins=30,
                title=f"Distribution of {feature1}",
                color_discrete_sequence=['#667eea']
            )
        
        st.plotly_chart(fig1, use_container_width=True)
        
        # Explanation
        with st.expander("ℹ️ Interpretasi Chart Ini", expanded=False):
            st.write(f"""
            **Variabel yang ditampilkan:** {feature1}
            
            📌 **Apa yang dilihat:**
            - Bar menunjukkan frekuensi nilai dalam rentang tertentu
            - Tinggi bar = jumlah data di rentang tersebut
            - Pola menunjukkan bentuk distribusi data
            
            📊 **Statistik:**
            - Mean (Rata-rata): {filtered_df[feature1].mean():.2f}
            - Median (Tengah): {filtered_df[feature1].median():.2f}
            - Std Dev (Variasi): {filtered_df[feature1].std():.2f}
            - Min: {filtered_df[feature1].min():.2f}
            - Max: {filtered_df[feature1].max():.2f}
            
            💡 **Apa yang bisa disimpulkan:**
            - Jika bar tinggi di satu titik → data terkonsentrasi
            - Jika bar menyebar merata → data tersebar luas
            - Jika ada gap → kemungkinan ada dua kelompok data
            """)
    
    with viz_col2:
        st.subheader("📈 Scatter Analysis")
        if len(selected_features) >= 2:
            feature2 = selected_features[1]
            fig2 = px.scatter(
                filtered_df,
                x=feature1,
                y=feature2,
                title=f"Scatter: {feature1} vs {feature2}",
                trendline="ols",
                color_discrete_sequence=['#764ba2']
            )
            st.plotly_chart(fig2, use_container_width=True)
            
            # Explanation
            with st.expander("ℹ️ Interpretasi Chart Ini", expanded=False):
                correlation = filtered_df[[feature1, feature2]].corr().iloc[0, 1]
                st.write(f"""
                **Variabel yang dibandingkan:**
                - X-axis: {feature1}
                - Y-axis: {feature2}
                
                📌 **Apa yang dilihat:**
                - Setiap titik = satu data point
                - Garis merah = trend/arah hubungan
                - Titik semakin rapat = hubungan lebih kuat
                
                📊 **Korelasi:**
                - Nilai Korelasi: {correlation:.3f}
                
                💡 **Interpretasi:**
                """)
                
                if correlation > 0.7:
                    st.success("✅ **Korelasi POSITIF KUAT** - Saat {feature1} naik, {feature2} juga naik")
                elif correlation > 0.3:
                    st.info("📊 **Korelasi POSITIF SEDANG** - Ada hubungan positif tapi tidak terlalu kuat")
                elif correlation > -0.3:
                    st.warning("⚪ **Korelasi LEMAH** - Hubungan tidak jelas atau hampir tidak ada")
                elif correlation > -0.7:
                    st.info("📊 **Korelasi NEGATIF SEDANG** - Ada hubungan negatif tapi tidak terlalu kuat")
                else:
                    st.error("❌ **Korelasi NEGATIF KUAT** - Saat {feature1} naik, {feature2} turun")
        else:
            st.info("⚠️ Pilih minimal 2 fitur untuk scatter plot")
    
    # Row 2: Comparison
    st.subheader("🔄 Perbandingan Fitur")
    viz_col3, viz_col4 = st.columns(2)
    
    with viz_col3:
        if len(selected_features) >= 2:
            # Comparison chart
            comparison_df = filtered_df[selected_features].describe().T
            fig3 = px.bar(
                comparison_df.reset_index(),
                x='index',
                y='mean',
                error_y='std',
                title="Mean ± Std Dev",
                labels={'index': 'Features', 'mean': 'Mean Value'},
                color_discrete_sequence=['#f093fb']
            )
            st.plotly_chart(fig3, use_container_width=True)
            
            # Explanation
            with st.expander("ℹ️ Interpretasi Chart Ini", expanded=False):
                st.write("""
                **Apa yang ditampilkan:**
                - Bar = Nilai rata-rata (mean) setiap fitur
                - Error bar (garis vertikal) = Standar deviasi
                
                📌 **Cara membaca:**
                - Bar lebih tinggi = nilai rata-rata lebih besar
                - Error bar panjang = data lebih tersebar (variasi besar)
                - Error bar pendek = data lebih konsisten (variasi kecil)
                
                💡 **Apa yang bisa disimpulkan:**
                - Perbandingan skala antar fitur
                - Konsistensi setiap fitur
                - Fitur mana yang paling stabil
                """)
    
    with viz_col4:
        if show_correlation and len(selected_features) >= 2:
            # Correlation heatmap
            corr_matrix = filtered_df[selected_features].corr()
            fig4 = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='Viridis',
                text=corr_matrix.values.round(2),
                texttemplate='%{text}',
                textfont={"size": 10}
            ))
            fig4.update_layout(title="Correlation Matrix", height=500)
            st.plotly_chart(fig4, use_container_width=True)
            
            # Explanation
            with st.expander("ℹ️ Interpretasi Chart Ini", expanded=False):
                st.write("""
                **Apa yang ditampilkan:**
                - Korelasi antara SEMUA pasangan fitur
                - Warna = kekuatan korelasi
                - Angka = nilai korelasi eksak
                
                📌 **Skala warna:**
                - 🟢 Hijau/Terang = Korelasi POSITIF (+1 = perfect positive)
                - 🟡 Kuning = Korelasi LEMAH (~0 = no relation)
                - 🔴 Ungu/Gelap = Korelasi NEGATIF (-1 = perfect negative)
                
                💡 **Tips interpretasi:**
                - Fokus pada warna gelap (korelasi kuat)
                - Diagonal selalu = 1 (variabel dengan dirinya sendiri)
                - Matriks simetris (X vs Y = Y vs X)
                
                ⚠️ **Penting:** Korelasi ≠ Kausalitas!
                Dua variabel bisa berkorelasi tapi tidak saling mempengaruhi.
                """)

st.markdown("---")

# ========================================
# LAYOUT: CONTAINERS
# ========================================
st.header("📦 Advanced Layouts")

# Container
with st.container():
    st.subheader("Container Example")
    st.write("Container digunakan untuk mengelompokkan elemen dengan rapi")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Statistik Deskriptif:**")
        stats_df = filtered_df[numeric_cols].describe().round(2)
        st.dataframe(stats_df, use_container_width=True)

    with col2:
        st.write("**Data Type Summary:**")
        dtype_count = pd.DataFrame({
            'Data Type': [str(t) for t in filtered_df.dtypes],
            'Column': filtered_df.columns
        }).groupby('Data Type').size().reset_index(name='Count')
        st.dataframe(dtype_count, use_container_width=True)

st.markdown("---")

# Expander
with st.expander("📖 Lihat Insights Detail"):
    st.subheader("Statistical Summary")
    
    col_exp1, col_exp2 = st.columns(2)
    
    with col_exp1:
        st.write("**Ukuran Pemusatan & Penyebaran:**")
        for col in numeric_cols[:3]:
            st.write(f"""
            **{col}**
            - Mean: {filtered_df[col].mean():.2f}
            - Median: {filtered_df[col].median():.2f}
            - Std Dev: {filtered_df[col].std():.2f}
            """)
    
    with col_exp2:
        st.write("**Nilai Ekstrem:**")
        for col in numeric_cols[:3]:
            st.write(f"""
            **{col}**
            - Min: {filtered_df[col].min():.2f}
            - Max: {filtered_df[col].max():.2f}
            - Range: {filtered_df[col].max() - filtered_df[col].min():.2f}
            """)

st.markdown("---")

# ========================================
# DATA TABLE
# ========================================
st.header("📋 Data Table & Export")
st.write(f"Menampilkan **{len(filtered_df):,}** records dari total **{len(df):,}** records")

# Column selector
available_cols = filtered_df.columns.tolist()
display_cols = st.multiselect(
    'Pilih kolom untuk ditampilkan:',
    available_cols,
    default=available_cols[:5]
)

if display_cols:
    # Display dataframe dengan pagination
    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True,
        height=400
    )
    
    # Data info
    with st.expander("ℹ️ Data Info"):
        st.write(f"Shape: {filtered_df[display_cols].shape}")
        st.write(f"Memory usage: {filtered_df[display_cols].memory_usage(deep=True).sum() / 1024:.2f} KB")

st.markdown("---")

# ========================================
# BUTTONS & INTERACTIVE ACTIONS
# ========================================
st.header("🎯 Interactive Features")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Reset All Filters", type="primary"):
        st.rerun()

with col2:
    if st.button("📊 Show Data Summary"):
        st.balloons()
        st.success(f"""
        **Summary Statistics:**
        - Total Records: {len(filtered_df):,}
        - Numeric Features: {len(numeric_cols)}
        - Memory Usage: {filtered_df.memory_usage(deep=True).sum() / 1024:.2f} KB
        """)

with col3:
    # Download button
    if display_cols:
        csv = filtered_df[display_cols].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="student_performance_filtered.csv",
            mime="text/csv"
        )

st.markdown("---")

# ========================================
# PROGRESS & STATUS MESSAGES
# ========================================
st.header("⏳ Data Quality & Status")

col_prog1, col_prog2 = st.columns(2)

with col_prog1:
    st.subheader("Data Completeness")
    completeness = (1 - (filtered_df.isnull().sum().sum() / (filtered_df.shape[0] * filtered_df.shape[1]))) * 100
    st.progress(completeness / 100)
    st.write(f"Data Completeness: {completeness:.1f}%")

with col_prog2:
    st.subheader("Data Status")
    if len(filtered_df) == 0:
        st.error("⚠️ Tidak ada data yang sesuai dengan filter")
    elif len(filtered_df) < 10:
        st.warning("⚡ Data yang ditampilkan sangat sedikit")
    elif len(filtered_df) / len(df) < 0.5:
        st.info(f"📊 Menampilkan {len(filtered_df):,} dari {len(df):,} records")
    else:
        st.success(f"✅ Menampilkan {len(filtered_df):,} records")

st.markdown("---")

# ========================================
# FOOTER
# ========================================
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p><strong>🎓 Student Performance Analytics Dashboard</strong></p>
        <p>Session 3: Streamlit Basics | Bootcamp Data Science | Day 2</p>
        <p style='font-size: 12px;'>Dataset: StudentPerformanceFactors.csv</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar info
with st.sidebar:
    st.markdown("---")
    st.subheader("📚 Fitur Yang Sudah Dipelajari")
    st.write("""
    ✅ Text Input & Multiselect
    ✅ Slider & Range Filter
    ✅ Checkbox & Radio Button
    ✅ Sidebar Tabs
    ✅ Columns Layout
    ✅ Containers & Expanders
    ✅ Metrics
    ✅ Plotly Charts (Histogram, Scatter, Heatmap)
    ✅ Data Table dengan Column Selection
    ✅ Download Button
    ✅ Progress Bar
    ✅ Status Messages
    ✅ Custom CSS Styling
    """)

    st.info("💡 **Next:** Session 4 akan menambahkan fitur advanced seperti Caching, Real-time Updates, dan Deployment!")

