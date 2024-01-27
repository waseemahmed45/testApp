# webApp/urls.py

from django.urls import path
from .views import home, DummyRecordList, add_dummy_record, edit_dummy_record, delete_dummy_record

urlpatterns = [
    path('', home, name='home'),
    path('api/dummy-records/', DummyRecordList.as_view(), name='dummy-record-list'),
    path('add', add_dummy_record, name='add-dummy-record'),
    path('edit/<int:pk>/', edit_dummy_record, name='edit-dummy-record'),
    path('delete/<int:pk>/', delete_dummy_record, name='delete-dummy-record'),
    # ... other URLs ...
]
