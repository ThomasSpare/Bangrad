from django.contrib import admin
from . import views
from .views import UserListView
from django.urls import path, include
from .views import Search, Lodge, LodgeTalk, AddInLodge, ProfileDetails, ArticleDetailView, CreateProfilePageView, DeletePostView, UpdatePostView, ProfileUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Search.as_view(), name="home"),
    path('home/', Search.as_view(), name="home"),
    path("lodge/", views.Lodge, name="lodge"),
    path("member/lodgetalk", views.LodgeTalk, name="lodgetalk"),
    path("member/addinlodge", views.AddInLodge, name="addinlodge"),
    path("member/profile", ProfileDetails.as_view(), name="profile"),
    path('member/memberlist', UserListView.as_view(), name='memberlist'),
    path('<int:pk>/edit_profile_page/', ProfileUpdateView.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfilePageView.as_view(), name='create_profile'),
    path('article/<int:id>/remove', DeletePostView.as_view(), name='deletepost'),
    path('article/edit/<int:id>', UpdatePostView.as_view(), name='updatepost'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)