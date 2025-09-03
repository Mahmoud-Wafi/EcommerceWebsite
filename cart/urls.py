from django.urls import path

from . import views

urlpatterns = [
    path('',views.cart ,name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart , name="add_cart"),
    path('decrement_cart/<int:product_id>/', views.decrement_cart , name="decrement_cart"),
    path('remove_cart/<int:product_id>/', views.remove_cart , name="remove_cart"),
    path('edit_quantity/<int:product_id>/', views.edit_quantity , name="edit_quantity"),
    
]
