from django.apps import AppConfig


class FinkixpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finkiXP_app'

    def ready(self):
        from . import signals
