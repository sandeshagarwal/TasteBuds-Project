from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
    
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return admin_permission
    
class CommentAuthorAndAdminOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            admin_permission = bool(request.user and request.user.is_staff)
            return obj.comment_author == request.user or admin_permission
        
class LikeAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.like_author == request.user
        
class RecipeAuthorAndAdminOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            admin_permission = bool(request.user and request.user.is_staff)
            return obj.author_id == request.user or admin_permission
        