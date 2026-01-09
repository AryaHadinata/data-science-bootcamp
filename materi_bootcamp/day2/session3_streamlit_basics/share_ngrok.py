#!/usr/bin/env python3
"""
Script untuk share aplikasi Streamlit menggunakan pyngrok
Install dulu: pip install pyngrok
Atau setup manual ngrok dari https://ngrok.com
"""

import subprocess
import time
import sys
from pathlib import Path

print("=" * 70)
print(" SHARE APLIKASI STREAMLIT KE INTERNET")
print("=" * 70)

# Cek apakah Streamlit masih berjalan
print("\n✓ Pastikan Streamlit sudah running di terminal lain")
print("  Terminal: streamlit run app_part1.py")
print("\n" + "-" * 70)

try:
    # Coba import pyngrok
    try:
        from pyngrok import ngrok, conf
        print("\n1. pyngrok ditemukan - menggunakan pyngrok")
    except ImportError:
        print("\n1. Installing pyngrok...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyngrok", "-q"])
        from pyngrok import ngrok, conf

    # Set ngrok auth token jika ada (opsional)
    # ngrok.set_auth_token("YOUR_TOKEN")
    
    print("2. Membuat tunnel ke port 8501...")
    time.sleep(1)
    
    # Buat tunnel
    public_url = ngrok.connect(8501)
    print(f"\n✓ TUNNEL BERHASIL DIBUAT!")
    print("=" * 70)
    print(f"\n🌐 SHARE URL INI KE ORANG LAIN:\n")
    print(f"   {public_url}\n")
    print("=" * 70)
    print("\nInfo Tunnel:")
    tunnels = ngrok.get_tunnels()
    for tunnel in tunnels:
        print(f"  - {tunnel.name}: {tunnel.public_url}")
    
    print("\n✓ Tekan CTRL+C untuk menghentikan tunnel")
    print("-" * 70 + "\n")
    
    # Keep running
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n✓ Tunnel dihentikan.")
    ngrok.kill()
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nAlternatif: Download ngrok manual dari https://ngrok.com/download")
    print("Kemudian jalankan: ngrok http 8501")
