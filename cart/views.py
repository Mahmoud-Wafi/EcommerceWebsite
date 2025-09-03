from django.shortcuts import render , redirect , get_object_or_404 
from product.models import Product
from .models import Cart , CartItem
from cart.utils import _cart_id




def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_id = _cart_id(request)

    # Get or create cart for this session
    cart, created = Cart.objects.get_or_create(cart_id=cart_id)

    # Get or create cart item
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        cart=cart,
        defaults={'quantity': 1}
    )
    if not created:
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')

def decrement_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, cart_id=_cart_id(request))
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
def remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, cart_id=_cart_id(request))
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

def edit_quantity(request, product_id):
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)
        cart = get_object_or_404(Cart, cart_id=_cart_id(request))
        cart_item = get_object_or_404(CartItem, product=product, cart=cart)

        if new_quantity > 0 and new_quantity <= product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()
        elif new_quantity == 0:
            cart_item.delete()
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    tax =0
    grand_total=0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
            
        tax = (2 * total) / 100
        grand_total = tax + total
    except Cart.DoesNotExist:
        pass  # Cart is empty
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'product/cart.html', context)                                

