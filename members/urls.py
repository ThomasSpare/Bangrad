from django.contrib import admin
from django.urls import path
from .views import UserRegistrationView, CreateProfilePageView, ProfileUpdateView, ProfileDetails
from SPOTIPY_APP.views import UpdatePostView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile'),
    path('edit_profile', ProfileUpdateView.as_view(), name='edit_profile_page'),
    path('profile/', ProfileDetails.as_view(), name="profile"),
]