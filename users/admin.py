from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("email", "is_admin")
    list_filter = ("is_admin",)

    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "s2nl")}),
        ("Permissions", {"fields": ("is_admin", "is_staff")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "phone", "password1", "password2"),
            },
        ),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = []


admin.site.register(User, UserAdmin)
