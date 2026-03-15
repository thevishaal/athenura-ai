from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = (
        "id",
        "email",
        "full_name",
        "is_staff",
        "is_active",
        "created_at"
    )

    list_display_links = ("id", "email")
    
    list_filter = ("is_active", "is_staff", "is_superuser")

    search_fields = ("email", "full_name")

    ordering = ("id", "-created_at")

    readonly_fields = ("email", "created_at", "updated_at", "image_preview")

    fieldsets = (
        ("User Info", {
            "fields": ("email", "password", "full_name", "profile_img", "image_preview")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser")
        }),
        ("Important Dates", {
            "fields": ("created_at", "updated_at")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2"),
        }),
    )

    def image_preview(self, obj):
        if obj.profile_img:
            return format_html(
                '<img src="{}" style="width:80px;height:80px;border-radius:8px;object-fit:cover;" />',
                obj.profile_img.url
            )
        return "No Image"

    image_preview.short_description = "Profile Image"