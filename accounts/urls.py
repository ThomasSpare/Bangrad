from django.urls import path
from .views import SignUpView


urlpatterns = [
    path("registration/signup/", SignUpView.as_view(), name="signup"),
]
