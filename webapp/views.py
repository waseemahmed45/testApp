# webApp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DummyRecord
from .serializers import DummyRecordSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DummyRecordForm
import requests

class DummyRecordList(APIView):
    def get(self, request, format=None):
        dummy_records = DummyRecord.objects.all()
        serializer = DummyRecordSerializer(dummy_records, many=True)
        return Response(serializer.data)

def home(request):
    dummy_records = DummyRecord.objects.all()
    return render(request, 'webApp/home.html', {'dummy_records': dummy_records})


def add_dummy_record(request):
    if request.method == 'POST':
        form = DummyRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DummyRecordForm()
    return render(request, 'webApp/add.html', {'form': form})

def edit_dummy_record(request, pk):
    dummy_record = get_object_or_404(DummyRecord, pk=pk)
    if request.method == 'POST':
        form = DummyRecordForm(request.POST, instance=dummy_record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DummyRecordForm(instance=dummy_record)
    return render(request, 'webApp/edit.html', {'form': form, 'dummy_record': dummy_record})

def delete_dummy_record(request, pk):
    dummy_record = get_object_or_404(DummyRecord, pk=pk)
    if request.method == 'POST':
        dummy_record.delete()
        return redirect('home')
    return render(request, 'webApp/delete.html', {'dummy_record': dummy_record})

def yahoo_stock(request, symbol):
    
    # Yahoo Finance API endpoint
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d'

    # Make a GET request to Yahoo Finance API
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        
        try:
            timestamp = data['chart']['result'][0]['timestamp']
            quote = data['chart']['result'][0]['indicators']['quote'][0]

            details = {
                'symbol': symbol,
                'market_cap': '',  # Update this based on the actual data structure
                'last_close': quote['close'][0],
                'open_price': quote['open'][0],
                'high_price': quote['high'][0],
                'low_price': quote['low'][0],
                'volume': quote['volume'][0],
            }

            return render(request, 'webApp/stock.html', details)
        except KeyError as e:
            return render(request, 'webApp/stock.html', {'error': f'Failed to extract stock details. KeyError: {e}'})
    else:

        # Handle the case where the request to Yahoo Finance failed
        return render(request, 'webApp/stock.html', {'error': 'Failed to fetch stock data from Yahoo Finance'})