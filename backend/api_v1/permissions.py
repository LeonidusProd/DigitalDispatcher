from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """
    Право доступа имею те авторизованные пользователи, у которых поле is_staff=True
    (являются персоналом: боты и диспетчеры)
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsSuperuser(permissions.BasePermission):
    """
    Право доступа имею те авторизованные пользователи, у которых поле is_superuser=True
    (являются администраторами)
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
