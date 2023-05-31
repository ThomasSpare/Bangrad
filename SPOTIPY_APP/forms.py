from .models import Profile
from django.forms import ModelForm
from .models import LodgeForum, Discussion, Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateInForum(forms.ModelForm):
    class Meta:
        model = LodgeForum
        fields = "__all__"


class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
