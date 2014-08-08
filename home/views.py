from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login

from home.models import Home

def index(request):
    return render(request, 'home/index.html')

def detail(request):
	return render(request, 'home/rules.html')




    

