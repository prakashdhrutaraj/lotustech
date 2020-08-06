"""
WSGI config for django_school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from django_school import classroom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_school.settings')

application = get_wsgi_application()
#application = classroom(application)
