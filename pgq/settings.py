"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/

isort:skip_file
"""
from django.conf import settings


SHOW_JOBS_ADMIN = getattr(settings, "SHOW_JOBS_ADMIN", True)
QUEUE_ALWAYS_EAGER = getattr(settings, "QUEUE_ALWAYS_EAGER", False)
