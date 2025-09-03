from django.shortcuts import render , get_object_or_404 , Http404
from .models import Product 
from category.models import Category
from cart.models import CartItem 
from cart.utils import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q
def product_list(request, category_slug=None):
    categories= None
    products= None
    if category_slug != None:
        categories= get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True) 
        product_count = products.count()
    else:   
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={
        'products': products,
        'product_count': product_count,
        'page_obj': page_obj
    }
    return render(request, 'product/product_list.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        category = get_object_or_404(Category, slug=category_slug)
        single_product = get_object_or_404(Product, slug=product_slug, category=category)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product/product_detail.html', context)




def search(request):
    query = request.GET.get("q")
    products_list = Product.objects.filter(is_available=True)

    if query:
        products_list = products_list.filter(
            Q(product_name__icontains=query) | Q(category__cat_name__icontains=query)
        )

    paginator = Paginator(products_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "query": query,
        "page_obj": page_obj,
        "product_count": products_list.count(),
        "categories": Category.objects.all(),
    }
    return render(request, "product/product_list.html", context)
