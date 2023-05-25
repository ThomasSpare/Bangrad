from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from .models import spotipy, Discussion, LodgeForum, forms, User, CloudinaryField, BangradSearchFields
from django.shortcuts import render, redirect
from .forms import CreateInForum, CreateInDiscussion


class Search(CreateView):

    # specify the model for create view
    model = BangradSearchFields
    template_name = "home.html"
    fields = ['key', 'tempo', 'language', 'release_year']


def Lodge(request):
    forums = LodgeForum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'lodge.html', context)


def AddInLodge(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lodge')
    context = {'form': form}
    return render(request, 'addinlodge.html', context)


def LodgeTalk(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lodge')
    context = {'form': form}
    return render(request, 'lodgetalk.html', context)
