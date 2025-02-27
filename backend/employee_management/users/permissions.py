from rest_framework import permissions

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET requests
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.role == 'admin'

class EmployeePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        elif view.action in ['create', 'update', 'destroy']:
            return request.user.is_authenticated and (request.user.role in ['admin', 'manager'])
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        elif request.user.role == 'manager':
            return obj.company == request.user.company
        elif request.user.role == 'employee':
            return obj.user == request.user
        return False