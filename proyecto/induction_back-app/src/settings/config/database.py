import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PG_DB_NAME'),
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASS'),
        'HOST': os.environ.get('PG_HOST'),
        'PORT': os.environ.get('PG_PORT')
    }
}
