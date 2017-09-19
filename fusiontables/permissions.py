from rest_framework import permissions
from djgmaps.settings import CREDENTIALS_KEY

class ManageFusionTablePermission(permissions.BasePermission):
    message = 'You need to login first: http://localhost:8000/auth'

    def has_permission(self, request, view):
        if request.session.get(CREDENTIALS_KEY, False):
            return True

        return False

class FusionTablePermissionNotExpired(permissions.BasePermission):
    pass