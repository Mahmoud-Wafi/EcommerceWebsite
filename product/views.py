from django.shortcuts import render , get_object_or_404 , Http404
from .models import Product 
from category.models import Category

# Create your views here.

def product_list(request, category_slug=None):
    categories= None
    products= None
    if category_slug != None:
        categories= get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)  
        product_count = products.count()
    else:   
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context={
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'product/product_list.html', context)



def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    single_product = get_object_or_404(Product, slug=product_slug, category=category)

    context = {
        'single_product': single_product,
    }
    return render(request, 'product/product_detail.html', context)



# def filter_by_price(request):
#     min= Product.objects.filter(min(price))
#     max = Product.objects.filter(max(price))