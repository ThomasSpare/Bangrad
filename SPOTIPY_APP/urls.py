from django.contrib import admin
from . import views
from .views import UserListView
from django.urls import path, include
from .views import Search, Lodge, LodgeTalk, AddInLodge, ProfileDetails, DeletePostView, UpdatePostView, ProfileUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('members.urls'), name="members.urls"),
    path('', Search.as_view(), name="home"),
    path('home/', Search.as_view(), name="home"),
    path("lodge/", views.Lodge, name="lodge"),
    path("lodgetalk/", views.LodgeTalk, name="lodgetalk"),
    path("addinlodge/", views.AddInLodge, name="addinlodge"),
    path('memberlist/', UserListView.as_view(), name='memberlist'),
    path('<int:pk>/edit_profile_page/', ProfileUpdateView.as_view(), name='edit_profile_page'),
    path('delete/<int:pk>/remove/', DeletePostView.as_view(), name='deletepost'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update_post'),]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)