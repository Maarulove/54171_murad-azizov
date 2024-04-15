from django.apps import AppConfig


class FarmersappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farmersapp'

    def ready(self):
        import farmersapp.signals