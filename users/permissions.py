from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка прав доступа Владельца привычки"""
    message = "Доступно только владельцу"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
