import tkinter as tk
import requests

def hava_durumu_goster(sehir):
    try:
        api_key = "24a069ced6e6f36f62c51347a553cc02"  # OpenWeatherMap API key'inizi buraya ekleyin
        url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "404":
            hava_durumu_etiketi.config(text="Şehir bulunamadı.")
        else:
            hava_durumu = f"Hava Durumu: {data['weather'][0]['description']}\nSıcaklık: {data['main']['temp']}°C"
            hava_durumu_etiketi.config(text=hava_durumu)
    except Exception as e:
        hava_durumu_etiketi.config(text=f"Bir hata oluştu: {str(e)}")

def sehir_sec(*args):
    sehir = sehirler.get()
    if sehir:
        hava_durumu_goster(sehir)
    else:
        hava_durumu_etiketi.config(text="Lütfen bir şehir seçin.")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hava Durumu")

# Widget'ları oluştur
label_baslik = tk.Label(root, text="Şehir Seçin ve Hava Durumunu Görüntüleyin", font=("Helvetica", 14))
label_sehir = tk.Label(root, text="Şehir:")
sehirler = tk.StringVar(root)
sehirler.set("İstanbul")  # Varsayılan şehir
option_menu_sehirler = tk.OptionMenu(root, sehirler, "İstanbul", "Ankara", "İzmir", "Antalya", "Bursa")

# Hava durumu bilgilerini göstermek için etiket
hava_durumu_etiketi = tk.Label(root, text="", font=("Helvetica", 12), justify="left")

# Widget'ları yerleştir
label_baslik.grid(row=0, column=0, columnspan=2, pady=10)
label_sehir.grid(row=1, column=0, padx=10)
option_menu_sehirler.grid(row=1, column=1, padx=10)
hava_durumu_etiketi.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# Seçenek menüsü değiştiğinde hava durumunu güncelle
sehirler.trace_add("write", sehir_sec)
hava_durumu_goster("istanbul")  # Varsayılan şehir için hava durumunu göster

# Pencereyi başlat
root.mainloop()
