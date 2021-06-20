from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    message = 'You must be the author to change this'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
