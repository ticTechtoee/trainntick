from django.http import HttpResponse
from django.shortcuts import render

# home function the is representation of the "Home" Page on the website.

def home(request):
    return render(request, 'home/home.html')
