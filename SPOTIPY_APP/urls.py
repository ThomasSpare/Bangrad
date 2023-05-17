from django.contrib import admin
from . import views
from django.urls import path, include
from .views import Search


urlpatterns = [
    path("", Search.as_view(), name="home"),
]
