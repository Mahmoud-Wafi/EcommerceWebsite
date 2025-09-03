from django.db import models
from product.models import Product

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)  
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return str(self.product)
