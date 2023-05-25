from django.forms import ModelForm
from .models import LodgeForum, Discussion
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateInForum(ModelForm):
    class Meta:
        model = LodgeForum
        fields = "__all__"


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
