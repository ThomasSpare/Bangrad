from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from SPOTIPY_APP.models import Profile
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views import generic
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from SPOTIPY_APP.models import Profile, Discussion, LodgeForum, forms, User, CloudinaryField
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserRegisterForm, UserCreationForm, UserUpdateForm, ProfilePageForm
from django.contrib import messages
from SPOTIPY_SEARCH.settings import sp
from django.urls import reverse_lazy


class UserRegistrationView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    
    def form_valid(self, form):     # makes active user id available
        form.instance.user = self.request.user
        return super().form_valid(form)


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

class ProfileDetails(LoginRequiredMixin, DetailView):
    """
    View to render profile page
    """
    model = Profile
    template_name = 'registration/profile.html'
    
    def get_object(self, *args, **kwargs):
        return self.request.user.profile


class UserProfileView(View):
    """Class based view for other user's profile pages"""

    def get(self, request, user, *args, **kwargs):
        """Get method for other user's profile page"""
        user_profile = Profile.objects.get(user__username=user)
        if user_profile.user == request.user:
            return HttpResponseRedirect(reverse('registration/user_profile.html'))
        bio = user_profile.bio
        image = user_profile.image
        user = user_profile.user
        
        context = {
            'user': user,
            'bio': bio,
            'image': image,
        }
        return render(request, 'registration/user_profile.html', context)


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    """
    View to render Edit profile page
    """
    model = Profile
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/edit_profile_page.html'
    success_message = 'Your profile was successfully updated !'
    
    def get_object(self, *args, **kwargs):
        return self.request.user.profile
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
