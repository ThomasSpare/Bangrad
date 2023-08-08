from .models import Profile
from django.forms import ModelForm
from .models import LodgeForum, Discussion, Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateInForum(forms.ModelForm):
    class Meta:
        model = LodgeForum
        fields = ['body', 'topic', 'description', 'link', 'image']
    
    def __init__(self, *args, **kwargs):
            super(CreateInForum, self).__init__(*args, **kwargs)
        
            self.fields['topic'].widget.attrs={'class': 'form-control'}
            self.fields['description'].widget.attrs={'class': 'form-control'}
            self.fields['link'].widget.attrs={'class': 'form-control'}
            self.fields['image'].widget.attrs={'class': 'form-control'}



class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
            super(CreateInDiscussion, self).__init__(*args, **kwargs)

            self.fields['forum'].widget.attrs={'class': 'form-control'}
            self.fields['discuss'].widget.attrs={'class': 'form-control'}


