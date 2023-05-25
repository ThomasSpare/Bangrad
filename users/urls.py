from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),

]
