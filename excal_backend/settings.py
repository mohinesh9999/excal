"""
Django settings for excal_backend project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import cloudinary,os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qb61+@61d(5oxppy9qs9yp25e4+j52c+#kahqb25t(u1u_vqs0'

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
    'user',
    'corsheaders',
    'rest_framework',
    'excal_admin',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'excal_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'excal_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": "excal",
           "host": "mongodb+srv://test:test@cluster0-nc9ml.mongodb.net/sih?retryWrites=true&w=majority",
           "username": "test",
           "password": "test",
           "authMechanism": "SCRAM-SHA-1",
        },
    }
}



#email credentials

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'swayamkriti@gmail.com'
EMAIL_HOST_PASSWORD = 'Exc@l2020'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# MEDIA_URL = '/static/'
MEDIA_URL = '/media/'
# MEDIA_ROOT=STATIC_URL + MEDIA_URL
cloudinary.config(
         cloud_name='studentmohinesh',
         api_key='738358349287446',
         api_secret='o0HrCNinx48oAaxCNY8ue0JhQBw'
     )
DEFAULT_FILE_STORAGE="cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_STORAGE={
    'CLOUD_NAME':("studentmohinesh"),
    'API_KEY':('738358349287446'),
    'API_SECRET':('o0HrCNinx48oAaxCNY8ue0JhQBw'),
    'CLOUDINARY_URL':'cloudinary://738358349287446:o0HrCNinx48oAaxCNY8ue0JhQBw@studentmohinesh'
}

# REST_FRAMEWORK = { 
#     'DEFAULT_AUTHENTICATION_CLASSES': [ 
#         'rest_framework_simplejwt.authentication.JWTAuthentication', 
#     ], 
# } 
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}
# AUTH_USER_MODEL = 'user.User'