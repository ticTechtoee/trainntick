from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Contact function the is representation of the "Contact Us" Page on the website.

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # send and email

        send_mail(
            'Testing of First Django App' + name, # subject
            message, # message
            email, # from the user
            ['udofficial10@gmail.com'], # to email
        )

        return render(request, 'contactus/contactus.html', {'name': name})
    else:
        return render(request, 'contactus/contactus.html')
