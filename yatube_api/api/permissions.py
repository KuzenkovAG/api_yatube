from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerOrReadOnly(BasePermission):
    """
    Prohibit permission for methods PUT, PATCH, DELETE, if user is
    not author of object.
    """
    UPDATE_DELETE_METHODS = ['PUT', 'PATCH', 'DELETE']

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.method in self.UPDATE_DELETE_METHODS:
                obj = view.get_object()
                return request.user == obj.author
            return True
