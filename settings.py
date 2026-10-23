import os
from pathlib import Path
from dotenv import load_dotenv

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env (Local development को लागि मात्र)
load_dotenv(BASE_DIR / ".env")

# Security settings
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "dev-only-change-this-secret-key-before-deployment"
)

# लाइभ जाँदा Render को Environment Variable मा DJANGO_DEBUG लाई False राख्नुहोला
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"

# settings.py भित्र खोजेर ALLOWED_HOSTS लाई यसरी परिवर्तन गर्नुहोस्:

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'my-portfolio2-crf3.onrender.com',  # 👈 तपाईंको अनलाइन लिङ्क यहाँ सिधै थपिएको छ
]


# Installed applications
INSTALLED_APPS = [
    "config.apps.MongoAdminConfig",
    "config.apps.MongoAuthConfig",
    "config.apps.MongoContentTypesConfig",

    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django_mongodb_backend",
    "rest_framework",
    "corsheaders",
    "portfolio",
]

# Middleware (WhiteNoise Middleware लाई दोस्रो नम्बरमा थपिएको छ)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # 👈 Static files लाइभमा लोड गराउन थपिएको
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Project configuration
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# MongoDB database configuration (Render मा MONGODB_URI र MONGODB_NAME थप्नुपर्छ)
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb_backend",
        "HOST": os.getenv(
            "MONGODB_URI",
            "mongodb://127.0.0.1:27017/"
        ),
        "NAME": os.getenv(
            "MONGODB_NAME",
            "bikash_portfolio"
        ),
    }
}

# MongoDB-compatible migrations for Django built-in apps
MIGRATION_MODULES = {
    "admin": "mongo_migrations.admin",
    "auth": "mongo_migrations.auth",
    "contenttypes": "mongo_migrations.contenttypes",
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]

# Language and timezone
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kathmandu"
USE_I18N = True
USE_TZ = True


# Static and uploaded files configuration
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# लाइभ सर्भरमा बुटस्ट्र्याप/CSS/JS स्टोर हुने ठाउँ
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise ले static file कम्प्रेस गरेर स्पिड बढाउन प्रयोग गर्ने स्टोरेज सेटिङ
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Default primary key
DEFAULT_AUTO_FIELD = (
    "django_mongodb_backend.fields.ObjectIdAutoField"
)

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Frontend CORS configuration
FRONTEND_ORIGIN = os.getenv(
    "FRONTEND_ORIGIN",
    "http://127.0.0.1:5500"
)

CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in FRONTEND_ORIGIN.split(",")
    if origin.strip()
]

CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

# Cloudinary configuration
CLOUDINARY_CLOUD_NAME = os.getenv(
    "CLOUDINARY_CLOUD_NAME", ""
)
CLOUDINARY_API_KEY = os.getenv(
    "CLOUDINARY_API_KEY", ""
)
CLOUDINARY_API_SECRET = os.getenv(
    "CLOUDINARY_API_SECRET", ""
)

# Email configuration for local development
EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# settings.py भित्र खोजेर यो पूरा भाग अपडेट गर्नुहोस्:
STORAGES = {
    # मिडिया वा डिफल्ट फाइल अपलोडका लागि यो अनिवार्य छ (यो छुटेको हुनाले एरर आएको हो)
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # WhiteNoise को लागि static file स्टोरेज सेटिङ
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
