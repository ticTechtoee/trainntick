from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import auth


# home function the is representation of the "SignUp" Page on the website.

def dash(request):
    if request.user.is_authenticated:
        name = request.user.username
        return render(request, 'dashboard/home.html', {'name': name})
    else:
        name = "None"
        return render(request, 'dashboard/home.html', {'name': name})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
