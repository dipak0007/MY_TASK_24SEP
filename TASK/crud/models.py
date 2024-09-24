from django.db import models

# Create your models here.

class My_Details(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
