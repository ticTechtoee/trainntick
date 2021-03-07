from django.db import models


# A Model to Save the User's Details.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)

