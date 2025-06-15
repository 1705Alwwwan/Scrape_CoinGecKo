import requests
from .models import CryptoPrice

def fetch_price(coin="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        price = data[coin][currency]

        # Simpan ke database
        CryptoPrice.objects.create(coin=coin, price=price)

        # Sistem alert
        if price > 70000:
            print("🚀 ALERT: Harga BTC melewati 70K USD")
        elif price < 60000:
            print("📉 ALERT: Harga BTC di bawah 60K USD")

        return price
    else:
        print(f"❌ Gagal mengambil data. Status code: {res.status_code}")
        return None
