from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = '4v_ti^y#9&b^)nz9epc%in6%7swg_0^wngs1u%@shhz)00ck7q'
DATABASES['default']['PASSWORD'] = ''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass

