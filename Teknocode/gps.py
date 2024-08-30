# gps.py
import serial
import threading
import requests
from PyQt5.QtWidgets import QLabel

def accident_gps(app_window):
    def read_gps():
        try:
            # Port adını ve ayarları kontrol edin
            serialGPS = serial.Serial('COM3', 9600, timeout=1)
            while True:
                if serialGPS.in_waiting > 0:
                    line = serialGPS.readline().decode('ascii', errors='replace')
                    if line.startswith('$GNRMC'):
                        parts = line.split(',')
                        if len(parts) > 3 and parts[2] == 'A':
                            latitude = float(parts[3]) / 100
                            longitude = float(parts[5]) / 100
                            latitude_str = "{:.6f}".format(latitude)
                            longitude_str = "{:.6f}".format(longitude)
                            
                            # GPS verilerini GUI'ye güncelle
                            app_window.ui.gps_label.setText(f"Enlem: {latitude_str}, Boylam: {longitude_str}")
                            # WhatsApp mesajı gönder
                            send_whatsapp_message(latitude_str, longitude_str)
        except Exception as e:
            print(f"GPS verisi okuma hatası: {e}")

    # GPS okumayı ayrı bir thread'de çalıştır
    gps_thread = threading.Thread(target=read_gps)
    gps_thread.daemon = True
    gps_thread.start()

def send_whatsapp_message(latitude, longitude):
    # WhatsApp mesajı göndermek için uygun API detaylarını buraya ekleyin
    url = "https://api.whatsapp.com/send"
    token = "YOUR_WHATSAPP_API_TOKEN"  # Buraya gerçek token'ınızı koyun
    phone_numbers = ["+1234567890", "+0987654321"]  # Alıcı numaralarını buraya ekleyin

    message = f"Konum: Enlem: {latitude}, Boylam: {longitude}"
    
    for number in phone_numbers:
        response = requests.post(
            url,
            data={"phone": number, "text": message},
            headers={"Authorization": f"Bearer {token}"}
        )
        if response.status_code == 200:
            print(f"Mesaj {number} numarasına gönderildi")
        else:
            print(f"Mesaj {number} numarasına gönderilemedi")
