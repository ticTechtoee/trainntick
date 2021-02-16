from django.http import HttpResponse

# Contact function the is representation of the "Contact Us" Page on the website.

def contact(request):
    return HttpResponse('Hello')