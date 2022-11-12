"""
Django settings for clinic project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o%lutb#jk0*#&_eg%dtg-d(y0p5jq))06a0%my9et=wvddiqs1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'user',
    'payment',
    'management',
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

ROOT_URLCONF = 'clinic.urls'

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

WSGI_APPLICATION = 'clinic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#Please use MySQL 5.7
#Succefully connectedm,please don't edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medica',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# djangostripe/settings.py
# 用于支付的环境变量 请勿更改
STRIPE_PUBLISHABLE_KEY = 'pk_test_51LfsxDBk6HVAywFcleWccBNnxbnuKPIRivlxw97Y80zxnxPWHAJwj82Bzqnv581hXgxPFGhB0rWshV2RC0HkWOaP00Uv6HlURv'
STRIPE_SECRET_KEY = 'sk_test_51LfsxDBk6HVAywFcLdzMXi2qN0WKZOuNVKFuMxQYSBoxyyO34neGqxEkegOXGbKgrttncO9iDhWLnNffFk11A1z7003Q2ZTIhh'

# STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
# # 设置图片等静态文件的路径
# STATICFILES_DIRS = (
#     ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/') ),
#     ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/') ),
#     ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/') ),
#     ('upload',os.path.join(STATIC_ROOT,'upload').replace('\\','/') ),
# )

EMAIL_USE_SSL = True
#EMAIL_USE_TSL = True
EMAIL_HOST = 'smtp.gmail.com'  # use gmail interface
EMAIL_PORT = 465
EMAIL_HOST_USER = 'qi912675127@gmail.com' # 帐号
EMAIL_HOST_PASSWORD = 'qtphxrswgwreovuf'  # 密码
DEFAULT_FROM_EMAIL = 'Medica Center <qi912675127@gmail.com>'