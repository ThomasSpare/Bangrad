from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


def Login_User(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(
                request, ("Something's wrong, please try again..."))
            return redirect('home')
    else:
        return render(request, 'login.html', {})
