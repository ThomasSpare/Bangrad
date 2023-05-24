from django.urls import path
from .views import Login_User
from . import views

urlpatterns = [
    path("login/", views.Login_User, name="login"),

]
