# Main_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Main_app/home.html', {'username': request.user.username})

