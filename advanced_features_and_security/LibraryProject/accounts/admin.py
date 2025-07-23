#from django.contrib import admin

# Register your models here.
# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\accounts\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser # Import your CustomUser from this app

# If you add custom fields to CustomUser, you'd add them to fieldsets/add_fieldsets here
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # You might add custom fields to fieldsets and add_fieldsets if they exist
    # Example:
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('date_of_birth',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('date_of_birth',)}),
    # )

admin.site.register(CustomUser, CustomUserAdmin)
