from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


ALLOWED_HOSTS = [
    
    ]

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
    'tailwind',
    'theme',

    'newsletters',
    'dashboard',

    'storages'
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "/usr/bin/npm"
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT=os.path.join(BASE_DIR, 'static_root')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if not DEBUG:
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST=env('EMAIL_HOST')
    EMAIL_HOST_USER=env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT=env('EMAIL_PORT')
    EMAIL_USE_TLS=env('EMAIL_USE_TLS')

    SESSION_COOKIE_SECURE=True
    SECURE_BROWSER_XSS_FILTER=True
    SECURE_CONTENT_TYPE_NOSNIFF=True
    SECURE_HSTS_INCLUDE_SUBDOMAINS=True
    SECURE_HSTS_SECONDS=31536000
    SECURE_REDIRECT_EXEMPT=[]
    SECURE_SSL_REDIRECT=True
    SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO', 'https')

    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    AWS_ACCESS_KEY_ID= env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')

    AWS_S3_CUSTOM_DOMAIN=f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMENTERS={'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL='public-read'

    STATIC_LOCATION='static'
    STATIC_URL=f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'

    PUBLIC_MEDIA_LOCATION='media'
    MEDIA_URL=f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE='core.storage_backends.MediaStore'

    STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'),)
    STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
