#!/usr/bin/env python
import django.core.handlers.wsgi
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
