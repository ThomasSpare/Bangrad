from django.forms import ModelForm
from SPOTIPY_APP.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from SPOTIPY_APP.forms import CreateInDiscussion


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
                'password1': forms.TextInput(attrs={'class': 'form-control'}),
                'password2': forms.TextInput(attrs={'class': 'form-control'}),
                }


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
            super(UserUpdateForm, self).__init__(*args, **kwargs)

            widgets = {     
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image', 'email',
                'website_url', 'spotify_artist', 'instagram', 'facebook',
                'twitter', 'mixcloud', 'soundcloud', 'youtube', 'link_1',
                'link_2' 
                ]
                
        widgets = {
        # 'image': forms.ImageField(attrs={'class': 'form-control'}),
        'bio': forms.Textarea(attrs={'class': 'form-control'}),
        'firstname': forms.TextInput(attrs={'class': 'form-control'}),
        'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        'website_url': forms.TextInput(attrs={'class': 'form-control'}),
        'spotify_artist': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram': forms.TextInput(attrs={'class': 'form-control'}),
        'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        'twitter': forms.TextInput(attrs={'class': 'form-control'}),
        'mixcloud': forms.TextInput(attrs={'class': 'form-control'}),
        'soundcloud': forms.TextInput(attrs={'class': 'form-control'}),
        'youtube': forms.TextInput(attrs={'class': 'form-control'}),
        'link_1': forms.TextInput(attrs={'class': 'form-control'}),
        'link_2': forms.TextInput(attrs={'class': 'form-control'}),
        }