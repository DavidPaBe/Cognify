from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Eliminar la parte de restaurantes
def index(request):
    return render(request, 'index.html')

