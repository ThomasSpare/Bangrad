from django.contrib import admin
from . import views
from .views import UserListView
from django.urls import path, include
from .views import Search, Lodge, LodgeTalk, AddInLodge, Profile, EditProfilePageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Search.as_view(), name="home"),
    path('home/', Search.as_view(), name="home"),
    path("lodge/", views.Lodge, name="lodge"),
    path("lodgetalk/", views.LodgeTalk, name="lodgetalk"),
    path("addinlodge/", views.AddInLodge, name="addinlodge"),
    path("profile/", Profile.as_view(), name="profile"),
    path('memberlist/', UserListView.as_view(), name='memberlist'),
    path('<int:pk>/edit_profile/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)