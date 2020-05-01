from django.apps import AppConfig

from . import logger


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals  # noqa