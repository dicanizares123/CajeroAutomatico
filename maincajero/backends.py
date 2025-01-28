from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class CedulaBackend(BaseBackend):
    def authenticate(self, request, cedula=None, password=None, **kwargs):
        try:
            user = User.objects.get(perfil__cedula=cedula)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None