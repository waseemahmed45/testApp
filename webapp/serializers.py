# webApp/serializers.py

from rest_framework import serializers
from .models import DummyRecord

class DummyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyRecord
        fields = ['name', 'description']
