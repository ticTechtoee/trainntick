from django.http import HttpResponse


# home function the is representation of the "Home" Page on the website.

def home(request):
    return HttpResponse('Hello and welcome to the Home Page')
