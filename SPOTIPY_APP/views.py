from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from .models import BangradSearchFields


class Search(CreateView):
 
    # specify the model for create view
    model = BangradSearchFields
    # specify the fields to be displayed
    fields = ['key', 'tempo', 'language', 'release_year']




