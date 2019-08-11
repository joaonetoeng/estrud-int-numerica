from django.shortcuts import render, redirect
from django.contrib.auth import logout



def home(request):
    return render(request, 'home.html')

def admin(request):
    return render(request, 'admin.html')

def pilares(request):
    return render(request, 'pilares.html')

def my_logout(request):
    logout(request)
    return redirect('home')