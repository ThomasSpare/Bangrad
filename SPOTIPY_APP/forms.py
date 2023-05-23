from django.forms import ModelForm
from .models import LodgeForum, Discussion


class CreateInForum(ModelForm):
    class Meta:
        model = LodgeForum
        fields = "__all__"


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
