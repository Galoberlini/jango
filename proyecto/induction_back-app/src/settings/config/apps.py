DJANGO_APPS = [
    'material',  # https://pypi.org/project/django-material-admin/
    'material.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",  # https://www.django-rest-framework.org/    
    'rest_framework_simplejwt',  # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html    
    'corsheaders',  # https://pypi.org/project/django-cors-headers/
    'simple_history',  # https://django-simple-history.readthedocs.io/en/latest/quick_start.html
    'drf_yasg'
]

LOCAL_APPS = [
    # "equality_proyect.users.apps.UsersConfig",
    # Your stuff: custom apps go here
    "apps.utils",
    "apps.patients",
    "apps.api",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
