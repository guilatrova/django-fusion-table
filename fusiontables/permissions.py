from rest_framework import permissions

class ManageFusionTablePermission(permissions.BasePermission):
    message = 'You need to login first: http://localhost:8000/auth'

    def has_permission(self, request, view):
        if request.session.get('google_auth_code', False):
            return True

        return False