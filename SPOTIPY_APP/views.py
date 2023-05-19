from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from .models import *
from django.shortcuts import render, redirect
from .forms import *


class Search(CreateView):

    # specify the model for create view
    model = BangradSearchFields
    template_name = "home.html"
    fields = ['key', 'tempo', 'language', 'release_year']


def Lodge(request):
    forums = LodgeForum.objects.all()
    template_name = "home.html"
    count = forums.count()
    discussions = []
    for i in forums:
        context = {'forums': forums,

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
def AddInLodge(request):


    form = CreateInForum()
    if request.method == 'POST':
        context = {'form': form}
    return render(request, 'templates/addinlodge.html', context)


def LodgeTalk(request):
    template_name = "lodgetalk.html"
    context = {'form': form}
    return render(request, 'templates/addinlodge.html', context)

    if form.is_valid():

    return render(request, 'templates/lodgetalk.html', context)
