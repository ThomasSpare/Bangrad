from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views import generic
from django.forms import ModelForm
from members.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Discussion, LodgeForum, BangradSearchFields
from members.views import ProfileDetails, ProfileUpdateView
from django.shortcuts import render, redirect
from .forms import CreateInForum, CreateInDiscussion
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from SPOTIPY_SEARCH.settings import sp
from django.urls import reverse_lazy
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)




class Search(CreateView):
    """ 
    Unused future View for Spotify search fields 
    """
    # specify the model for create view
    model = BangradSearchFields
    template_name = "home.html"
    fields = ['key', 'tempo', 'language', 'release_year']


class UpdatePostView(UpdateView):
    """ 
    View Update forum posts
    """
    model = LodgeForum
    form_class = CreateInForum
    template_name = 'registration/editpost.html'
    success_url = reverse_lazy('lodge')
   

class DeletePostView(DeleteView):
    """ 
    View to delete posts in forum
    """
    model = LodgeForum
    template_name = 'registration/deletepost.html'
    success_url = reverse_lazy('lodge')


def Lodge(request):
    """ 
    Lodge forums
    """
    forums = LodgeForum.objects.all()
    count = forums.count()
    discussions = []
    for forum in forums:
        discussions.append(forum.comments.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'lodge.html', context)


def AddInLodge(request):
    """ 
    Adds new posts in forum
    """
    model = LodgeForum
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            new_forum_post = form.save(commit=False)
            new_forum_post.author = request.user
            new_forum_post.save()
            posts = LodgeForum.objects.all()  # gets all posts, consider ordering by 'date' for relevancy
            context = {'form': CreateInForum(), 'posts': posts}
            messages.success(request, 'Your forum post has been added successfully.')
            return render(request, 'addinlodge.html', context)
    else:
        form = CreateInForum()
    return render(request, 'addinlodge.html', {'form': form})


def LodgeTalk(request):
    """ 
    Adds comments to posts in forum
    """
    model = Discussion
    form = CreateInDiscussion()
    success_url = reverse_lazy('lodge')
    
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'lodgetalk.html')
    context = {'form': form}
    return render(request, 'lodgetalk.html', context)


def form_valid(self, form):     # makes active user id available
    form.instance.user = self.request.user
    return super(UpdatePostView, self).form_valid(form)


def register(request):
    """ 
    User register view
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('registration/login.html')
    else:
        form = UserRegisterForm()
    return render(request, '/register/signup.html', {'form': form})


def delete_post(request, id):
    """ 
    delete a users posts in forum
    """
    post = get_object_or_404(LodgeForum, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'lodge/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('lodge')


class UserListView(ListView):
    """ 
    View to render all members
    """
    model = User
    template_name = 'registration/memberlist.html'
    fields = '__all__'
