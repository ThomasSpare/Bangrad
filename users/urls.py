from django.urls import path
from django.contrib import admin
from .views import register
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
