"""
ASGI config for restaurant_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')

application = get_asgi_application()

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "your-domain.com"]