from rest_framework.permissions import BasePermission


# These methods should return True to grant access, or False otherwise.
class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
