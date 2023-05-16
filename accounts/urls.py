from django.urls import path
from .views import SignUpView


urlpatterns = [
    path("templates/registration/signup.html",
         SignUpView.as_view(), name="signup")
]
