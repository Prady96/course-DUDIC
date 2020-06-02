"""
Django settings for dudic project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#####################################################################

PROJECT_DIR = os.path.join(BASE_DIR, 'dudic')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_STATIC = os.path.join(BASE_DIR, 'login')

COURSE_STATIC = os.path.join(BASE_DIR, 'course')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(LOGIN_STATIC, 'static'),
    os.path.join(COURSE_STATIC, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_URL = '/images/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


#####################################################################



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yn!bk5(u80crtcnq@*hf*!**0-vr5d^#54!f-=9u#*in$4kr$*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'course',
    'phonenumber_field',
    # 'linkcheck',
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

ROOT_URLCONF = 'dudic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
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

WSGI_APPLICATION = 'dudic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

########################################################
#    Sending Mails from ( course@dudic.io ) ZOHO Mail
########################################################

# EMAIL_HOST = 'smtp.zoho.com'
# EMAIL_HOST_USER = 'course@dudic.io'
# EMAIL_HOST_PASSWORD = 'harebol@123'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Team DIC <course@dudic.io>'

""" Sending Mail Procedure
from django.conf import settings
from django.core.mail import send_mail

subject = 'Some subject'
from_email = settings.DEFAULT_FROM_EMAIL
message = 'This is my test message'
recipient_list = ['pradyumg@gmail.com',]
html_message = '<h1>This is my HTML test</h1>'


send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)

"""

PHONENUMBER_DB_FORMAT = "NATIONAL"
PHONENUMBER_DEFAULT_REGION = "IN"


#######################################################
#    Sending Mails from ( course@dudic.io ) Send Grid
#######################################################

# SENDGRID_API_KEY = os.getenv('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')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'TEST MAIL <course@dudic.io>'
FROM_EMAIL = 'course@dudic.io'

# import os

# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_API_KEY= "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"
# # SENDGRID_API_KEY = os.environ.get(SENDGRID_API_KEY)
# SENDGRID_SANDBOX_MODE_IN_DEBUG=False
# SENDGRID_ECHO_TO_STDOUT=True




















