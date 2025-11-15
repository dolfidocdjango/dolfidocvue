"""
Production settings for Dolfidoc project.
"""

from .base import *
from decouple import config, Csv
import os

# ==============================================================
#  DEBUG & SECURITY
# ==============================================================

DEBUG = config('DEBUG', default=False, cast=bool)

# Em produção, defina as origens reais no .env
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='dolfidoc.com.br,www.dolfidoc.com.br,api.dolfidoc.com.br,dolfidoc-main-dolfidoc-djangoo.babqvt.easypanel.host',
    cast=Csv()
)


# ==============================================================
#  DATABASE (PostgreSQL - Railway ou Render)
# ==============================================================

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': config('DB_NAME', default='dolfidoc'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# ==============================================================
#  SECURITY
# ==============================================================

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ==============================================================
#  CORS (apenas domínios autorizados)
# ==============================================================

CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default="https://dolfidoc.com.br,https://www.dolfidoc.com.br,https://dolfidoc-main-dolfidoc-vue.babqvt.easypanel.host",
    cast=Csv()
)


# ==============================================================
#  TIMEZONE / LINGUA
# ==============================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt-br')
TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')

USE_I18N = True
USE_TZ = True

# ==============================================================
#  STATIC & MEDIA (Render / Railway / CDN)
# ==============================================================

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==============================================================
#  LOGGING (opcional - útil pra debug no Render)
# ==============================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}


CSRF_TRUSTED_ORIGINS = [
    "https://dolfidoc-main-dolfidoc-vue.babqvt.easypanel.host",
    "https://dolfidoc-main-dolfidoc-djangoo.babqvt.easypanel.host",
]


