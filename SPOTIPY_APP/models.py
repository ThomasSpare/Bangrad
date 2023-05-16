from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import spotipy


class BangradSearchFields(forms.Form):
    Key = forms.CharField(max_length=2, required=False) 
    Tempo = forms.IntegerField(max_length=3, required=False)
    Language = models.CharField(max_length=20, required=False)
    Release_year = forms.DateField(widget=forms.SelectDateWidget, required=False)

    def __str__(self):
        return self.title
