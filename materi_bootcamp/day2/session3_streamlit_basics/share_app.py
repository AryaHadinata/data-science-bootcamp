import subprocess
import time
import webbrowser
from urllib.request import urlopen
import json

print("=" * 60)
print("Membuat tunnel dengan ngrok untuk share aplikasi Streamlit")
print("=" * 60)

# Download ngrok jika belum ada
import os
import zipfile
from urllib.request import urlretrieve

ngrok_path = r"C:\ngrok\ngrok.exe"
if not os.path.exists(ngrok_path):
    print("\n1. Download ngrok...")
    os.makedirs(r"C:\ngrok", exist_ok=True)
    try:
        urlretrieve(
            'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-windows-amd64.zip',
            r'C:\ngrok\ngrok.zip'
        )
        print("   ✓ Download selesai")
        
        print("2. Extract ngrok...")
        with zipfile.ZipFile(r'C:\ngrok\ngrok.zip', 'r') as zip_ref:
            zip_ref.extractall(r'C:\ngrok')
        print("   ✓ Extract selesai")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        print("\n   Alternatif: Download manual dari https://ngrok.com/download")
        exit(1)

print("\n3. Menjalankan ngrok tunnel...")
print("-" * 60)

try:
    # Jalankan ngrok
    process = subprocess.Popen([ngrok_path, 'http', '8501'])
    time.sleep(3)
    
    # Dapatkan URL publik dari API ngrok
    try:
        response = urlopen('http://localhost:4040/api/tunnels')
        data = json.loads(response.read().decode())
        tunnels = data['tunnels']
        
        for tunnel in tunnels:
            if tunnel['proto'] == 'https':
                public_url = tunnel['public_url']
                print(f"\n✓ BERHASIL! Aplikasi Anda dapat diakses di:")
                print(f"\n   🌐 {public_url}")
                print(f"\n   (Copy dan bagikan URL ini ke orang lain)")
                print("\n" + "-" * 60)
                print("Tekan CTRL+C untuk menghentikan tunnel")
                print("-" * 60 + "\n")
                break
    except:
        print("Tunnel sedang dibuat... Aplikasi dapat diakses di:")
        print("http://localhost:8501 (lokal)")
    
    # Keep process running
    process.wait()
    
except KeyboardInterrupt:
    print("\n\nTunnel dihentikan.")
except Exception as e:
    print(f"Error: {e}")
