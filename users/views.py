from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, template_name="index.html")

def login(request):
    return render(request, template_name="login.html")

def register(request):
    return render(request, template_name="register.html")