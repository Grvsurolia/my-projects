"""
Django settings for MailSaaS project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime 
# from decouple import config
from decouple import config
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'atKdSovwyebchqILGtQCobosgFuyZZqQVNMjRpZb'
# SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# CORS_ALLOWED_ORIGINS = ['*']
SITE_URL = 'http://localhost:8000'

CORS_ALLOW_ALL_ORIGINS = True


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.forms',
  
    'celery_progress',
    "django_celery_results",
    'django_crontab',
    'django_celery_beat',
]

# Put your third-party apps here
THIRD_PARTY_APPS = [
    
    
    # 'django_pipedrive',

    'corsheaders',
    # stripe integration
    'djstripe',
    'salesforce',
   
]

PEGASUS_APPS = [
    'apps.pegasus',
    'django_google.apps.DjangoGoogleConfig',
]

# Put your project-specific apps here
PROJECT_APPS = [
    'apps.subscriptions.apps.SubscriptionConfig',
    'apps.users.apps.UserConfig',
    'apps.web',
    'apps.campaign',
    'apps.campaignschedule.apps.CampaignscheduleConfig',
    'apps.teams.apps.TeamConfig',
    'apps.integration',
    "apps.unsubscribes",

    'apps.mailaccounts',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    'django.contrib.sites',

    'allauth',  # allauth account/registration management
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PEGASUS_APPS + PROJECT_APPS

SITE_ID = 1
AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'mail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.web.context_processors.project_meta',
                 # this line can be removed if not using google analytics
                'apps.web.context_processors.google_analytics_id',
            ],
        },
    },
]

WSGI_APPLICATION = 'mail.wsgi.application'

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT':config('DATABASE_PORT'),
    }
}

GOOGLE_CLIENT_SECRET_FILE = os.path.join(BASE_DIR, 'client_secret_178038321765-1d24dsmngr7cmthb1ksvno3kehirnqbg.apps.googleusercontent.com.json')
GOOGLE_AUTH_SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]




# Auth / login stuff

# Django recommends overriding the user model even if you don't think you need to because it makes
# future changes much easier.
# LOGIN_REDIRECT_URL = '/'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Allauth setup
REST_SESSION_LOGIN = True
REST_USE_JWT = True

ACCOUNT_ADAPTER = 'apps.teams.adapter.AcceptInvitationAdapter'
ACCOUNT_ADAPTER = 'apps.users.adapter.CustomUserAccountAdapter'


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'


ACCOUNT_FORMS = {
    'signup': 'apps.teams.forms.TeamSignupForm',
}



# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# )


# enable social login
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True
USE_L10N = True
USE_TZ = True
DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S' 



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# uncomment to use manifest storage to bust cache when file change
# note: this may break some image references in sass files which is why it is not enabled by default
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email setup

# use in development
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# use in production
# see https://github.com/anymail/django-anymail for more details/examples
# EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

# Django sites



# DRF config
REST_FRAMEWORK = {
    # "DATE_INPUT_FORMATS": ["%m-%d-%Y"],

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',

        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
        
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


# Celery setup (using redis)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = ('apps.campaignschedule.tasks',)
CELERY_CACHE_BACKEND = 'django-cache'




# JWT_AUTH = { 
#     'JWT_AUTH_HEADER_PREFIX': 'JWT',
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=500)
# }





REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'apps.users.serializer.RegisterSerializer',
}


# Pegasus config

# replace any values below with specifics for your project
PROJECT_METADATA = {
    'NAME': 'MailSaaS',
    'URL': 'http://localhost:8000',
    'DESCRIPTION': 'The most amazing SaaS application the world has ever seen!',
    'IMAGE': 'https://upload.wikimedia.org/wikipedia/commons/2/20/PEO-pegasus_black.svg',
    'KEYWORDS': 'SaaS, django',
    'CONTACT_EMAIL': 'elon.musk@localhost:8000',
}


ADMINS = [('Elon Musk', 'elon.musk@localhost:8000')]

GOOGLE_ANALYTICS_ID = ''  # replace with your google analytics ID to connect to Google Analytics

# Stripe config

# modeled to be the same as https://github.com/dj-stripe/dj-stripe
STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "<your publishable key>")
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "<your secret key>")
STRIPE_TEST_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_<your publishable key>")
STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_<your secret key>")
STRIPE_LIVE_MODE = False  # Change to True in production

# Get it from the section in the Stripe dashboard where you added the webhook endpoint
# or from the stripe CLI when testing
DJSTRIPE_WEBHOOK_SECRET = os.environ.get('DJSTRIPE_WEBHOOK_SECRET', "whsec_xxx")

DJSTRIPE_FOREIGN_KEY_TO_FIELD = 'id'  # change to 'djstripe_id' if not a new installation
DJSTRIPE_USE_NATIVE_JSONFIELD = True  # change to False if not a new installation


# JWT settings
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': False,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}




#Mail_configuration

EMAIL_HOST='sg3plcpnl0063.prod.sin3.secureserver.net'
EMAIL_PORT=config('EMAIL_PORT')
EMAIL_USE_SSL=config('EMAIL_USE_SSL')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')




# Slack Configuration
VERIFICATION_TOKEN = config('VERIFICATION_TOKEN')
OAUTH_ACCESS_TOKEN = config('OAUTH_ACCESS_TOKEN')
BOT_USER_ACCESS_TOKEN = config('BOT_USER_ACCESS_TOKEN')
SLACK_CLIENT_ID = config('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = config('SLACK_CLIENT_SECRET')

#Salesforce Configuration

# SALESFORCE_USERNAME = config('SALESFORCE_USERNAME')
# SALESFORCE_PASSWORD = config('SALESFORCE_PASSWORD')
# SALESFORCE_SECURITY_TOKEN = config('SALESFORCE_SECURITY_TOKEN')
# SALESFORCE_DOMAIN = 'test'
# SALESFORCE_USE_SANDBOX = True
# SALESFORCE_API_VERSION = '43.0'


PIPEDRIVE_API_KEY="67ffc61ad9d85760cee59c2115bddd5cc536e9c6"

#Google Configuration
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')