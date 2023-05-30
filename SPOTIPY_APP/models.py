from PIL import Image
from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import spotipy

# Search fields on home page


class BangradSearchFields(models.Model):
    key = models.CharField(max_length=10)
    tempo = models.IntegerField()
    language = models.CharField(max_length=20)
    release_year = models.DateField()

    def __str__(self):
        return self.key


# Lodge Forum parent model
class LodgeForum(models.Model):
    name = models.CharField(max_length=200, default='anonymous')
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)


# Lodge child model
class Discussion(models.Model):
    forum = models.ForeignKey(
        LodgeForum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)


# Model to create user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'
