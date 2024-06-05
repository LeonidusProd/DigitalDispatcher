from rest_framework import permissions
from .models import TemporaryToken


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsValidTemporaryToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.data.get('token')
        if token:
            temp_token = TemporaryToken.objects.filter(token=token).first()
            if temp_token and temp_token.is_valid():
                return True
        return False
