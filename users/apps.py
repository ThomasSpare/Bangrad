from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    label = 'userapp'

    def ready(self):
        import users.signals
