from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

env_path = Path(".")/".env"
load_dotenv(dotenv_path=env_path)

load_dotenv()

#SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_KEY = os.environ["SECRET_KEY"]
# DEBUG = os.getenv("DEBUG")
DEBUG = os.environ.get("DEBUG", "") != "False"

# DEBUG = True
# SECRET_KEY = (
#     "django-insecure-8ovil3xu6=eaoqd#-#&ricv159p0pypoh5_lgm*)-dfcjqe=yc"
# )
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#ALLOWED_HOSTS = ["127.0.0.1", "https://newspaper-1.onrender.com"]
ALLOWED_HOSTS = []
INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "crispy_forms",
    "newspaper",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "newspaper_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "newspaper.tests.context_processors.cfg_assets_root",
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

WSGI_APPLICATION = "newspaper_service.wsgi.application"


DATABASES = {
    'default': dj_database_url.config(
        default='postgres://ovnreimv:N1z3qQnbt2fVPJwoNrLSP8BHvn27m_Lu@snuffleupagus.db.elephantsql.com/ovnreimv'
    )
    # ),
    # 'sqlite': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# DATABASES = {
#     'default': dj_database_url.config(
#         default='postgres://ovnreimv:N1z3qQnbt2fVPJwoNrLSP8BHvn27m_Lu@snuffleupagus.db.elephantsql.com/ovnreimv'
#     )
# }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)
#DATABASES_URL = "postgres://ovnreimv:N1z3qQnbt2fVPJwoNrLSP8BHvn27m_Lu@snuffleupagus.db.elephantsql.com/ovnreimv"
# DATABASES_URL = os.getenv("DATABASES")

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "newspaper.Redactor"

LOGIN_REDIRECT_URL = "/"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

ASSETS_ROOT = "/static/assets"

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_ROOT = "staticfiles/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
