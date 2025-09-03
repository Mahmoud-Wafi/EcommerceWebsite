from .models import Cart , CartItem
from .utils import _cart_id
from django.db import models

def counter(request):
    if 'admin' in request.path:
        return {}

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_count = CartItem.objects.filter(cart=cart, is_active=True).aggregate(total=models.Sum('quantity'))['total'] or 0
    except Cart.DoesNotExist:
        cart_count = 0

    return dict(cart_count=cart_count)
