from django.contrib import admin
from . import views
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", include("SPOTIPY_SEARCH.urls"), name="bangrad"),
    path("accounts/", include("accounts.urls"), name="accounts"),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts2"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
