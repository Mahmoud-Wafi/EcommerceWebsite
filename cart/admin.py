from django.contrib import admin
from .models import Cart , CartItem
# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added')
    list_filter = ('date_added',)
    search_fields = ('cart_id',)
   
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity','is_active')
    list_filter = ('cart',)
    search_fields = ('cart',)
    readonly_fields=('sub_total',)
    


