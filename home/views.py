from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# home function the is representation of the "Home" Page on the website.

def home(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['re_pass']:
            try:
                user = User.objects.get(username = request.POST['name'])
                return render(request, 'home/home.html', {'error':'Username Already Exists'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['name'], password=request.POST['pass'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'home/home.html', {'error': 'Password does not match'})

    else:
        return render(request, 'home/home.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['name'], password = request.POST['pass'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'home/login.html', {'error': 'Username and Password Must Match in Any Case'})

    else:
        return render(request, 'home/login.html')