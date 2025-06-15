from django.core.management.base import BaseCommand
import requests
from cryptoapp.models import CryptoPrice

class Command(BaseCommand):
    help = 'Fetch current crypto price from CoinGecko and save to DB'

    def handle(self, *args, **kwargs):
        coin = "bitcoin"
        currency = "usd"
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            price = data[coin][currency]

            # Simpan ke database
            CryptoPrice.objects.create(coin=coin, price=price)
            self.stdout.write(self.style.SUCCESS(f"✅ Harga {coin.upper()}: {price} {currency.upper()} disimpan ke DB"))

            # Alert
            if price > 70000:
                self.stdout.write(self.style.WARNING("🚀 ALERT: Harga BTC melewati 70K USD"))
            elif price < 60000:
                self.stdout.write(self.style.WARNING("📉 ALERT: Harga BTC di bawah 60K USD"))

        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f"❌ Gagal mengambil data: {e}"))
