from django.contrib import admin
from . import views
from django.urls import path, include
from .views import Search, Lodge, LodgeTalk, AddInLodge


urlpatterns = [
    path("home/", Search.as_view(), name="home"),
    path("lodge/", views.Lodge, name="lodge"),
    path("lodgetalk/", views.LodgeTalk, name="lodgetalk"),
    path("addinlodge/", views.AddInLodge, name="addinlodge"),
]
