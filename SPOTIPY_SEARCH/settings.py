import os
from datetime import timedelta
from pathlib import Path
from django.contrib.messages import constants as messages

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


import dj_database_url
if os.path.isfile("env.py"):
    import env
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dj_database_url
import env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# SPOTIPY GET CREDENTIALS
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=os.environ.get(
    'os.environ["SPOTIPY_CLIENT_ID"], ["SPOTIPY_CLIENT_SECRET"]'))
sp.trace = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ["https://bangrad.herokuapp.com",
                "localhost",
                "127.0.0.1",
                "[::1]",
                ]

CSRF_TRUSTED_ORIGINS = [
                    "localhost",
                    "127.0.0.1",
                    "[::1]",
                    "https://bangrad.herokuapp.com",
                    ]

CORS_ALLOW_ALL_HEADERS = True

CORS_ALLOW_CREDENTIALS = True


INSTALLED_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'allauth',
    'members',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_bootstrap4',
    'SPOTIPY_APP',
    'SPOTIPY_SEARCH',
    'spotipy',
    'whitenoise',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/home/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SPOTIPY_SEARCH.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SPOTIPY_SEARCH.wsgi.application'


DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



CKEDITOR_BASEPATH = "static/ckeditor/ckeditor/"

# CKEditor settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'None',
    },
}


STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
   'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL'),
   'API_KEY': os.environ.get('API_KEY'),
   'API_SECRET': os.environ.get('API_SECRET'),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFTETIME': timedelta(minutes=30),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
