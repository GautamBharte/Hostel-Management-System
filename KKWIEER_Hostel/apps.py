from django.apps import AppConfig


class KkwieerHostelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'KKWIEER_Hostel'
    
    def ready(self):
        import KKWIEER_Hostel.signals