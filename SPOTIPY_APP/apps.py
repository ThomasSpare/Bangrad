from django.apps import AppConfig
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotipyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SPOTIPY_APP'


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import SPOTIPY_APP.signals
