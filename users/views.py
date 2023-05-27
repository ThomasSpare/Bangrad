from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic.base import View
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required  # user logged in before they can access profile page
def profile(request):
    return render(request, 'users/profile.html')
