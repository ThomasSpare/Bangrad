from django.urls import path
from django.contrib import admin
from .views import register
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userslogout.html'), name='logout')

]
