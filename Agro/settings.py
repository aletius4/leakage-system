import os
from pathlib import Path

# GDAL library path (weka path sahihi ya gdal.dll kulingana na ulivyo-install)
  # 🔁 badilisha hii kulingana na system

# GDAL path (adjust according to your installation)
os.environ['PATH'] += r';C:\OSGeo4W\bin'  # au path yako ya GDAL
os.environ['GDAL_DATA'] = r'C:\OSGeo4W\share\gdal'  # directory ya GDAL data files



LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-1.3319, 31.8123),  # Bukoba coordinates
    'DEFAULT_ZOOM': 13,
}


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-u1qn=gy=dz*t&@ycth%gi_ayz8#uqm!%izgda^&=pt*mon%+zj'
DEBUG = False
ALLOWED_HOSTS = ['onrender.com']

AUTH_USER_MODEL = 'account.Account'
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = '/login/'  # 👈 hii imeongezwa hapa

# Database Configuration with PostGIS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leakage_db',
        'USER': 'leakage_db_user',
        'PASSWORD': 'ifvNp3BI8B9Iiowp0230iJ3FrMLEnbPO',
        'HOST': 'dpg-d1ev8rndiees73afbtog-a',
        'PORT': '5432'
    }    
}
# Static and Media settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.gis',
    'leaflet',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agroresearch',
    'account',
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

ROOT_URLCONF = 'Agro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'agroresearch', 'templates')],
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

WSGI_APPLICATION = 'Agro.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
