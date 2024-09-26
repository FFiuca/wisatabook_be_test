import environ
from pathlib import Path
import os
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(
    DEBUG=(bool, False),
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

APP_NAME=env('APP_NAME')
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '34.128.122.153',
    'localhost',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third
    "debug_toolbar",
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
    "safedelete",
    "django_seed",
    "corsheaders",

    # apps
    "todo",
    "master",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # third
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'wisatabook_be.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'wisatabook_be.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'ENGINE': 'django.db.backends.mysql',
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'PASSWORD': env('DB_PASSWORD'),
        'USER': env('DB_USER'),
        'NAME': env('DB_NAME'),
    }
}

FIXTURE_DIRS = [
    BASE_DIR / "database" / "seeder"
]


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True

APPEND_SLASH = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
REST_FRAMEWORK  = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication', # this module neeede for default auth djano, in section is django temporray login and logout
        'rest_framework.authentication.TokenAuthentication', # way to know avaible auth type: open https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme and rest_xxx.autxxx.{List of APIReference}
    ],
    'DEFAULT_RENDERER_CLASSES' : [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated', # any route who access must login
        'rest_framework.permissions.AllowAny',
    ],
    # https://www.django-rest-framework.org/api-guide/throttling/
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '10000/day', # test for login view
    #     'user': '10000/day',
    #     'login-attempt' : '2/minute', # look user_app.throttling.LoginThrottle
    #     'register-attempt' : '10/minute',
    # },
    # 'TEST_REQUEST_RENDERER_CLASSES': [
    #     # 'rest_framework.renderers.MultiPartRenderer',
    #     'rest_framework.renderers.JSONRenderer',
    #     # 'rest_framework.renderers.TemplateHTMLRenderer'
    # ]

    # for default setting on generic and viewset view, if want on APIView to apply see https://stackoverflow.com/questions/35830779/django-rest-framework-apiview-pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', # "next": "http://127.0.0.1:8000/watch/stream/review/filter/?limit=4&offset=4&username=admin",
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?cursor=cD0yMDIzLTA3LTIzKzA4JTNBMTIlM0E0Mi44NTg2NzYlMkIwMCUzQTAw&username=admin
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', # http://127.0.0.1:8000/watch/stream/review/filter/?page=2&username=admin
    # 'PAGE_SIZE': 4
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=1),
    'ROTATE_REFRESH_TOKENS' : True,
}

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env('EMAIL_HOST')
EMAIL_PORT=env('EMAIL_PORT')
EMAIL_HOST_USER=env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=env('EMAIL_USE_TLS')
EMAIL_FROM_ADDRESS=env('EMAIL_FROM_ADDRESS')
EMAIL_FROM_NAME=env('EMAIL_FROM_NAME')

# DJANGO CORS
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://34.128.122.153$",
]

# CRONTAB
# CRONJOBS = [
#     ('*/5 * * * *', 'myapp.tasks.my_scheduled_task'),  # Example: Run every 5 minutes
# ]
