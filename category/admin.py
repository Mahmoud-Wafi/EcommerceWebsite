from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("get_category_name", "slug")
    prepopulated_fields = {"slug": ("cat_name",)}

    def get_category_name(self, obj):
        return obj.cat_name

    get_category_name.short_description = "Category Name"
    get_category_name.admin_order_field = "cat_name"
