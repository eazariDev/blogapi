# posts/permissions.py

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        #authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user
    