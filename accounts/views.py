# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html' 


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to your actual home view
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(request.POST)
        print('Is form valid?', form.is_valid())
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("login")
                login(request, user)
                return redirect('home')  # Change 'home' to your actual home view
            else:
                # Authentication failed
                print('Authentication failed for user:', username)
                form.add_error(None, 'Invalid login credentials')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')
