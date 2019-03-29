from django.apps import AppConfig


class BlogConfig(AppConfig):  # copy class name and add it to projects settings.py
    name = 'blog'             # like this in INSTALLED_APPS[ 'blog.apps.BlogConfig',]
