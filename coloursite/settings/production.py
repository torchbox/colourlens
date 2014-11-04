from .base import *

# Do not set SECRET_KEY, Postgres or LDAP password or any other sensitive data here.
# Instead, create a local.py file on the server.

# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False


try:
        from .local import *
except ImportError:
        pass
