from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class SingleTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        if key == settings.API_TOKEN:
            return User(), key
        else:
            raise AuthenticationFailed(_('Invalid token.'))
