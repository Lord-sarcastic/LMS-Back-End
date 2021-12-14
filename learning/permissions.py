from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwnerOfResource(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('DELETE', 'PUT'):
            if n:= getattr(obj, 'OWNER_FIELD'):
                return n == request.user
            return obj.user == request.user
        return True
