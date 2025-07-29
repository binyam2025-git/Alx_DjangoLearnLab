# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\permissions.py

from rest_framework import permissions

class IsPremiumUser(permissions.BasePermission):
    """
    Custom permission to only allow premium users access.
    Checks if the authenticated user has a related UserProfile
    with an 'is_premium' boolean field set to True.
    """
    message = 'You must be a premium user to access this content.'

    def has_permission(self, request, view):
        # Allow unauthenticated users to be rejected by IsAuthenticated first,
        # or handle it explicitly here.
        # If the user is not authenticated, they can't be premium, so return False.
        if not request.user.is_authenticated:
            return False

        # Check if the user object has a 'profile' attribute and if 'is_premium' is True
        # The 'profile' attribute is created by related_name='profile' on the OneToOneField
        return hasattr(request.user, 'profile') and request.user.profile.is_premium