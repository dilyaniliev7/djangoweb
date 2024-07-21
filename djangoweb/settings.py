import os
from pathlib import Path
import cloudinary
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY ='django-insecure-_t39k)a540zzf(j%o@c7_jui5%)8r28vwh=j$pu%i92pn1)7xq'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',
    'django_mailjet',

    'djangoweb.djangogram',
    'djangoweb.accounts',
    'djangoweb.photos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoweb.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "11qWE3",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
MEDIA_URL = '/media/'

# MEDIA_ROOT = BASE_DIR / 'mediafiles'

cloudinary.config(
  cloud_name="dli5xlcmp",
  api_key="741836319852411",
  api_secret="5MfSikHjvCcfpEgxBfDsFaLP6DM",
  secure=True
)

AUTH_USER_MODEL = 'accounts.AppUser'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "socialgraminfo224@gmail.com"
EMAIL_HOST_PASSWORD = 'uhwq nmhy tgav deqk'
