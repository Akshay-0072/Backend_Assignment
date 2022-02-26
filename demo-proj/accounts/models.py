
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    company_name = models.CharField(max_length=70)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.CharField(max_length=255)
    