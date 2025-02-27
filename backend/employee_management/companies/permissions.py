from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read operations for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        # Allow write operations only for admin/manager
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser) 