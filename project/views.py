from django.shortcuts import render
from product.models import Product
def home(request):
    products=Product.objects.filter(is_available=True).order_by('-created_at')[:9]   
    context={
        'products':products,
    }
    return render(request, 'home.html',context)
              