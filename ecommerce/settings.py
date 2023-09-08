import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "SADB@OEJ@EJDWOJE@QPJENINDWQ#1W#!@U!(&U!(HEQ!W@H))asasw2w19w*(!1@)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "items.apps.ItemsConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "users.apps.UsersConfig",
    "django.contrib.admindocs",
    # 3rd party
    "django_filters",
    "crispy_forms",
    "crispy_bootstrap4",
    "ckeditor"
    
]




MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"

AUTH_USER_MODEL = "users.User"

# auth
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)


ACCOUNT_UNIQUE_EMAIL = True

# redirects
LOGIN_URL = "/user/login/"
LOGIN_REDIRECT_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"
SOCIAL_AUTH_BACKEND_ERROR_URL = "/"


# for crispy forms
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kathmandu"

USE_I18N = True

USE_L10N = True

USE_TZ = False

CRISPY_FAIL_SILENTLY = True

CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"


# urls
STATIC_URL = "/static/"
MEDIA_URL = "/media/"


# number of items in a paginated page
ITEMS_PER_PAGE = 25


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CKEDITOR_BASEPATH = STATIC_URL + "ckeditor/ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_FILE_OVERWRITE = False
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_FILENAME_GENERATOR = "core.utils.get_filename"
AWS_QUERYSTRING_AUTH = False
CKEDITOR_UPLOAD_IMAGE_FORMATS = ["jpg", "jpeg", "png", "gif"]