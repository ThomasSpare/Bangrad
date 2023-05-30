from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from .models import Profile, Discussion, LodgeForum, forms, User, CloudinaryField, BangradSearchFields
from django.shortcuts import render, redirect
from .forms import UserUpdateForm, UserCreationForm, UserRegisterForm, CreateInDiscussion, CreateInForum, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from SPOTIPY_SEARCH.settings import sp


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required  # user logged in before they can access profile page
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile.html')  # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
