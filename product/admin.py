from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price','old_price','slug', 'stock', 'category','is_available', 'created_at', 'updated_at')
    list_filter = ('is_available', 'created_at', 'updated_at')
    search_fields = ('product_name', 'description')
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ('price', 'stock', 'is_available','old_price')


admin.site.register(Product, ProductAdmin)
   