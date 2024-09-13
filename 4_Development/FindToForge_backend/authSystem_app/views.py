# auth_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page of Main_app
    else:
        form = LoginForm()
    return render(request, 'authSystem_app/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authSystem_app/register.html', {'form': form})

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('login')
