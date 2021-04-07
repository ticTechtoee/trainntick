from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')



# home function the is representation of the "SignUp" Page on the website.

def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['re_pass']:
            try:
                user = User.objects.get(username = request.POST['name'])
                return render(request, 'accounts/signup.html', {'error':'Username Already Exists'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['name'], password=request.POST['pass'])
                auth.login(request,user)
                return redirect('dashboard')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password does not match'})

    else:
        return render(request, 'accounts/signup.html')

# Login fucntion is the representation of the "Login page" on the website.

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['name'], password = request.POST['pass'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard/home.html')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and Password Must Match in Any Case'})

    else:
        return render(request, 'accounts/login.html')