from .base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['.railway.app'])

import dj_database_url
DATABASES['default'] = dj_database_url.config(default=env('DATABASE_URL'))
