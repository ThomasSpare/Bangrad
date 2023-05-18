from django.contrib import admin
from . import views
from django.urls import path, include
from .views import Search


urlpatterns = [
    path("home/", Search.as_view(), name="home"),
    path("lodge/", Search.as_view(), name="lodge"),
    path("lodgetalk/", Search.as_view(), name="lodgetalk"),
    path("addinlodge/", Search.as_view(), name="addinlodge"),
    path("profile/", Search.as_view(), name="profile"),
]
