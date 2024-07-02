from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsers

class CustomUsersAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname',)}),
    )

admin.site.register(CustomUsers, CustomUsersAdmin)