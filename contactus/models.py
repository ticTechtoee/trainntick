from django.db import models

# A Model to get the Query From Customer.
class Query(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=25)
    query = models.TextField()