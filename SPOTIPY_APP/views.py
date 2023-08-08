from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views import generic
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Discussion, LodgeForum, forms, User, CloudinaryField, BangradSearchFields
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserCreationForm, UserRegisterForm, CreateInDiscussion, CreateInForum, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from SPOTIPY_SEARCH.settings import sp
from django.urls import reverse_lazy


class Search(CreateView):
    # specify the model for create view
    model = BangradSearchFields
    template_name = "home.html"
    fields = ['key', 'tempo', 'language', 'release_year']


class ArticleDetailView(DetailView):
    model = LodgeForum
    template_name = 'registration/article_details.html'


class UpdatePostView(UpdateView):
    model = LodgeForum
    template_name = 'registration/editpost.html'
    fields = ['topic','description', 'body', 'link', 'image' ]

class DeletePostView(DeleteView):
    model = LodgeForum
    template_name = 'registration/deletepost.html'
    success_url = reverse_lazy('lodge')


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
            messages.success(
                request, f'Your forum is added successfully')
            return redirect('lodge.html')
        else:
            form = CreateInForum()
            return render(request, 'registration/addinlodge.html', {'form': form})


def LodgeTalk(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lodge.html')
    context = {'form': form}
    return render(request, 'registration/lodgetalk.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login.html')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

class ProfileDetails(DetailView):
    """
    View to render profile page
    """
    model = Profile
    template_name = 'registration/profile.html'
    fields = [  'image', 'bio', 'first_name', 'last_name', 'email',
                'website_url', 'spotify_artist', 'instagram', 'facebook',
                'twitter', 'mixcloud', 'soundcloud', 'youtube', 'link_1',
                'link_2'
            ]
    def get_object(self, *args, **kwargs):
        return self.request.user


class ProfileUpdateView(UpdateView):
    """
    View to render Edit profile page
    """
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [  'image', 'bio', 'first_name', 'last_name', 'email',
                'website_url', 'spotify_artist', 'instagram', 'facebook',
                'twitter', 'mixcloud', 'soundcloud', 'youtube', 'link_1',
                'link_2'
            ]
    def get_object(self, *args, **kwargs):
        return self.request.user


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'image', 'website_url', 'spotify_artist', 'instagram',
                'facebook', 'twitter', 'mixcloud', 'soundcloud', 'youtube',
                'link_1', 'link_2'
            ]
    success_url = reverse_lazy('registration/profile')


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}    
    
    if request.method == 'GET':
        return render(request, 'lodge/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('lodge')


@login_required  # user logged in before they can access profile page
def profile_update(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        post_form = CreateInForum(request.POST, instance=request.user.profile)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/templates/home/profile_page.html')  # Redirect back to profile pag
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)


class UserListView(ListView):

    model = User
    template_name = 'registration/memberlist.html'
    fields = '__all__'
