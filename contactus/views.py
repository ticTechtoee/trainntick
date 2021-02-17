from django.http import HttpResponse
from django.shortcuts import render

# Contact function the is representation of the "Contact Us" Page on the website.

def contact(request):
    return render(request, 'contactus/contactus.html')
