# accounts/urls.py
from django.urls import path
from .views import register, user_login
from .views import CustomPasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),


]
