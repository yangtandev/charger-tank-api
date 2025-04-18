from django.apps import AppConfig


class ChargerTankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charger_tank'

    def ready(self):
        from . import signals
