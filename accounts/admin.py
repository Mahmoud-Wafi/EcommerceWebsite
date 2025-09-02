# from django.contrib import admin
# from .models import User
# admin.site.register(User)       



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Fields shown in list view
    list_display = ("email", "username", "first_name", "last_name", "phone_number", "is_staff", "is_active")

    # Fields to search
    search_fields = ("email", "username", "first_name", "last_name")

    # Fields to filter
    list_filter = ("is_staff", "is_active", "is_admin")

    # Order by
    ordering = ("email",)

    # Organize form fields
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("username", "first_name", "last_name", "phone_number")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_admin", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "first_name", "last_name", "phone_number", "password1", "password2", "is_active", "is_staff"),
        }),
    )

admin.site.register(User, UserAdmin)
