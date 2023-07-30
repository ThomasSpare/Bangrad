from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import spotipy
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy

# Search fields on home page


class BangradSearchFields(models.Model):
    key = models.CharField(max_length=10)
    tempo = models.IntegerField()
    language = models.CharField(max_length=20)
    release_year = models.DateField()

    def __str__(self):
        return self.key


# Lodge parent model
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
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to='profile_pics')
    # profile_pic = models.ImageField(null=True, upload_to='profile_pics')
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    spotify_artist = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    mixcloud = models.CharField(max_length=255, null=True, blank=True)
    soundcloud = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    link_1 = models.CharField(max_length=255, null=True, blank=True)
    link_2 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'self.s})



        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            # Save it again and override the larger image
            img.save(self.image.path)
            
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Profile.objects.create(user=instance)
