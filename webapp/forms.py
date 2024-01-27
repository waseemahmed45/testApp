# webApp/forms.py

from django import forms
from .models import DummyRecord

class DummyRecordForm(forms.ModelForm):
    class Meta:
        model = DummyRecord
        fields = ['name', 'description']
