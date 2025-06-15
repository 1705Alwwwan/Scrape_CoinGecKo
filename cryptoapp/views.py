from django.shortcuts import render
from .models import CryptoPrice
import json

def dashboard(request):
    data = CryptoPrice.objects.filter(coin="bitcoin").order_by('-timestamp')[:30]
    data = data[::-1]  # urut dari lama ke baru
    labels = [d.timestamp.strftime("%Y-%m-%d %H:%M") for d in data]
    prices = [d.price for d in data]
    return render(request, 'dashboard.html', {
        'labels': json.dumps(labels),
        'prices': json.dumps(prices),
    })
