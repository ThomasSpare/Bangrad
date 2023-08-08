from django.forms import ModelForm
from SPOTIPY_APP.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
            super(CreateInDiscussion, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs={'class': 'form-control'}
            self.fields['email'].widget.attrs={'class': 'form-control'}
            self.fields['password1'].widget.attrs={'class': 'form-control'}
            self.fields['password2'].widget.attrs={'class': 'form-control'}


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
            super(UserUpdateForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs={'class': 'form-control'}
            self.fields['email'].widget.attrs={'class': 'form-control'}
        

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'image', 'email',
                'website_url', 'spotify_artist', 'instagram', 'facebook',
                'twitter', 'mixcloud', 'soundcloud', 'youtube', 'link_1',
                'link_2' 
                ]
        
        def __init__(self, *args, **kwargs):
            super(ProfileUpdateForm, self).__init__(*args, **kwargs)

            self.fields['image'].widget.attrs={'class': 'form-control'}
            self.fields['bio'].widget.attrs={'class': 'form-control'}
            self.fields['firstname'].widget.attrs={'class': 'form-control'}
            self.fields['lastname'].widget.attrs={'class': 'form-control'}
            self.fields['website_url'].widget.attrs={'class': 'form-control'}
            self.fields['spotify_artist'].widget.attrs={'class': 'form-control'}
            self.fields['instagram'].widget.attrs={'class': 'form-control'}
            self.fields['facebook'].widget.attrs={'class': 'form-control'}
            self.fields['twitter'].widget.attrs={'class': 'form-control'}
            self.fields['mixcloud'].widget.attrs={'class': 'form-control'}
            self.fields['soundcloud'].widget.attrs={'class': 'form-control'}
            self.fields['youtube'].widget.attrs={'class': 'form-control'}
            self.fields['link_1'].widget.attrs={'class': 'form-control'}
            self.fields['link_2'].widget.attrs={'class': 'form-control'}