# -*- coding: utf-8 -*-
"""
Django settings for JXXT project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.cstaom/en/1.8/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_COOKIE_AGE=60*30

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w#7b^&a@0bzsnqq*jdnqxbj__j3)3y=01_s%115w)!wwxxdgxp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ustcjxxt',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'JXXT.urls'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), '../templates').replace('\\', '/'), ],
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
# print(TEMPLATES)
WSGI_APPLICATION = 'JXXT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# 'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'jxxt',
#         'USER':'root',
#         'PASSWORD': 'haolin',
#         'HOST': '',
#         'PORT': '',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jxxt.db',
        'USER': 'root',
        'PASSWORD': 'haolin',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/'),
    os.path.join(os.path.dirname(__file__), '../upload/').replace('\\', '/'),
)

MEDIA_URL = '/upload/'
MEDIA_ROOT = (
    os.path.join(os.path.dirname(__file__), '../upload/').replace('\\', '/')
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '科大教学管理系统',
    'LIST_PER_PAGE': 10,
    'MENU': (
        'sites',
        {'app': 'ustcjxxt', 'label': u'教学管理', 'icon': 'icon-wrench'},
    ),
}
