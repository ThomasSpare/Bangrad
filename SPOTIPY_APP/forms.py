from .models import Profile
from django.forms import ModelForm
from .models import LodgeForum, Discussion, Profile
from django.forms import MultiWidget, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import LodgeForum


class CreateInForum(forms.ModelForm):
    class Meta:
        model = LodgeForum
        fields = ['topic', 'description', 'body', 'link']
    
    def __init__(self, *args, **kwargs):
        super(CreateInForum, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs = {'class': 'form-control'}
        self.fields['description'].widget.attrs = {'class': 'form-control'}
        self.fields['body'].widget.attrs = {'class': 'CKEditorWidget', 'rows': 4}
        self.fields['link'].widget.attrs = {'class': 'form-control'}
    
    def clean_link(self):                       # Validates if the user link provided
        link = self.cleaned_data['link']
        if link and not link.startswith(('http://', 'https://')):
            raise forms.ValidationError(
                ("Invalid link. Please provide a valid URL starting with 'http://' or 'https://'"))
        return link



class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['forum', 'discuss', 'name']
        success_url = "lodge.html"
    
    def __init__(self, *args, **kwargs):
            super(CreateInDiscussion, self).__init__(*args, **kwargs)

            self.fields['forum'].widget.attrs={'class': 'form-control'}
            self.fields['name'].widget.attrs={'class': 'form-control'}
            self.fields['discuss'].widget.attrs={'class': 'CKEditorWidget'}
