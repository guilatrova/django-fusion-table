from rest_framework import permissions
from djgmaps.settings import CREDENTIALS_KEY
from oauth2client import client

class HasFusionTableCredentialsPermission(permissions.BasePermission):
    message = 'You need to authorize first: http://localhost:8000/auth'

    def has_permission(self, request, view):
        if request.session.get(CREDENTIALS_KEY, False):
            return True

        return False

class FusionTableNotExpiredPermission(permissions.BasePermission):
    message = 'Credentials Expired! You need to authorize again: http://localhost:8000/auth'

    def has_permission(self, request, view):
        credentials_session = request.session.get(CREDENTIALS_KEY)
        credentials = client.OAuth2Credentials.from_json(credentials_session)
        return False if credentials.access_token_expired else True