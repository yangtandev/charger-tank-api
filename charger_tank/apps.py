from django.apps import AppConfig
import threading


class ChargerTankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'charger_tank'

    def ready(self):
        from . import signals
        from .schedulers import start_scheduler

        threading.Thread(target=start_scheduler, daemon=True).start()
