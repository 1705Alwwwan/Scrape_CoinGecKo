from django.db import models

class CryptoPrice(models.Model):
    coin = models.CharField(max_length=50)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coin} - {self.price} USD @ {self.timestamp}"
