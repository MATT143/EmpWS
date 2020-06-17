from django.apps import AppConfig


class ExpertappConfig(AppConfig):
    name = 'expertapp'

    def ready(self):
        import expertapp.signals

