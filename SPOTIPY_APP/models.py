from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class BangradSearchFields(models.Model):
    key = models.CharField(max_length=10)
    tempo = models.IntegerField(max_length=10)
    language = models.CharField(max_length=20)
    release_year = models.DateField()

      
    def __str__(self):
        return self.key