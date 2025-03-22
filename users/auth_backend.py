from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameBackend(ModelBackend):
    """
    Custom authentication backend that allows login with email or username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if "@" in username:  # If input contains '@', assume it's an email
            user = User.objects.filter(email=username).first()
        else:  # Otherwise, assume it's a username
            user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user
        return None
