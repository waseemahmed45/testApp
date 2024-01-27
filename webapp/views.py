# webApp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DummyRecord
from .serializers import DummyRecordSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DummyRecordForm

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